/***************************************************************************/
/*                                                                         */
/*        --- CAEN Engineering Srl - Computing Systems Division ---        */
/*                                                                         */
/*    CAENHVWRAPPER.H                                                      */
/*                                                                         */
/*                                                                         */
/*    Source code written in ANSI C                                        */
/*                                                                         */ 
/*    Created:  March 2000                                                 */
/*                                                                         */
/***************************************************************************/

#ifndef __CAENHVWRAPPER_H
#define __CAENHVWRAPPER_H

#include "caenhvoslib.h"

#ifndef uchar 
#define uchar unsigned char
#endif
#ifndef ushort 
#define ushort unsigned short
#endif
#ifndef ulong
#define ulong unsigned long
#endif

#define MAX_CH_NAME                12
 
#define MAX_PARAM_NAME             10

#define MAX_CRATES                             8
#define MAX_SLOTS                             32
#define MAX_BOARDS    ( MAX_SLOTS * MAX_CRATES )

#define MAX_BOARD_NAME             12
#define MAX_BOARD_DESC             28 
#define SET                         1
#define MON                         0
#define SIGNED                      1
#define UNSIGNED                    0

#define PARAM_TYPE_NUMERIC          0
#define PARAM_TYPE_ONOFF            1
#define PARAM_TYPE_CHSTATUS         2
#define PARAM_TYPE_BDSTATUS         3

#define PARAM_MODE_RDONLY           0
#define PARAM_MODE_WRONLY           1
#define PARAM_MODE_RDWR             2

#define PARAM_UN_NONE               0
#define PARAM_UN_AMPERE             1
#define PARAM_UN_VOLT               2
#define PARAM_UN_WATT               3
#define PARAM_UN_CELSIUS            4
#define PARAM_UN_HERTZ              5
#define PARAM_UN_BAR                6
#define PARAM_UN_VPS                7
#define PARAM_UN_SECOND             8
#define PARAM_UN_RPM                9             // Rel. 1.4
#define PARAM_UN_COUNT             10             // Rel. 2.6

#define SYSPROP_TYPE_STR            0
#define SYSPROP_TYPE_REAL           1
#define SYSPROP_TYPE_UINT2          2
#define SYSPROP_TYPE_UINT4          3
#define SYSPROP_TYPE_INT2           4
#define SYSPROP_TYPE_INT4           5
#define SYSPROP_TYPE_BOOLEAN        6

#define SYSPROP_MODE_RDONLY         0
#define SYSPROP_MODE_WRONLY         1
#define SYSPROP_MODE_RDWR           2

/*-----------------------------------------------------------------------------
                                                                             
                             ERROR    CODES                                 
                                                                             
  Their meaning is the next:                                                 
   CODES                                                                     
     0    Command wrapper correctly executed                                 
     1    Error of operatived system                                         
     2    Write error in communication channel                               
     3    Read error in communication channel                                
     4    Time out in server communication                                   
     5    Command Front End application is down                              
     6    Comunication with system not yet connected by a Login command      
     7    Execute Command not yet implementated                              
     8    Get Property not yet implementated                                 
     9    Set Property not yet implementated                                 
     10   Communication with RS232 not yet implementated                     
     11   User memory not sufficient                                          
	 12   Value out of range
     13   Property not yet implementated
     14   Property not found
     15   Execute command not found
     16   No System property
     17   No get property
     18   No set property
     19   No execute command
     20   configuration change
     21   Property of param not found
     22   Param not found
 -----------------------------------------------------------------------------*/
#define CAENHV_OK                   0
#define CAENHV_SYSERR               1
#define CAENHV_WRITEERR             2
#define CAENHV_READERR              3
#define CAENHV_TIMEERR              4
#define CAENHV_DOWN                 5
#define CAENHV_NOTPRES              6
#define CAENHV_SLOTNOTPRES          7
#define CAENHV_NOSERIAL             8
#define CAENHV_MEMORYFAULT          9
#define CAENHV_OUTOFRANGE           10
#define CAENHV_EXECCOMNOTIMPL       11
#define CAENHV_GETPROPNOTIMPL       12
#define CAENHV_SETPROPNOTIMPL       13
#define CAENHV_PROPNOTFOUND         14
#define CAENHV_EXECNOTFOUND         15
#define CAENHV_NOTSYSPROP		        16
#define CAENHV_NOTGETPROP		        17
#define CAENHV_NOTSETPROP           18
#define CAENHV_NOTEXECOMM           19
#define CAENHV_SYSCONFCHANGE	      20
#define CAENHV_PARAMPROPNOTFOUND    21
#define CAENHV_PARAMNOTFOUND        22
#define CAENHV_CONNECTED	         (0x1000 + 1)
#define CAENHV_NOTCONNECTED	       (0x1000 + 2)
#define CAENHV_OS    	             (0x1000 + 3)
#define CAENHV_LOGINFAILED         (0x1000 + 4)
#define CAENHV_LOGOUTFAILED        (0x1000 + 5)
#define CAENHV_LINKNOTSUPPORTED    (0x1000 + 6)  // Rel. 1.2

/* Link Types for InitSystem */
#define LINKTYPE_TCPIP		  0
#define LINKTYPE_RS232		  1
#define LINKTYPE_CAENET		  2

