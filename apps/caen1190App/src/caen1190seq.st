program caen1190seq

%%#include <math.h>

// TDC resolution (seconds):
#define TDC 195.3125e-12

// TDC time window (microseconds):
#define MAXMICRO 102.4000

// number of TDC bins:
#define FIFO 0x80000

// number of FFT bins:
#define HALF_FIFO 0x40000

// maximum FFT frequency corresponding to TDC resolution (Hz):
#define MAXHERTZ 2.56E9

// number of channels:
#define NCHANS 4

// number of FFT maxima to calculate:
#define NMAXES 4

#define PI  (3.14159265358979323846)

// sequencer states:
#define UDF 0
#define INIT 1
#define WAIT 2
#define READ 3
#define CLEAR 4
#define ERROR 5
#define PVS 6
#define ANA 7

%%extern int caen1190_init();
%%extern int caen1190_readOne(unsigned int*,unsigned int*,unsigned int*);
%%extern int caen1190_readDeltas(unsigned int*,unsigned int*,unsigned int);
%%extern void fft_float(unsigned,int,unsigned int*,unsigned int*,float*,float*);
%%extern void fft_double(unsigned,int,unsigned int*,unsigned int*,double*,double*);
%%int get_freq_bin(float freq) {
%%  int bin=(int)((float)HALF_FIFO*freq/MAXHERTZ);
%%  if (bin<0 || bin>=HALF_FIFO) bin=0;
%%  return bin;
%%}

// input PVs:
short clear;           assign clear  to      "{P}:clear";  monitor clear;
short enable;          assign enable to      "{P}:enable"; monitor enable;
float dwell;           assign dwell  to      "{P}:dwell";  monitor dwell;
float binsize;         assign binsize to     "{P}:binsize";
int prescale;          assign prescale to    "{P}:prescale";
int ticsperbin;        assign ticsperbin to  "{P}:ticsperbin";
short pulser_enab;     assign pulser_enab to "{P}:pulser:enable";
float pulser_freq;     assign pulser_freq to "{P}:pulser:freq";
short enables[NCHANS]; assign enables to     {};

// output PVs:
int errors;                            assign errors to   "{P}:errors";
short status;                          assign status to   "{P}:status";
float timer;                           assign timer  to   "{P}:timer";
unsigned int complete;                 assign complete to "{P}:complete";
float xaxis[FIFO];                     assign xaxis to    "{P}:xaxis";
double faxis[HALF_FIFO];               assign faxis to    "{P}:faxis";
float rates[NCHANS];                   assign rates to {};
float histos[NCHANS][FIFO];            assign histos to {};
float dwellpower[NCHANS][HALF_FIFO];   assign dwellpower to {};
float dwellpowermax[NCHANS];           assign dwellpowermax to {};
float dwellpowerslowmax[NCHANS];       assign dwellpowerslowmax to {};
float powermaxes[NCHANS][NMAXES];      assign powermaxes to {};
float fpowermaxes[NCHANS][NMAXES];     assign fpowermaxes to {};
float powerslowmaxes[NCHANS][NMAXES];  assign powerslowmaxes to {};
float fpowerslowmaxes[NCHANS][NMAXES]; assign fpowerslowmaxes to {};
float power250MHz[NCHANS];             assign power250MHz to {};
float power120KHz[NCHANS];             assign power120KHz to {};

float dwellpowersum[HALF_FIFO];   assign dwellpowersum        to "{P}:dwellpower:sum";
float dwellpowermaxsum;           assign dwellpowermaxsum     to "{P}:dwellpower:max:sum";
float dwellpowerslowmaxsum;       assign dwellpowerslowmaxsum to "{P}:dwellpower:slow:max:sum";
float powermaxessum[NMAXES];      assign powermaxessum        to "{P}:power:maxes:amp:sum";
float fpowermaxessum[NMAXES];     assign fpowermaxessum       to "{P}:power:maxes:freq:sum";
float powerslowmaxessum[NMAXES];  assign powerslowmaxessum    to "{P}:power:slow:maxes:amp:sum";
float fpowerslowmaxessum[NMAXES]; assign fpowerslowmaxessum   to "{P}:power:slow:maxes:freq:sum";

float power250MHzsum; assign power250MHzsum to "{P}:power:250MHz:sum";
float power120KHzsum; assign power120KHzsum to "{P}:power:120KHz:sum";

float rmspower[HALF_FIFO];
float rms;                assign rms           to "{P}:rms";
float rmscutofffreq;      assign rmscutofffreq to "{P}:rms:cutoff:freq";
int rmsrebin;             assign rmsrebin      to "{P}:rms:rebin";

