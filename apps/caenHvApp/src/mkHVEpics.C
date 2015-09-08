// mkHVEpics.C   Ken Livingston
// see https://clasweb.jlab.org/wiki/index.php/Slow_Control_HV_name_and_alias_tool
//
// Here's the general procedure:
// 1. Get a description from the Detector expert - eg algorithm. spreadsheet etc.
// 2. Make this into a specific function. (See below, eg ECGen() ). This needs to have
//    nested loops going through the specific heirarchy of systems for that detector.
//    At the innermost level, we'll be incrementing element numbers. 
// 3. As the element number is incremented, we need to incrememt the channel, slot, crate
//    on the HV, mainframe. Again, the method of doing this will be different for every system.
//    see the examples below.
// 4. The function should construct the names according to some rules, which will more or less be the 
//    EPICS pv names and aliases.
//
// 5. There's the added option of baing able to make a quick test crate.
//
// Here's how it works:
//
// mkHVEpics() runs the functions to ceate the names and aliases in one big file (currently HV_allnames.txt).
//             if a file of swaps (currently HVswaps.txt) is present, this will be read,
//             and the correct name / alias created in HV_allnames.txt with swapped channels commented.
//
// mkHVTestEpics() similar to above, but will create a test crate on the fly for testing and dev purposes
//                 see https://clasweb.jlab.org/wiki/index.php/Slow_Control_HV_name_and_alias_tool
//
// g++ -o mkHVEpics mkHVEpics.C
//
//
// (or run as ROOT macro like this)
// >root mkHVEpics.C
//
// or call specific functions in ROOT (at you own risk).


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <iostream>
#include <fstream>

using namespace std;
void  mkHVEpics();                 //The main function which makes names, aliases, startups and substitutions for all defined systems
void  mkHVTestEpics(char *name=NULL, char *ip=NULL, int nslots=0, int *slots=NULL); 
void  makeStartups();
void  printUsage(char **argv);
void  getCurrentCrate(int det, int crate);
char *checkSwap(char *alias=NULL, char *canonical=NULL);
char *checkAlias(char *name=NULL, char *alias=NULL, char *canonical=NULL);
void  printHierarchy(int det, const char **SysFull, const char **SysAbbr, int level);
void  printNames(char *canonicalName,char *alias);
void  loadStoredEpics(char *epicsFile);
void  makeStartupStart(const char *startupFile,const char *comment);
void  makeStartupEnd(char *lastlines=NULL);
void  makeStartupAddCrateFromList(int crate);
void  makeStartupAddCrate(char *name=NULL, char *ip=NULL, int index=0);
void  makeSubStart(const char *subFile,const char *comment);
void  makeSubAddLine(int cr=0,char *name=NULL, char *alias=NULL, char *crname=NULL);
void  makeSubEnd();


// Some global stuff

// Pro-forma for the start and end of the startup and substitution files
const char *stFileHeading[] = {"#!../../bin/linux-x86/ioccaen",
			      "",
			       "< envPaths",
			       "cd ${TOP}",
			       "",
			       "## Register all support components",
			       "dbLoadDatabase(\"dbd/ioccaen.dbd\")",
			       "ioccaen_registerRecordDeviceDriver(pdbbase)",
			       "# call to run sy1527Init()",
			       "Init_CAEN()",
			       "",
			       "# Start_CAEN - call to run sy1527Start(), sy1527GetMap(), sy1527PrintMap()",
			       "",
			       NULL};

const char *stFileTail[]=   {  "",
			       "cd ${TOP}/iocBoot/${IOC}",
			       "iocInit()",
			       "",
			       "asSetFilename(\"caenhv.acf\")",
			       "",
			       NULL};

const char *subFileHeading[]= {"file \"db/caenhv.db\" {",
			       "        pattern { Cr,     CrName,        Sl,     Ch,    Sys,     Det,    Element,                CScode, pwonoff, v0set, i0set, trip,  rampup, rampdn, svmax}",
			       NULL};

const char *subFileTail[]  =  {"}",
			       NULL};


//some default values 
char stDir[]= "../../iocBoot/ioccaenhv";
char dbDir[]= "../Db";

char fullHVName[]="allcaenhv";

ofstream stfile;  //output file for startups
ofstream subfile; //output file for sub files

// Detector spec - add new ones before DETNULL
enum         Detectors { DC,  ECAL,  PCAL,  FTOF,  LTCC,   TEST, DETNULL};
const char  *DetAbbr[]={"DC","ECAL","PCAL","FTOF","LTCC", "TEST"        };    //Abbr. names used in PVs
const char  *HVCrate[]={"DC","ECAL","FTOF","FTOF","ECAL", "TEST"        };    //Names of HV MainFrames per detector
const char  *DetFull[]={"Drift Chambers",                                     //Full names of detectors
			  "Calorimiter",
			  "Pre Calorimiter",
			  "Forward Time of Flight",
			  "Low Threshold Cerenkov Counter",
			  "Test crate"};

// Crate spec
enum             Geography { CRATE,   CRATENAME,    SLOT,   CHANNEL, NGEOG}; 

const char  *GeogMacro[]={ "Cr",    "CrName",     "SL",   "CH"     };
const char  *GeogAbbr[] ={ "HV",    "CrName",     "SL",   "CH"     };
const char  *GeogFull[] ={ "HV",    "CrateName",  "Slot", "Channel"};

//HV - Crate, Slot, Element = same scheme for all detector formatting for output.
const char *hv_template="B_%s%s%d_%s%02d_%s%02d";

