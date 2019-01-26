#include <stdio.h>
#include <time.h>
#include <aSubRecord.h>
#include <epicsExport.h>
#include <registryFunction.h>

/*
 * plcSoeTimestamp
 *
 * Convert upper and lower timestamp registers, 32 bit DINTs from Allen-Bradley PLC
 * and already read into aiRecords, into string formatted for human consumption.
 */
static long plcSoeTimestamp(aSubRecord *precord) {
    const unsigned long upper = (unsigned long)(*(double*)(precord->a));
    const unsigned int lower = (unsigned long)(*(double*)(precord->b));
	if (upper>0) {
		const unsigned long timestamp = (upper<<32) | lower;
		const unsigned long seconds = timestamp/1e6;
		const double subseconds = (timestamp-seconds*1e6)/1e6;
		const int microseconds = subseconds*1e6;
		char prettydate[39];
		time_t rawtime = seconds;
		strftime(prettydate,39,"%Y-%m-%d %H:%M:%S",localtime(&rawtime));
		sprintf((char*)precord->vala,"%s.%06d",prettydate,microseconds);
		*((double*)precord->valb) = (double)seconds+subseconds;
	}
	else {
		sprintf((char*)precord->vala,"N/A");
		*((double*)precord->valb) = 0;
	}
    return 0;
}

epicsRegisterFunction(plcSoeTimestamp);

