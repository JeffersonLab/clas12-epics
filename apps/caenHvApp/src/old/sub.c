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
#include <subRecord.h>
#include <dbCommon.h>
#include <dbAccess.h>
#include <recSup.h>
#include <callback.h>

#ifndef ERROR
#define ERROR  (-1)
#endif


long InitSub(struct subRecord *psub)
{
  printf("This is a Dummy Function for sub\n");
   return(0);
}

 

long ScanSub(struct subRecord *psub)
{
  
  printf("Processing Sub Record\n");

  return(0);
}

