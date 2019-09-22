/*
 * wave2rootSub.c
 *
 *  Created on: Mar 25, 2014
 *      Author: yqiang
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include <dbDefs.h>
#include <registryFunction.h>
#include <subRecord.h>
#include <aSubRecord.h>
#include <epicsTypes.h>
#include <epicsTime.h>
#include <epicsExport.h>

#include "wave2rootManager.h"

int wave2rootDebug;

/*
 * Initialize record to kill IOC
 */
static long wave2rootKillInit(aSubRecord *record) {
	if (wave2rootDebug > 1)
		printf("Record %s called wave2rootKillInit(%p)\n", record->name,
				(void*) record);
	return 0;
}

/*
 * Process record to kill IOC
 */
static long wave2rootKillProcess(aSubRecord *record) {

	if (wave2rootDebug > 1)
		printf("Record %s called wave2rootKillProcess(%p)\n", record->name,
				(void*) record);

	epicsEnum16 killStatReq = *((epicsEnum16*) record->a);
	if (wave2rootDebug > 1)
		printf("Kill state is %d\n", killStatReq);

	// If the record is set anything from 0, IOC will exit
	if (record != NULL && killStatReq != 0) {
		printf("Aborting IOC per external request!\n");
		abort();
	}

	return 0;
}

/*
 * Initialize record to control DAQ
 */
static long wave2rootDAQInit(aSubRecord *record) {
	if (wave2rootDebug > 1)
		printf("Record %s called wave2rootDAQInit(%p)\n", record->name,
				(void*) record);
	return 0;
}

/*
 * Process record to control DAQ
 */
static long wave2rootDAQProcess(aSubRecord *record) {

	if (wave2rootDebug > 1)
		printf("Record %s called wave2rootDAQProcess(%p)\n", record->name,
				(void*) record);

	epicsEnum16 daqStatReq = *((epicsEnum16*) record->a);
	char* file_dir = (char*) record->b;
	if (wave2rootDebug > 1)
		printf("DAQ state is %d, directory is %s \n", daqStatReq, file_dir);

	if (record != NULL && daqStatReq == 0) {
		StartRootDAQ(file_dir, "w2r_", "", ((long*) record->d)[0]);
		if (wave2rootDebug > 0)
			printf("Start recording ROOT files ...\n");
	} else if (record != NULL && daqStatReq == 1) {
		CloseRootFile();
		if (wave2rootDebug > 0)
			printf("ROOT file recording stopped\n");
	}

	return 0;
}

/*
 * Initialize records to save waveform data
 */
static long wave2rootDataInit(aSubRecord *record) {
	if (wave2rootDebug > 2)
		printf("Record %s called wave2rootDataInit(%p)\n", record->name,
				(void*) record);
	return 0;
}

/*
 * Process records to save waveform data
 */
static long wave2rootDataProcess(aSubRecord *record) {

	if (wave2rootDebug > 2)
		printf("Record %s called wave2rootDataProcess(%p)\n", record->name,
				(void*) record);

	// daq_state: 0 = writing, 1 = stopped
	epicsEnum16 daq_state = *(epicsEnum16*) (record->c);

	// convert EPICS time to POSIX time
	struct timespec posixTime = { 0, 0 };
	epicsTimeToTimespec(&posixTime, &record->time);

	// save previous timestamp, posixTime, and data, vala, to file
	if (!daq_state && posixTime.tv_sec > 0) {
		if (GetBufferSize() < 1000) {
			WriteRootFile(record->b, &posixTime, record->vala, record->noa);
		} else {
			printf("Buffer length exceeds 1000, exiting the program!");
			return 1;
		}
	}
	if (wave2rootDebug > 2) {
		struct tm tsLocal = *localtime(&posixTime.tv_sec);
		char timeString[128];  // Reserve string for timestamp
		strftime(timeString, sizeof(timeString), "%Z %a %Y-%m-%d %H:%M:%S",
				&tsLocal);
		char nsTime[64];
		sprintf(nsTime, "%ld", posixTime.tv_nsec);
/* 		if (strcmp(record->b, "halld-pxi:array:vtt4") == 0) */
/* 			printf("%s : %s.%s   %8.5f   %8.5f \n", (char*) record->b, */
/* 					timeString, nsTime, ((float*) record->a)[5000 - 1], */
/* 					((float*) record->vala)[5000 - 1]); */
	}

	// update file name and size
	const char* file_name = GetFileName();
	long file_size = GetFileSize();
	strcpy(record->vald, file_name);
	((long*) record->vale)[0] = file_size;

	// copy updated data to vala
	memcpy(record->vala, record->a, record->noa * (sizeof(float)));

	return 0;
}

// Register functions for EPICS IOC shell

epicsExportAddress(int, wave2rootDebug);

epicsRegisterFunction(wave2rootKillInit);
epicsRegisterFunction(wave2rootKillProcess);

epicsRegisterFunction(wave2rootDAQInit);
epicsRegisterFunction(wave2rootDAQProcess);

epicsRegisterFunction(wave2rootDataInit);
epicsRegisterFunction(wave2rootDataProcess);