// local variables:
string stmp;
unsigned int completions;
double ftmp,ftmp2,favg;
float real[FIFO],imag[FIFO];
int ii,jj,kk,ll,itmp,nbins,imax,imax2,ndwellpower[NCHANS];
int ipowermaxes[NCHANS][NMAXES],ipowerslowmaxes[NCHANS][NMAXES];
int ipowermaxessum[NMAXES],ipowerslowmaxessum[NMAXES];
unsigned int tdcs[NCHANS][FIFO],len[NCHANS],null_fifo[FIFO];
evflag ef_timer_stop,ef_timer_start;


ss caen1190seq {

	state start {

		entry {
			status=INIT;
			pvPut(status);
            for (ii=0; ii<NCHANS; ii++) {
                sprintf(stmp,"{P}:wf:%d",ii);
                pvAssignSubst(histos[ii],stmp);
                sprintf(stmp,"{P}:hz:%d",ii);
                pvAssignSubst(rates[ii],stmp);
                sprintf(stmp,"{P}:dwellpower:%d",ii);
                pvAssignSubst(dwellpower[ii],stmp);
                sprintf(stmp,"{P}:dwellpower:max:%d",ii);
                pvAssignSubst(dwellpowermax[ii],stmp);
                sprintf(stmp,"{P}:dwellpower:slow:max:%d",ii);
                pvAssignSubst(dwellpowerslowmax[ii],stmp);
                sprintf(stmp,"{P}:enable:%d",ii);
                pvAssignSubst(enables[ii],stmp);
                sprintf(stmp,"{P}:power:120KHz:%d",ii);
                pvAssignSubst(power120KHz[ii],stmp);
                sprintf(stmp,"{P}:power:250MHz:%d",ii);
                pvAssignSubst(power250MHz[ii],stmp);
                sprintf(stmp,"{P}:power:maxes:amp:%d",ii);
                pvAssignSubst(powermaxes[ii],stmp);
                sprintf(stmp,"{P}:power:slow:maxes:amp:%d",ii);
                pvAssignSubst(powerslowmaxes[ii],stmp);
                sprintf(stmp,"{P}:power:maxes:freq:%d",ii);
                pvAssignSubst(fpowermaxes[ii],stmp);
                sprintf(stmp,"{P}:power:slow:maxes:freq:%d",ii);
                pvAssignSubst(fpowerslowmaxes[ii],stmp);
            }
            // initialize caen1190:
		    if (caen1190_init()!=0) {
				status=ERROR;
				pvPut(status);
			}
            // intialize axes at full-scale:
            for (ii=0; ii<FIFO; ii++) {
                xaxis[ii]=ii*TDC*1E6; // ps
                if (ii < HALF_FIFO) {
                    faxis[ii]=ii/(MAXMICRO/1E6)/1000; //kHz
                }
            }
		}

        // if initialization error, never leave this state:
        when (status==ERROR) {} state start

        // wait for pvs to connect:
        when (pvConnectCount() < pvChannelCount()) {
			status=PVS;
			pvPut(status);
            sprintf(stmp,"Waiting for PVs (%d/%d)",pvConnectCount(),pvChannelCount());
            printf("%s\n",stmp);
            epicsThreadSleep(1);
        } state start

		when () {
			status=INIT;
			pvPut(status);
            pvPut(faxis);
            pvPut(xaxis);
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

        when (clear)     {} state clear
        when (enable==1) {} state read
	}

	state clear {

        // zero histograms/integrals/counters:
		entry {
			clear=0;
			pvPut(clear);
			pvGet(status);
			itmp=status;
			status=CLEAR;
			pvPut(status);
            status=itmp;
            for (jj=0; jj<HALF_FIFO; jj++) {
                dwellpowersum[jj]=0;
                rmspower[jj]=0;
            }
			for (ii=0; ii<NCHANS; ii++) {
				for (jj=0; jj<FIFO; jj++) {
					histos[ii][jj]=0;
                    if (jj<HALF_FIFO) {
                        dwellpower[ii][jj]=0;
                    }
				}
				rates[ii]=0;
                ndwellpower[ii]=0;
                dwellpowermax[ii]=0;
                dwellpowerslowmax[ii]=0;
                power250MHz[ii]=0;
                power120KHz[ii]=0;
                for (jj=0; jj<NMAXES; jj++) {
                    powermaxes[ii][jj]=0;
                    powerslowmaxes[ii][jj]=0;
                    fpowermaxes[ii][jj]=0;
                    fpowerslowmaxes[ii][jj]=0;
                    ipowermaxes[ii][jj]=0;
                    ipowerslowmaxes[ii][jj]=0;

                    powermaxessum[jj]=0;
                    fpowermaxessum[jj]=0;
                    ipowermaxessum[jj]=0;
                    powerslowmaxessum[jj]=0;
                    fpowerslowmaxessum[jj]=0;
                    ipowerslowmaxessum[jj]=0;
                }
			}
		}

        // determine which state to return to based on previous status:
        when (delay(0.2) && status==ANA)  {} state read
		when (delay(0.2) && status==READ) {} state read
		when (delay(0.2) && status==WAIT) {} state watch
	}

	state read {
        
		// do not reset timer unless entering from a different state:
        option -t;

        // get the setup for this read cycle and start timer:
		entry {
			status=READ;
            errors=0;
            pvPut(errors);
			pvPut(status);
            pvGet(binsize);
            pvGet(ticsperbin);
            pvGet(prescale);
            pvGet(pulser_enab);
            pvGet(pulser_freq);
            for (ii=0; ii<NCHANS; ii++) pvGet(enables[ii]);
            efSet(ef_timer_start);
            completions=0;
		}

        // respond to user input and dwell timer:
		when (clear)        {} state update
		when (enable==0)    {} state watch
		when (delay(dwell)) {} state update

        // read data:
		when () {

            // time-delta read for histogramming:
			errors = caen1190_readDeltas((unsigned int*)tdcs,len,prescale);

            // fill histograms:
            for (ii=0; ii<NCHANS; ii++) {

                if (enables[ii]==0) continue;

                // real data:
				for (jj=0; jj<len[ii]; jj++) {
                    // find the histogram bin and fill it:
                    itmp = (int)tdcs[ii][jj]/ticsperbin;
					if (itmp<FIFO) histos[ii][itmp]++;
                    // count total rate:
					rates[ii]++;
				}
                
                // overlay fake data (1st channel only):
                if (ii==0 && pulser_enab) {
                    nbins = FIFO/ticsperbin;
                    // pulser period (micro-seconds):
                    ftmp = (float)1./pulser_freq/1E3*1E6;
                    // pulser period (bins):
                    for (jj=0; jj<nbins; jj++) {
%%                      histos[ii][jj] += 1000*sin(2*PI/(ftmp/MAXMICRO)*jj/nbins);
%%                      //+7000*cos(7*2*PI/(ftmp/MAXMICRO)*jj/nbins-0.5);;
                    }
                }
            }

            // one-window read for fourier:
			errors += caen1190_readOne((unsigned int*)tdcs,len,&complete);

            // analyze it: 
            for (ii=0; ii<NCHANS; ii++) {

                if (enables[ii]==0) continue;
                
                // overlay fake data (1st channel only):
                if (pulser_enab && ii==0) {
                    ftmp = (float)1./pulser_freq/1E3*1E6;
                    for (jj=0; jj<FIFO; jj++) {
%%                      tdcs[ii][jj] += 100000000*sin(2*PI/(ftmp/MAXMICRO)*jj/FIFO);
%%                      //+7000*cos(7*2*PI/(ftmp/MAXMICRO)*jj/FIFO-0.5);
                    }
                    complete |= 1;
                }
               
                // ignore if not a complete window read for this channel:
                else if ( (complete & (1<<ii)) == 0) continue;

                // do fourier transform:
                fft_float(FIFO,0,&tdcs[ii][0],null_fifo,real,imag);

                // 0Hz/DC component and its running sum:
%%              dwellpower[ii][0] += sqrt(real[0]*real[0]+imag[0]*imag[0]);

                // higher components:
                ftmp=0;
                for (jj=1; jj<(FIFO-1)/2; jj++) {
                    // jj-th frequency and its running sum:
%%                  dwellpower[ii][jj] += sqrt(real[jj]*real[jj]+imag[jj]*imag[jj]);
                }

                // keep track of #reads for later averaging:
                ndwellpower[ii]++;
            }
			
            pvPut(errors);
            pvPut(complete);

            completions |= complete;

		} state read

        // stop timer:
        exit {
            efSet(ef_timer_stop);
        }

    }

    state update {

        // do averaging, update pvs: 
		entry {
			for (ii=0; ii<NCHANS; ii++) {

                if (enables[ii]==0) continue;

				rates[ii] /= dwell;
               
                // find maximum frequencies:
                ftmp  = 0;
                ftmp2 = 0;
                nbins = 0;
                favg  = 0;
                for (jj=1; jj<(FIFO-1)/2; jj++) {

                    // scale by 0Hz component and average:
                    dwellpower[ii][jj] /= dwellpower[ii][0];// * ndwellpower[ii];

                    if (completions & (1<<ii)) 
                    dwellpowersum[jj] += dwellpower[ii][jj];

%%                  if (abs(jj-get_freq_bin(249.502E6+1)>10 &&
%%                      abs(jj-get_freq_bin(126.953E3+1)>10))) {
                        favg += dwellpower[ii][jj];
                        nbins++;
%%                    }

                    if (dwellpower[ii][jj] > ftmp) {
                        ftmp = dwellpower[ii][jj];
                        imax = jj;
                    }
                    if (faxis[jj]>10 && faxis[jj]<1E4) {
                        if (dwellpower[ii][jj] > ftmp2) {
                            ftmp2 = dwellpower[ii][jj];
                            imax2 = jj;
                        }
                    }

                    for (kk=0; kk<NMAXES; kk++) {
                        if (dwellpower[ii][jj] > powermaxes[ii][kk]) {
                            for (ll=NMAXES-1; ll>kk; ll--) {
                                powermaxes[ii][ll]  = powermaxes[ii][ll-1];
                                ipowermaxes[ii][ll] = ipowermaxes[ii][ll-1];
                            }
                            powermaxes[ii][kk]  = dwellpower[ii][jj];
                            ipowermaxes[ii][kk] = jj;
                            break;
                        }
                    }

                    for (kk=0; kk<NMAXES; kk++) {
                        if (faxis[jj]>10 && faxis[jj]<1E4) {
                            if (dwellpower[ii][jj] > powerslowmaxes[ii][kk]) {
                                for (ll=NMAXES-1; ll>kk; ll--) {
                                    powerslowmaxes[ii][ll]  = powerslowmaxes[ii][ll-1];
                                    ipowerslowmaxes[ii][ll] = ipowerslowmaxes[ii][ll-1];
                                }
                                powerslowmaxes[ii][kk]  = dwellpower[ii][jj];
                                ipowerslowmaxes[ii][kk] = jj;
                                break;
                            }
                        }
                    }
                }
                dwellpower[ii][0]     = 0;//dwellpower[ii][1]/ndwellpower[ii];

                dwellpowermax[ii]     = imax/(MAXMICRO/1E6)/1000;
                dwellpowerslowmax[ii] = imax2/(MAXMICRO/1E6)/1000;
                
                ftmp = 0;
                itmp = get_freq_bin(249.502E6+1);
                for (jj=itmp-1; jj<=itmp+1; jj++) {
                    ftmp += dwellpower[ii][jj];
                }
                power250MHz[ii] = ftmp-3.0*favg/nbins;
                
                ftmp = 0;
                itmp = get_freq_bin(126.953E3+1);
                for (jj=itmp-1; jj<=itmp+1; jj++) {
                    ftmp += dwellpower[ii][jj];
                }
                power120KHz[ii] = ftmp-3.0*favg/nbins;
            }

            for (ii=0; ii<NCHANS; ii++) {
                if (enables[ii]==0) continue;
                for (jj=0; jj<NMAXES; jj++) {
                    fpowermaxes[ii][jj]     = faxis[ipowermaxes[ii][jj]];
                    fpowerslowmaxes[ii][jj] = faxis[ipowerslowmaxes[ii][jj]];
                }
            }

            ////////////////////////////////////////////////
            dwellpowersum[0] = 0;
            ftmp=0;
            ftmp2=0;
            nbins = 0;
            favg  = 0;
            for (jj=1; jj<(FIFO-1)/2; jj++) {
%%                  if (abs(jj-get_freq_bin(249.502E6+1)>10 &&
%%                      abs(jj-get_freq_bin(126.953E3+1)>10))) {
                        favg += dwellpower[ii][jj];
                        nbins++;
%%                    }

                if (dwellpowersum[jj] > ftmp) {
                    ftmp = dwellpowersum[jj];
                    imax = jj;
                }
                if (faxis[jj]>10 && faxis[jj]<1E4) {
                    if (dwellpowersum[jj] > ftmp2) {
                        ftmp2 = dwellpowersum[jj];
                        imax2 = jj;
                    }
                }
                for (kk=0; kk<NMAXES; kk++) {
                    if (dwellpowersum[jj] > powermaxessum[kk]) {
                        for (ll=NMAXES-1; ll>kk; ll--) {
                            powermaxessum[ll]  = powermaxessum[ll-1];
                            ipowermaxessum[ll] = ipowermaxessum[ll-1];
                        }
                        powermaxessum[kk]  = dwellpowersum[jj];
                        ipowermaxessum[kk] = jj;
                        break;
                    }
                }
                for (kk=0; kk<NMAXES; kk++) {
                    if (faxis[jj]>10 && faxis[jj]<1E4) {
                        if (dwellpowersum[jj] > powerslowmaxessum[kk]) {
                            for (ll=NMAXES-1; ll>kk; ll--) {
                                powerslowmaxessum[ll]  = powerslowmaxessum[ll-1];
                                ipowerslowmaxessum[ll] = ipowerslowmaxessum[ll-1];
                            }
                            powerslowmaxessum[kk]  = dwellpowersum[jj];
                            ipowerslowmaxessum[kk] = jj;
                            break;
                        }
                    }
                }
            }
            dwellpowermaxsum = imax/(MAXMICRO/1E6)/1000;
            dwellpowerslowmaxsum = imax2/(MAXMICRO/1E6)/1000;
            ftmp = 0;
            itmp = get_freq_bin(249.502E6+1);
            for (jj=itmp-1; jj<=itmp+1; jj++) {
                ftmp += dwellpowersum[jj];
            }
            power250MHzsum = ftmp-3.0*favg/nbins;

            ftmp = 0;
            itmp = get_freq_bin(126.953E3+1);
            for (jj=itmp-1; jj<=itmp+1; jj++) {
                ftmp += dwellpowersum[jj];
            }
            power120KHzsum = ftmp-3.0*favg/nbins;
            for (jj=0; jj<NMAXES; jj++) {
                fpowermaxessum[jj] = faxis[ipowermaxessum[jj]];
                fpowerslowmaxessum[jj] = faxis[ipowerslowmaxessum[jj]];
            }

            for (ii=0; ii<NCHANS; ii++) {
                pvPut(dwellpower[ii]);
                pvPut(dwellpowermax[ii]);
                pvPut(dwellpowerslowmax[ii]);
				pvPut(rates[ii]);
				pvPut(histos[ii]);
                pvPut(power250MHz[ii]);
                pvPut(power120KHz[ii]);
                pvPut(powermaxes[ii]);
                pvPut(powerslowmaxes[ii]);
                pvPut(fpowermaxes[ii]);
                pvPut(fpowerslowmaxes[ii]);
			}
            pvPut(dwellpowersum);
            pvPut(dwellpowermaxsum);
            pvPut(dwellpowerslowmaxsum);
            pvPut(power250MHzsum);
            pvPut(power120KHzsum);
            pvPut(powermaxessum);
            pvPut(powerslowmaxessum);
            pvPut(fpowermaxessum);
            pvPut(fpowerslowmaxessum);

            // update bin coordinates:
            for (ii=0; ii<FIFO; ii++) {
                xaxis[ii]=ii*ticsperbin*TDC*1E6;
            }
            pvPut(xaxis);
		}
        
        when () {} state rms
    }

    state rms {
        entry {
            pvGet(rmscutofffreq);
            pvGet(rmsrebin);
            rms = 0;
            ftmp = 0;
            itmp = get_freq_bin(rmscutofffreq)/rmsrebin;
            nbins = 0;
            if (itmp>1 && itmp<HALF_FIFO) {
                for (jj=0; jj<HALF_FIFO; jj++) {
                    kk = jj/rmsrebin;
                    if (kk >= itmp) break;
                    rmspower[kk] += dwellpowersum[jj];
                    ftmp += dwellpowersum[jj];
                    nbins++;
                }
                // the mean:
                ftmp /= nbins;
                // the rms:
                rms=0;
                for (jj=0; jj<itmp; jj++) {
%%                  rms += pow(rmspower[jj]-ftmp,2);
                }
%%              rms = sqrt(rms/(nbins-1));
                // poisson-subtracted rms:
                rms -= sqrt(ftmp);
            }
            pvPut(rms);
        }
        when () {} state clear
    }
}


// a 1-second clock just for user feedback:
ss caen1190timer {
    state start {
        when (pvConnectCount() < pvChannelCount()) {
            epicsThreadSleep(1);
        } state start
        when () {} state idle
    }
    state idle {
        when (efTestAndClear(ef_timer_start)) {
            timer=0;
            pvPut(timer);
        } state run
    }
    state run {
        option -t;
        when (delay(timer+1)) {
            timer+=1;
            pvPut(timer);
        } state run
        when (efTestAndClear(ef_timer_stop)) {} state idle
    }
}

