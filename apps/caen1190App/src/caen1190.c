#include "caen1190.h"

#define SLOT_ADDR 0x11300000
#define SLOT_INDX 0
#define ALMOSTFULL 1024

#define MICROSEC(tv1,tv2) \
    (1e6*(tv2.tv_sec-tv1.tv_sec)+(tv2.tv_usec-tv1.tv_usec))

extern struct v1190_struct* c1190p[V1190_MAX_MODULES];
unsigned int *TDCBUF;
unsigned int IPHYS,IUSER,ISIZE,IDMA;

int caen1190_init()
{
	int ntdc,ret;
	
    vmeOpenDefaultWindows();
    //vmeCheckMutexHealth(1); // this may kill DiagGuiServer?

    usrVmeDmaSetMemSize(0x200000);
    usrVmeDmaInit();
    usrVmeDmaSetConfig(2,3,0); // A32,MBLT
    usrVmeDmaMemory(&IPHYS, &IUSER, &ISIZE);
    // some sort of address bounday conditions, maybe not necessary:
    IDMA = IUSER;
    IDMA = IDMA & 0xFFFFFFF0;
    IDMA = IDMA + 0x10;
    TDCBUF = (unsigned int*)IDMA;

	ntdc=tdc1190Init(SLOT_ADDR,0x00000,1,0);
	printf("Init %d:                    %d\n",SLOT_INDX,ntdc);

    // probably not necssary, but might as well:
    ret=tdc1190Reset(SLOT_INDX);
    printf("Reset:                      %d\n",ret);

    // this reads from $CLON_PARMS/tdc1190/hostname.cnf:
	if (ntdc) tdc1190Config("");

	ret=tdc1190SetContinuousStorageMode(SLOT_INDX);
	printf("Set Continuous Storage %d:  %d\n",SLOT_INDX,ret);
	ret=tdc1190ReadAcquisitionMode(SLOT_INDX);
	printf("Read Acquisition Mode %d:   %d\n",SLOT_INDX,ret);
	ret=tdc1190SetEdgeResolution(SLOT_INDX,200);
	printf("Set Edge Resolution: %d:    %d\n",SLOT_INDX,ret);
	ret=tdc1190GetEdgeResolution(SLOT_INDX);
	printf("Get Edge Resolution: %d:    %d\n",SLOT_INDX,ret);
    ret=tdc1190SetEdgeDetectionConfig(SLOT_INDX,2);
	printf("Set Edge Detection: %d:     %d\n",SLOT_INDX,ret);
    ret=tdc1190ReadEdgeDetectionConfig(SLOT_INDX);
	printf("Get Edge Detection: %d:     %d\n",SLOT_INDX,ret);
    ret=tdc1190SetAlmostFullLevel(SLOT_INDX,ALMOSTFULL);
    printf("Set Almost Full: %d:        %d\n",SLOT_INDX,ret);
    ret=tdc1190GetAlmostFullLevel(SLOT_INDX);
    printf("Get Almost Full: %d:        %d\n",SLOT_INDX,ret);
    if (ret!=ALMOSTFULL) {
        printf("Error setting almostfull.");
        return 1;
    }

    printf("caen1190 Initialization complete.\n\n");
    return 0;

    //ret=tdc1190SetMaxNumberOfHitsPerEvent(SLOT_INDX,128);
	//ret=tdc1190GetMaxNumberOfHitsPerEvent(SLOT_INDX);
	//printf("Read Max Hits Per Event %d: %d\n",SLOT_INDX,ret);
	//tdc1190SetWindowWidth(SLOT_INDX,51175);
	//printf("Set Window Width %d:        %d\n",SLOT_INDX,ret);
	//ret=tdc1190GetWindowWidth(SLOT_INDX);
	//printf("Set Window Width %d:        %d\n",SLOT_INDX,ret);
    //tdc1190SetWindowOffset(SLOT_INDX,0);
    //ret=tdc1190EnableTDCErrorBypass(SLOT_INDX);
	//printf("Set Error Bypass %d:        %d\n",SLOT_INDX,ret);
    //ret=tdc1190DisableChannel(SLOT_INDX,0);
	//printf("Set Disable Channel %d:      %d\n",SLOT_INDX,ret);
    //ret=tdc1190EnableChannel(SLOT_INDX,0);
	//printf("Set Enable Channel %d:      %d\n",SLOT_INDX,ret);
    // DREADY works, but don't need it, use AlmostFull
    //statReg = vmeRead16(&(c1190p[SLOT_INDX]->status));
    //if (statReg & V1190_STATUS_DATA_READY)
	//tdc1190Status(SLOT_INDX);
	//tdc1190Mon(SLOT_INDX);
}