#ifndef __CAENHVRESULT__                         /* Rel. 2.0 - Linux */
/* The Error Code type */
typedef int CAENHVRESULT;
#define __CAENHVRESULT__
#endif

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

CAENHVLIB_API char         *CAENHVGetError(const char *SystemName);

CAENHVLIB_API char         *CAENHVLibSwRel(void);

CAENHVLIB_API CAENHVRESULT  CAENHVInitSystem(const char *SystemName, 
 int LinkType, void *Arg, const char *UserName, const char *Passwd);

CAENHVLIB_API CAENHVRESULT  CAENHVDeinitSystem(const char *SystemName);

CAENHVLIB_API CAENHVRESULT  CAENHVGetChName(const char *SystemName, ushort slot, 
 ushort ChNum, const ushort *ChList, char (*ChNameList)[MAX_CH_NAME]);

CAENHVLIB_API CAENHVRESULT  CAENHVSetChName(const char *SystemName, ushort slot, 
 ushort ChNum, const ushort *ChList, const char *ChName);

CAENHVLIB_API CAENHVRESULT  CAENHVGetChParamInfo(const char *SystemName, 
 ushort slot, ushort Ch, char **ParNameList);

CAENHVLIB_API CAENHVRESULT  CAENHVGetChParamProp(const char *SystemName, 
 ushort slot, ushort Ch, const char *ParName, const char *PropName, void *retval);

CAENHVLIB_API CAENHVRESULT  CAENHVGetChParam(const char *SystemName, ushort slot, 
 const char *ParName, ushort ChNum, const ushort *ChList, void *ParValList);

CAENHVLIB_API CAENHVRESULT  CAENHVSetChParam(const char *SystemName, ushort slot, 
 const char *ParName, ushort ChNum, const ushort *ChList, void *ParValue);

CAENHVLIB_API CAENHVRESULT  CAENHVTestBdPresence(const char *SystemName, 
 ushort slot, ushort *NrofCh, char *Model, char *Description, ushort *SerNum, 
 uchar *FmwRelMin, uchar *FmwRelMax);

CAENHVLIB_API CAENHVRESULT  CAENHVGetBdParamInfo(const char *SystemName, 
 ushort slot, char **ParNameList);

CAENHVLIB_API CAENHVRESULT  CAENHVGetBdParamProp(const char *SystemName, 
 ushort slot, const char *ParName, const char *PropName, void *retval);

CAENHVLIB_API CAENHVRESULT  CAENHVGetBdParam(const char *SystemName, 
 ushort slotNum, const ushort *slotList, const char *ParName, void *ParValList);

CAENHVLIB_API CAENHVRESULT  CAENHVSetBdParam(const char *SystemName, 
 ushort slotNum, const ushort *slotList, const char *ParName, void *ParValue);

CAENHVLIB_API CAENHVRESULT  CAENHVGetGrpComp(const char *SystemName, ushort group, 
 ushort *NrOfCh, ulong **ChList);

CAENHVLIB_API CAENHVRESULT  CAENHVAddChToGrp(const char *SystemName, ushort group, 
 ushort NrOfCh, const ulong *ChList);

CAENHVLIB_API CAENHVRESULT  CAENHVRemChToGrp(const char *SystemName, ushort group, 
 ushort NrOfCh, const ulong *ChList);

CAENHVLIB_API CAENHVRESULT  CAENHVGetGrpParam(const char *SystemName, ushort Group, 
 ushort NrOfPar, const uchar **ParNameList, void *ParValList);

CAENHVLIB_API CAENHVRESULT  CAENHVSetGrpParam(const char *SystemName, ushort Group, 
 const uchar *ParName, void *ParVal);

CAENHVLIB_API CAENHVRESULT  CAENHVGetCrateMap(const char *SystemName,	
 ushort *NrOfSlot, ushort **NrofChList, char **ModelList, char **DescriptionList,
 ushort **SerNumList, uchar **FmwRelMinList, uchar **FmwRelMaxList);

CAENHVLIB_API CAENHVRESULT  CAENHVGetExecCommList(const char *SystemName,
 ushort *NumComm, char **CommNameList);

CAENHVLIB_API CAENHVRESULT  CAENHVExecComm(const char *SystemName, 
 const char *CommName);

CAENHVLIB_API CAENHVRESULT  CAENHVGetSysPropList(const char *SystemName, 
 ushort *NumProp, char **PropNameList);

CAENHVLIB_API CAENHVRESULT  CAENHVGetSysPropInfo(const char *SystemName, 
 const char *PropName, unsigned *PropMode, unsigned *PropType);

CAENHVLIB_API CAENHVRESULT  CAENHVGetSysProp(const char *SystemName, 
 const char *PropName, void *Result);

/* Rel. 1.2 */
CAENHVLIB_API CAENHVRESULT  CAENHVSetSysProp(const char *SystemName, 
 const char	*PropName, void *Set);

/* Rel. 1.1 */
CAENHVLIB_API CAENHVRESULT CAENHVCaenetComm(const char *SystemName, 
 ushort Crate, ushort Code, ushort NrWCode, ushort *WCode, short *Result,
 ushort *NrOfData, ushort **Data);

#ifdef __cplusplus
}
#endif /* __cplusplus */

/* ------------------------------------------------------ !!! CAEN */
/*
#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>
*/
/* ------------------------------------------------------ !!! CAEN */


#endif /* __CAENHVWRAPPER_H */
