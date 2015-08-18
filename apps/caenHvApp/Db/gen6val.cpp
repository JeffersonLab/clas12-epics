#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>
#include <iostream>

using namespace std;
void printUsage(char **);
void printCommandPattern();
void printMacroPart(int cr, char* crname, int slot, int chan, const char* detabbr,char* macro);
void printCommandMacros(int crate, int slot, int chan);
void getCurrentCrate(int det, int crate);
#define b_templates \
cout <<  "file \"b_templates.db\" "; 


//Make a big table to hold every hv channel, electronic and detector
//keep this as simple as possible, not always easy given the complexity of the layering
//of subsystems for some detectors.
//
//
//Here's the general procedure:
// 1. Get a description from the Detector expert - eg algorithm. spreadsheet etc.
// 2. Make this into a specific function. (See below). This needs to have
//    nested loops going through the specific heirarchy of systems for that detector.
//    At the innermost level, we'll be incrementing element numbers. 
// 3. As the element number is incremented, we need to incrememt the channel, slot, crate
//    on the HV, mainframe. Again the method of doing this will be different for every system.
//    see the examples below.
// 4. The function should construct the names according to some rules, which will more or less be the 
//    EPICS pv names and aliases.
//    This is essential to allow checking of the system. Get feedback fromm the expert.
// 5. The information in the table will for the basis for creating a database.
//    No doubt will need some changes for the database.

// Some global info and defs

// Detector spec - add new ones before DETNULL
enum         Detectors { DC,  ECAL,  PCAL,  FTOF,  CTOF,  LTCC,  DETNULL};
const char  *DetAbbr[]={"DC","ECAL","PCAL","FTOF","CTOF", "LTCC"};    //Abbr. names used in PVs
const char  *HVCrate[]={"DC","ECAL","FTOF","FTOF","CTOF","ECAL"};    //Names of HV MainFrames per detector
const char  *DetFull[]={"Drift Chambers",              //Full names of detectors
			  "Calorimiter",
			  "Pre Calorimiter",
			  "Forward Time of Flight",
			  "Low Threshold Cerenkov Counter"};

// Crate spec
enum             Geography { CRATE,   CRATENAME,    SLOT,   CHANNEL, NGEOG};

const char  *GeogMacro[]={ "Cr",    "CrName",     "Sl",   "Ch"};
const char  *GeogAbbr[] ={ "HV",    "CrName",     "Sl",   "Ch"};
const char  *GeogFull[] ={ "HV",    "CrateName",  "Slot", "Channel"};

//HV - Crate, Slot, Element = same scheme for all detector formatting for output.
const char *hv_template="B_%s%s%d_%s%d_%s%d";

int macros=1;  //set this to 0 for aliases

//This is the list of the crate names (dns names) and ip addresses in the order that they
const char *subnet       = "129.157.167.";
const int  crateNumber[] = {        0,        1,        2,        3,        4,        5,        6,        7,        8,        9,      10,       11,        12,       13,      14,      15,     16,      17,    18,         -1    };
const char *crateName[]  = {"HVTEST0","HVFTOF6","HVFTOF5","HVFTOF4","HVECAL1","HVFTOF1","HVFTOF2","HVFTOF3","HVECAL5","HVECAL6","HVECAL2","HVECAL3","HVLTCC0","HVECAL4", "HVDC1", "HVDC2","HVDC3", "HVDC4",    "HVCTOF0", "NULL" };
const int  crateIP[]     = {       70,     161,      162,        79,       53,       78,       47,       46,       55,       56,      191,       51,       36,      190,     666,     667,    668,     669,    81,         -1};

char crName[20];    //The current values from the above arrays, 
int crNumber=0;

//commands codes for CAEN
#define NoSupport 0x00    /* No device support for PV       */
#define G_Valid   0x80    /* Get HV validity                */
#define G_HV      0x81    /* Get HV on/off                  */
#define G_Alarm   0x82    /* Get Chassis alarm status       */
#define S_CE      0x01    /* Set enable/disable             */
#define S_DV      0x02    /* Set demand voltage             */
#define S_RDN     0x03    /* Set ramp down                  */
#define S_RUP     0x04    /* Set ramp up                    */
#define S_TC      0x05    /* Set trip current               */
#define S_MVDZ    0x06    /* Set measured voltage dead-zone */
#define S_MCDZ    0x07    /* Set measured current dead-zone */
#define S_HV      0x08    /* Set HV on/off                  */
#define S_SOT     0x09    /* Set samples over threshold     */
/// my: it is actually the time with high current before trip occurs
#define S_PRD     0x0A    /* Set post ramp delay            */ 
/// my:
#define S_CHHV      0x0B    /* Set CHANNEL HV on/off                  */ 
/// my:
#define S_BDHV      0x0C    /* Set BOARD HV on/off                  */ 
#define S_VMAX      0x0D    /* Set MAX CHANNEL VOLATAGE                 */ 

//to skip these uncomment this one.
//int command_codes[] = {-1};
const char *command_macros[]= {"pwonoff", "v0set", "i0set", "trip", "rampup", "rampdn","svmax", NULL}; /// my_piece : const
int command_codes[]   = {S_CHHV,    S_DV,    S_TC,    S_PRD,   S_RUP,    S_RDN, S_VMAX,  -1};