int macros=1;  //set this to 0 for aliases

//teThis is the list of the crate names (dns names) and ip addresses in the order that they
const char *subnet       = "129.157.167.";

//                             0,         1,          2,         3,         4,         5,        6,           7,        8,        9,          10,       11,      12,      13,      14,      15,      16,        17,         
enum            Mainframes { HVFTOF1,    HVFTOF2,   HVFTOF3,   HVFTOF4,   HVFTOF5,   HVFTOF6,   HVECAL1,   HVECAL2,   HVECAL3,   HVECAL4,   HVECAL5,   HVECAL6,   HVDC1,   HVDC2,  HVDC3,   HVDC4,   HVTEST0,   HVLTCC0        };
const char *crateName[]  = {"HVFTOF1",  "HVFTOF2", "HVFTOF3", "HVFTOF4", "HVFTOF5", "HVFTOF6", "HVECAL1", "HVECAL2", "HVECAL3", "HVECAL4", "HVECAL5", "HVECAL6", "HVDC1", "HVDC2","HVDC3", "HVDC4", "HVTEST0", "HVLTCC0",  NULL};
const int  crateIP[]     = {   78,        47,         46,        79,        162,       161,       53,      191,         51,       190,       55,        56,       666,     667,    668,     669,      70,        36,         -1};

const int EC_LTCC_Names[]  = { HVECAL1 ,  HVECAL2 ,  HVECAL3 ,  HVECAL4 ,  HVECAL5 ,  HVECAL6 ,  -1};
const int FTOF_PC_Names[]  = { HVFTOF1 ,  HVFTOF2 ,  HVFTOF3 ,  HVFTOF4 ,  HVFTOF5 ,  HVFTOF6 ,  -1};
const int DC_Names[]       = {   HVDC1 ,    HVDC2 ,    HVDC3 ,    HVDC4 ,   -1};

const int  *groupLists[]  = { EC_LTCC_Names,  FTOF_PC_Names,  DC_Names, NULL};
const char *groupNames[]  = {"EC_LTCC",      "FTOF_PC",      "DC",      NULL};
const char *groupTitles[] = {"EC and LTCC",  "FTOF and PC",  "DC",      NULL};

char crName[20];    //The current values from the above arrays, 
int crNumber=0;

ofstream allnames;  //output file for allnames.txt
ifstream allsaved;  //in file for allnames.txt
const char defaultAllnamesFile[] = "HV_allnames.txt";
char allnamesFile[100];
int haveStoredEpics=0;
int nStored=0;
char *allepics[10000][2];

const int defaultNChan = 24;
const int defaultNSlot = 16;


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
/// val: it is actually the time with high current before trip occurs
#define S_PRD     0x0A    /* Set post ramp delay            */ 
/// val:
#define S_CHHV    0x0B    /* Set CHANNEL HV on/off          */ 
/// val:
#define S_BDHV    0x0C    /* Set BOARD HV on/off            */ 
#define S_VMAX    0x0D    /* Set MAX CHANNEL VOLATAGE       */ 

//to skip these uncomment this one.
//int command_codes[] = {-1};
const char *command_macros[]= {"pwonoff", "v0set", "i0set", "trip", "rampup", "rampdn","svmax", NULL}; /// val_piece : const
int command_codes[]         = { S_CHHV,    S_DV,    S_TC,    S_PRD,  S_RUP,    S_RDN,   S_VMAX,  -1};

//For the list of broken channels to be sapped
enum swapFields{ORIG_CSC, ALIAS, NEW_CSC};
char *swapTable[1000][3];  //to hold strings from the swap file;
int  nSwaps=0;
int haveSwap=0;
const char *defaultSwapFile="HVswaps.txt";
char swapFile[100];

//For test crates where aliases are to be provided
char *aliasTable[1000][2];  //to hold strings for aliases
int  nAlias=0;
int haveAlias=0;
char aliasFile[100];


//********************************************************************************************************
//Now there are specific functions for each detector (so far DC,  ECAL,  PCAL,  FTOF, LTCC)
//Based on the descriptions given by the respective detector experts
//********************************************************************************************************
// This is for the FTOF, which fills the left halves of the FTOF/PCAL Mainframes
int FTOFGen(int crate0=1, int slot0=0, int chan0=0,int det=FTOF ){
  int cr=crate0;
  int sl=slot0;
  int ch=chan0;
  char canonicalName[64];
  char alias[64];
  char macro[64];
  int n;

  enum                SYS{ SECTOR,   LAYER,           SIDE,          ELEMENT        };
  const char  *SysAbbr[]={ "SEC",    "PANEL",         "",             ""            };
  const char  *SysFull[]={ "Sector", "Panel 1A,1B,2", "Side L or R", "Element 1-62" };
  
  //Detector Sector,Layer, ...
  const char *det_template   ="B_%s_%s_%s%d_%s%s_%s_E%02d";
  const char *macro_template ="%s%d_%s%s_%s_E%02d";

  int maxSlot=7;
  int maxChan=23;

  int   nInLayer[]={ 0, 23, 62,   5 };
  const  char *layers[] = {"","1A","1B","2"}; /// val_piece : const
  const  char *side[] = {"","L","R"}; /// val_piece : const

  printHierarchy(det,SysFull,SysAbbr,ELEMENT);


  //Detector Sector,Layer, ...
     
  for(int s=1;s<=6;s++){
    for(int lr=1;lr<=2;lr++){
      for(int l=1;l<=3;l++){
	for(int e=1; e<=nInLayer[l];e++){
	  
	  getCurrentCrate(det,cr);
	  
	  sprintf(alias, det_template,GeogAbbr[CRATE],DetAbbr[det],SysAbbr[SECTOR],s,SysAbbr[LAYER],layers[l],side[lr],e);
	  sprintf(canonicalName, hv_template,GeogAbbr[CRATE],HVCrate[det],cr,GeogAbbr[SLOT],sl,GeogAbbr[CHANNEL],ch);
	  printNames(canonicalName,alias);

	  ch++;
	  
	  if((ch>maxChan)||((l==3)&&(e>=nInLayer[l]))){
	    allnames << endl;
	    ch=0; sl++;
	    if(sl>maxSlot){
	      allnames << endl;
	      sl=0;cr++;
	    }
	  }
	}
      }
    }
  }
  return 0;
}


