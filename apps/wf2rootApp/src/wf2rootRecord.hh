/*
 * wf2rootRecord.hh
 *
 *  Created on: Mar 24, 2014
 *      Author: yqiang
 */

#ifndef WF2ROOTRECORD_HH_
#define WF2ROOTRECORD_HH_

#include <time.h>

#include <TObject.h>
#include <TArrayF.h>

class wf2rootRecord: public TObject {

private:
	struct timespec prrTime;			// POSIX timestamp
	TArrayF prrData;			// ROOT array of floats

public:
	wf2rootRecord(struct timespec posixTime, unsigned nElm,
			const float* arrayPtr) :
			TObject(), prrTime(posixTime), prrData(nElm, arrayPtr) {
		;
	}

	wf2rootRecord& operator=(const wf2rootRecord &record) {
		*dynamic_cast<TObject*>(this) = record;
		prrTime = record.prrTime;
		prrData = record.prrData;
		return *this;
	}

	virtual ~wf2rootRecord() {
	}
	;

	void CopyToBuffer(void* bufferPtr);

	inline struct timespec GetTimeStamp() const {
		return prrTime;
	}

	inline TArrayF& GetData() {
		return prrData;
	}

	inline struct timespec SetTimeStamp(struct timespec posixTime) {
		return prrTime = posixTime;
	}

	inline TArrayF& SetData(Int_t nElm, const Float_t* arrayPtr) {
		return prrData = TArrayF(nElm, arrayPtr);
	}

	inline TArrayF& SetData(const TArrayF& array) {
		return prrData = array;
	}
};

void wf2rootRecord::CopyToBuffer(void* bufferPtr) {
	// Copy second
	memcpy(bufferPtr, &(prrTime.tv_sec), sizeof(Long64_t));

	// Copy Nanosecond
	void * currentPtr = &((static_cast<Long64_t*>(bufferPtr))[1]);
	memcpy(currentPtr, &(prrTime.tv_nsec), sizeof(Long64_t));

	// Copy Data array
	currentPtr = &((static_cast<Long64_t*>(bufferPtr))[2]);
	memcpy(currentPtr, prrData.fArray, prrData.GetSize() * sizeof(Float_t));

	return;
}

#endif /* WF2ROOTRECORD_HH_ */