int caen1190_readOne(unsigned int *data,unsigned int *len,unsigned int *complete) {

    int jj,ii,ret,itdc;
    unsigned int word,chan,tdc,tdcbit,zeroes,trailing;
    unsigned int tdc_prev[NCHANS];
    unsigned int ready=0;
    struct timeval tv_start,tv_now;

    // initialize status counters:
    int errors=0,fulls=0;

    // initialize times and output lengths: 
    gettimeofday(&tv_start,NULL);
    for (jj=0; jj<NCHANS; jj++) {
        tdc_prev[jj]=-1;
        len[jj]=MAXHITSPERCHAN;
        for (ii=0; ii<MAXHITSPERCHAN; ii++) {
            *(data + jj*MAXHITSPERCHAN + ii) = 0;
        }
    }
    *complete=0;

    // start by clearing the 1190's buffer:
	ret=tdc1190Clear(SLOT_INDX);

    // loop until we get enough data or time elapsed:
	while (1) {

        // return if all outputs are ready:
        if (!(*complete^0xF)) {
            return errors+fulls;
        }

        // return if elapsed time is too much:
        gettimeofday(&tv_now,NULL);
        if (MICROSEC(tv_start,tv_now) > 5e5) {
			return errors+fulls;
		}

        // clear if 1190's buffer is full:
        if (tdc1190StatusFull(SLOT_INDX) > 0) {
            fulls++;
            ready=0;
            *complete=0;
            for (jj=0; jj<NCHANS; jj++) {
                tdc_prev[jj]=-1;
            }
            ret=tdc1190Clear(SLOT_INDX);
            continue;
        }
        
        // read data if 1190's buffer is almost full:
        if (tdc1190StatusAlmostFull(SLOT_INDX) > 0) {

            vmeBusLock();
            if (usrVme2MemDmaStart(SLOT_ADDR, (unsigned int)&TDCBUF[0], ALMOSTFULL*4) < 0) {
                errors++;
                printf("DMA ERROR: %d",ret);
                continue;
            }
            if (tdc1190ReadBoardDmaDone(SLOT_INDX) != ALMOSTFULL) {
                errors++;
                printf("DMA READ BYTES ERROR: %d/%d\n",ALMOSTFULL,ret);
                continue;
            }
            vmeBusUnlock();

            for (jj=0; jj<ALMOSTFULL; jj++) {
                word     = LSWAP(TDCBUF[jj]);
                chan     = (word>>19) & 0x7F;
                tdc      = (word)     & 0x7FFFF;
                zeroes   = (word>>27) & 0x1F;
                trailing = (word>>26) & 1;
                if (zeroes!=0) {
                    // this can be due to filler words
                    continue;
                }
                switch (chan) {
                    case 32:
                        itdc=0;
                        break;
                    case 33:
                        itdc=1;
                        break;
                    case 34:
                        itdc=2;
                        break;
                    case 35:
                        itdc=3;
                        break;
                    default:
                        errors++;
                        printf("Invalid Channel: %d\n",chan);
                        tdc1190Clear(SLOT_INDX);
                        continue;
                }

                tdcbit = 1<<itdc;

                // ignore if this tdc channel is complete:
                if (*complete & tdcbit) {
                    continue;
                }

                // if previous tdc is uninitialized,
                // initialize it and ignore this one:
                else if (tdc_prev[itdc]<0) {
                   tdc_prev[itdc]=tdc;
                   continue;
                }

                // check for clock rollover:
                else if (tdc_prev[itdc]>tdc) {
                    // mark as complete if already ready:
                    if (ready & tdcbit) {
                        *complete |= tdcbit;
                        continue;
                    }
                    // otherwise mark as ready:
                    else {
                        ready |= tdcbit;
                    }
                }

                // store in output buffer if ready and not complete:
                if ( (ready & tdcbit) && !(*complete & tdcbit) ) {
                    *(data + itdc*MAXHITSPERCHAN + tdc) = 1;
                    tdc_prev[itdc]=tdc;
                }
            }
        }
	}
}