// This is for the LTCC, which fills slots 14,15 in the ECAL Mainframes
int LTCCGen(int crate0=1, int slot0=14, int chan0=0,int det=LTCC ){
  int cr=crate0;
  int sl=slot0;
  int ch=chan0;
  char canonicalName[64];
  char alias[64];
  char macro[64];
  int n;

  enum                  SYS{ SECTOR,   SIDE,          ELEMENT        };
  const char  *SysAbbr[]={ "SEC",    "",            ""             };
  const char  *SysFull[]={ "Sector", "Side L or R", "Element 1-18" };
  
  //Detector Sector,Layer, ...
  const char *det_template   ="B_%s_%s_%s%d_%s_E%02d";
  const char *macro_template ="%s%d_%s_E%02d";

  int maxSlot=15;
  int maxChan=17;

  int   nSide=18;
  const  char *side[] = {"","L","R"}; /// val_piece : const

  printHierarchy(det,SysFull,SysAbbr,ELEMENT);

  
  //Detector Sector,Layer, ...
      
  for(int s=1;s<=6;s++){
    for(int lr=1;lr<=2;lr++){
      for(int e=1; e<=nSide;e++){
	
	getCurrentCrate(det,cr);
	
	sprintf(alias, det_template,GeogAbbr[CRATE],DetAbbr[det],SysAbbr[SECTOR],s,side[lr],e);
	sprintf(canonicalName, hv_template,GeogAbbr[CRATE],HVCrate[det],cr,GeogAbbr[SLOT],sl,GeogAbbr[CHANNEL],ch);
	printNames(canonicalName,alias);
	ch++;
	
	if(ch>maxChan){
	  allnames << endl;
	  ch=0; sl++;
	  if(sl>maxSlot){
	    allnames << endl;
	    sl=slot0;cr++;
	  }
	}
      }
    }
  }
  return 0;
}



