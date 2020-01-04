/*
 * wave2rootRecord.hh
 *
 *  Created on: Mar 24, 2014
 *      Author: yqiang
 */

#ifndef WAVE2ROOTRECORD_HH_
#define WAVE2ROOTRECORD_HH_

#include <time.h>

#include <TObject.h>
#include <TArrayF.h>

class wave2rootRecord: public TObject {

private:
	struct timespec prrTime;			// POSIX timestamp
	TArrayF prrData;			// ROOT array of floats

public:
	wave2rootRecord(struct timespec posixTime, unsigned nElm,
			const float* arrayPtr) :
			TObject(), prrTime(posixTime), prrData(nElm, arrayPtr) {
		;
	}

	wave2rootRecord& operator=(const wave2rootRecord &record) {
		*dynamic_cast<TObject*>(this) = record;
		prrTime = record.prrTime;
		prrData = record.prrData;
		return *this;
	}

	virtual ~wave2rootRecord() {
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

void wave2rootRecord::CopyToBuffer(void* bufferPtr) {
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

#endif /* WAVE2ROOTRECORD_HH_ */
