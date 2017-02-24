/*
 *   Translate Alarm from 12 records
 *      INPA-INPL  the values from 12 records
 *      Return:
 *         The value of the PV in the most severe Alarm state.
*/
#include <math.h>
#include <dbDefs.h>
#include <dbCommon.h>
#include <recSup.h>
#include <bigsubRecord.h>
#include <epicsVersion.h>
#if EPICS_VERSION >= 3 && EPICS_REVISION >= 14
# define HAVE_314_API
#include <epicsExport.h>
#include <registryFunction.h>
typedef long (*processMethod)(bigsubRecord *precord);
typedef long (*subProcMethod)(bigsubRecord *precord);
#endif

#ifdef HAVE_314_API
static long trnslateAlmInit (bigsubRecord *psub)
#else
long trnslateAlmInit (psub)
   struct bigsubRecord *psub;
#endif
{
         psub->val = (long)0;
 return(0);
}
#ifdef HAVE_314_API
static long trnslateAlarm (bigsubRecord *psub)
#else
long trnslateAlarm (psub)
   struct bigsubRecord *psub; 
#endif
{
 int i;
 int alm[12];
   alm[0] = psub->a; 
   alm[1] = psub->b; 
   alm[2] = psub->c; 
   alm[3] = psub->d; 
   alm[4] = psub->e; 
   alm[5] = psub->f; 
   alm[6] = psub->g; 
   alm[7] = psub->h; 
   alm[8] = psub->i; 
   alm[9] = psub->j; 
   alm[10] = psub->k; 
   alm[11] = psub->l; 
/* check for HIHI alarm */
   for(i=0;i<12;i++){
     if(alm[i] >= psub->hihi) {
          psub->val = alm[i];
          return(0);
     }
   }
/* check for LOLO alarm */
   for(i=0;i<12;i++){
     if(alm[i] <= psub->lolo) {
          psub->val = alm[i];
          return(0);
     }
   }
/* check for High alarm */
   for(i=0;i<12;i++){
     if(alm[i] >= psub->high) {
          psub->val = alm[i];
          return(0);
     }
   }
/* check for Low alarm */
   for(i=0;i<12;i++){
     if(alm[i] <= psub->low) {
          psub->val = alm[i];
          return(0);
     }
   }
   psub->val = 0;
 return(0);
}
#ifdef HAVE_314_API
static registryFunctionRef translateAlarmRef[] = {
  {"trnslateAlmInit", (REGISTRYFUNCTION)trnslateAlmInit},
  {"trnslateAlarm", (REGISTRYFUNCTION)trnslateAlarm}
};
void translateAlarm_reg(void)
{ registryFunctionRefAdd(translateAlarmRef,NELEMENTS(translateAlarmRef)); }
epicsExportRegistrar(translateAlarm_reg);
#endif