int PCGen(int crate0=1, int slot0=8, int chan0=0, int det=PCAL ){
  int cr=crate0;
  int sl=slot0;
  int ch=chan0;
  char canonicalName[64];
  char alias[64];
  char macro[64];
  int n;

  enum                  SYS{ SECTOR,   LAYER,         ELEMENT     };
  const char  *SysAbbr[]={ "SEC",    "",            ""           };
  const char  *SysFull[]={ "Sector", "Layer U,V,W", "Element 1 - 68(U), 62(V,W)"};
  
  //Detector Sector,Layer, ...
  const char *det_template="B_%s_%s_%s%d_%s_E%02d";
  const char *macro_template="%s%d_%s_E%02d";

  int minSlot=8;
  int maxSlot=15;
  int maxChan=23;

  int   nInLayer[]={ 0, 68, 62, 62 };
  const  char *layers[] = {"", "U","V","W"}; /// val_piece : const

  printHierarchy(det,SysFull,SysAbbr,ELEMENT);
  
  //Detector Sector,Layer, ...
  

  for(int s=1;s<=6;s++){
    for(int l=1;l<=3;l++){
      for(int e=1; e<=nInLayer[l];e++){
	
	getCurrentCrate(det,cr);
	
	sprintf(alias, det_template,GeogAbbr[CRATE],DetAbbr[det],SysAbbr[SECTOR],s,layers[l],e);
	sprintf(canonicalName, hv_template,GeogAbbr[CRATE],HVCrate[det],cr,GeogAbbr[SLOT],sl,GeogAbbr[CHANNEL],ch);
	
	printNames(canonicalName,alias);
	
	ch++;
	
	if(ch>maxChan){
	  allnames << endl;
	  ch=0; sl++;
	  if(sl>maxSlot){
	    allnames << endl;
	    sl=minSlot;cr++;
	  }
	}
      }
    }
  }
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

  enum                SYS{ SECTOR,   LAYER,                      ELEMENT         };
  const char  *SysAbbr[]={ "SEC",    "",                        ""               };
  const char  *SysFull[]={ "Sector", "Layer UI,UO,VI,VO,WI,WO", "Element 1 - 36" };
  
  const char *det_template="B_%s_%s_%s%d_%s_E%02d";
  const char *macro_template="%s%d_%s_E%02d";

  
  int maxSlot=8;
  int maxChan=23;
  
  int   nInLayer[]={ 0, 36, 36,  36,  36,  36,  36 };
  const  char *layers[] = {"","UI","UO","VI","VO","WI","WO"}; /// val_piece : const
  
  printHierarchy(det,SysFull,SysAbbr,ELEMENT);
  
  //Detector Sector,Layer, ...

  for(int s=1;s<=6;s++){
    for(int l=1;l<=6;l++){
      for(int e=1; e<=nInLayer[l];e++){

	getCurrentCrate(det,cr);

	sprintf(alias, det_template,GeogAbbr[CRATE],DetAbbr[det],SysAbbr[SECTOR],s,layers[l],e);
	sprintf(canonicalName, hv_template,GeogAbbr[CRATE],HVCrate[det],cr,GeogAbbr[SLOT],sl,GeogAbbr[CHANNEL],ch);
	printNames(canonicalName,alias);
	ch++;
	
	if(ch>maxChan){
	  allnames << endl;
	  ch=0; sl++;
	  if(sl>maxSlot){
	    allnames << endl;
	    sl=0;cr++;
	  }
	}
      }
    }
  }
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
  const char  *SysAbbr[]={ "SEC",    "R",      "SL",           "",      ""           };
  const char  *SysFull[]={ "Sector", "Region", "Super Layer",  "S,F,G", "Wire Group" };

  //Detector Sector,SuperLayer,
  const char *det_template="B_%s_%s_%s%d_%s%d_%s%d_%s%s";
  const char *macro_template="%s%d_%s%d_%s%d_%s%s";

  int maxSlot=9;
  int maxChan=23;

  //0th element not used in these arrays since detector labels start at 1
  int Sec[2][4]={{0,6,1,2},{0,5,4,3}}; //the sequence of sector for each "half"
  const  char *type[]={"0","S","F","G"};      //sense,field,guard /// val_piece : const
  int nElem[] ={0,   8,  8,  2};       //no of HV elements for each of the above types
  const  char *wiresLabel[] = {"","01-08","09-16","17-24","25-32","33-48","49-64","65-80","81-112"}; /// val_piece : const
  const  char *guardLabel[] = {"","01-32","33-112"}; /// val_piece : const

  printHierarchy(det,SysFull,SysAbbr,ELEMENT);
  
  //Detector Sector,Layer, ...

  for(int r=1;r<=3;r++){          //region 1,2,3
    for(int h=0;h<2;h++){            //half
      for(int t=1;t<=3;t++){            //type (s,f,g)
	for(int s=1;s<=3;s++){             //sector 
	  for(int l=1;l<=2;l++){              //super Layer
	    for(int e=1;e<=nElem[t];e++){;       //elements

	      //now fill the crate, slot, channel
	      getCurrentCrate(det,cr);  //Set the variables crName and crIndex for the current crate
	      
	      if(t==3) sprintf(alias, det_template,GeogAbbr[CRATE],DetAbbr[det],SysAbbr[SECTOR],Sec[h][s],SysAbbr[REGION],r,SysAbbr[LAYER],l,type[t],guardLabel[e]);
	      else     sprintf(alias, det_template,GeogAbbr[CRATE],DetAbbr[det],SysAbbr[SECTOR],Sec[h][s],SysAbbr[REGION],r,SysAbbr[LAYER],l,type[t],wiresLabel[e]);
	      
	      sprintf(canonicalName, hv_template,GeogAbbr[CRATE],HVCrate[det],cr,GeogAbbr[SLOT],sl,GeogAbbr[CHANNEL],ch);
	      printNames(canonicalName,alias);

	      ch++;

	      if(ch>maxChan){
		allnames << endl;
		ch=0; sl++;
		if((sl>maxSlot)||((sl>4)&&(r==1))){
		  allnames << endl;
		  sl=0;
		  cr++;
		}
	      }
	    }
	  }
	}
      }
      allnames << endl;
      ch=0;sl++; //for the 2nd half go to the next slot
      if(((r==1)&&(sl>4))||(sl>maxSlot)) {
	cr++;
	sl=0;
      }
    }
  }
  return 0;
}



int TestGen(char *name=NULL, int chans=24, int nslots=16, int *slotlist=NULL){

  char canonicalName[64];
  char alias[64];
  char macro[64];
  int n,s;
  int cr=0;
  char  *swappedAlias=NULL;
  
  
  enum          SYS{ TCRATE,        SYSSLOT,  ELEMENT,   };
  const char  *SysAbbr[]={ name,          "SL",     "CH",      };
  const char  *SysFull[]={ name,          "Slot",   "Channel", };

  const char *can_template="B_%s_%s%02d_%s%02d";
  const char *alias_template="B_HV_%s_%s%02d_%s%02d";


  int maxChan=chans;



  for(int sl=0;sl<nslots;sl++){
    s=slotlist[sl];
    for(int e=0;e<maxChan;e++){       //elements
      
      sprintf(alias, alias_template,name,SysAbbr[SYSSLOT],s,SysAbbr[ELEMENT],e);
      sprintf(canonicalName, can_template,name,SysAbbr[SYSSLOT],s,SysAbbr[ELEMENT],e);
      swappedAlias=checkAlias(name,alias,canonicalName);
      if(swappedAlias){
	allnames << canonicalName  << "    " << swappedAlias << "   // aliased " << endl;
      }
      else{
	allnames << canonicalName  << "    " << alias << endl;
      }
      
    }
  }
  
  return 0;
}

//******** End of the generatrs for the specific detectors  *************************************************
//***********************************************************************************************************


// Utility functions called from those above

