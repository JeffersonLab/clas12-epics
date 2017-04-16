
/* sy1527.h - EPICS driver support for CAEN SY1527 HV mainframe */

/* data structures */

#define MAX_CAEN_NAME  81
#define MAX_SLOT  16
#define MAX_CHAN  32
#define MAX_PARAM 40
/// my_n_smi:
#define MAX_BOARDPARTS 24

#define MAX_HVPS        50
#define CAENHV_OK       0
#define CAENHV_SYSERR   1

#define LINKTYPE_TCPIP              0
#define LINKTYPE_RS232              1
#define LINKTYPE_CAENET             2

#define PARAM_TYPE_NUMERIC          0
#define PARAM_TYPE_ONOFF            1
#define PARAM_TYPE_CHSTATUS         2
#define PARAM_TYPE_BDSTATUS         3

///#define CRATE_PREFIX "sy1527_%03d"  /// my:
#define CRATE_LABEL "B_HV%03d" /// my:

/// statuses: my: smi 
/// Channel is on
#define BIT_ON 1 
/// 1 Channel is ramping up
#define BIT_RAMPUP 1 << 1 
/// 2 Channel is ramping down
#define BIT_RAMPDOWN 1 << 2
/// 3 Channel is in overcurrent
#define BIT_OVERCUR 1 << 3 
/// 4 Channel is in overvoltage
#define BIT_OVERVOLT 1 << 4 
/// 5 Channel is in undervoltage
#define BIT_UNDERVOLT 1 << 5 
/// 6 Channel is in external trip
#define BIT_EXTTRIP 1 << 6 
/// 7 Channel is in max V
#define BIT_MAXVOLT 1 << 7 
/// 8 Channel is in external disable
#define BIT_EXTDISABLED 1 << 8 
/// 9 Channel is in internal trip
#define BIT_INTTRIP 1 << 9 
/// 10 Channel is in calibration error
#define BIT_CALIBERROR 1 << 10 
/// 11 Channel is unplugged
#define BIT_CHUNPLAGGED 1 << 11
/// my: 
#define BIT_OFF 1 << 11
/// my_n_smi:
#define BIT_CRATE_OFF 1 << 12
#define BIT_BOARD_NOT_PRESENT 1 << 13 
#define BIT_CRATE_OFF_ON_WAY 1 << 14

/// 12 ... 31 Reserved, forced to 0



///==============================================================================
int  CAENHVInitSystem(const char *SystemName, int LinkType, void *Arg,
                      const char *UserName, const char *Passwd);

int  CAENHVDeinitSystem(const char *SystemName);

char *CAENHVGetError(const char *SystemName);

int  CAENHVGetCrateMap(const char *SystemName, ushort *NrOfSlot,
                      ushort **NrofChList, char **ModelList,
                      char **DescriptionList, ushort **SerNumList,
                      unsigned char **FmwRelMinList, 
                      unsigned char **FmwRelMaxList);

int  CAENHVGetChParam(const char *SystemName, ushort slot, const char *ParName,
                      ushort ChNum, const ushort *ChList, void *ParValList);

int  CAENHVSetChParam(const char *SystemName, ushort slot, const char *ParName,
                      ushort ChNum, const ushort *ChList, void *ParValue);

int  CAENHVGetChParamInfo(const char *SystemName, ushort slot, ushort Ch,
                      char **ParNameList);

int  CAENHVGetChParamProp(const char *SystemName, ushort slot, ushort Ch,
                      const char *ParName, const char *PropName, void *retval);

int  CAENHVGetSysProp(const char *SystemName, const char *PropName, void *Result);

///==============================================================================



typedef struct thread
{
  int threadid;
  struct timespec   start;
  struct timespec   end;
} THREAD;


typedef struct channel
{
  char          name[MAX_CAEN_NAME];
  float         fval[MAX_PARAM];
  unsigned long lval[MAX_PARAM];
  int           setflag[MAX_PARAM]; /* if 1, n:eed to write */
} CHANNEL;

typedef struct board
{
  int           nchannels;
  char          modelname[MAX_CAEN_NAME];
  char          description[MAX_CAEN_NAME];
  int           sernum;
  int           relmax;
  int           relmin;
  int           nparams;
  char          parnames[MAX_PARAM][MAX_CAEN_NAME];
  unsigned long partypes[MAX_PARAM];
  CHANNEL       channel[MAX_CHAN];
  int           setflag; /* if 1, need to write */
  int V0Set;
  int I0Set;
  int V1Set;
  int I1Set;
  int RUp;
  int RDWn;
  int Trip;
  int SVMax;
  int VMon;
  int IMon;
  int Status;
  int Pw;
  int PwEn;
  int TripInt;
  int TripExt;
  int PDwn;
  int Tdrift;
  int RUpTime;
  int RDwTime;
  int UNVThr;
  int OVVThr;
  int VCon;
  int Temp;
  int ChToGroup;
  int OnGrDel;
  int OffGrDel;
  int Intck;
} BOARD;

