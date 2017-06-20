
/* sy1527epics1.c - EPICS driver support for CAEN SY1527 HV mainframe */
/*                  (a la Lecroy)                                     */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>

#include "sy1527.h"
#include "sy1527epics1.h"
#include <unistd.h>

/* open communication with mainframe under logical number 'id' */
int
CAEN_HVstart(unsigned id, char *ip_address)
{
  return(sy1527Start(id,ip_address));
}

/* close communication with mainframe under logical number 'id' */
int
CAEN_HVstop(unsigned id)
{
  return(sy1527Stop(id));
}

/* returns 1 if mainframe is ON, otherwise returns 0 */
int
CAEN_GetHv(unsigned id, int *onoff1)
{
 int active, onoff, alarm;

 int retv=sy1527GetMainframeStatus(id, &active, &onoff, &alarm);

 *onoff1=onoff; 
 return retv;
}

/* returns 1 if any channel is alarming, otherwise returns 0 */
int
CAEN_GetAlarm(unsigned id)
{
  int active, onoff, alarm;

  sy1527GetMainframeStatus(id, &active, &onoff, &alarm);

  return(alarm);
}

/* */
int
CAEN_GetValidity(unsigned id)
{
  int active, onoff, alarm;

  sy1527GetMainframeStatus(id, &active, &onoff, &alarm);

  return(active);
}

/* set HV on/off for whole mainframe */
int
CAEN_SetHV(unsigned id, unsigned char on_off)
{
  unsigned int u = on_off;

  sy1527SetMainframeOnOff(id, u);

  return(0);
}

/* */
STATUS
CAEN_HVload(unsigned id, unsigned slot, unsigned channel,
            char *property, float value)
{
  if(!strncmp("MC",property,2))
  {
    printf("CAEN_HVload: request for MC\n");
    printf("!!! NEVER CALL IT AGAIN !!!\n");
  }
  else if(!strncmp("MV",property,2))
  {
    printf("CAEN_HVload: request for MV\n");
    printf("!!! NEVER CALL IT AGAIN !!!\n");
  }
  else if(!strncmp("DV",property,2))
  {
    printf("CAEN_HVload: request for DV\n");
    sy1527SetChannelDemandVoltage(id, slot, channel, value);
  }
  else if(!strncmp("RUP",property,3))
  {
    printf("CAEN_HVload: request for RUP\n");
    sy1527SetChannelRampUp(id, slot, channel, value);
  }
  else if(!strncmp("RDN",property,3))
  {
    printf("CAEN_HVload: request for RDN\n");
    sy1527SetChannelRampDown(id, slot, channel, value);
  }
  else if(!strncmp("TC",property,2))
  {
    printf("CAEN_HVload: request for TC\n");
    sy1527SetChannelMaxCurrent(id, slot, channel, value);
  }
  else if(!strncmp("CE",property,2))
  {
    printf("CAEN_HVload: request for CE: id=%d sl=%d ch=%d val=%f\n",
      id,slot,channel,value);
    if(value > 0.5)
    {
      /* enable the channel */
      sy1527SetChannelEnableDisable(id, slot, channel, 1);
      sleep(2);

      /* if mainframe is ON, turn channel ON */
	  {
        int active, onoff, alarm;
        sy1527GetMainframeStatus(id, &active, &onoff, &alarm);
        if(onoff)
        {
          sleep(2);
          sy1527SetChannelOnOff(id, slot, channel, 1);
        }
	  }
	}
    else
    {
      /* disable the channel */
      sy1527SetChannelOnOff(id, slot, channel, 0);
      sleep(2);
      sy1527SetChannelEnableDisable(id, slot, channel, 0);
      sleep(2);
	}
  }
  else if(!strncmp("CHONOFF",property,7))
  {
    printf("CAEN_HVload: request for CHONOFF: id=%d sl=%d ch=%d val=%f\n",
      id,slot,channel,value);
    if(value > 0.5)
    {
          sy1527SetChannelOnOff(id, slot, channel, 1);
    }
    else
    {
      sy1527SetChannelOnOff(id, slot, channel, 0);

    }
  }

  else if(!strncmp("ST",property,2))
  {
    printf("CAEN_HVload: request for ST\n");
  }
  else if(!strncmp("MVDZ",property,4))
  {
    printf("CAEN_HVload: request for MVDZ\n");
    printf("!!! NEVER CALL IT AGAIN !!!\n");
  }
  else if(!strncmp("MCDZ",property,4))
  {
    printf("CAEN_HVload: request for MCDZ\n");
    printf("!!! NEVER CALL IT AGAIN !!!\n");
  }
  else if(!strncmp("HVL",property,3))
  {
    printf("CAEN_HVload: request for HVL\n");
    sy1527SetChannelMaxVoltage(id, slot, channel, value);
  }
  else if(!strncmp("UNVT",property,3))
  {
    printf("CAEN_HVload: request for UNVT\n");
    sy1527SetChannelUnderVoltage(id, slot, channel, value);
  }
  else if(!strncmp("OVVT",property,3))
  {
    printf("CAEN_HVload: request for OVVT\n");
    sy1527SetChannelOverVoltage(id, slot, channel, value);
  }

  return(0);
}