// If running compiled, as opposed to within root, here's the main.
int main(int argc, char **argv){
  int nslots;
  int slots[16];
  char *name;
  char *ip;
  
  if(argc==2) {
    if(!strcmp(argv[1],"all")){
      mkHVEpics();
      makeStartups();
    }
    else{
      printUsage(argv);
    }
    return 0;
  }
  
  else if(argc >= 3) {                         //name and ip fo a crate, at least
    name=argv[1];
    ip=argv[2];
    if(argc==3){                               //if only 3 args, no of slots is not provided, use default and number from 0
      nslots = defaultNSlot;
      for(int n=0;n<nslots;n++)slots[n]=n;
    }
    else{
      sscanf(argv[3],"%d",&nslots);            //else, get nslots from arg
      if(argc==4){                             //no more args, so start numbering from 0, since slots not specified
	for(int n=0;n<nslots;n++)slots[n]=n;   
      }
      if((argc>4)&&(argc-4!=nslots)){          //if more args, there needs to be nslots worth, so check
	  cout << "ERROR: " << nslots << " slots were requested, but only " << argc-4 <<  " slot indices provided on the command line" << endl;
	  printUsage(argv);
	  exit;
	}
      else{                                    //number the slots as specified in the args.
	for(int n=4;n<argc;n++)sscanf(argv[n],"%d,",&slots[n-4]);
      }
    }
    mkHVTestEpics(name, ip, nslots, slots);
  }
  else printUsage(argv);
  return 0; 
}

void printUsage(char **argv){
  cout << endl;
  cout << "Usage:     " << argv[0] << " -h  Print this message" << endl << endl;
  cout << "Usage:     " << argv[0] << " all Generate all standard EPICS CaenHV ioc started files, and related substititions files" << endl << endl;
  cout << "Usage:     " << argv[0] << " <name> <ipaddress> [nslots] [slot1, slot2, ...]" << endl << endl;

  cout << "              Generate an ioc startup and related substitutions for a single crate with speficied name, ip and slots, where" << endl;
  cout << "              name           Name of Mainframe" << endl; 
  cout << "              ipaddress      i.p. of Mainframe" << endl; 
  cout << "              [nslots]:      No of slots with modules (default to all slots, and starts at slot 0 unless a list specified, see below)  " << endl;
  cout << "              [slot1,slot2, ..... slotn] specific slot numbers"  << endl << endl;
  cout << "All generated startup files will go into ../../iocBoot/ioccaenhv/"  << endl;
  cout << "All generated substitution files will go into ../Db/"  << endl  << endl;
  cout << "For the gory details see https://clasweb.jlab.org/wiki/index.php/Slow_Control_HV_name_and_alias_tool"  << endl  << endl;;
}

void getCurrentCrate(int det, int crate){
  
  //crIndex and crName are global
  crNumber=0;
  
  sprintf(crName,"HV%s%d",HVCrate[det],crate);  //work out the name of the crate
  while(crateName[crNumber]){
    if(strcmp(crName,crateName[crNumber++])==0){
      return;
    }
  }
  cout << "Warning: can't find crate called " << crName << ", defined in \"const char *crateName[] = .....\"" << endl;
  crNumber=666;   //set this to 666
  return;
}


//Called to check whether the element has been swapped to anothe channel 
char *checkSwap(char *alias, char *canonical){
  
  FILE *fp;
  char line[200];                 //to scan lines from the file
  int nline=0;
  char fstring[3][100];
  char cratename[100];
  char origcratename[100];
  
  if(!haveSwap){                  //if table no loaded, load it now
    cout << endl;
    cout << "Checking for list of swaps: ";
    if((fp=fopen(swapFile,"r"))==NULL){
      cout << "Warning - swap file " << swapFile << " not found, assuming there are no swaps." << endl;
      haveSwap=1;
      return 0;
    }
    else{
      cout << "Found swap file " << swapFile << endl;
    }
    cout << endl<<endl;

    cout << "The following swaps will be implemented:" << endl;
    
    while(fgets(line,200,fp) != NULL){		// check got a line from file
      nline++;
      if((line[0] == '*')||(line[0] == '#')) continue;    // skip comments 
      if(sscanf(line,"%s%s%s",fstring[ORIG_CSC],fstring[ALIAS],fstring[NEW_CSC])!=3){
	cout << "Error, not enough parameters on line " << nline << " in " << swapFile << endl;
	exit;
      }
      cout << "Swap: " << fstring[ALIAS] << " from " << fstring[ORIG_CSC] << " to " << fstring[NEW_CSC] << endl;
      strcpy(cratename,fstring[NEW_CSC]+2);
      sprintf(strstr(cratename,"_SL"),"");
      strcpy(origcratename,fstring[ORIG_CSC]+2);
      sprintf(strstr(origcratename,"_SL"),"");
      cout << "      Checking crate " << cratename <<": ";
      if(strcmp(cratename,origcratename)){
	  cout << "Warning, new crate (" << cratename << ") is different from original crate ("<< origcratename <<  "). See line " << nline << " in " << swapFile << endl;
	  cout << "      Let's hope you know what you're doing!" << endl<< endl;
      }
      else{	
	cout << "OK same crate as original channel" << endl<< endl;
      }
      
      for(int n=0;n<3;n++){
	swapTable[nSwaps][n]= new char[strlen(fstring[n])+1];   strcpy(swapTable[nSwaps][n],fstring[n]);
      }
      nSwaps++;
    }
    cout << endl;
    haveSwap=1;
  }
  
  if((!nSwaps)||(!alias))return NULL;             //was callwed with alias=NULL, just to load the table.
  
  for(int n=0;n<nSwaps;n++){
    if(strcmp(swapTable[n][ALIAS],alias)==0){     //found the alias in the swap table
      return swapTable[n][NEW_CSC];
    }
  }
  return NULL;
}


