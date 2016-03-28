/*
 * wf2rootManager.hh
 *
 *  Created on: Mar 24, 2014
 *      Author: yqiang
 */

#ifndef WF2ROOTMANAGER_HH_
#define WF2ROOTMANAGER_HH_

#include <queue>
#include <iostream>
#include <time.h>
#include <string.h>
#include <pthread.h>

#include <TString.h>
#include <TDatime.h>
#include <TTree.h>
// #include <DRootSpy.h>

#include "wf2rootFile.hh"
#include "wf2rootRecord.hh"

class recordBuffer {
public:
	string treename;
	wf2rootRecord record;
	inline recordBuffer(string treeName, wf2rootRecord prRecord) :
			treename(treeName), record(prRecord) {
	}
	recordBuffer& operator=(const recordBuffer &rbuffer) {
		treename = rbuffer.treename;
		record = rbuffer.record;
		return *this;
	}

	virtual ~recordBuffer() {
	}
};

class wf2rootManager {

private:

	string prmPrefix;
	string prmSuffix;

public:
	static wf2rootManager* selfPtr;	// Self pointer
	static Int_t prmCompressFactor;	// Compression factor
	static UInt_t prmFileSizeTolerance;	// Maximum file size
	static std::queue<recordBuffer> prmBuffer;	// record buffer

	pthread_t prmThread;
	bool prmStop;
	wf2rootFile* prmFile;
	string prmDir;
	string prmFileName;
	long prmFileLimit;
	long prmFileSize;
	pthread_mutex_t *prmMutex;

	wf2rootManager();
	virtual ~wf2rootManager();

	inline static wf2rootManager* GetInstance() {
		if (selfPtr == 0)
			selfPtr = new wf2rootManager();
		return selfPtr;
	}

	void StartDAQ(string dir, string prefix, string suffix, long nlim);
	void NewRootFile();
	void WriteFile(const char* channelName, struct timespec* timeStamp,
			float* buffPtr, int nElm);
	void CloseFile();

	inline wf2rootFile* GetFile() const {
		return prmFile;
	}

	inline wf2rootFile* SetFile(wf2rootFile* file) {
		return prmFile = file;
	}
};

void *WriteThread(void* argument);

#endif /* WF2ROOTMANAGER_HH_ */
