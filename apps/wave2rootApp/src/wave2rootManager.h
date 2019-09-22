/*
 * wave2rootManager.h
 *
 *  Created on: Mar 24, 2014
 *      Author: yqiang
 */

#ifndef WAVE2ROOTMANAGER_H_
#define WAVE2ROOTMANAGER_H_

#include <time.h>
#include <string.h>

void StartRootDAQ(const char* dir, const char* prefix,
		const char* suffix, long nLim);

void CloseRootFile();

void WriteRootFile(const char* channelName, struct timespec* timeStamp,
		float* buffPtr, int nElm);

int GetBufferSize();

const char* GetFileName();

long GetFileSize();

#endif /* WAVE2ROOTMANAGER_H_ */