int caen1190_readDeltas(unsigned int *data,unsigned int *len,unsigned int prescale) {

    int dt,jj,ret,itdc;
    unsigned int word,chan,tdc,zeroes,trailing;
    unsigned int tdc_prev[NCHANS];
    struct timeval tv_t0[NCHANS];
    struct timeval tv_start,tv_now;

    // initialize status counters:
    int errors=0,fulls=0,gaps=0;

    // initialize times and output lengths: 
    gettimeofday(&tv_start,NULL);
    for (jj=0; jj<NCHANS; jj++) {
        tdc_prev[jj]=-1;
        len[jj]=0;
    }

    // start by clearing the 1190's buffer:
	ret=tdc1190Clear(SLOT_INDX);

    // loop until we get enough data or time elapsed:
	while (1) {

        // return if any output array is almost full:
        for (jj=0; jj<NCHANS; jj++) {
            if (len[jj] >= MAXHITSPERCHAN-ALMOSTFULL) {
                return errors+gaps+fulls;
            }
        }

        // return if elapsed time is too much:
        gettimeofday(&tv_now,NULL);
        if (MICROSEC(tv_start,tv_now) > 5e5) {
			return errors+gaps+fulls;
		}

        // clear if 1190's buffer is full:
        if (tdc1190StatusFull(SLOT_INDX) > 0) {
            fulls++;
            ret=tdc1190Clear(SLOT_INDX);
            continue;
        }
        
        // read data if 1190's buffer is almost full:
        if (tdc1190StatusAlmostFull(SLOT_INDX) > 0) {

            vmeBusLock();
            if (usrVme2MemDmaStart(SLOT_ADDR, (unsigned int)&TDCBUF[0], ALMOSTFULL*4) < 0) {
                errors++;
                printf("DMA ERROR: %d",ret);
                continue;
            }
            if (tdc1190ReadBoardDmaDone(SLOT_INDX) != ALMOSTFULL) {
                errors++;
                printf("DMA READ BYTES ERROR: %d/%d\n",ALMOSTFULL,ret);
                continue;
            }
            vmeBusUnlock();

            for (jj=0; jj<ALMOSTFULL; jj++) {
                word     = LSWAP(TDCBUF[jj]);
                chan     = (word>>19) & 0x7F;
                tdc      = (word)     & 0x7FFFF;
                zeroes   = (word>>27) & 0x1F;
                trailing = (word>>26) & 1;
                if (zeroes!=0) {
                    // this can be due to filler words
                    continue;
                }
                switch (chan) {
                    case 32:
                        itdc=0;
                        break;
                    case 33:
                        itdc=1;
                        break;
                    case 34:
                        itdc=2;
                        break;
                    case 35:
                        itdc=3;
                        break;
                    default:
                        errors++;
                        printf("Invalid Channel: %d\n",chan);
                        tdc1190Clear(SLOT_INDX);
                        continue;
                }

                // store time of this readout:
                gettimeofday(&tv_now,NULL);
                
                // if previous tdc is uninitialized,
                // initialize it and ignore this one:
                if (tdc_prev[itdc]<0) {
                    tdc_prev[itdc]=tdc;
                }

                // if too much time elapsed (2 clock rollovers),
                // uninitialize previous tdc and ignore this one:
                else if (MICROSEC(tv_t0[itdc],tv_now) > 180) {
                    tdc_prev[itdc]=-1;
                    tv_t0[itdc]=tv_now;
                    gaps++;
                }

                // otherwise it's a keeper:
                else {

                    // do prescaling:
                    if (prescale>1) {
                        if ((float)rand()/RAND_MAX > (float)1./prescale) {
                            continue;
                        }
                    }

                    // calculate tdc-difference,
                    // assuming at most one clock rollover:
                    dt = (tdc-tdc_prev[itdc]) & 0x7FFFF;
                    
                    // update the output buffers:
                    *(data + itdc*MAXHITSPERCHAN + len[itdc]) = dt;
                    len[itdc]++;
                    tdc_prev[itdc]=tdc;
                }
            }
        }
	}
}
/*
int main(int argc,char *argv[]) {
	unsigned int ii,jj;
    unsigned int data[NCHANS][MAXHITSPERCHAN];
    unsigned int len[NCHANS];
    caen1190_init();
	printf("READING ...\n");
    caen1190_read((unsigned int*)data,len);
    for (ii=0; ii<NCHANS; ii++) {
        printf("MAIN: %d\n",len[ii]);
        for (jj=0; jj<len[ii]; jj++) {
            printf("MAIN: %d %d %u\n",ii,jj,data[ii][jj]);
        }
    }
    return(0);
}
*/
