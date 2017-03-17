#include <string.h>
#include <dbDefs.h>
#include <subRecord.h>
#include <dbCommon.h>
#include <recSup.h>

#include <epicsExport.h>
#include <registryFunction.h>

#define RAW     psub->a
#define MULT    psub->b
#define UNITS   psub->c
#define VAL		psub->val

long fieldCalc(struct subRecord *psub) {
    if (MULT == 0) {
        VAL = RAW * 1.0e-6;
    } else if (MULT == 1) {
        VAL = RAW * 1.0e-3;
    } else if ( MULT == 2) {
        VAL = RAW * 1.0e3;
    } else {
        VAL = RAW;
    }

    if (UNITS == 0) {
        strcpy((char *)psub->egu,"G");
    } else {
        strcpy((char *)psub->egu,"T");
    }

	return(0);
}
epicsRegisterFunction(fieldCalc);
