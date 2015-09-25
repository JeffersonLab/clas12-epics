// mkHVEpics.C   Ken Livingston
// see https://clasweb.jlab.org/wiki/index.php/Slow_Control_HV_name_and_alias_tool
//
// Here's the general procedure:
// 1. Get a description from the Detector expert - eg algorithm. spreadsheet etc.
// 2. Make this into a specific function. (See below, eg ECGen() ). This needs to have
//    nested loops going through the specific heirarchy of systems for that detector
//    At the innermost level, we'll be incrementing element numbers. 
// 3. As the element number is incremented, we need to incrememt the channel, slot, crate
//    on the HV, mainframe. Again, the method of doing this will be different for every system.
//    see the examples below.
// 4. The function should construct the names according to some rules, which will more or less be the 
//    EPICS pv names and aliases.
//
// 5. There's the added option of being able to make a quick single, named crate for testing
//
// Here's how it works:
// mkHVEpics 
// 
// Usage:     ./mkHVEpics -h     Print this message
//
// Usage:     ./mkHVEpics all    Generate one big ioc startup file, and related substititions files for all defined crates.
// Usage:     ./mkHVEpics crates Generate separate ioc startup files and related substitutions files for each defined crate.
// Usage:     ./mkHVEpics groups Generate group ioc startup files and related substitutions files for each defined group
//
// Usage:     ./mkHVEpics <name> <ipaddress> [nslots] [slot1, slot2, ...]
// 
//               Generate an ioc startup and related substitutions for a single crate with speficied name, ip and slots, where
//               name           Name of Mainframe
//               ipaddress      i.p. of Mainframe
//               [nslots]:      No of slots with modules (default to all slots, and starts at slot 0 unless a list specified, see below)  
//               [slot1,slot2, ..... slotn] specific slot numbers
//
// All generated startup files will go into ../../iocBoot/ioccaenhv/
// All generated substitution files will go into ../Db/
//
// For the gory details see https://clasweb.jlab.org/wiki/index.php/Slow_Control_HV_name_and_alias_tool
// 
// 
// To compile:
// g++ -o mkHVEpics mkHVEpics.C
//
//


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <iostream>
#include <fstream>

using namespace std;
void  mkHVEpics();                 
void  mkSubFiles();
void  mkStartups(int type);
void  mkHVSingleCrateEpics(char *name=NULL, char *ip=NULL, int nslots=0, int *slots=NULL); 
void  markCSCUsed(int det, int crate, int sl, int ch);
char *checkSwap(char *alias=NULL, char *canonical=NULL);
char *checkAlias(char *name=NULL, char *alias=NULL, char *canonical=NULL);
void  printHierarchy(int det, const char **SysFull, const char **SysAbbr, int level);
void  printNames(char *canonicalName,char *alias);
void  loadStoredEpics(char *epicsFile);
void  mkStartupStart(ofstream &stfile,const char *startupFile,const char *comment, char *ioc=NULL);
void  mkStartupEnd(ofstream &stfile,char *lastlines=NULL);
void  mkStartupAddCrateFromList(ofstream &stfile,int crate);
void  mkStartupAddCrate(ofstream &stfile,char *name=NULL, char *ip=NULL, int index=0);
void  mkSubStart(ofstream &subfile,const char *comment);
void  mkSubAddLine(ofstream &subfile,int cr=0,char *name=NULL, char *alias=NULL, char *crname=NULL);
void  mkLinkIoc(char *bootdir, char *iocdir, char *linkname);
void  printUsage(char **argv);


// Some global stuff

// Pro-forma for the start and end of the startup and substitution files
const char *stFileHeading[] = {"#!../../bin/linux-x86/ioccaen",
			      "",
			       "< envPaths",
			       "",
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
			       "",
                               "asSetFilename(\"caenhv.acf\")",
                               "",
			       "iocInit()",
			       "",
                               "caPutLogInit(\"clonioc2:7011\")",
			       "",
			       NULL};

const char *subFileHeading[]= {"file \"db/caenhv.db\" {",
			       "        pattern { Cr,     CrName,        Sl,     Ch,    Sys,     Det,    Element,                CScode, pwonoff, v0set, i0set, trip,  rampup, rampdn, svmax}",
			       NULL};

const char *subFileTail[]  =  {"}",
			       NULL};


//some default values for file and directory names
char bootDir[]    = "../../iocBoot";
char iocDir[]     = "ioccaenhv";
char dbDir[]      = "../Db";