//Now there are specific functions for each detector (so far DC,  ECAL,  PCAL,  FTOF, CTOF)
//Based on the descriptions given by the respective detector experts

// This is for the FTOF, which fills the left half of the TOF/PCAL Mainframe
int FTOFGen(int crate0=1, int slot0=0, int chan0=0,int det=FTOF ){
  int cr=crate0;
  int sl=slot0;
  int ch=chan0;
  char alias[64];
  char macro[64];
  int n;

  enum                  SYS{ SECTOR,   LAYER,           SIDE,          ELEMENT        };
  const char  *SysAbbr[]={ "Sec",    "Panel",         "",             ""            };
  const char  *SysFull[]={ "Sector", "Panel 1A,1B,2", "Side L or R", "Element 1-62" };
  
  //Detector Sector,Layer, ...
  const char *det_template   ="B_%s_%s_%s%d_%s%s_%s%02d";
  const char *macro_template ="%s%d_%s%s_%s%02d";

  int table[5000][NGEOG+ELEMENT+1];    //table for all the stuff
  int nRow=0;                    //counter for rows in table
  int maxSlot=7;
  int maxChan=23;

  int   nInLayer[]={ 0, 23, 62,   5 };
  const  char *layers[] = {"","1A","1B","2"}; /// my_piece : const
  const  char *side[] = {"","L","R"}; /// my_piece : const

  char canonicalName[64];
///  char alias[64]; my_piece
///  char macro[64]; my_piece

  //print out the heirarchy so we understand
  cout << "# Structure of the HV For the " << DetFull[det] << "(Abbr:" << DetAbbr[det] << ")" << endl;
  cout << "# Geographical:\n#" << endl;
  cout << "# " <<  GeogFull[CRATE] << " (Abbr: " << GeogAbbr[CRATE] << ")" << endl;
  cout << "#\t " <<  GeogFull[SLOT] << " (Abbr: " << GeogAbbr[SLOT] << ")" << endl;
  cout << "#\t\t " <<  GeogFull[CHANNEL] << " (Abbr: " << GeogAbbr[CHANNEL] << ")" << endl;
  cout << endl;
  cout << "#Detector based: " <<  endl;
  
  for(int d=0;d<=ELEMENT;d++){
    cout << "# "; for(int t=0;t<d;t++) cout << "\t";
    cout << SysFull[d] << " (Abbr: " << SysAbbr[d] << ")" << endl;
  }
  cout << endl;

  //If we're printing out macros for templating
  if(macros==1){
    b_templates; /// my_piece
    cout <<  "{" << endl;
    cout << "\tpattern {" <<   GeogMacro[CRATE] << ",\t"  << GeogMacro[CRATENAME] << ",\t" <<  GeogMacro[SLOT] << ",\t" << GeogMacro[CHANNEL] << 
      ",\tSys,\tDet,\tElement"; /// my_piece  "}" --> "" and removed \" everywhere
      
    printCommandPattern();
    cout <<  "}" << endl;   
  }
  
      
  for(int s=1;s<=6;s++){
    for(int lr=1;lr<=2;lr++){
      for(int l=1;l<=3;l++){
	for(int e=1; e<=nInLayer[l];e++){
	  table[nRow][NGEOG+SECTOR]=s;
	  table[nRow][NGEOG+LAYER]=l;
	  table[nRow][NGEOG+SIDE]=lr;
	  table[nRow][NGEOG+ELEMENT]=e;
	  
	  getCurrentCrate(det,cr);
	  table[nRow][CRATE]=crNumber;
	  table[nRow][SLOT]=sl;
	  table[nRow][CHANNEL]=ch;

	  sprintf(alias, det_template,GeogAbbr[CRATE],DetAbbr[det],SysAbbr[SECTOR],s,SysAbbr[LAYER],layers[l],side[lr],e);
	  sprintf(macro, macro_template,SysAbbr[SECTOR],s,SysAbbr[LAYER],layers[l],side[lr],e);
	  sprintf(canonicalName, hv_template,GeogAbbr[CRATE],HVCrate[det],cr,GeogAbbr[SLOT],sl,GeogAbbr[CHANNEL],ch);

	  if(macros==0){
	    cout << canonicalName << "    " << alias << endl;
	  }
	  else if(macros==1){
	    printMacroPart(table[nRow][CRATE],crName,table[nRow][SLOT],table[nRow][CHANNEL],DetAbbr[det],macro);
	    printCommandMacros(crNumber,sl,ch);
	    cout <<  "}" << endl;	    
	  }
	  ch++;
	  nRow++;
	  
	  if((ch>maxChan)||((l==3)&&(e>=nInLayer[l]))){
	    cout << endl;
	    ch=0; sl++;
	    if(sl>maxSlot){
	      cout << endl;
	      sl=0;cr++;
	    }
	  }
	}
      }
    }
  }
  if (macros==1) cout << "}" << endl;
  return 0;
}