char *checkAlias(char *name, char *alias, char *canonical){
  
  FILE *fp;
  char line[200];                 //to scan lines from the file
  int nline=0;
  char fstring[2][100];
  char cratename[100];
  char origcratename[100];

  sprintf(aliasFile,"HV_%s_aliases.txt",name);
  
  if(!haveAlias){                  //if table no loaded, load it now
    cout << "Looking for list of aliases: ";
    if((fp=fopen(aliasFile,"r"))==NULL){
      cout << "Warning - alias file " << aliasFile << " not found, assuming there are no aliases." << endl;
      haveAlias=1;
      return 0;
    }
    else{
      cout << "Found alias file " << aliasFile << endl;
    }
    cout << endl<<endl;

    cout << "The following aliases will be implemented:" << endl;
    
    while(fgets(line,200,fp) != NULL){		// check got a line from file
      nline++;
      if((line[0] == '*')||(line[0] == '#')) continue;    // skip comments 
      if(sscanf(line,"%s%s",fstring[ORIG_CSC],fstring[ALIAS])!=2){
	cout << "Error, not enough parameters on line " << nline << " in " << swapFile << endl;
	exit;
      }
      cout << "Alias: " << fstring[ORIG_CSC] << " to " << fstring[ALIAS] << endl;
      
      for(int n=0;n<2;n++){
	aliasTable[nAlias][n]= new char[strlen(fstring[n])+1];   strcpy(aliasTable[nAlias][n],fstring[n]);
      }
      nAlias++;
    }
    cout << endl;
    haveAlias=1;
  }
  
  if((!nAlias)||(!canonical))return NULL;
  
  for(int n=0;n<nAlias;n++){
    if(strcmp(aliasTable[n][ORIG_CSC],canonical)==0){     //found a line in the alias table
      return aliasTable[n][ALIAS];
    }
  }
  return NULL;
}



//generate ioc startup files, names and aliases for the detectors with special algorithms specified in this code.
void mkHVEpics(){
  time_t rawtime;    //to timestame auto generated files
  time (&rawtime);

  strcpy(swapFile,defaultSwapFile);
  strcpy(allnamesFile,defaultAllnamesFile);
  
  checkSwap();                 //force the reading of the swap table list
  cout << "Generating names and aliases: "  << endl;
  allnames.open(allnamesFile); //open output file
  allnames << "#" << endl << "#This file was autogenerated by mkHVEpics on: " << ctime (&rawtime) << endl << "#" << endl;
  
  ECGen();  LTCCGen(); FTOFGen(); PCGen(); DCGen();  //call all the generators
  allnames.close();            //close output file
  //now  written all the names and aliases, taking account of any swap
  cout << "Saved in " << allnamesFile << endl << endl;
}

//generate startup file, names and aliases for a single ioc (usually for testing), specifcied on the commannd line,
//and with an optional file of aliases
void mkHVTestEpics(char *name, char *ip, int nslots, int *slots){
 
  time_t rawtime;     //to timestame auto generated files
  time (&rawtime);
  char comment[200];

  char stName[200];   //startup files
  char subName[200];  //subst filenames
  char dumpLine[200]; 
  
  sprintf(allnamesFile,"HV_allnames_%s.txt",name);

  checkAlias(name,NULL,NULL);   //force the reading of the alias table
  cout << "Generating names and aliases: "  << endl;
  allnames.open(allnamesFile); //open output file
  allnames << "#" << endl << "#This file was autogenerated by mkHVEpics on: " << ctime (&rawtime) << endl << "#" << endl;
  
  TestGen(name, defaultNChan, nslots, slots);
  
  allnames.close();            //close output file

  sprintf(stName,"%s/st.%s",stDir,name);
  sprintf(subName,"%s/%s.substitutions",dbDir,name);
  sprintf(dumpLine,"dbDumpRecord > st.%s.dump",name); 
  
  if(!haveStoredEpics) loadStoredEpics(allnamesFile); //load all the names and aliases from file if required.

  sprintf(comment,"IOC for single mainframe:  %s",name);
  makeStartupStart(stName,comment);                 // Make the startup first lines:
  
  sprintf(comment,"Substitutions for IOC for single mainframe:  %s", name);
  makeSubStart(subName,comment);                    // Make the substitution file first lines:
  
  makeStartupAddCrate(name,ip,0);
  for(int n=0;n<nStored;n++){
    makeSubAddLine(0,allepics[n][ORIG_CSC],allepics[n][ALIAS],name);
  }
  stfile <<  "## Load record instances" << endl << "dbLoadTemplate(\"db/" << fullHVName << ".substitutions\")" << endl;
  
  makeStartupEnd(dumpLine);
  makeSubEnd();
  return;
  
}

