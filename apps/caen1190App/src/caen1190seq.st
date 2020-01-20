program caen1190seq

#define TDC 195.3125e-12
#define MAXBINS 0x80000

#define NCHANS 4
#define MAXHITS 10000

%% extern int caen1190_init();
%% extern int caen1190_read(unsigned int*,unsigned int*,unsigned int);

//%%#include "time.h"
//%% extern void gettimeofday(struct timeval*,struct timezone*);
//float microseconds(struct timeval t1,struct timeval t2) {
//  return 1e6*(t2.tv_sec-t1.tv_sec)+(t2.tv_usec-t1.tv_usec);
//}
//struct timeval tv_t1,tv_t2;

// input PVs:
int errors;    assign errors to  "{P}:errors";
short status;  assign status to  "{P}:status";
short clear;   assign clear  to  "{P}:clear";  monitor clear;
short enable;  assign enable to  "{P}:enable"; monitor enable;
float timer;   assign timer  to  "{P}:timer";
float dwell;   assign dwell  to  "{P}:dwell";
float binsize; assign binsize to "{P}:binsize";
int prescale;  assign prescale to "{P}:prescale";
int ticsperbin;assign ticsperbin to "{P}:ticsperbin";

// output PVs:
float rates[NCHANS];           assign rates to {};
float histos[NCHANS][MAXBINS]; assign histos to {};
float xaxis[MAXBINS];          assign xaxis to "{P}:xaxis";

// local variables:
int ii,jj,itmp;
unsigned int tdcs[NCHANS][MAXHITS],len[NCHANS];

#define UDF 0
#define INIT 1
#define WAIT 2
#define READ 3
#define CLEAR 4
#define ERROR 5
#define PVS 6

ss caen1190seq {

	state start {

		entry {
			status=UDF;
			pvPut(status);
			pvAssignSubst(histos[0],"{P}:wf:0");
			pvAssignSubst(histos[1],"{P}:wf:1");
			pvAssignSubst(histos[2],"{P}:wf:2");
			pvAssignSubst(histos[3],"{P}:wf:3");
			pvAssignSubst(rates[0],"{P}:hz:0");
			pvAssignSubst(rates[1],"{P}:hz:1");
			pvAssignSubst(rates[2],"{P}:hz:2");
			pvAssignSubst(rates[3],"{P}:hz:3");
		    if (caen1190_init()!=0) {
				status=ERROR;
				pvPut(status);
			}
		}

        when (pvConnectCount() < pvChannelCount()) {
			status=PVS;
			pvPut(status);
            epicsThreadSleep(1);
        } state start

		when () {
			status=INIT;
			pvPut(status);
		} state watch
	}

	state watch {
		entry {
			status=WAIT;
			pvPut(status);
		}
        when (pvConnectCount() < pvChannelCount()) {
			status=PVS;
			pvPut(status);
            epicsThreadSleep(1);
        } state watch
		when (clear) {} state clear
		when (enable==1) {} state read
	}

	state clear {
		entry {
			clear=0;
			pvPut(clear);
			pvGet(status);
			itmp=status;
			status=CLEAR;
			pvPut(status);
			for (ii=0; ii<NCHANS; ii++) {
				for (jj=0; jj<MAXBINS; jj++) {
					histos[ii][jj]=0;
				}
				rates[ii]=0;
			}
            epicsThreadSleep(0.2);
		}
		when (itmp==READ) {} state read
		when (itmp==WAIT) {} state watch
	}

	state read {
        
		// do not reset timer unless entering from a different state:
        option -t;
	
		entry {
			status=READ;
			pvPut(status);
            pvGet(binsize);
            pvGet(dwell);
            pvGet(ticsperbin);
            pvGet(prescale);
            //gettimeofday(&tv_t1,NULL);
		}

		when (clear) {} state clear
		when (enable==0) {} state watch

        // dwell time expired:
		when (delay(dwell)) {
            // update rates and bin contents:
			for (ii=0; ii<NCHANS; ii++) {
				rates[ii]/=dwell;
				pvPut(rates[ii]);
				pvPut(histos[ii]);
			}
            // update bin coordinates:
            itmp=MAXBINS/ticsperbin;
            for (ii=0; ii<itmp; ii++) {
                xaxis[ii]=ii*ticsperbin*TDC*1E6;
            }
            pvPut(xaxis);
		} state clear

        // read data:
		when () {
			errors=caen1190_read((unsigned int*)tdcs,len,prescale);
			pvPut(errors);
			for (ii=0; ii<NCHANS; ii++) {
				for (jj=0; jj<len[ii]; jj++) {
                    // find the bin and fill it:
                    itmp=(int)tdcs[ii][jj]/ticsperbin;
					if (itmp<MAXBINS) {
						histos[ii][itmp]++;
					}
                    // count total rate:
					rates[ii]++;
				}
			}
            //gettimeofday(&tv_t2);
            //timer=microseconds(tv_t1,tv_t2)*1e-6;
            //pvPut(timer);
		} state read

    }

}