// This is for the CTOF
int CTOFGen(int crate0=0, int slot0=0, int chan0=0,int det=CTOF ){
  int cr=crate0;
  int sl=slot0;
  int ch=chan0;
  char alias[64];
  char macro[64];
  int n;

  enum                SYS{ GROUP,        SIDE,          ELEMENT        };
  const char  *SysAbbr[]={ ""   ,          "",         ""             };
  const char  *SysFull[]={ ""  ,"Side U or D",         "Element 1-48" };
  
  //Detector Sector,Layer, ...
  const char *det_template   ="B_%s_%s_%s%02d";
  const char *macro_template ="%s%02d";

  int table[5000][NGEOG+ELEMENT+1];    //table for all the stuff
  int nRow=0;                          //counter for rows in table
  int maxChan=23;

  const  char *side[] = {"","U","D"}; /// my_piece : const

  char canonicalName[64];

  //print out the heirarchy so we understand
  cout << "# Structure of the HV For the " << DetFull[det] << "(Abbr:" << DetAbbr[det] << ")" << endl;
  cout << "# Geographical:\n#" << endl;
  cout << "# " <<  GeogFull[CRATE] << " (Abbr: " << GeogAbbr[CRATE] << ")" << endl;
  cout << "#\t " <<  GeogFull[SLOT] << " (Abbr: " << GeogAbbr[SLOT] << ")" << endl;
  cout << "#\t\t " <<  GeogFull[CHANNEL] << " (Abbr: " << GeogAbbr[CHANNEL] << ")" << endl;
  cout << endl;
  cout << "#Detector based: " <<  endl;
  
  for(int d=0;d<=ELEMENT;d++){
    cout << "# "; for(int t=0;t<d;t++) cout << "\t";
    cout << SysFull[d] << " (Abbr: " << SysAbbr[d] << ")" << endl;
  }
  cout << endl;

  //If we're printing out macros for templating
  if(macros==1){
    b_templates; /// my_piece
    cout <<  "{" << endl;
    cout << "\tpattern {" <<   GeogMacro[CRATE] << ",\t"  << GeogMacro[CRATENAME] << ",\t" <<  GeogMacro[SLOT] << ",\t" << GeogMacro[CHANNEL] << 
      ",\tSys,\tDet,\tElement"; /// my_piece  "}" --> "" and removed \" everywhere
      
    printCommandPattern();
    cout <<  "}" << endl;   
  }
  
      
  for(int gr=1;gr<=6;gr++){
    for(int s=1;s<3;s++){
      for(int e=1+8*(gr-1); e<=8*gr;e++){
	table[nRow][NGEOG+GROUP]=gr;
	table[nRow][NGEOG+SIDE]=s;
	table[nRow][NGEOG+ELEMENT]=e;
	  
	getCurrentCrate(det,cr);
	table[nRow][CRATE]=crNumber;
	table[nRow][SLOT]=sl;
	table[nRow][CHANNEL]=ch;
	  
	sprintf(alias, det_template,GeogAbbr[CRATE],DetAbbr[det],side[s],e);
	sprintf(macro, macro_template,side[s],e);
	sprintf(canonicalName, hv_template,GeogAbbr[CRATE],HVCrate[det],cr,GeogAbbr[SLOT],sl,GeogAbbr[CHANNEL],ch);

	if(macros==0){
	  cout << canonicalName << "    " << alias << endl;
	}
	else if(macros==1){
	  printMacroPart(table[nRow][CRATE],crName,table[nRow][SLOT],table[nRow][CHANNEL],DetAbbr[det],macro);
	  printCommandMacros(crNumber,sl,ch);
	  cout <<  "}" << endl;	    
	}
	ch++;
	nRow++;
	  
	if((ch>maxChan)){
	  cout << endl;
	  ch=0; sl++;
	}
      }
    }
  }

  if (macros==1) cout << "}" << endl;
  return 0;
}