//generate ioc startup files and substitution files for the detectors with special algorithms specified in this code.
void makeStartups(){
  char cratename[100];
  char comment[100];
  int stCrateId=0;
  int stGroupId=0;
  char stName[200];  //startup files
  char subName[200];  //subst filenames
  char dumpLine[200]; 
  
  if(!haveStoredEpics) loadStoredEpics(allnamesFile); //load all the names and aliases from file if required.
  
  //Generate startup files for each different way of running:
  
  //**** All together in a biggie ****
  sprintf(stName,"%s/st.%s",stDir,fullHVName);
  sprintf(subName,"%s/%s.substitutions",dbDir,fullHVName);
  sprintf(dumpLine,"dbDumpRecord > st.%s.dump",fullHVName); 

  cout << endl << "Generating "<< stName << " and " << subName <<  " for full HV system ....." << endl << endl; 
  
  makeStartupStart(stName,"All HV crates in single IOC");                 // Make the startup first lines:
  makeSubStart(subName,"Substitutions for all HV crates in single IOC");  // Make the substitution file first lines:
  
  stCrateId=0;           
  while(crateName[stCrateId]){      // loop over all crates    
    makeStartupAddCrateFromList(stCrateId);
    for(int n=0;n<nStored;n++){
      if(strstr(allepics[n][ORIG_CSC],crateName[stCrateId])){
	makeSubAddLine(stCrateId,allepics[n][ORIG_CSC],allepics[n][ALIAS]);
      }
    }
    stCrateId++;
  }
  stfile <<  "## Load record instances" << endl;
  stfile << "dbLoadRecords(\"$(DEVIOCSTATS)/db/iocAdminSoft.db\", \"IOC=$(IOC)\")" << endl;
  stfile << "dbLoadTemplate(\"db/" << fullHVName << ".substitutions\")" << endl;
  
  makeStartupEnd(dumpLine);
  makeSubEnd();

  //**** one per detector ****//  
  stCrateId=0;
  cout << endl << "Generating startups and  substitutions for each Mainframe:" << endl;
  while(crateName[stCrateId]){
    sprintf(stName,"%s/st.%s",stDir,crateName[stCrateId]);
    sprintf(subName,"%s/%s.substitutions",dbDir,crateName[stCrateId]);
    sprintf(dumpLine,"dbDumpRecord > st.%s.dump",crateName[stCrateId]); 
    
    cout << "   " << stName << " and " << subName <<  " ....." << endl ; 
    
    sprintf(comment,"Crate name: %s",crateName[stCrateId]);
    makeStartupStart(stName,comment);                                                 // Make the startup first lines:
    sprintf(comment,"Substitutions for single crate: %s",crateName[stCrateId]);
    makeSubStart(subName,comment);                                                    // Make the substitution file first lines:
    
    makeStartupAddCrateFromList(stCrateId);
    for(int n=0;n<nStored;n++){
      if(strstr(allepics[n][ORIG_CSC],crateName[stCrateId])){
	makeSubAddLine(stCrateId,allepics[n][ORIG_CSC],allepics[n][ALIAS]);
      }
    }
    stfile <<  "## Load record instances" << endl;
    stfile << "dbLoadRecords(\"$(DEVIOCSTATS)/db/iocAdminSoft.db\", \"IOC=$(IOC)\")" << endl;
    stfile   << "dbLoadTemplate(\"db/" << crateName[stCrateId] << ".substitutions\")" << endl;
    makeStartupEnd(dumpLine);
    makeSubEnd();
    stCrateId++;
  }

  //**** one per group **** //

  cout << endl << "Generating startups and substitutions for each systems sharing Mainframes:" << endl;
  while(groupLists[stGroupId]){
    stCrateId=0;
    sprintf(stName,"%s/st.%s",stDir,groupNames[stGroupId]);
    sprintf(subName,"%s/%s.substitutions",dbDir,groupNames[stGroupId]);
    sprintf(dumpLine,"dbDumpRecord > st.%s.dump",groupNames[stGroupId]); 
    
    sprintf(comment,"Group name: %s (all crates for %s)",groupNames[stGroupId],groupTitles[stGroupId]);
    makeStartupStart(stName,comment);                                                 // Make the startup first lines:
    sprintf(comment,"Substitutions for group of crates for %s",groupTitles[stGroupId]);

    cout << "   " << stName << " and " << subName <<  " ....." << endl ; 
    
    makeSubStart(subName,comment);                                                    // Make the substitution file first lines:
    while(groupLists[stGroupId][stCrateId]!=-1){
      makeStartupAddCrateFromList(groupLists[stGroupId][stCrateId]);
      for(int n=0;n<nStored;n++){
	if(strstr(allepics[n][ORIG_CSC],crateName[groupLists[stGroupId][stCrateId]])){
	  makeSubAddLine(groupLists[stGroupId][stCrateId],allepics[n][ORIG_CSC],allepics[n][ALIAS]);
	}
      }
      stCrateId++;
    }
    stfile <<  "## Load record instances" << endl;
    stfile << "dbLoadRecords(\"$(DEVIOCSTATS)/db/iocAdminSoft.db\", \"IOC=$(IOC)\")" << endl;
    stfile << "dbLoadTemplate(\"db/" << groupNames[stGroupId] << ".substitutions\")" << endl;
    makeStartupEnd(dumpLine);
    makeSubEnd();
    stGroupId++;
  }
  return;
} 



void printNames(char *canonicalName, char *alias){
  char *swappedName=checkSwap(alias,canonicalName);
  if(swappedName){
    allnames << swappedName << "    " << alias << "   //Swapped from " << canonicalName  << endl;
  }
  else{
    allnames << canonicalName << "    " << alias << endl;
  }
}