char fullHVName[] = "ALL";


// Detector spec - add new ones before NDETECTORS
enum         Detectors   { DC,  ECAL,  PCAL,  FTOF,  LTCC,   TEST, NDETECTORS};
const char  *DetAbbr[] = {"DC","ECAL","PCAL","FTOF","LTCC", "TEST", NULL     };    //Abbr. names used in PVs
const char  *HVCrate[] = {"DC","ECAL","FTOF","FTOF","ECAL", "TEST", NULL     };    //Names of HV MainFrames per detector
const char  *DetFull[] = {"Drift Chambers",                                        //Full names of detectors
			  "Calorimiter",
			  "Pre Calorimiter",
			  "Forward Time of Flight",
			  "Low Threshold Cerenkov Counter",
			  "Test crate"};

// Crate spec add new ones before NGEOG
enum             Geography { CRATE,   CRATENAME,    SLOT,   CHANNEL, NGEOG}; 

const char  *GeogMacro[] = { "Cr",    "CrName",     "SL",   "CH",      NULL };
const char  *GeogAbbr[]  = { "HV",    "CrName",     "SL",   "CH",      NULL };
const char  *GeogFull[]  = { "HV",    "CrateName",  "Slot", "Channel", NULL };


//HV - Crate, Slot, Element = same scheme for all detector formatting for output.
const char *hv_template  = "B_%s%s%d_%s%02d_%s%02d";


const char *subnet       = "129.157.167.";  //will need to change the way this is done if the are on more than one subnet

//This is the list of the defined crate names (dns names) and ip addresses - add new ones before NMAINFRAMES
//                             0,         1,          2,         3,         4,         5,        6,           7,        8,        9,          10,       11,      12,      13,      14,      15,      16,        17,         
enum            Mainframes { HVFTOF1,    HVFTOF2,   HVFTOF3,   HVFTOF4,   HVFTOF5,   HVFTOF6,   HVECAL1,   HVECAL2,   HVECAL3,   HVECAL4,   HVECAL5,   HVECAL6,   HVDC1,   HVDC2,  HVDC3,   HVDC4,   HVTEST0,   HVLTCC0,   NMAINFRAMES};
const char *crateName[]  = {"HVFTOF1",  "HVFTOF2", "HVFTOF3", "HVFTOF4", "HVFTOF5", "HVFTOF6", "HVECAL1", "HVECAL2", "HVECAL3", "HVECAL4", "HVECAL5", "HVECAL6", "HVDC1", "HVDC2","HVDC3", "HVDC4", "HVTEST0", "HVLTCC0",  NULL};
const int  crateIP[]     = {   78,        47,         46,        79,        162,       161,       53,      191,         51,       190,       55,        56,       666,     667,    668,     669,      70,        36,         -1};


//For diferent configurations of the ioc/startup files
enum        StartupTypes     { ALL,  GROUPS,   CRATES , NSTARTUPTYPES  };
const char *StartupNames[] = {"all","groups", "crates", NULL};

//The crates involved in the dfferent groups
const int EC_LTCC_Names[]  = { HVECAL1 ,  HVECAL2 ,  HVECAL3 ,  HVECAL4 ,  HVECAL5 ,  HVECAL6 ,  -1};
const int FTOF_PC_Names[]  = { HVFTOF1 ,  HVFTOF2 ,  HVFTOF3 ,  HVFTOF4 ,  HVFTOF5 ,  HVFTOF6 ,  -1};
const int DC_Names[]       = {   HVDC1 ,    HVDC2 ,    HVDC3 ,    HVDC4 ,   -1};

//and pointers to them
const int  *groupLists[]  = { EC_LTCC_Names,  FTOF_PC_Names,  DC_Names, NULL};
const char *groupNames[]  = {"EC_LTCC",      "FTOF_PC",      "DC",      NULL};
const char *groupTitles[] = {"EC and LTCC",  "FTOF and PC",  "DC",      NULL};

//The detectors involved in each grouping, when they are written as groups
int groupDets[][5] = { ECAL,  LTCC, -1, -1, -1,
			FTOF,  PCAL, -1, -1, -1,
			DC,    -1,   -1, -1, -1};

//default filenename for all the names and aliases
const char defaultAllnamesFile[] = "HV_allnames.txt";
char allnamesFile[100];

ofstream allnames;  //streams for read / write to allnamesFile