// This is for the LTCC, which fills slots 14,15 in the ECAL Mainframes
int LTCCGen(int crate0=1, int slot0=14, int chan0=0,int det=LTCC ){
  int cr=crate0;
  int sl=slot0;
  int ch=chan0;
  char alias[64];
  char macro[64];
  int n;

  enum                  SYS{ SECTOR,   SIDE,          ELEMENT        };
  const char  *SysAbbr[]={ "Sec",    "",            ""             };
  const char  *SysFull[]={ "Sector", "Side L or R", "Element 1-18" };
  
  //Detector Sector,Layer, ...
  const char *det_template   ="B_%s_%s_%s%d_%s%02d";
  const char *macro_template ="%s%d_%s%02d";

  int table[5000][NGEOG+ELEMENT+1];    //table for all the stuff
  int nRow=0;                    //counter for rows in table
  int maxSlot=15;
  int maxChan=17;

  int   nSide=18;
  const  char *side[] = {"","L","R"}; /// my_piece : const

  char canonicalName[64];
  
  //print out the heirarchy so we understand
  cout << "# Structure of the HV For the " << DetFull[det] << "(Abbr:" << DetAbbr[det] << ")" << endl;
  cout << "# Geographical:\n#" << endl;
  cout << "# " <<  GeogFull[CRATE] << " (Abbr: " << GeogAbbr[CRATE] << ")" << endl;
  cout << "#\t " <<  GeogFull[SLOT] << " (Abbr: " << GeogAbbr[SLOT] << ")" << endl;
  cout << "#\t\t " <<  GeogFull[CHANNEL] << " (Abbr: " << GeogAbbr[CHANNEL] << ")" << endl;
  cout << endl;
  cout << "#Detector based: " <<  endl;
  
  for(int d=0;d<=ELEMENT;d++){
    cout << "# "; for(int t=0;t<d;t++) cout << "\t";
    cout << SysFull[d] << " (Abbr: " << SysAbbr[d] << ")" << endl;
  }
  cout << endl;

  //If we're printing out macros for templating
  if(macros==1){
    b_templates; /// my_piece
    cout <<  "{" << endl;
    cout << "\tpattern {" <<   GeogMacro[CRATE] << ",\t"  << GeogMacro[CRATENAME] << ",\t" <<  GeogMacro[SLOT] << ",\t" << GeogMacro[CHANNEL] << 
      ",\tSys,\tDet,\tElement"; /// my_piece  "}" --> "" and removed \" everywhere
      
    printCommandPattern();
    cout <<  "}" << endl;   
  }
  
      
  for(int s=1;s<=6;s++){
    for(int lr=1;lr<=2;lr++){
      for(int e=1; e<=nSide;e++){
	table[nRow][NGEOG+SECTOR]=s;
	table[nRow][NGEOG+SIDE]=lr;
	table[nRow][NGEOG+ELEMENT]=e;
	
	getCurrentCrate(det,cr);
	table[nRow][CRATE]=crNumber;
	table[nRow][SLOT]=sl;
	table[nRow][CHANNEL]=ch;
	
	sprintf(alias, det_template,GeogAbbr[CRATE],DetAbbr[det],SysAbbr[SECTOR],s,side[lr],e);
	sprintf(macro, macro_template,SysAbbr[SECTOR],s,side[lr],e);
	sprintf(canonicalName, hv_template,GeogAbbr[CRATE],HVCrate[det],cr,GeogAbbr[SLOT],sl,GeogAbbr[CHANNEL],ch);
	
	if(macros==0){
	  cout << canonicalName << "    " << alias << endl;
	}
	else if(macros==1){
	  printMacroPart(table[nRow][CRATE],crName,table[nRow][SLOT],table[nRow][CHANNEL],DetAbbr[det],macro);
	  printCommandMacros(crNumber,sl,ch);
	  cout <<  "}" << endl;	    
	}
	ch++;
	nRow++;
	
	if(ch>maxChan){
	  cout << endl;
	  ch=0; sl++;
	  if(sl>maxSlot){
	    cout << endl;
	    sl=slot0;cr++;
	  }
	}
      }
    }
  }

  if (macros==1) cout << "}" << endl;
  return 0;
}


int PCGen(int crate0=1, int slot0=8, int chan0=0, int det=PCAL ){
  int cr=crate0;
  int sl=slot0;
  int ch=chan0;
  char alias[64];
  char macro[64];
  int n;

  enum                  SYS{ SECTOR,   LAYER,         ELEMENT     };
  const char  *SysAbbr[]={ "Sec",    "",            ""           };
  const char  *SysFull[]={ "Sector", "Layer U,V,W", "Element 1 - 68(U), 62(V,W)"};
  
  //Detector Sector,Layer, ...
  const char *det_template="B_%s_%s_%s%d_%s%02d";
  const char *macro_template="%s%d_%s%02d";

  int table[5000][NGEOG+ELEMENT+1];    //table for all the stuff
  int nRow=0;                    //counter for rows in table

  int minSlot=8;
  int maxSlot=15;
  int maxChan=23;

  int   nInLayer[]={ 0, 68, 62, 62 };
const  char *layers[] = {"", "U","V","W"}; /// my_piece : const

  //ordering of mainframes with current PV names
  //int   mf[] = {0,5,6,7,3,2,1};
  //int   mf[] = {0,1,2,3,4,5,6}; //comment this in for straigh ordering

  char canonicalName[64];
///  char alias[64]; my_piece
///  char macro[64]; my_piece
  
  //print out the heirarchy so we understand
  cout << "# Structure of the HV For the " << DetFull[det] << "(" << DetAbbr[det] << ")" << endl;
  cout << "# Geographical:\n#" << endl;
  cout << "# " <<  GeogFull[CRATE] << " (Abbr: " << GeogAbbr[CRATE] << ")" << endl;
  cout << "#\t " <<  GeogFull[SLOT] << " (Abbr: " << GeogAbbr[SLOT] << ")" << endl;
  cout << "#\t\t " <<  GeogFull[CHANNEL] << " (Abbr: " << GeogAbbr[CHANNEL] << ")" << endl;
  cout << endl;
  cout << "#Detector based: " <<  endl;
  for(int d=0;d<=ELEMENT;d++){
    cout << "# "; for(int t=0;t<d;t++) cout << "\t";
    cout << SysFull[d] << " (Abbr: " << SysAbbr[d] << ")" << endl;
  }
  cout << endl;

  //If we're printing out macros for templating
  if(macros==1){
    b_templates; /// my_piece
    cout <<  "{" << endl;
    cout << "\tpattern {" <<  GeogMacro[CRATE] << ",\t" << GeogMacro[CRATENAME] << ",\t" <<  GeogMacro[SLOT] << ",\t" << GeogMacro[CHANNEL] << 
      ",\tSys,\tDet,\tElement"; /// my_piece: removed \" everywhere

    printCommandPattern();
    cout <<  "}" << endl;
  }


  for(int s=1;s<=6;s++){
    for(int l=1;l<=3;l++){
      for(int e=1; e<=nInLayer[l];e++){
	table[nRow][NGEOG+SECTOR]=s;
	table[nRow][NGEOG+LAYER]=l;
	table[nRow][NGEOG+ELEMENT]=e;

	getCurrentCrate(det,cr);
	table[nRow][CRATE]=crNumber;
	table[nRow][SLOT]=sl;
	table[nRow][CHANNEL]=ch;
	
	sprintf(alias, det_template,GeogAbbr[CRATE],DetAbbr[det],SysAbbr[SECTOR],s,layers[l],e);
	sprintf(macro, macro_template,SysAbbr[SECTOR],s,layers[l],e);
	sprintf(canonicalName, hv_template,GeogAbbr[CRATE],HVCrate[det],cr,GeogAbbr[SLOT],sl,GeogAbbr[CHANNEL],ch);
	
	if(macros==0){
	  cout << canonicalName << "    " << alias << endl;
	}
	else if(macros==1){
	  printMacroPart(table[nRow][CRATE],crName,table[nRow][SLOT],table[nRow][CHANNEL],DetAbbr[det],macro);
	  printCommandMacros(crNumber,sl,ch);
	  cout <<  "}" << endl;
	}


	ch++;
	nRow++;
	
	if(ch>maxChan){
	  cout << endl;
	  ch=0; sl++;
	  if(sl>maxSlot){
	    cout << endl;
	    sl=minSlot;cr++;
	  }
	}
      }
    }
  }
  if (macros==1) cout << "}" << endl;
  return 0;
}