typedef struct sys
{
  int   id;
  char  name[MAX_CAEN_NAME];
  int   nslots;
  BOARD board[MAX_SLOT];
  int   setflag; /* if 1, need to write */
  char  IPADDR[MAX_CAEN_NAME]; /// my:
  char  ModelName[MAX_CAEN_NAME];
  char  SwRelease[MAX_CAEN_NAME];
  char  HVFanStat[MAX_CAEN_NAME];
  char  HVFanSpeed[MAX_CAEN_NAME];
  char  PWFanStat[MAX_CAEN_NAME];
  char  HvPwSM[MAX_CAEN_NAME];
  char  PWVoltage[MAX_CAEN_NAME];
} HV;

int boards_status[MAX_HVPS][MAX_SLOT][MAX_BOARDPARTS]; /// my: smi temporal: should be dynamic

void printBoard(BOARD bb);

/* functions */

int
sy1527Measure2Demand(unsigned int id, unsigned int board);
int
sy1527GetBoard(unsigned int id, unsigned int board);
int
sy1527SetBoard(unsigned int id, unsigned int board);
int
sy1527GetMap(unsigned int id);
int
sy1527PrintMap(unsigned int id);
int
sy1527PrintParams(unsigned int id);
int
sy1527PrintSysProp(unsigned int id,const char* prop);
int
sy1527PrintSysProps(unsigned int id);
int
sy1527GetSystemProps(unsigned int id);
void *
sy1527MainframeThread(void *arg);
int
sy1527Init();
int
sy1527Start(unsigned id, char *ip_address);
int
sy1527Stop(unsigned id);

int
sy1527SetMainframeOnOff(unsigned int id, unsigned int on_off);

int
sy1527GetHeartBeat(unsigned int id, unsigned int board,
                           unsigned int chan);
int
sy1527GetMainframeStatus(unsigned int id, int *active, int *onoff, int *alarm);

int
sy1527SetChannelDemandVoltage(unsigned int id, unsigned int board,
                              unsigned int chan, float u);
float
sy1527GetChannelDemandVoltage(unsigned int id, unsigned int board,
                              unsigned int chan);
int
sy1527SetChannelMaxVoltage(unsigned int id, unsigned int board,
                           unsigned int chan, float u);
float
sy1527GetChannelMaxVoltage(unsigned int id, unsigned int board,
                           unsigned int chan);
int
sy1527SetChannelMaxCurrent(unsigned int id, unsigned int board,
                           unsigned int chan, float u);
float
sy1527GetChannelMaxCurrent(unsigned int id, unsigned int board,
                           unsigned int chan);
float
sy1527GetChannelMeasuredVoltage(unsigned int id, unsigned int board,
                                unsigned int chan);
float
sy1527GetChannelMeasuredCurrent(unsigned int id, unsigned int board,
                                unsigned int chan);
int
sy1527SetChannelRampUp(unsigned int id, unsigned int board, unsigned int chan,
                       float u);
float
sy1527GetChannelRampUp(unsigned int id, unsigned int board, unsigned int chan);
int
sy1527SetChannelRampDown(unsigned int id, unsigned int board,
                         unsigned int chan, float u);
float
sy1527GetChannelRampDown(unsigned int id, unsigned int board,
                         unsigned int chan);
int
sy1527SetChannelOnOff(unsigned int id, unsigned int board,
                      unsigned int chan, unsigned int u);
unsigned int
sy1527GetChannelOnOff(unsigned int id, unsigned int board,
                      unsigned int chan);
int
sy1527SetChannelEnableDisable(unsigned int id, unsigned int board,
                              unsigned int chan, unsigned int u);
unsigned int
sy1527GetChannelEnableDisable(unsigned int id, unsigned int board,
                              unsigned int chan);
unsigned int
sy1527GetChannelStatus(unsigned int id, unsigned int board,
                       unsigned int chan);
float
sy1527GetChannelTripTime(unsigned int id, unsigned int board,
                         unsigned int chan);


float
sy1527GetChannelConnectorVoltage(unsigned int id, unsigned int board,
                           unsigned int chan);
float
sy1527GetChannelTemperature(unsigned int id, unsigned int board,
                           unsigned int chan);
float
sy1527GetChannelOverVoltage(unsigned int id, unsigned int board,
                           unsigned int chan);
float
sy1527GetChannelUnderVoltage(unsigned int id, unsigned int board,
                           unsigned int chan);
int
sy1527SetChannelOverVoltage(unsigned int id, unsigned int board,
                           unsigned int chan,float u);
int
sy1527SetChannelUnderVoltage(unsigned int id, unsigned int board,
                           unsigned int chan,float u);


void
sy1527SetBoardParams(BOARD *bb);

///////////////////////////////////////////////////
///////////////////////////////////////////////////
// SMI:
int
sy1527SetBoardOnOff(unsigned int id, unsigned int slot, unsigned int on_off); 

int sy1527BoardSmiMonitor
(char *smi_obj_name, unsigned int id, unsigned int board, unsigned int first_channel, unsigned int ch_numbers);

int sy1527CrateSmiInit
(char *smi_obj_name, unsigned int id);

int sy1527BoardSmiControl
(char *smi_obj_name, unsigned int id, unsigned int first_board,
unsigned int first_channel, unsigned int ch_numbers, unsigned int onoff);

