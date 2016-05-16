/*
 * wf2rootMain.cpp
 *
 *  Created on: Mar 25, 2014
 *      Author: yqiang
 */

#include <TROOT.h>
#include <iocsh.h>
#include <epicsExit.h>
#include <epicsThread.h>
//#include <DRootSpy.h>
#include <TH1.h>

int main(int argc, char*argv[]) {
	if (argc >= 2) {
		iocsh(argv[1]);
		epicsThreadSleep(.2);
	}
	iocsh(NULL);
	gROOT->CloseFiles();
	epicsExit(0);
	return 0;
}