int ECGen(int crate0=1, int slot0=0, int chan0=0, int det=ECAL  ){
  int cr=crate0;
  int sl=slot0;
  int ch=chan0;
  char canonicalName[64];
  char alias[64];
  char macro[64];
  int n;

  enum                  SYS{ SECTOR,   LAYER,                      ELEMENT     };
  const char  *SysAbbr[]={ "Sec",    "",                        ""           };
  const char  *SysFull[]={ "Sector", "Layer UI,VI,WI,UI,VI,WI", "Element 1 - 68(U), 62(V,W)"};
  
  const char *det_template="B_%s_%s_%s%d_%s%02d";
  const char *macro_template="%s%d_%s%02d";


  //Make a big table to hold every hv channel, electronic and detector
  //then can order as required to print out

  int table[10000][NGEOG+ELEMENT+1];    //table for all the stuff
  int nRow=0;
  
  int maxSlot=8;
  int maxChan=23;
  
  int   nInLayer[]={ 0, 36, 36,  36,  36,  36,  36 };
const  char *layers[] = {"","UI","UO","VI","VO","WI","WO"}; /// my_piece : const
  
  //print out the heirarchy so we understand
  cout << "# Structure of the HV For the " << DetFull[det] << "(" << DetAbbr[det] << ")" << endl;
  cout << "# Geographical:\n#" << endl;
  cout << "# " <<  GeogFull[CRATE] << " (Abbr: " << GeogAbbr[CRATE] << ")" << endl;
  cout << "#\t " <<  GeogFull[SLOT] << " (Abbr: " << GeogAbbr[SLOT] << ")" << endl;
  cout << "#\t\t " <<  GeogFull[CHANNEL] << " (Abbr: " << GeogAbbr[CHANNEL] << ")" << endl;
  cout << endl;
  cout << "#Detector based: " <<  endl;
  for(int d=0;d<=ELEMENT;d++){
    cout << "# "; for(int t=0;t<d;t++) cout << "\t";
    cout << SysFull[d] << " (Abbr: " << SysAbbr[d] << ")" << endl;
  }
  cout << endl;

  //If we're printing out macros for templating
  if(macros==1){
    b_templates; /// my_piece: my_piece
    cout <<  "{" << endl;
    cout << "\tpattern {" <<  GeogMacro[CRATE] << ",\t" << GeogMacro[CRATENAME] << ",\t" <<  GeogMacro[SLOT] << ",\t" << GeogMacro[CHANNEL] << 
      ",\tSys,\tDet,\tElement"; /// my_piece: removed \" everywhere

    printCommandPattern();
    cout <<  "}" << endl;
  }

  //Detector Sector,Layer, ...

  for(int s=1;s<=6;s++){
    for(int l=1;l<=6;l++){
      for(int e=1; e<=nInLayer[l];e++){
	table[nRow][NGEOG+SECTOR]=s;
	table[nRow][NGEOG+LAYER]=l;
	table[nRow][NGEOG+ELEMENT]=e;

	getCurrentCrate(det,cr);
	table[nRow][CRATE]=crNumber;
	table[nRow][SLOT]=sl;
	table[nRow][CHANNEL]=ch;
	
	sprintf(alias, det_template,GeogAbbr[CRATE],DetAbbr[det],SysAbbr[SECTOR],s,layers[l],e);
	sprintf(macro, macro_template,SysAbbr[SECTOR],s,layers[l],e);
	sprintf(canonicalName, hv_template,GeogAbbr[CRATE],HVCrate[det],cr,GeogAbbr[SLOT],sl,GeogAbbr[CHANNEL],ch);

	if(macros==0){
	  cout << canonicalName << "    " << alias << endl;
	}
	else if(macros==1){
        // if(strstr(crName, "HVECAL2") || strstr(crName, "HVECAL6")){ /// temporary
	  printMacroPart(table[nRow][CRATE],crName,table[nRow][SLOT],table[nRow][CHANNEL],DetAbbr[det],macro);
	  printCommandMacros(crNumber,sl,ch);
	  cout <<  "}" << endl;
        // }
	}
	
	ch++;
	nRow++;
	
	if(ch>maxChan){
	  cout << endl;
	  ch=0; sl++;
	  if(sl>maxSlot){
	    cout << endl;
	    sl=0;cr++;
	  }
	}
      }
    }
  }
  if (macros==1) cout << "}" << endl;
  return 0;
}