void loadStoredEpics(char *epicsFile){
  //Read in all EPICS names and aliases from a file 
  FILE *fp;
  char line[200];                 //to scan lines from the file
  int nline=0;
  char fstring[2][100];

  
  if(!haveStoredEpics){  
    cout << endl;
    cout << "Loading stored names: "  << epicsFile << endl;
    if((fp=fopen(epicsFile,"r"))==NULL){
      cout << "" << endl;
      cout << "Fatal Error: " << epicsFile << " not found." << endl;
      exit;
    }
    
    while(fgets(line,200,fp) != NULL){		// check got a line from file
      nline++;
      if((line[0] == '*')||(line[0] == '#')||(line[0]=='\n')) continue;    // skip comments and blank lines
      if(sscanf(line,"%s%s",fstring[ORIG_CSC],fstring[ALIAS])!=2){
	cout << "Error, not enough parameters on line " << nline << epicsFile << endl;
	exit;
      }
      for(int n=0;n<2;n++){
	//	cout << " " << strlen(fstring[n]) << endl;
	allepics[nStored][n]=new char [strlen(fstring[n])+1];
	strcpy(allepics[nStored][n],fstring[n]);
      }
      nStored++;
    }
    haveStoredEpics=1;
  }
  fclose(fp);
}


void makeStartupStart(const char *startupFile,const char *comment){
  int n=0;
  time_t rawtime;
  time (&rawtime);
  
  stfile.open(startupFile);
  while(stFileHeading[n]){
    stfile << stFileHeading[n++] << endl;
    if(n==1) stfile << "#" << endl << "#This file was autogenerated by mkHVEpics on: " << ctime (&rawtime) << "#" << comment << endl << "#" << endl;
  }
}

void makeStartupEnd(char *lastlines){
  int n=0;
  while(stFileTail[n]){
    stfile << stFileTail[n++] << endl;
  }
  if(lastlines) stfile << lastlines << endl;
  stfile.close();
}

void makeStartupAddCrateFromList(int crate){
  stfile << "# " << crateName[crate] << " ###" << endl;
  stfile << "Start_CAEN(" << crate << ", \"" << subnet << crateIP[crate] << "\")" << endl << endl;

}
void makeStartupAddCrate(char *name, char *ip, int index){
  stfile << "# " << name << " ###" << endl;
  stfile << "Start_CAEN(" << index << ", \"" << ip << "\")" << endl << endl;
}

void makeSubStart(const char *subFile,const char *comment){
  int n=0;
  time_t rawtime;
  time (&rawtime);
  
  subfile.open(subFile);
  subfile << "#" << endl << "#This file was autogenerated by mkHVEpics.C on: " << ctime (&rawtime) << "#" << comment << endl << "#" << endl;
  while(subFileHeading[n]){
    subfile << subFileHeading[n++] << endl;
  }
}

void makeSubAddLine(int cr,char *name, char *alias, char *crname){
  char subline[200];
  int slot,chan;
  char detabbr[50];
  char element[50];
  int n=0;
  int cs;
  int com;
  
  //get slot, channel, from name (like this: B_HVECAL1_SL00_CH01);
  sscanf(strstr(name,"_SL"),"_SL%d_CH%d",&slot,&chan);

  //get det name and element from alias (eg "B_HV_ECAL_SEC1_UI_E01" -> "ECAL", "SEC1_UI_E01")
  strcpy(detabbr,strstr(alias,"B_HV_")+5);  //copy this part to detabbr: "ECAL_SEC1_UI_E01"
  strcpy(element,strstr(detabbr,"_")+1);    //copy this part to element:  "SEC1_UI_E01"
  sprintf(strstr(detabbr,"_"),"");          //Terminate after the "ECAL" part
  
  if(crname) sprintf(subline,"\t\t{\"%02d\",\t\"%s\",\t\"%02d\",\t\"%02d\",\t\"HV\",\t\"%s\",\t\"%s\"",cr,crname,slot,chan,detabbr,element);
  else sprintf(subline,"\t\t{\"%02d\",\t\"%s\",\t\"%02d\",\t\"%02d\",\t\"HV\",\t\"%s\",\t\"%s\"",cr,crateName[cr],slot,chan,detabbr,element);
  subfile << subline;

  cs = cr + (slot<<8);
  subfile << ",\t\"#C" << cs << "\""; 
  while(command_codes[n]!=-1){
    com= chan+ (command_codes[n]<<8);
    subfile <<  ", \"S" << com << "\"";
    n++;
  }
  subfile << "}"<< endl;
}

void makeSubEnd(){
  int n=0;
  while(subFileTail[n]){
    subfile << subFileTail[n++] << endl;
  }
  subfile.close();
}

void printHierarchy(int det, const char **SysFull, const char **SysAbbr, int level){
  //print out the heirarchy so we understand

  cout << "Doing " <<  DetFull[det] << " ..." << endl;
  allnames << "# Structure of the HV For the " << DetFull[det] << "(Abbr:" << DetAbbr[det] << ")" << endl;
  allnames << "# Geographical:\n#" << endl;
  allnames << "# " <<  GeogFull[CRATE] << " (Abbr: " << GeogAbbr[CRATE] << ")" << endl;
  allnames << "#\t " <<  GeogFull[SLOT] << " (Abbr: " << GeogAbbr[SLOT] << ")" << endl;
  allnames << "#\t\t " <<  GeogFull[CHANNEL] << " (Abbr: " << GeogAbbr[CHANNEL] << ")" << endl;
  allnames << endl;
  allnames << "#Detector based: " <<  endl;

  for(int d=0;d<=level;d++){
    allnames << "# "; for(int t=0;t<d;t++) allnames << "\t";
    allnames << SysFull[d] << " (Abbr: " << SysAbbr[d] << ")" << endl;
  }

  allnames << endl;
}