int haveStoredEpics=0;    //Flag the the names and aliases are in memory
int nStored=0;            //Number of them
char *allepics[10000][2]; //array to hold them

//Arrays and counters for the namse of substitution files
int nSubFiles=0;
int nSpareFiles=0;
char startupSubFileNames[50][200];
char startupSpareFileNames[50][200];

//For each defined mainframe allow for the possibility that all it's channels are spare and available.
enum chanState { CHAN_SPARE, CHAN_USED};
const int defaultNChan = 24;
const int defaultNSlot = 16;
int CSCstatus[NMAINFRAMES][defaultNSlot][defaultNChan];

//commands codes for CAEN  - Let's hope we can ditch this soon

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
enum swapFields{CSC, ALIAS, NEW_CSC};
char *swapTable[1000][3];  //to hold strings from the swap file;
int  nSwaps=0;
int haveSwap=0;
const char *defaultSwapFile="HVswaps.txt";
char swapFile[100];

//For single test crates where aliases are to be provided
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
	  
	  markCSCUsed(det,cr,sl,ch);
	  
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

  int maxSlot=15;
  int maxChan=17;

  int   nSide=18;
  const  char *side[] = {"","L","R"}; /// val_piece : const

  printHierarchy(det,SysFull,SysAbbr,ELEMENT);

  
  //Detector Sector,Layer, ...
      
  for(int s=1;s<=6;s++){
    for(int lr=1;lr<=2;lr++){
      for(int e=1; e<=nSide;e++){
	
	markCSCUsed(det,cr,sl,ch);
	
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
	
	markCSCUsed(det,cr,sl,ch);
	
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

  
  int maxSlot=8;
  int maxChan=23;
  
  int   nInLayer[]={ 0, 36, 36,  36,  36,  36,  36 };
  const  char *layers[] = {"","UI","UO","VI","VO","WI","WO"}; /// val_piece : const
  
  printHierarchy(det,SysFull,SysAbbr,ELEMENT);
  
  //Detector Sector,Layer, ...

  for(int s=1;s<=6;s++){
    for(int l=1;l<=6;l++){
      for(int e=1; e<=nInLayer[l];e++){

       	markCSCUsed(det,cr,sl,ch);

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

	      markCSCUsed(det,cr,sl,ch);
	      
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


//This generates a single named ioc 
int SingleCrateGen(char *name=NULL, int chans=24, int nslots=16, int *slotlist=NULL){

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
    for(int ch=0;ch<maxChan;ch++){       //elements
      
      sprintf(alias, alias_template,name,SysAbbr[SYSSLOT],s,SysAbbr[ELEMENT],ch);
      sprintf(canonicalName, can_template,name,SysAbbr[SYSSLOT],s,SysAbbr[ELEMENT],ch);
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
  
  if(argc==2) {                                        //Should be an arg for specific set of startups 
    for(int stType=0;stType<NSTARTUPTYPES;stType++){   //figure out if arg is "all", "crates" ....etc
      if(!strcmp(argv[1],StartupNames[stType])){
	mkHVEpics();                                   //make all the names and aliases
	mkSubFiles();                                  //make all the substitutions files
	mkStartups(stType);                            //make the relevant startup files
	return 0;
      }
    }
    printUsage(argv);
    return 0;
  }
  
  else if(argc >= 3) {                         //Should be arg for setting up ioc for single crate specified on command line
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
	  exit(1);
	}
      else{                                    //number the slots as specified in the args.
	for(int n=4;n<argc;n++)sscanf(argv[n],"%d,",&slots[n-4]);
      }
    }
    mkHVSingleCrateEpics(name, ip, nslots, slots);
  }
  else printUsage(argv);
  return 0; 
}



void printUsage(char **argv){
  cout << endl;
  cout << "Usage:     " << argv[0] << " -h     Print this message" << endl << endl;
  
  cout << "Usage:     " << argv[0] << " all    Generate one big ioc startup file, and related substititions files for all defined crates." << endl;
  cout << "Usage:     " << argv[0] << " crates Generate separate ioc startup files and related substitutions files for each defined crate." << endl;
  cout << "Usage:     " << argv[0] << " groups Generate group ioc startup files and related substitutions files for each defined group" << endl << endl;
  
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

//Flag that the crate,slot,channel is used, and nolonger spare (the default)
void markCSCUsed(int det, int crate, int sl, int ch){
  int cr=0;
  char crName[100];
  
  sprintf(crName,"HV%s%d",HVCrate[det],crate);  //work out the name of the crate 
  while(crateName[cr]){                         //find the index
    if(strcmp(crName,crateName[cr])==0){
      CSCstatus[cr][sl][ch]=CHAN_USED;          //mark the cr,sl,ch as used
      return;
    }
    cr++;
  }
}

//Called to check whether the element has been swapped to another channel 
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
      if(sscanf(line,"%s%s%s",fstring[CSC],fstring[ALIAS],fstring[NEW_CSC])!=3){
	cout << "Error, not enough parameters on line " << nline << " in " << swapFile << endl;
	exit(1);
      }
      cout << "Swap: " << fstring[ALIAS] << " from " << fstring[CSC] << " to " << fstring[NEW_CSC] << endl;
      strcpy(cratename,fstring[NEW_CSC]+2);
      sprintf(strstr(cratename,"_SL"),"");
      strcpy(origcratename,fstring[CSC]+2);
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
      if(sscanf(line,"%s%s",fstring[CSC],fstring[ALIAS])!=2){
	cout << "Error, not enough parameters on line " << nline << " in " << swapFile << endl;
	exit(1);
      }
      cout << "Alias: " << fstring[CSC] << " to " << fstring[ALIAS] << endl;
      
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
    if(strcmp(aliasTable[n][CSC],canonical)==0){     //found a line in the alias table
      return aliasTable[n][ALIAS];
    }
  }
  return NULL;
}



//generate ioc startup files, names and aliases for the detectors with special algorithms specified in this code.
void mkHVEpics(){
  time_t rawtime;    //to timestame auto generated files
  time (&rawtime);
  char canonicalName[64];
  char alias[64];

  //flag all crates,slots and channels as spare to start with. 
  for(int cr=0;cr<NMAINFRAMES;cr++){
    for(int sl=0;sl<defaultNSlot;sl++){
      for(int ch=0;ch<defaultNChan;ch++){
	CSCstatus[cr][sl][ch]=CHAN_SPARE;
      }
    }
  }

  
  
  strcpy(swapFile,defaultSwapFile);
  strcpy(allnamesFile,defaultAllnamesFile);
  
  checkSwap();                 //force the reading of the swap table list
  cout << "Generating names and aliases: "  << endl;
  allnames.open(allnamesFile); //open output file
  allnames << "#" << endl << "#This file was autogenerated by mkHVEpics on: " << ctime (&rawtime) << endl << "#" << endl;
  
  ECGen();  LTCCGen(); FTOFGen(); PCGen(); DCGen();  //call all the generators

  //Go over all the defined crates and assume all channels in all slots which have not been taken are alive:
  allnames << endl;
  allnames << "################################################################################" << endl << "#" << endl;
  allnames << "# Below here are the names and aliases for unused slots and elements in each MF " << endl << "#" << endl;
  allnames << "# To see if they are populated and available, look on the HV GUI " <<  endl << "#" << endl;

  cout << "Doing spare channels ..." << endl;
  
  for(int cr=0;cr<NMAINFRAMES;cr++){
    allnames << "# " << crateName[cr] << endl;
    for(int sl=0;sl<defaultNSlot;sl++){
      for(int ch=0;ch<defaultNChan;ch++){
	if(CSCstatus[cr][sl][ch]==CHAN_SPARE){
	  sprintf(alias, "B_HV_%s_SPARE_SL%02d_CH%02d",crateName[cr],sl,ch);
	  sprintf(canonicalName, "B_%s_SL%02d_CH%02d",crateName[cr],sl,ch);
	  allnames << canonicalName  << "    " << alias << endl;
	}
      }
    }
  }
  
  allnames.close();            //close output file
  //now  written all the names and aliases, taking account of any swap
  cout << endl <<  "All names and aliases saved in " << allnamesFile << endl << endl;
}

//generate startup file, names and aliases for a single ioc (usually for testing), specifcied on the command line,
//and with an optional file of aliases
void mkHVSingleCrateEpics(char *name, char *ip, int nslots, int *slots){
 
  time_t rawtime;     //to timestame auto generated files
  time (&rawtime);
  char comment[200];

  char stName[200];   //startup files
  char subName[200];  //subst filenames
  char dumpLine[200]; 
  char iocName[200]; 
  ofstream subfile;
  ofstream stfile;
  int line=0;
  
  sprintf(allnamesFile,"HV_allnames_%s.txt",name);

  checkAlias(name,NULL,NULL);   //force the reading of the alias table
  allnames.open(allnamesFile); //open output file
  allnames << "#" << endl << "#This file was autogenerated by mkHVEpics on: " << ctime (&rawtime) << endl << "#" << endl;
  
  SingleCrateGen(name, defaultNChan, nslots, slots);
  
  allnames.close();            //close output file

  sprintf(stName,"%s/%s/st.cmd.%s",bootDir,iocDir,name);
  sprintf(subName,"%s/%s.hv_substitutions",dbDir,name);
  sprintf(dumpLine,"dbDumpRecord > st.cmd.%s.dump",name); 
  sprintf(iocName,"%s_%s",iocDir,name); 
  
  if(!haveStoredEpics) loadStoredEpics(allnamesFile); //load all the names and aliases from file if required.

  cout << endl << "Generating "<< stName <<  " for HV system: " << name  << endl << endl; 

  sprintf(comment,"IOC for single mainframe:  %s",name);
  stfile.open(stName);
  mkStartupStart(stfile,stName,comment,iocName);                 // Make the startup first lines:
  
  sprintf(comment,"Substitutions for IOC for single mainframe:  %s", name);
  subfile.open(subName);
  mkSubStart(subfile,comment);                           // Make the substitution file first lines:
  
  mkStartupAddCrate(stfile,name,ip,0);
  for(int n=0;n<nStored;n++){
    mkSubAddLine(subfile,0,allepics[n][CSC],allepics[n][ALIAS],name);
  }
  stfile <<  "## Load record instances" << endl << "dbLoadTemplate(\"db/" << name << ".hv_substitutions\")" << endl;
  
  mkStartupEnd(stfile,dumpLine);
  stfile.close();

  while(subFileTail[line]){
    subfile << subFileTail[line++] << endl;
  }
  subfile.close();
  
  mkLinkIoc(bootDir,iocDir,iocName);
  
  return;
  
}

//generate ioc startup files
void mkStartups(int type){
  char cratename[100];
  char comment[100];
  int stCrateId=0;
  int stGroupId=0;
  int stDetId=0;
  char stName[200];  //startup files
  char subName[200];  //subst filenames
  char dumpLine[200]; 
  char iocName[200]; 
  char longDetName[200];
  int line=0;
  int det=0;
  ofstream stfile;                                   //output file for startups
  ofstream crateDetStream[NMAINFRAMES][NDETECTORS];  //output file for startups
  
  
  if(type==ALL){                                                        //All together in a biggie in one ioc/startup file
    sprintf(stName,"%s/%s/st.cmd.%s",bootDir,iocDir,fullHVName);        //make some file name strings etc
    sprintf(subName,"%s/%s.hv_substitutions",dbDir,fullHVName);
    sprintf(dumpLine,"dbDumpRecord > st.cmd.%s.dump",fullHVName); 
    sprintf(iocName,"%s_%s",iocDir,fullHVName); 
    
    cout << endl << "Generating "<< stName <<   " for full HV system ....." << endl << endl; 
    
    stfile.open(stName);                                                         //open the ioc startup file and
    mkStartupStart(stfile,stName,"All HV crates in single IOC", iocName);        //write the startup first lines
    
    stCrateId=0;           
    while(crateName[stCrateId]){                                 //loop over all crates    
      mkStartupAddCrateFromList(stfile,stCrateId);               //add the startup file lines for this crate
      stCrateId++;
    }
    
    stfile <<  "## Load record instances" << endl << endl;       //add some proforma stuff to the ioc
    stfile << "dbLoadRecords(\"$(DEVIOCSTATS)/db/iocAdminSoft.db\", \"IOC=$(IOC)\")" << endl<< endl;

    for(int n=0;n<nSubFiles;n++){                     //add the lines to load all the templates
      stfile << "dbLoadTemplate(\"" << startupSubFileNames[n] << "\")" << endl;
    }

    stfile << endl << "#PVs for unused slots, channels which may be available in the above crates" << endl;
    stfile << "#Comment in as required" << endl << endl;
      
    for(int n=0;n<nSpareFiles;n++){                   //add commented lines to load the spare channels for each crate
      stfile << "#dbLoadTemplate(\"" << startupSpareFileNames[n] << "\")" << endl;
    }
    
    mkStartupEnd(stfile,dumpLine);
    stfile.close();
    mkLinkIoc(bootDir,iocDir,iocName);

  }
  else if(type==CRATES){                                                       //All together in a biggie in one ioc/startup file
    stCrateId=0;
    cout << endl << "Generating startups for each Mainframe:" << endl;
    while(crateName[stCrateId]){                                               //for each crate in the list
      sprintf(stName,"%s/%s/st.cmd.%s",bootDir,iocDir,crateName[stCrateId]);   //make some file name strings etc
      sprintf(subName,"%s/%s.hv_substitutions",dbDir,crateName[stCrateId]);
      sprintf(dumpLine,"dbDumpRecord > st.cmd.%s.dump",crateName[stCrateId]); 
      sprintf(iocName,"%s_%s",iocDir,crateName[stCrateId]); 
      
      cout << "   " << stName << " and " << subName <<  " ....." << endl ; 
      
      sprintf(comment,"Crate name: %s",crateName[stCrateId]);                  //make crate specific comment
      stfile.open(stName);                                                     //open the ioc startup file and
      mkStartupStart(stfile,stName,comment,iocName);                           //write the startup first lines
       
      mkStartupAddCrateFromList(stfile,stCrateId);                  //add the startup file lines for this crate

      stfile <<  "## Load record instances" << endl << endl;       //add some proforma stuff to the ioc
      stfile << "dbLoadRecords(\"$(DEVIOCSTATS)/db/iocAdminSoft.db\", \"IOC=$(IOC)\")" << endl<< endl;

      sprintf(longDetName,"%s_",crateName[stCrateId]);   // Make the "this_crate" -> "this_crate_" for string uniqueness  
      for(int n=0;n<nSubFiles;n++){                      // find all substitution files with "this_crate_" string in name
	if(strstr(startupSubFileNames[n],longDetName)){
	  stfile << "dbLoadTemplate(\"" << startupSubFileNames[n] << "\")" << endl; //and add a line in the startup to load them.
	}
      }

      stfile << endl << "#PVs for unused slots, channels which may be available in the above crates" << endl;
      stfile << "#Comment in as required" << endl << endl;
      
      for(int n=0;n<nSpareFiles;n++){                    //as above, but for all "this_crate_SPARES" substitutions
	sprintf(longDetName,"%s_SPARES",crateName[stCrateId]);
	if(strstr(startupSpareFileNames[n],longDetName)){
	  stfile << "#dbLoadTemplate(\"" << startupSpareFileNames[n] << "\")" << endl; //add a commented out line for each
	}
      }
      
      mkStartupEnd(stfile,dumpLine);                     //write end lines and close the ioc startup file
      stfile.close();

      mkLinkIoc(bootDir,iocDir,iocName);                 //link the file to make a unique ioc directory.
      
      stCrateId++;
    }
  }
  
  else if(type==GROUPS){     //An ioc for each group where detectors share crates.
    
    cout << endl << "Generating startups each of the systems sharing Mainframes:" << endl;
    
    while(groupLists[stGroupId]){                                                 //for each defined group
      stCrateId=0;
      sprintf(stName,"%s/%s/st.cmd.%s",bootDir,iocDir,groupNames[stGroupId]);     //make some file name strings etc
      sprintf(subName,"%s/%s.hv_substitutions",dbDir,groupNames[stGroupId]);
      sprintf(dumpLine,"dbDumpRecord > st.%s.dump",groupNames[stGroupId]); 
      sprintf(iocName,"%s_%s",iocDir,groupNames[stGroupId]); 
      
      sprintf(comment,"Group name: %s (all crates for %s)",groupNames[stGroupId],groupTitles[stGroupId]);
      stfile.open(stName);                                                        //open the ioc startup file and
      mkStartupStart(stfile,stName,comment, iocName);                             //write the startup first lines                           
      
      cout << "   " << stName <<  " ....." << endl ; 
      
      while(groupLists[stGroupId][stCrateId] != -1){                                //go over all the crates in the group
	mkStartupAddCrateFromList(stfile,groupLists[stGroupId][stCrateId]);       //add the startup file lines for this crate 
	stCrateId++;
      }
      
      stfile <<  "## Load record instances" << endl << endl;       //add some proforma stuff to the ioc
      stfile << "dbLoadRecords(\"$(DEVIOCSTATS)/db/iocAdminSoft.db\", \"IOC=$(IOC)\")" << endl<< endl;

      stCrateId=0;
      while(groupLists[stGroupId][stCrateId]!=-1){                      //go over all the crates in the group
	det=0;
	while(groupDets[stGroupId][det] !=-1){	                                        //for each detector in the group, make name
	  sprintf(longDetName,"%s_%s",crateName[groupLists[stGroupId][stCrateId]],DetAbbr[groupDets[stGroupId][det]]);
	  for(int n=0;n<nSubFiles;n++){                                                 //and find subst. file
	    if(strstr(startupSubFileNames[n],longDetName)){                             //by comparing with list
	      stfile << "dbLoadTemplate(\"" << startupSubFileNames[n] << "\")" << endl; //add a line in the startup to load subst. file
	    }
	  }
	  det++;
	}
	stCrateId++;
      }

      stfile << endl << "#PVs for unused slots, channels which may be available in the above crates" << endl;
      stfile << "#Comment in as required" << endl << endl;
      

      stCrateId=0;
      while(groupLists[stGroupId][stCrateId]!=-1){                      //go over all the crates in the group
	sprintf(longDetName,"%s_SPARES",crateName[groupLists[stGroupId][stCrateId]]);
	for(int n=0;n<nSpareFiles;n++){                                 //as above, but for all "this_crate_SPARES" substitutions
	  if(strstr(startupSpareFileNames[n],longDetName)){
	    stfile << "#dbLoadTemplate(\"" << startupSpareFileNames[n] << "\")" << endl; //add a commented out line for each
	  }
	}
	stCrateId++;
      }
      
      mkStartupEnd(stfile,dumpLine);
      stfile.close();
      
      mkLinkIoc(bootDir,iocDir,iocName);

      stGroupId++;
    }
  }
  else{
    return;
  }
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
      exit(1);
    }
    
    while(fgets(line,200,fp) != NULL){		// check got a line from file
      nline++;
      if((line[0] == '*')||(line[0] == '#')||(line[0]=='\n')) continue;    // skip comments and blank lines
      if(sscanf(line,"%s%s",fstring[CSC],fstring[ALIAS])!=2){
	cout << "Error, not enough parameters on line " << nline << epicsFile << endl;
	exit(1);
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


void mkStartupStart(ofstream &stfile,const char *startupFile,const char *comment, char *ioc){
  int n=0;
  time_t rawtime;
  time (&rawtime);
  char iocline[100];
  
  while(stFileHeading[n]){
    stfile << stFileHeading[n++] << endl;
    if(n==1) stfile << "#" << endl << "#This file was autogenerated by mkHVEpics on: " << ctime (&rawtime) << "#" << comment << endl << "#" << endl;
    
    //if we've just printed the envPATHS line, override the IOC if required
    if(ioc&&strstr(stFileHeading[n-1],"envPaths")){
      sprintf(iocline,"epicsEnvSet(\"IOC\",\"%s\")",ioc);
      stfile << iocline  << endl;
    }
  }
}

void mkStartupEnd(ofstream &stfile,char *lastlines){
  int n=0;
  while(stFileTail[n]){
    stfile << stFileTail[n++] << endl;
  }
  if(lastlines) stfile << lastlines << endl;
}

void mkStartupAddCrateFromList(ofstream &stfile,int crate){
  stfile << "# " << crateName[crate] << " ###" << endl;
  stfile << "Start_CAEN(" << crate << ", \"" << subnet << crateIP[crate] << "\")" << endl << endl;

}

void mkStartupAddCrate(ofstream &stfile,char *name, char *ip, int index){
  stfile << "# " << name << " ###" << endl;
  stfile << "Start_CAEN(" << index << ", \"" << ip << "\")" << endl << endl;
}



void mkSubFiles(){
  char cratename[100];
  char comment[100];
  int stCrateId=0;
  int stGroupId=0;
  int stDetId=0;
  char stName[200];  //startup files
  char subName[200];  //subst filenames
  char dumpLine[200]; 
  char iocName[200]; 
  char longDetName[200];
  int line=0;
  int g=0;
  ofstream stfile;                                   //output file for startups
  ofstream crateDetStream[NMAINFRAMES][NDETECTORS];  //output file for startups
  ofstream crateSpareStream[NMAINFRAMES];
  

  
  if(!haveStoredEpics) loadStoredEpics(allnamesFile); //load all the names and aliases from file if required.
  //make all the substitution files

  cout << "Generating substitution (ie macro) files for all system:" << endl;
  cout << "Note: *_SPARES.hv_substitutions files will be commented out in ioc startup files for optional inclusion"  << endl;
  
  stCrateId=0;
  //loop over all the Mainframes
  while(crateName[stCrateId]){         // loop over all crates
    for(int n=0;n<nStored;n++){
      if((strstr(allepics[n][CSC],crateName[stCrateId]))&&(strstr(allepics[n][ALIAS],"SPARE"))){ //if this crate, and the alias has the word SPARE
	if(!crateSpareStream[stCrateId].is_open()){                                              //if the files not open yet	    
	  sprintf(subName,"%s/%s_SPARES.hv_substitutions",dbDir,crateName[stCrateId]);                     //make the name and
	  crateSpareStream[stCrateId].open(subName);                                                       //open the file
	  cout << "Writing " << subName << endl;
	  sprintf(comment,"Substitutions for crate: %s SPARES",crateName[stCrateId]);                      //make the comment
	  mkSubStart(crateSpareStream[stCrateId],comment);                                                 //write the start lines to the file
	  sprintf(startupSpareFileNames[nSpareFiles++],"db/%s_SPARES.hv_substitutions",crateName[stCrateId]);  //make the name for the line in startup files to load the subs
	}
	mkSubAddLine(crateSpareStream[stCrateId],stCrateId,allepics[n][CSC],allepics[n][ALIAS]);  //add the macros for this line
      }
    }
    stDetId=0;
    while(DetAbbr[stDetId]){             // loop over all detectors    
      for(int n=0;n<nStored;n++){
	sprintf(longDetName,"_%s_",DetAbbr[stDetId]);
	if(strstr(allepics[n][CSC],crateName[stCrateId]) && strstr(allepics[n][ALIAS],longDetName)){	//if name contains crate name and alias contains detector name
	  if(!crateDetStream[stCrateId][stDetId].is_open()){                                            //if the files not open yet
	    sprintf(subName,"%s/%s_%s.hv_substitutions",dbDir,crateName[stCrateId],DetAbbr[stDetId]);   //make the name and
	    cout << "Writing " << subName << endl;
	    crateDetStream[stCrateId][stDetId].open(subName);                                                          //open the file
	    sprintf(comment,"Substitutions for crate: %s,  detector: %s",crateName[stCrateId],DetAbbr[stDetId]);       //make the comment
	    mkSubStart(crateDetStream[stCrateId][stDetId],comment);                                                  //write the start lines to the file
	    sprintf(startupSubFileNames[nSubFiles++],"db/%s_%s.hv_substitutions",crateName[stCrateId],DetAbbr[stDetId]);  //make the name for the line in startup files to load the subs
	  }
	  mkSubAddLine(crateDetStream[stCrateId][stDetId],stCrateId,allepics[n][CSC],allepics[n][ALIAS]);  //add the macros for this line
	}
      }
      stDetId++;
    }
    stCrateId++;
  }
  stCrateId=0;
  
  while(crateName[stCrateId]){         // loop over all crates, and detectors, print endings and close open files
    if(crateSpareStream[stCrateId].is_open()){
      line=0;
      while(subFileTail[line]){
	crateSpareStream[stCrateId] << subFileTail[line++] << endl;
      }
      crateSpareStream[stCrateId].close();
    }
    stDetId=0;
    while(DetAbbr[stDetId]){    
      if(crateDetStream[stCrateId][stDetId].is_open()){
	line=0;
	while(subFileTail[line]){
	  crateDetStream[stCrateId][stDetId] << subFileTail[line++] << endl;
	}
	crateDetStream[stCrateId][stDetId].close();
      }
      stDetId++; 
    }
    stCrateId++;
  }
  
}



void mkSubStart(ofstream &subfile,const char *comment){
  int n=0;
  time_t rawtime;
  time (&rawtime);
  
  subfile << "#" << endl << "#This file was autogenerated by mkHVEpics.C on: " << ctime (&rawtime) << "#" << comment << endl << "#" << endl;
  while(subFileHeading[n]){
    subfile << subFileHeading[n++] << endl;
  }
}

void mkSubAddLine(ofstream &subfile,int cr,char *name, char *alias, char *crname){
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


void mkLinkIoc(char *bootdir, char *iocdir, char *linkname){
  char linkCommand[200]; 

  cout << "Linking " << bootdir << "/" << iocdir << " as " <<  bootdir << "/" << linkname << endl;
  sprintf(linkCommand,"cd %s; ln -T -s %s %s",bootdir,iocdir,linkname);
  system(linkCommand);
  cout << endl;
}