int DCGen(int crate0=1, int slot0=0, int chan0=0, int det = DC){
  int cr=crate0;
  int sl=slot0;
  int ch=chan0;
  char canonicalName[64];
  char alias[64];
  char macro[64];
  int n;

  enum                  SYS{ SECTOR, REGION,     LAYER,          TYPE,    ELEMENT,     };
  const char  *SysAbbr[]={ "Sec",    "R",      "SL",           "",      ""           };
  const char  *SysFull[]={ "Sector", "Region", "Super Layer",  "S,F,G", "Wire Group" };

  //  //Detector Sector,SuperLayer,  const char *det_template="B_%s_%s_%s%d_%s%d_%s%d_%s%s";
  //  const char *macro_template="%s%d_%s%d_%s%d_%s%s";
  //  const char *det_template="B_HV:DC:S%d:R%d:SL%d:%s%s";

  //Detector Sector,SuperLayer,
  const char *det_template="B_%s_%s_%s%d_%s%d_%s%d_%s%s";
  const char *macro_template="%s%d_%s%d_%s%d_%s%s";
  //  const char *det_template="B_HV:DC:S%d:R%d:SL%d:%s%s";

  //Make a big table to hold every hv channel, electronic and detector
  //then can order as required to print out

  int table[10000][NGEOG+ELEMENT+1];    //table for all the stuff
  int nRow=0;

  int maxSlot=9;
  int maxChan=23;

  //0th element not used in these arrays since detector labels start at 1
  int Sec[2][4]={{0,6,1,2},{0,5,4,3}}; //the sequence of sector for each "half"
const  char *type[]={"0","S","F","G"};      //sense,field,guard /// my_piece : const
  int nElem[] ={0,   8,  8,  2};       //no of HV elements for each of the above types
const  char *wiresLabel[] = {"","01-08","09-16","17-24","25-32","33-48","49-64","65-80","81-112"}; /// my_piece : const
const  char *guardLabel[] = {"","01-32","33-112"}; /// my_piece : const

  //print out the heirarchy so we understand
  cout << "# Structure of the HV For the " << DetFull[det] << "(" << DetAbbr[det] << ")" << endl;
  cout << "# Geographical:\n#" << endl;
  cout << "# " <<  GeogFull[CRATE] << " (Abbr: " << GeogAbbr[CRATE] << ")" << endl;
  cout << "#\t " <<  GeogFull[SLOT] << " (Abbr: " << GeogAbbr[SLOT] << ")" << endl;
  cout << "#\t\t " <<  GeogFull[CHANNEL] << " (Abbr: " << GeogAbbr[CHANNEL] << ")" << endl;
  cout << endl;
  cout << "#Detector based: " <<  endl;
  for(int d=0;d<=ELEMENT;d++){
    cout << "# "; for(int t=0;t<d;t++) cout << "\t";
    cout << SysFull[d] << " (Abbr: " << SysAbbr[d] << ")" << endl;
  }
  cout << endl;

  //If we're printing out macros for templating
  if(macros==1){ 
    b_templates; /// my_piece
    cout <<  "{" << endl;
    cout << "\tpattern {" <<  GeogMacro[CRATE] << ",\t" << GeogMacro[CRATENAME] << ",\t" <<  GeogMacro[SLOT] << ",\t" << GeogMacro[CHANNEL] << 
      ",\tSys,\tDet,\tElement"; /// my_piece: removed \" everywhere
      
    printCommandPattern();
    cout <<  "}" << endl;
    
  }

  
  //fill up the table in the easiest way according to the geometry description in Mac's spreadsheet
  for(int r=1;r<=3;r++){          //region 1,2,3
    for(int h=0;h<2;h++){            //half
      for(int t=1;t<=3;t++){            //type (s,f,g)
	for(int s=1;s<=3;s++){             //sector 
	  for(int l=1;l<=2;l++){              //super Layer
	    for(int e=1;e<=nElem[t];e++){;       //elements
	      //fill all the geog info in the table
	      table[nRow][NGEOG+SECTOR]=Sec[h][s]; 
	      table[nRow][NGEOG+REGION]=r;
	      table[nRow][NGEOG+LAYER]=l; 
	      table[nRow][NGEOG+TYPE]=t; 
	      table[nRow][NGEOG+ELEMENT]=e;

	      //now fill the crate, slot, channel
	      getCurrentCrate(det,cr);  //Set the variables crName and crIndex for the current crate
	      table[nRow][CRATE]=crNumber;
	      table[nRow][SLOT]=sl;
	      table[nRow][CHANNEL]=ch;
	      //	      if(t==3) sprintf(alias, det_template,Sec[h][s],r,l,type[t],guardLabel[e]);
	      //else sprintf(alias, det_template,Sec[h][s],r,l,type[t],wiresLabel[e]);
	      if(t==3) {
		sprintf(alias, det_template,GeogAbbr[CRATE],DetAbbr[det],SysAbbr[SECTOR],Sec[h][s],SysAbbr[REGION],r,SysAbbr[LAYER],l,type[t],guardLabel[e]);
		sprintf(macro, macro_template,SysAbbr[SECTOR],Sec[h][s],SysAbbr[REGION],r,SysAbbr[LAYER],l,type[t],guardLabel[e]);
	      }
	      else{ 
		sprintf(alias, det_template,GeogAbbr[CRATE],DetAbbr[det],SysAbbr[SECTOR],Sec[h][s],SysAbbr[REGION],r,SysAbbr[LAYER],l,type[t],wiresLabel[e]);
		sprintf(macro, macro_template,SysAbbr[SECTOR],Sec[h][s],SysAbbr[REGION],r,SysAbbr[LAYER],l,type[t],wiresLabel[e]);
	      }
	      sprintf(canonicalName, hv_template,GeogAbbr[CRATE],HVCrate[det],cr,GeogAbbr[SLOT],sl,GeogAbbr[CHANNEL],ch);

	      if(macros==0){
		cout << canonicalName << "    " << alias <<  "      " << macro <<endl;
	      }
	      else if(macros==1){
		printMacroPart(table[nRow][CRATE],crName,table[nRow][SLOT],table[nRow][CHANNEL],DetAbbr[det],macro);
		printCommandMacros(crNumber,sl,ch);
		cout <<  "}" << endl;
	      }
	      
	      ch++;

	      if(ch>maxChan){
		cout << endl;
		ch=0; sl++;
		if((sl>maxSlot)||((sl>4)&&(r==1))){
		  cout << endl;
		  sl=0;
		  cr++;
		}
	      }
	      nRow++;
	    }
	  }
	}
      }
      cout << endl;
      ch=0;sl++; //for the 2nd half go to the next slot
      if(((r==1)&&(sl>4))||(sl>maxSlot)) {
	cr++;
	sl=0;
      }
    }
  }
  if (macros==1) cout << "}" << endl;
  return 0;
}