/* */
STATUS
CAEN_GetProperty(unsigned id, unsigned slot, unsigned channel,
                 char *property, float *value)
{
  if(!strncmp("MC",property,2))
  {
   /// printf("CAEN_GetProperty: request for MC\n");
    *value = sy1527GetChannelMeasuredCurrent(id, slot, channel);
  }
  else if(!strncmp("MV",property,2))
  {
  ///  printf("CAEN_GetProperty: request for MV\n");
    *value = sy1527GetChannelMeasuredVoltage(id, slot, channel);
  }
  else if(!strncmp("DV",property,2))
  {
  ///  printf("CAEN_GetProperty: request for DV\n");
    *value = sy1527GetChannelDemandVoltage(id, slot, channel);
  }
  else if(!strncmp("RUP",property,3))
  {
   /// printf("CAEN_GetProperty: request for RUP\n");
    *value = sy1527GetChannelRampUp(id, slot, channel);
  }
  else if(!strncmp("RDN",property,3))
  {
   /// printf("CAEN_GetProperty: request for RDN\n");
    *value = sy1527GetChannelRampDown(id, slot, channel);
  }
  else if(!strncmp("TC",property,2))
  {
   /// printf("CAEN_GetProperty: request for TC\n");
    *value = sy1527GetChannelMaxCurrent(id, slot, channel);
  }
  else if(!strncmp("CE",property,2))
  {
   /// printf("CAEN_GetProperty: request for CE\n");
    *value = (float) sy1527GetChannelEnableDisable(id, slot, channel);
  }
  else if(!strncmp("ST",property,2))
  {
   /// printf("CAEN_GetProperty: request for ST\n");
    *value = (float) sy1527GetChannelStatus(id, slot, channel);
  }
  else if(!strncmp("MVDZ",property,4))
  {
   /// printf("CAEN_GetProperty: request for MVDZ\n");
    printf("!!! NEVER CALL IT AGAIN !!!\n");
  }
  else if(!strncmp("MCDZ",property,4))
  {
   /// printf("CAEN_GetProperty: request for MCDZ\n");
    printf("!!! NEVER CALL IT AGAIN !!!\n");
  }
  else if(!strncmp("HVL",property,3))
  {
   /// printf("CAEN_GetProperty: request for HVL\n");
    *value = sy1527GetChannelMaxVoltage(id, slot, channel);
  }
  else if(!strncmp("PRD",property,3))
  {
   /// printf("CAEN_GetProperty: request for Trip Time\n");
    *value = sy1527GetChannelTripTime(id, slot, channel);
  }
  else if (!strncmp("UNVT",property,4))
  {
      *value = sy1527GetChannelUnderVoltage(id, slot, channel);
  }
  else if (!strncmp("OVVT",property,4))
  {
      *value = sy1527GetChannelOverVoltage(id, slot, channel);
  }
  else if (!strncmp("RANGE",property,4))
  {
      *value = sy1527GetChannelRange(id, slot, channel);
  }
  else if (!strncmp("INTLK",property,5))
  {
      *value = sy1527GetChannelInterlock(id, slot, channel);
  }
  return(0);
}

