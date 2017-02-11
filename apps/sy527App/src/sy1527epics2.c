
/* sy1527epics1.c - EPICS driver support for CAEN SY1527 HV mainframe */
/*                  (a la Lecroy)                                     */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>

#include "sy1527.h"
#include "sy1527epics2.h"
#include <unistd.h>

/* static structure to keep track of active channels */
/// my: static double properties[MAX_HVPS][NUM_CAEN_PROP];


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
CAEN_GetHv(unsigned id, int *onoff1) // my: &onoff
{
 int active, onoff, alarm;
 /// int active, alarm;  /// my:

 int retv=  /// my:
 sy1527GetMainframeStatus(id, &active, &onoff, &alarm);

 //printf("============== %d\n", onoff); // my:
 *onoff1=onoff; 
 /// my: return(onoff)
 return retv; /// my:
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


// need to add this to header sy1527epics?.h
// currently sharing header with syX527App - will need to change this
STATUS
CAEN_HVgroupload(unsigned id, unsigned group, char* property, float value)
{
  if (!strncmp("DV",property,2))
  {
    printf("CAEN_HVgroupload: request for DV\n");
    sy1527SetGroupDemandVoltage(id,group,value);
  }
  else if (!strncmp("TC",property,2))
  {
    printf("CAENHV_groupload: request for TC\n");
    sy1527SetGroupMaxCurrent(id,group,value);
  }
  else if (!strncmp("RUP",property,3))
  {
    printf("CAENHV_groupload: request for RUP\n");
    sy1527SetGroupRampUp(id,group,value);
  }
  else if (!strncmp("RDN",property,3))
  {
    printf("CAENHV_groupload: request for RDN\n");
    sy1527SetGroupRampDown(id,group,value);
  }
  else if (!strncmp("ONOFF",property,5))
  {
    printf("CAENHV_groupload: request for ONOFF\n");
    if (value>0.5) sy1527SetGroupOnOff(id,group,0);
    else           sy1527SetGroupOnOff(id,group,1);
  }
  else
  {
    printf("CAENHV_groupload:  UNKNOWN PROPERTY:  %s\n",property);
  }
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
  else if(!strncmp("PRD",property,3))  /// my:
  {
   /// printf("CAEN_GetProperty: request for Trip Time\n");
    *value = sy1527GetChannelTripTime(id, slot, channel);
//printf(" PRD *value=%f\n",v);
  }  
  return(0);
}

/* returns all values for one channel */
STATUS
CAEN_GetChannel(unsigned id, unsigned slot, unsigned channel,
                double *property, double *delta)
{
  /*  printf("CAEN_GetChannel reached\n"); */
  property[PROP_MC] = sy1527GetChannelMeasuredCurrent(id, slot, channel); // e
  property[PROP_MV] = sy1527GetChannelMeasuredVoltage(id, slot, channel); // f
  property[PROP_DV] = sy1527GetChannelDemandVoltage(id, slot, channel);   // g
  property[PROP_RUP] = sy1527GetChannelRampUp(id, slot, channel);         // h
  property[PROP_RDN] = sy1527GetChannelRampDown(id, slot, channel);       // i
  property[PROP_TC] = sy1527GetChannelMaxCurrent(id, slot, channel);      // j
  property[PROP_CE] = (float) sy1527GetChannelEnableDisable(id, slot, channel);  // k
  property[PROP_ST] = (float) sy1527GetChannelStatus(id, slot, channel);  // l
  property[PROP_MVDZ] = 0.0;  // m
  property[PROP_MCDZ] = 0.0;  // n
  property[PROP_HVL] = sy1527GetChannelMaxVoltage(id, slot, channel); //o

  property[PROP_HBEAT] = sy1527GetHeartBeat(id, slot, channel); /// my_n:  // t

  /*
  if( ((int)property[PROP_ST] & (BIT_INTTRIP |  BIT_OVERVOLT | BIT_OVERCUR )   ) ) *delta=100;
  else *delta=0;
  //delta =  fabs(property[PROP_MV] - property[PROP_DV]) ;
  return(0);
  */

  // this is what we alarm on:
  *delta=0;

#define HRDWERROR  999999
#define COMMERROR -999999
 
  const int prop=property[PROP_ST];

  // If channel is ON, then delta is difference between measured and demand voltages,
  // This should allow to alarm any time a channel is turned on or off, in addition
  // to serving as a voltage tolerance alarm.
  if ( prop & (BIT527_ON) || prop & (BIT527_RUP) || prop & (BIT527_RDN ) )   
    *delta =  property[PROP_MV] - property[PROP_DV];
/*
  // delta is difference between measured and demand voltages
  // if channel is not ON, or RAMPING, do not set delta
  if ( ((int)property[PROP_ST] & (BIT527_ON) ) )
    if ( ! ((int)property[PROP_ST] & (BIT527_RUP | BIT527_RDN) ) )
      *delta =  property[PROP_MV] - property[PROP_DV];
*/

  // if ERROR bits are set, override delta with very big number
  if( ((int)property[PROP_ST] & (BIT527_EXTRIP | BIT527_INTRIP | BIT527_OVV | BIT527_OVC | BIT527_KILL)   ) ) 
    *delta=HRDWERROR;

  // if HEARTBEAT error, override delta with very big negative number
  if( (int)property[PROP_HBEAT] ) *delta=COMMERROR;

  return(0);


}
