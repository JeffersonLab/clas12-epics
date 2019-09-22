/*
 * wave2rootManager.hh
 *
 *  Created on: Mar 24, 2014
 *      Author: yqiang
 */

#ifndef WAVE2ROOTMANAGER_HH_
#define WAVE2ROOTMANAGER_HH_

#include <queue>
#include <iostream>
#include <time.h>
#include <string.h>
#include <pthread.h>

#include <TString.h>
#include <TDatime.h>
#include <TTree.h>
//#include <DRootSpy.h>

#include "wave2rootFile.hh"
#include "wave2rootRecord.hh"

class recordBuffer {
public:
	string treename;
	wave2rootRecord record;
	inline recordBuffer(string treeName, wave2rootRecord prRecord) :
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

class wave2rootManager {

private:

	string prmPrefix;
	string prmSuffix;

public:
	static wave2rootManager* selfPtr;	// Self pointer
	static Int_t prmCompressFactor;	// Compression factor
	static UInt_t prmFileSizeTolerance;	// Maximum file size
	static std::queue<recordBuffer> prmBuffer;	// record buffer

	pthread_t prmThread;
	bool prmStop;
	wave2rootFile* prmFile;
	string prmDir;
	string prmFileName;
	long prmFileLimit;
	long prmFileSize;
	pthread_mutex_t *prmMutex;

	wave2rootManager();
	virtual ~wave2rootManager();

	inline static wave2rootManager* GetInstance() {
		if (selfPtr == 0)
			selfPtr = new wave2rootManager();
		return selfPtr;
	}

	void StartDAQ(string dir, string prefix, string suffix, long nlim);
	void NewRootFile();
	void WriteFile(const char* channelName, struct timespec* timeStamp,
			float* buffPtr, int nElm);
	void CloseFile();

	inline wave2rootFile* GetFile() const {
		return prmFile;
	}

	inline wave2rootFile* SetFile(wave2rootFile* file) {
		return prmFile = file;
	}
};

void *WriteThread(void* argument);

#endif /* WAVE2ROOTMANAGER_HH_ */
