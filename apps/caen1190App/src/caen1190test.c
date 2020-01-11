#include <stddef.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>

#include "jvme.h"
#include "tdc1190.h"

#define ALMOSTFULL 2
#define FULL 4

#define SLOT_ID 0

int main(int argc,char *argv[])
{
	int ntdc,ii,ret,ret1,ret2;

	vmeOpenDefaultWindows();

	// from Sergey's tdc1190init executable:
	//tdc1190Init(0x11100000,0x80000,20,0);

	// works for classc10's caen1190 slot:
	ntdc=tdc1190Init(0x11300000,0x00000,1,0);

	if (ntdc) tdc1190Config("");

	ret=tdc1190ReadAcquisitionMode(SLOT_ID);
	printf("Read Acquisition Mode %d:   %d\n",SLOT_ID,ret);
  
	ret=tdc1190SetContinuousStorageMode(SLOT_ID);
	printf("Set Continuous Storage %d:  %d\n",SLOT_ID,ret);

	ret=tdc1190ReadAcquisitionMode(SLOT_ID);
	printf("Read Acquisition Mode %d:   %d\n",SLOT_ID,ret);
  
	ret=tdc1190SetMaxNumberOfHitsPerEvent(SLOT_ID,128);
	ret=tdc1190GetMaxNumberOfHitsPerEvent(SLOT_ID);
	printf("Read Max Hits Per Event %d: %d\n",SLOT_ID,ret);
  
	ret=tdc1190SetEdgeResolution(SLOT_ID,200);
	printf("Set Edge Resolution: %d:    %d\n",SLOT_ID,ret);
	ret=tdc1190GetEdgeResolution(SLOT_ID);
	printf("Get Edge Resolution: %d:    %d\n",SLOT_ID,ret);
  
	tdc1190SetWindowWidth(SLOT_ID,51175);
	printf("Set Window Width %d:        %d\n",SLOT_ID,ret);
	//ret=tdc1190GetWindowWidth(SLOT_ID,51175);
	//printf("Set Window Width %d:        %d\n",SLOT_ID,ret);

	ret=tdc1190EnableChannel(SLOT_ID,0);
	printf("Set Enable Channel %d:      %d\n",SLOT_ID,ret);

	tdc1190Status(SLOT_ID);
	tdc1190Mon(SLOT_ID);

	for (ii=0; ii<100; ii++) {
	  
		ret=tdc1190GetEventCounter(SLOT_ID);
		printf("Event Counter/Stored %d:    %d/%d\n",SLOT_ID,ret,tdc1190GetEventStored(SLOT_ID));
		ret1=tdc1190StatusAlmostFull(SLOT_ID);
		ret2=tdc1190StatusFull(SLOT_ID);
		printf("AlmostFull/Full %d:         %d/%d\n",SLOT_ID,ret1,ret2);

		if (ret2==FULL) {
			ret=tdc1190Clear(SLOT_ID);
			printf("Clear %d:                   %d\n",SLOT_ID,ret);
			ret=tdc1190Dready(SLOT_ID);
			printf("Data Ready %d:              %d/%d\n",SLOT_ID,ret,tdc1190Dready(SLOT_ID));
			ret=tdc1190Reset(SLOT_ID);
			printf("Reset:                      %d\n",ret);
		}

		sleep(1);
	}

    return(0);
}
