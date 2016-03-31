/* --------------------------------------------- */
program struckDaq
/* --------------------------------------------- */
option +c;
/*option -t;*/

%%#include <math.h>
%%#include <time.h>

#include "struckDaq.h" 

short stop;
assign stop to "struckDaq_0.STOP";

short erase_start; 
assign erase_start to "struckDaq_0.ERST";

short start;
assign start to "struckDaq_0.STRT";
 
short acqg;
assign acqg to "struckDaq_0.ACQG";
monitor acqg;

double dwel;
assign dwel to "struckDaq_0.DWEL";

double elapsedTime;
assign elapsedTime to "struckDaq_0.ELTM";

double deadTime;
assign deadTime to "struckDaq_0.DTIM";


char tmp_name[128];

unsigned long fifo_all[NCHAN][NFIFO];
/*assign fifo_all to {"struckDaq_0",  "struckDaq_1",  "struckDaq_2",  "struckDaq_3", 
                    "struckDaq_4",  "struckDaq_5",  "struckDaq_6",  "struckDaq_7", 
                    "struckDaq_8",  "struckDaq_9",  "struckDaq_10", "struckDaq_11",
                    "struckDaq_12", "struckDaq_13", "struckDaq_14", "struckDaq_15",
                    "struckDaq_16", "struckDaq_17", "struckDaq_18", "struckDaq_19",
                    "struckDaq_20", "struckDaq_21", "struckDaq_22", "struckDaq_23",
                    "struckDaq_24", "struckDaq_25", "struckDaq_26", "struckDaq_27",
                    "struckDaq_28", "struckDaq_29", "struckDaq_30", "struckDaq_31"}; 
*/
assign fifo_all to {"struckDaq_0",  "struckDaq_1",  "struckDaq_2",  "struckDaq_3", 
                    "struckDaq_4"};

unsigned long fifo_0[NFIFO];
assign fifo_0 to "struckDaq_0";

float copy_fifo[NFIFO]; 
assign copy_fifo to "";

float total_rate;
assign total_rate to "";

float struckDaq_debug;
assign struckDaq_debug to "struckDaq_debug";
monitor struckDaq_debug;

int struckDaq_bin;

short tmp_short;
assign tmp_short to "";

float tmp_float;
assign tmp_float to "";

float time_2_fill_fifo;

float pause_time = 0.00000; /* Time to pause before reading */ 


int i_chan;
int i;
int j;

float sum;

%%struct timespec currTime; 
%%double stopTime = 0;
%%double startTime = 0;
%%double deltaTime = 0;


ss struckDaqSequence {
  state init {
    when () {
	    printf( "struckDaq: state init...");
/*	    stop = 1;
        pvPut(stop);
*/
%%      clock_gettime(CLOCK_REALTIME, &currTime );
        printf("done.\n");
    } state  wait
  }

  state wait {
    entry { printf( "struckDaq: state wait...\n"); }
    when (delay(10)) { 
        erase_start = 1; 
        pvPut(erase_start);
        pvGet(dwel);
	    pvGet(struckDaq_debug);
        time_2_fill_fifo = dwel*(NFIFO+10);
        struckDaq_bin = 60.*NFIFO*dwel+0.499999;
        printf("struckDaq: wait done, data in  %f secs %i\n", time_2_fill_fifo, struckDaq_bin);
    } state stop
  } 
 
  state stop{
    when() { 
/*	    stop = 1;
        pvPut(stop); 
*/
    } state read
  } 

  state read {
    when( acqg == 0 ) { 
	    for (i=0; i<NCHAN; i++) {
            sprintf(tmp_name,"struckDaq_%i.READ",i);
            pvAssign(tmp_short, tmp_name); 
            tmp_short = 1;
            pvPut(tmp_short);
        }
    } state get_fifo
  }
 
  state get_fifo {
    when() {
	    for (i_chan = 0; i_chan < NCHAN; i_chan++) {  
            pvGet(fifo_all[i_chan], ASYNC);
        }
    } state restart_sis 
  }

  state restart_sis {
    when() { 
        erase_start = 1;
        pvPut(erase_start);
%%      clock_gettime(CLOCK_REALTIME, &currTime );
%%      startTime = (1.0e+09 * currTime.tv_sec + currTime.tv_nsec); 
        pvGet(dwel);
    } state process_data
  }

  state process_data {
    when() {
        for (i_chan = 0; i_chan < NCHAN; i_chan++) { 
            sum = 0.0;
            for (j=0; j < NFIFO; j++) { 
/*              if( fifo_all[i_chan][j] < 10 ) 
		   	        printf( "FIFO [%d][%d] is %lu\n", i_chan, j, fifo_all[i_chan][j]); 
*/
                sum = sum + fifo_all[i_chan][j];
                copy_fifo[j] = fifo_all[i_chan][j];                 
            }

            total_rate = sum/(NFIFO*dwel);  
            sprintf(tmp_name,"struckDaq_total_rate_%i",i_chan);
            pvAssign(total_rate, tmp_name);
            pvPut(total_rate, ASYNC );
            
            sprintf(tmp_name,"struckDaq_copy_%i",i_chan);
            pvAssign(copy_fifo, tmp_name);
            pvPut(copy_fifo, ASYNC ); 
        }
%%      clock_gettime(CLOCK_REALTIME, &currTime );
%%    	stopTime = (1.0e+09 * currTime.tv_sec + currTime.tv_nsec); 
%%	    deltaTime = stopTime - startTime;
%%	    if (struckDaq_debug) printf( "struckDaq: Seconds %ld :: millisecond %ld \n", currTime.tv_sec, currTime.tv_nsec/1000000 );
	    time_2_fill_fifo =  (1.1*(NFIFO)*dwel) - ( deltaTime / 1.0e+09 );
	    if( time_2_fill_fifo < 0 ) time_2_fill_fifo = 0.;
	    epicsThreadSleep(time_2_fill_fifo);	  
    } state stop
  }

} // end state set

