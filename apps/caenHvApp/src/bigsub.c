/*****************************************************************************\
 * File: bigsub.c                                   Author:  Hovanes Egiyan  *
 *                                                                           *
 * Overview:                                                                 *
 *   This file contains the functions called by EPICS "bigsub" record        *
 *   processing for the LeCroy High Voltage Mainframe database application.  *
 *   Note that the significant part of this procedure is through the         *
 *   external function "GetChannel", which is part of the lecroyDev device   *
 *   support package. This was taken from Slominski's HV code.               *
 *                                                                           *
 * Revision History:                                                         *
 *   07/10/2003 - Initial release                                            *
\*****************************************************************************/


#include <stdio.h>
#include "epicsPrint.h"
#include "recGbl.h"



#include <dbDefs.h>
#include <bigsubRecord.h>
#include <dbCommon.h>
#include <dbAccess.h>
#include <recSup.h>
#include <callback.h>

#ifndef ERROR
#define ERROR  (-1)
#endif

char CAEN_GetChannel(unsigned, unsigned, unsigned, double *, double *);


/*                                                                           *\
 | Name: InitChannel                                                         |
 | Parameters: psub - pointer to a bigsub record                             |
 | Return: EPICS completion status; 0 = success                              |
 | Remarks:                                                                  |
 |   This function is a place holder and does nothing but return success.    |
\*                                                                           */
long InitChannel(struct bigsubRecord *psub)
{
  /*  printf("This is a Dummy Function \n"); */
// printf("bigsub init\n"); // my:
   return(0);
}

 
/*                                                                           *\
 | Name: ScanChannel                                                         |
 | Parameters: psub - pointer to bigsub record                               |
 | Return: EPICS completion status; 0 = success                              |
 | Remarks:                                                                  |
 |   This function is called for each scan of a CAENHV    bigsub record.  It |
 |   calls the device support routine "GetChannel" to fill record slots with |
 |   channel information.  Note that the input fields 'e' through 't' are    |
 |   used for this purpose, giving a maximum of 16 pieces of channel data    |
 |   that may be fetched.                                                    |
\*                                                                           */
long ScanChannel(struct bigsubRecord *psub)
{
  /* The first three input fields of the record identify the specific channel
   * desired by chassis ID, slot number, and onboard channel number.  The
   * fourth field contains non-zero when the desired information is a CAEN
   * module's block generator as opposed to a regular channel.  If it is
   * a generator, the channel number's bit 31 is set as a flag.
   */
  // my: comment +++++++++++++ // replaced by copying : cp ./base-3.14.8.2/include/bigsubRecord.h ./base-3.14.12.3/include/.
  
  unsigned chassis = (unsigned) psub->a;
  unsigned slot = (unsigned) psub->b;
  unsigned channel = (unsigned) psub->c;
  if (psub->d != 0) channel |= 0x80;
  
//  printf("bigsub\n"); // my:

  /* Call device support routine to get channel data for this record, filled
   * in starting at field 'e'.  Also pass the 'val' field which will be set to
   * the difference (absolute value) between measured and demand voltage (if
   * applicable).
   */
  // my: comment +++++++++++++ // replaced by copying : cp ./base-3.14.8.2/include/bigsubRecord.h ./base-3.14.12.3/include/.
  
//return 0;
  if (CAEN_GetChannel(chassis, slot, channel, &psub->e, &psub->val) == ERROR)
  { char alert[128];
    sprintf(alert, "Bigsub - %s(%d): Chassis=%u Slot=%u Channel=%u",
            __FILE__, __LINE__, chassis, slot, channel);
    recGblRecordError(S_db_badField, (void *) psub, alert);
    return(S_db_badField);
  }
  


  /*
  else {
	printf("Read values %d  %f %f \n", psub->k, psub->f, psub->g ); 
  }
  */
  return(0);
}

