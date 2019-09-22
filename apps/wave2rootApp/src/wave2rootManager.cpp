/*
 * wave2rootManager.cpp
 *
 *  Created on: Mar 24, 2014
 *      Author: yqiang
 */

#include "wave2rootManager.hh"
#include "wave2rootFile.hh"

wave2rootManager* wave2rootManager::selfPtr = 0;
Int_t wave2rootManager::prmCompressFactor = 1; // no compression
std::queue<recordBuffer> wave2rootManager::prmBuffer;

UInt_t wave2rootFile::prfTreeBuffSize = static_cast<UInt_t>(1 << 16);
UInt_t wave2rootFile::prfAutoSaveSize = static_cast<UInt_t>(1 << 30);
string wave2rootFile::prfBranchName = "record";

// constructor
wave2rootManager::wave2rootManager() :
		prmPrefix(""), prmSuffix(""), prmThread(0), prmStop(true), prmFile(0), prmDir(
				""), prmFileName("nofile"), prmFileLimit(1000000000), prmFileSize(0) {

	// reinitialize self pointer
	if (selfPtr != 0)
		delete selfPtr;
	selfPtr = this;

	// clear FIFO
	while (prmBuffer.size() > 0)
		prmBuffer.pop();

	// Create mutex for buffer operation
	if (prmMutex)
		delete prmMutex;
	pthread_mutexattr_t attr;
	pthread_mutexattr_init(&attr);
	pthread_mutexattr_settype(&attr, PTHREAD_MUTEX_ERRORCHECK);
	prmMutex = new pthread_mutex_t;
	pthread_mutex_init(prmMutex, &attr);

	return;
}

// destructor
wave2rootManager::~wave2rootManager() {
	if (prmFile != 0 && prmFile->IsOpen()) {
		prmFile->Close();
		prmFile = 0;
	}
	selfPtr = 0;
	return;
}

void wave2rootManager::StartDAQ(string dir, string prefix, string suffix,
		long nlim) {
	prmDir = dir;
	prmPrefix = prefix;
	prmSuffix = suffix;
	prmFileLimit = nlim;
	prmStop = false;
	pthread_create(&prmThread, NULL, WriteThread, (void*) this);

	return;
}

void wave2rootManager::NewRootFile() {
	// new filename
	TDatime dtTime;
	TString rsTime(dtTime.AsSQLString());
	rsTime.ReplaceAll(" ", "_");
	rsTime.ReplaceAll(":", "");
	rsTime.ReplaceAll("-", "");
	prmFileName = prmPrefix + string(rsTime.Data()) + prmSuffix + ".root";
	string fullpath = prmDir + prmFileName;
	prmFile = new wave2rootFile(fullpath.c_str(), "RECREATE", "PXI ROOT File",
			prmCompressFactor);
}

void wave2rootManager::WriteFile(const char* channelName,
		struct timespec* timeStamp, float* buffPtr, int nElm) {

	recordBuffer tmprecord(string(channelName),
			wave2rootRecord(*timeStamp, nElm, buffPtr));

	// push to buffer
	pthread_mutex_lock(prmMutex);
	prmBuffer.push(tmprecord);
	pthread_mutex_unlock(prmMutex);

	return;
}

void wave2rootManager::CloseFile() {
	prmStop = true;
	if (prmThread) {
		pthread_join(prmThread, NULL);
		prmThread = 0;
	}
}

void *WriteThread(void *argument) {

	// sleep timer
	struct timespec sleeptime;
	sleeptime.tv_sec = 0;
	sleeptime.tv_nsec = (long int) (0.01 * 1.e9);

	wave2rootManager *prmPtr = (wave2rootManager*) argument;

	// CLose Existing Root file
	if (prmPtr->prmFile != 0 && prmPtr->prmFile->IsOpen())
		prmPtr->prmFile->Close();

	while (!prmPtr->prmStop) {

		// read buffer if non-empty
		if (prmPtr->prmBuffer.size()) {
			pthread_mutex_lock(prmPtr->prmMutex);
			recordBuffer tmprecord = prmPtr->prmBuffer.front();
			prmPtr->prmBuffer.pop();
			pthread_mutex_unlock(prmPtr->prmMutex);

			// check if file open
			if (prmPtr->prmFile == 0 || !prmPtr->prmFile->IsOpen()) {
				prmPtr->NewRootFile();
			}

			// write to disk
			prmPtr->prmFile->FillTree(tmprecord.treename, tmprecord.record);

			// check file size, close if larger than tolerance
			prmPtr->prmFileSize = prmPtr->prmFile->GetEND();
			if (prmPtr->prmFileSize >= prmPtr->prmFileLimit) {
				prmPtr->prmFile->Close();
			}
		} else
			nanosleep(&sleeptime, &sleeptime);
	}

	// clear buffer
	while (prmPtr->prmBuffer.size()) {
		pthread_mutex_lock(prmPtr->prmMutex);
		recordBuffer tmprecord = prmPtr->prmBuffer.front();
		prmPtr->prmBuffer.pop();
		pthread_mutex_unlock(prmPtr->prmMutex);
		// check if file open
		if (prmPtr->prmFile == 0 || !prmPtr->prmFile->IsOpen()) {
			prmPtr->NewRootFile();
		}
		// write to disk
		prmPtr->prmFile->FillTree(tmprecord.treename, tmprecord.record);
	}

	if (prmPtr->prmFile != 0 && prmPtr->prmFile->IsOpen())
		prmPtr->prmFile->Close();
	prmPtr->prmFile = 0;
	prmPtr->prmFileName = string("nofile");
	prmPtr->prmFileSize = 0;
	return NULL;
}

extern "C" {

#include "wave2rootManager.h"

void StartRootDAQ(const char* dir, const char* prefix, const char* suffix,
		long nlim) {
	string strdir(dir);
	string strpfx(prefix);
	string strsfx(suffix);
	wave2rootManager::GetInstance()->StartDAQ(strdir, strpfx, strsfx, nlim);
	return;
}

void CloseRootFile() {
	wave2rootManager::GetInstance()->CloseFile();
	return;
}

void WriteRootFile(const char* channelName, struct timespec* timeStamp,
		float* buffPtr, int nElm) {
	wave2rootManager::GetInstance()->WriteFile(channelName, timeStamp, buffPtr,
			nElm);
	return;
}

int GetBufferSize() {
	return wave2rootManager::GetInstance()->prmBuffer.size();
}

const char* GetFileName() {
	return wave2rootManager::GetInstance()->prmFileName.c_str();
}

long GetFileSize() {
	return wave2rootManager::GetInstance()->prmFileSize;
}
}
;