int TestGen(int crate_id, char *crateName="test", int slots=16, int chans=24){

  char canonicalName[64];
  char alias[64];
  char macro[64];
  int n;

  enum                  SYS{ SYSSLOT,    ELEMENT,   };
  const char  *SysAbbr[]={ "Sl",    "Ch",      };
  const char  *SysFull[]={ "Slot",  "Channel", };

  //Detector Sector,SuperLayer,
  const char *det_template="B_%s_%s%02d_%s%02d";
  const char *macro_template="%s%02d_%s%02d";

  //Make a big table to hold every hv channel, electronic and detector
  //then can order as required to print out

  int table[10000][NGEOG+ELEMENT+1];    //table for all the stuff
  int nRow=0;

  int maxSlot=slots;
  int maxChan=chans;


  //If we're printing out macros for templating
  if(macros==1){ 
    b_templates; /// my_piece
    cout <<  "{" << endl;
    cout << "\tpattern {" <<  GeogMacro[CRATE] << ",\t" << GeogMacro[CRATENAME] << ",\t\t" <<  GeogMacro[SLOT] << ",\t" << GeogMacro[CHANNEL] << 
      ",\tSys,\tDet,\tElement"; /// my_piece: removed \" everywhere
      
    printCommandPattern();
    cout <<  "}" << endl;
    
  }

  
  //fill up the table in the easiest way according to the geometry description in Mac's spreadsheet
  for(int s=0;s<maxSlot;s++){
    for(int e=0;e<maxChan;e++){       //elements
    //fill all the geog info in the table
      table[nRow][NGEOG+SLOT]=s; 
      table[nRow][NGEOG+ELEMENT]=e;
      
      //now fill the crate, slot, channel
      table[nRow][SLOT]=s;
      table[nRow][CHANNEL]=e;
      
      sprintf(alias, det_template,GeogAbbr[CRATE],SysAbbr[SYSSLOT],s,SysAbbr[ELEMENT],e);
      sprintf(macro, macro_template,SysAbbr[SYSSLOT],s,SysAbbr[ELEMENT],e);
      //      sprintf(canonicalName, hv_template,GeogAbbr[CRATE],crateName,GeogAbbr[SLOT],s,GeogAbbr[CHANNEL],e);

      if(macros==0){
	cout << canonicalName << "    " << alias <<  "      " << macro <<endl;
      }
      else if(macros==1){
	printMacroPart(crate_id,crateName,table[nRow][SLOT],table[nRow][CHANNEL],crateName,macro);
	printCommandMacros(crate_id,s,e);
	cout <<  "}" << endl;
      }
      
      nRow++;
    }
  }
  if (macros==1) cout << "}" << endl;
  return 0;
}