/* returns all values for one channel */
STATUS
CAEN_GetChannel(unsigned id, unsigned slot, unsigned channel,
                double *property, double *delta)
{

  const unsigned int demandOn = sy1527GetChannelDemandOnOff(id,slot,channel);

  property[PROP_MC] = sy1527GetChannelMeasuredCurrent(id, slot, channel); // e
  property[PROP_MV] = sy1527GetChannelMeasuredVoltage(id, slot, channel); // f
  property[PROP_DV] = sy1527GetChannelDemandVoltage(id, slot, channel);   // g
  property[PROP_RUP] = sy1527GetChannelRampUp(id, slot, channel);         // h
  property[PROP_RDN] = sy1527GetChannelRampDown(id, slot, channel);       // i
  property[PROP_TC] = sy1527GetChannelMaxCurrent(id, slot, channel);      // j
  property[PROP_CE] = (float) sy1527GetChannelEnableDisable(id, slot, channel);  // k
  property[PROP_ST] = (float) sy1527GetChannelStatus(id, slot, channel);  // l
  property[PROP_HVL] = sy1527GetChannelMaxVoltage(id, slot, channel); //o

  // used to have this:
  //property[PROP_MVDZ] = 0.0;  // m
  //property[PROP_MCDZ] = 0.0;  // n
 
  // LV-Only:
  property[PROP_UNVT] = sy1527GetChannelUnderVoltage(id, slot, channel); // m
  property[PROP_OVVT] = sy1527GetChannelOverVoltage(id, slot, channel); // n
  property[PROP_TEMP] = sy1527GetChannelTemperature(id, slot, channel); // p
  property[PROP_VCON] = sy1527GetChannelConnectorVoltage(id, slot, channel); // r
  property[PROP_INTLK] = sy1527GetChannelInterlock(id, slot, channel); // r

  // Dual-Range Only:
  property[PROP_RANGE] = sy1527GetChannelRange(id, slot, channel); // s

  property[PROP_HBEAT] = sy1527GetHeartBeat(id, slot, channel); // t

  // this is what we alarm on:
  *delta=0;
 
#define HRDWERROR  999999
#define COMMERROR -999999
#define MISMERROR -111111
    
//  printf("!!! BOO - %d\n",BITS_ANYHWERROR);
  
  // if HEARTBEAT error, override delta with very big negative number
  if ( (int)property[PROP_HBEAT] )
    *delta = COMMERROR;

  // if ERROR bits are set, override delta with very big positive number
  else if ( ( (int)property[PROP_ST] & 
    (BIT_INTTRIP |
     BIT_EXTTRIP |
     BIT_OVERVOLT |
     BIT_OVERCUR |
     BIT_UNDERVOLT |
     BIT_MAXVOLT |
     BIT_EXTDISABLED |
     BIT_CALIBERROR |
     BIT_CHUNPLUGGED) ) )
    *delta = HRDWERROR;
  
  // Mismatch between ON/OFF request and status reported by hardware:
  else if ( demandOn != ((int)property[PROP_ST] & (BIT_ON) ) )
    *delta = MISMERROR;
 
  // If channel is ON, then delta is difference between measured and demand voltages.
  // This should allow to alarm any time a channel is turned on or off, in addition
  // to serving as a voltage tolerance alarm.
  else if ( ((int)property[PROP_ST] & (BIT_ON) ) )
    *delta =  property[PROP_MV] - property[PROP_DV];
 
  // We used to not set delta if in RUP/DRN state:
  // ( ! ((int)property[PROP_ST] & (BIT_RAMPUP | BIT_RAMPDOWN) ) )

  return(0);
}