void printStartup(){
  int index = 0;

  cout << "#" << endl;
  cout << "#  startup file  test for CLAS12 CAEN HV" << endl;
  cout << "#" << endl;
  cout << "Init_CAEN()" << endl;
  
  while(crateNumber[index] != -1){
/// my_piece: comment out:    cout << endl;
    cout << "# "<< crateName[index] << endl;
    cout << "Start_CAEN(" << crateNumber[index] << ",  \"" << subnet << crateIP[index] << "\")" << endl;
    cout << endl;
    index++;
  }
  
/// my_piece: comment out:  cout << endl;
/// my_piece: comment out:  cout << "dbLoadDatabase(\"/usr/local/clas12/release/0.1/epics/drivers/CAEN_HV/level0/IocShell/O.Common/ioccaen.dbd\",0,0)" << endl;
  cout << "dbLoadDatabase(\"O.Common/ioccaen.dbd\",0,0)" << endl; /// my_piece:
  
/// my_piece: comment out:  cout << endl;
  cout << "ioccaen_registerRecordDeviceDriver(pdbbase)" << endl;
/// my_piece: comment out:  cout << endl;
/// my_piece: comment out:  cout << "dbLoadRecords(\"/usr/local/clas12/release/0.1/epics/drivers/CAEN_HV/level0/IocShell/hvprod.db\")" << endl;
  cout << "dbLoadTemplate(\"test.substitutions\")" << endl; /// my_piece:
/// my_piece: comment out:  cout << endl;
  cout << "#" << endl;
  cout << "iocInit()" << endl;
  cout << "#" << endl;
  cout << "#end of linux ioc startup script" << endl;
}
  
void printCommandPattern(){
  int n=0;
  if(command_codes[n]==-1) return;
  
    cout << ",    CScode"; /// my_piece: removed \" everywhere
  while(command_codes[n]!=-1){
    cout <<  ", " << command_macros[n] ; /// my_piece: removed \" everywhere
    n++;
  } 
}

void printCommandMacros(int crate, int slot, int chan){
  int n=0;
  int cs;
  int com;
  if(command_codes[n]==-1) return;

  cs = crate + (slot<<8);
  cout << ",\t\"#C" << cs << "\""; 
  while(command_codes[n]!=-1){
    com= chan+ (command_codes[n]<<8);
    cout <<  ", \"S" << com << "\"";
    n++;
  }
}

void getCurrentCrate(int det, int crate){
  int n=0;
  //crIndex and crName are global
  crNumber=-1;
  
  sprintf(crName,"HV%s%d",HVCrate[det],crate);  //work out the name of the crate
  while(crateNumber[n]!=-1){
    if(strcmp(crName,crateName[n])==0){
      crNumber=crateNumber[n];
      return;
    }
    n++;
  }
  cout << "Warning: can't find crate called " << crName << ", defined in \"const char *crateName[] = .....\"" << endl;
  crNumber=666;   //set this to 666
}
  
int
main(int argc, char **argv){ 
  
  //printf("%d, %s\n", argc);
  int slots;
  int chanPerSlot;
  int crate_id;

  if(argc>=2 && !strcmp(argv[1],"aliases")) macros=0;
  else macros=1;
  
  if(argc>=2 && (!strcmp(argv[1],"macros") || !strcmp(argv[1],"aliases"))){
    if(argc>=3){
      if(!strcmp(argv[2],"dc")){
	DCGen();
      }
      else if(!strcmp(argv[2],"ecal")){
	ECGen();
      }
      else if(!strcmp(argv[2],"pcal")){
	PCGen();
      }
      else if(!strcmp(argv[2],"ftof")){
	FTOFGen();
      }
      else if(!strcmp(argv[2],"ctof")){
		//CTOFGen(0,1,0,CTOF); starting from slot 1
		CTOFGen();
      }
      else if(!strcmp(argv[2],"ltcc")){
	LTCCGen();
      }
      else if(!strcmp(argv[2],"test")){
	sscanf(argv[4],"%d", &slots);
	sscanf(argv[5],"%d", &chanPerSlot);
	sscanf(argv[6],"%d", &crate_id);
	TestGen(crate_id,argv[3],slots,chanPerSlot);
      }
      else{
	printUsage(argv);
	return  0;
      }
    }
  }
      
  else if(argc==2 && !strcmp(argv[1],"startup")){
    printStartup();
  }
  else {
    printUsage(argv);
  }  
  return 0; 
}

void printUsage( char **argv){
  cout << "Usage:     " << argv[0] << " [aliases|macros] [dc|ecal|pcal|ftof|ltcc]" << endl;
  cout << "Usage:     " << argv[0] << " macros test [crateName] [slots] [chanPerSlot] [crate_id]" << endl;
  cout << "           " << argv[0] << " startup" << endl << endl;
  cout << "Examples:"   << endl;
  cout << "         "   << argv[0] << " macros ltcc" << endl;
  cout << "         "   << argv[0] << " macros test HVLTCC0 16 24 12" << endl;
} 

void printMacroPart(int cr, char* crname, int slot, int chan, const char* detabbr,char* macro){
  fprintf(stdout,"\t\t{\"%d\",\t\"%s\",\t\"%d\",\t\"%d\",\t\"HV\",\t\"%s\",\t\"%s\"",cr,crname,slot,chan,detabbr,macro);
}
