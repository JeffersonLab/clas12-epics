program asym
option +c;

#define NFIFO 32768
#define NCHAN 25
#define LOCAL_DEPTH 64     	

//#define FULLDEBUG
//#define CHANNELACCESS
//#define DOSLMPEDESTAL

#define DATAFILE

// minimum SLM rate (Hz) for including in asymmetry
//#define SLMMINIMUM (20.*240.)
#define SLMMINIMUM 0

%%extern int getbits(unsigned , int, int);
%%extern int get_idx_skip( unsigned idx );
%%extern int dumpbits(unsigned ival);
%%extern int find_pair(int index);
%%extern float sqrt( float );
%%extern int get_delay( int );
%%extern float abs( float ); 

string seq_status;
assign seq_status to "asym_seq_status";

long current_cut;
assign current_cut to "HB:Q_THRESHOLD";

int coinc_minus_cnts; assign coinc_minus_cnts to "sum_minus_5";
int coinc_plus_cnts;  assign coinc_plus_cnts to "sum_plus_5";
int accid_minus_cnts; assign accid_minus_cnts to "sum_minus_6";
int accid_plus_cnts;  assign accid_plus_cnts to "sum_plus_6";

int slm_minus_cnts;
assign slm_minus_cnts to "sum_minus_3";

int slm_plus_cnts;
assign slm_plus_cnts to "sum_plus_3";

int clk_minus_cnts;
assign clk_minus_cnts to "sum_minus_0";

int clk_plus_cnts;
assign clk_plus_cnts to "sum_plus_0";

short start;
assign start to "asym_0.STRT";

short stop;
assign stop to "asym_0.STOP";

short acqg;
assign acqg to "asym_0.ACQG";
monitor acqg;

unsigned int clock_fifo[NFIFO];
assign clock_fifo to "asym_0";

unsigned int slm_index=3;
unsigned int slm_fifo[NFIFO];
assign slm_fifo to "asym_3";

// provide defaults in case of no channel access:
unsigned int hls_rptg_scheme=4; // 8 windows is HELDELAYd=4
//unsigned int hls_rptg_scheme=0; // 0 windows is HELDELAYd=0
double hls_stbl_time=33330;
double hls_setl_time=500;
double hls_flip_freq=29.5596;

double slm_offset=595;
double slm_slope=15968;

#ifdef CHANNELACCESS

// Reporting Delay in helicity cycle
// assign hls_rptg_scheme to "HELG0DELAYd";
assign hls_rptg_scheme to "HELDELAYd";

// T_Stable in usec
assign hls_stbl_time to "HELTSTABLEd";

// T_Settle in usec 
assign hls_setl_time to "HELTSETTLEd";

// Rate of possible helicty flips
assign hls_flip_freq to "HELFREQ";

assign slm_offset to "slm_offset";
assign slm_slope to "slm_slope";

#endif

double asym_acqg_time;
assign asym_acqg_time to "asym_acqg_time";
monitor asym_acqg_time;

double beam_sync_pairs;
assign beam_sync_pairs to "beam_sync_pairs";

double asym_fifo_depth;
assign asym_fifo_depth to "asym_fifo_depth";

double unix_stamp;
assign unix_stamp to "iocclassc6:GTIM_TIME";

double asym_fdbk_stamp;
assign asym_fdbk_stamp to "HB:Q_STAMP"; 


#ifdef DATAFILE
/////////////////////////////////////////////
// THIS IS FOR RECORDING A DATA FILE:
string fname; assign fname to "asym_filename";
int filedisable; assign filedisable to "asym_file_disable";
int fd;
int isFileOpen=0;
char cfname[1024];
char shortname[1024];
int moller_reset;      assign moller_reset to "moller_reset";
int moller_accumulate; assign moller_accumulate to "moller_accumulate";
monitor asym_fdbk_stamp;
monitor moller_reset;
monitor moller_accumulate;
monitor filedisable;
evflag ev_daqReadFifo;  sync asym_fdbk_stamp   to ev_daqReadFifo;
evflag ev_daqReset;     sync moller_reset      to ev_daqReset;
evflag ev_daqStartStop; sync moller_accumulate to ev_daqStartStop;
/////////////////////////////////////////////
#endif

int asym_calc_enable[16];

int i;
int n_pairs;
int i_pair;
int i_chan;
int sync_bit;
int helicity_bit;
int value;
int pairs[NFIFO];
int idx_skip[NFIFO];
int hls_1;
int hls_2;
int sum[2];
float q_asym;
float dq_asym;
float beam_current;
int sum_plus;
int sum_minus;
unsigned int raw_value;
unsigned int raw_value_d;
char  tmp_name[128];
int i_skip;

unsigned int tmp_fifo[NFIFO];
assign tmp_fifo to "";

short tmp_short;
assign tmp_short to "";

float tmp_float;
assign tmp_float to "";

int nfifo_used;
int n_dly_cycle;
%%int asym_chan[32] ={1, 0, 0, 1, 
%%                    0, 1, 1, 1, 
%%                    1, 1, 1, 1,
%%                    0, 0, 0, 0,
%%                    1, 0, 0, 0,
%%                    1, 0, 0, 0,
%%                    1, 0, 0, 0,
%%                    0, 0, 0, 0};

%{
int open_file(char *fname, char *shortname)
{
    int fd;
    time_t calTime;
    struct tm *lclTimePtr;
    char fileDate[18];
    char thename[150];

    time( &calTime );
    lclTimePtr = localtime( &calTime );
    // add an hour because of DST and ioc time one hour behind
    lclTimePtr->tm_hour++;

    fileDate[0] = '\0'; 
    thename[0] = '\0';
    shortname[0] ='\0'; 
    strftime(&fileDate[0], 18, "%m-%d-%y_%H:%M:%S", lclTimePtr);
    strcpy( fname, fileDate );
    strcpy(shortname, "moeller_");
    strcat(shortname, fname);
    strcat(shortname, ".txt" );
    strcpy(thename, "/home/epics/DATA/MOELLER/");
    strcat(thename, shortname);
    printf("creating : %s\n",thename);
    fd = creat(thename,0);
    if (fd == ERROR)
    {
        printf("Can't open %s\n",thename);
        fd = ioGlobalStdGet(1);
    }
    printf("fd = %d\n",fd);
    return fd;
}
}%


#ifdef DATAFILE
// run a separate state code just for recording data to a file
// this works based only on listening for event updates, and
// there may be some synchronicity issues if acquisition time
// is small, i.e. less than few seconds
ss asym_file {
   
    // start by just clearing all events:
    state init {
        when () {
            efClear(ev_daqReadFifo);
            efClear(ev_daqReset);
            efClear(ev_daqStartStop);
        } state listen
    }

    state listen {
       
        // user clicked "Reset", so close file and open a new one:
        when (efTestAndClear(ev_daqReset) && moller_reset==1) {
        } state closeAndOpenFile

        // user clicked "Start", so close file and open a new one:
        when (efTest(ev_daqStartStop) && moller_accumulate==0) {
            efClear(ev_daqStartStop);
        } state closeAndOpenFile
        
        // user clicked "Stop", so close file:
        when (efTest(ev_daqStartStop) && moller_accumulate==1) {
            efClear(ev_daqStartStop);
        } state closeFile
        
        // timestamp on moller DAQ got updated, so record data to file:
        when (efTestAndClear(ev_daqReadFifo)) {
        } state appendFile 
    }
    
    state openFile {
        when (delay(1)) {
            if (filedisable) {
                strcpy(fname,"Data File Disabled");
                pvPut(fname);
            }
            else {
                printf("asym_file:  OPENING FILE ...\n");
                fd = open_file(&cfname,&shortname);
                strcpy(fname,shortname);
                pvPut(fname);
                isFileOpen=1;
                fdprintf(fd,"coin+ coin- accid+ accid- slm+ slm-\n");
            }
        } state listen
    }

    state closeFile {
        when (delay(1)) {
            if (isFileOpen && fd>0 && fd!=ioGlobalStdGet(1)) {
                printf("asym_file:  CLOSING FILE ...\n");
                close(fd);
                isFileOpen=0;
            }
        } state listen
    }

    state closeAndOpenFile {
        when (delay(1)) {
            if (isFileOpen && fd>0 && fd!=ioGlobalStdGet(1)) {
                printf("asym_file:  CLOSING FILE ...\n");
                close(fd);
                isFileOpen=0;
            }
        } state openFile
    }

    state appendFile {
        when () {
            if (isFileOpen && fd>0 && fd!=ioGlobalStdGet(1)) {
                printf("asym_file:  APPENDING FILE ...\n");
                pvGet(coinc_minus_cnts);
                pvGet(coinc_plus_cnts);
                pvGet(accid_minus_cnts);
                pvGet(accid_plus_cnts);
                pvGet(slm_plus_cnts);
                pvGet(slm_minus_cnts);
                fdprintf(fd,"%d %d %d %d %d %d\n",
                        coinc_plus_cnts,coinc_minus_cnts,
                        accid_plus_cnts,accid_minus_cnts,
                        slm_plus_cnts,slm_minus_cnts);
            }
        } state listen
    }
}
#endif

ss asym_calc {
    
    state init {
        entry {
            printf( "asym.st:  STATE INIT\n");
            sprintf(seq_status,"INIT");
            pvPut(seq_status);
        }
        when () {
#ifdef CHANNELACCESS
            pvGet( hls_setl_time );
            pvGet( hls_stbl_time );
#endif
            for (i=0; i<NCHAN; i++) {
                if (asym_chan[i]) {
                    sprintf(tmp_name,"asym_%i.ERAS",i);
                    pvAssign(tmp_short, tmp_name);
                    tmp_short = 1;
                    pvPut(tmp_short);
                    /* find number of delayed cycles  */ 
                    /* for helicty signals versus real data */
#ifdef CHANNELACCESS
                    pvGet( hls_rptg_scheme ) ;
#endif
                    n_dly_cycle = get_delay( hls_rptg_scheme );
                }
            }
        } state  start
    }

    state start{
        entry {
            printf( "asym.st:  STATE START\n");
            sprintf(seq_status,"START");
            pvPut(seq_status);
        }
        when()  {
            start = 1;
            pvPut(start);
        } state stop

    }

    state stop{
        entry {
            printf( "asym.st:  STATE STOP\n");
            sprintf(seq_status,"STOP");
            pvPut(seq_status);
        }
        when(delay(asym_acqg_time))  {
            stop = 1;
            pvPut(stop);
            pvGet(asym_acqg_time);
#ifdef CHANNELACCESS
            pvGet( hls_flip_freq ) ;
#endif
            nfifo_used = asym_acqg_time * hls_flip_freq * 2.0;
            if (nfifo_used > NFIFO - LOCAL_DEPTH) {
                nfifo_used = NFIFO - LOCAL_DEPTH;
            }
            printf(stderr,"asym.st-STOP:  T=%.1f F=%.4f NFIFOUSED=%d\n",
                    asym_acqg_time,hls_flip_freq,nfifo_used);
        } state pause
    }

    state pause {
        entry {
            printf( "asym.st:  STATE PAUSE\n");
            sprintf(seq_status,"PAUSE");
            pvPut(seq_status);
        }
        when (delay(1)) { 
            ;
        } state read
    }

    state read {
        entry {
            printf( "asym.st:  STATE READ\n");
            sprintf(seq_status,"READ");
            pvPut(seq_status);
        }
        when (acqg == 0) {
            sprintf(tmp_name,"asym_0.READ");
            pvAssign(tmp_short, tmp_name);
            tmp_short = 1;
            pvPut(tmp_short);
            sprintf(tmp_name,"asym_3.READ");
            pvAssign(tmp_short, tmp_name);
            tmp_short = 1;
            pvPut(tmp_short);
        } state find_good_pairs
    }

    state find_good_pairs {
        when() {
            fprintf(stderr, "asym.st:  FIND GOOD PAIRS\n");
            sprintf(seq_status,"FINDPAIRS");
            pvPut(seq_status);

            pvGet(current_cut);
#ifdef CHANNELACCESS
            pvGet(slm_slope);   
            pvGet(slm_offset);
#endif
            pvGet(slm_fifo);   
            pvGet(clock_fifo);   

            fprintf(stderr,"asym.st-FIND1:  %f %f\n",slm_slope,slm_offset);
            fprintf(stderr,"asym.st-FIND2:  %d %d\n",nfifo_used,LOCAL_DEPTH);

            i = 0;
            n_pairs = 0;
            fprintf(stderr,"lookging for pairs ...\n");
            while (i < nfifo_used-LOCAL_DEPTH) {
#ifdef FULLDEBUG
                fprintf(stderr,"looking for pairs..index at: %i out of %i\n",i,nfifo_used);
#endif
                i = find_pair(i);
                if (i < nfifo_used-LOCAL_DEPTH) {
                    asym_fifo_depth = i+3;
                    pairs[n_pairs] = i;
                    idx_skip[n_pairs] = get_idx_skip( i );
#ifdef FULLDEBUG
                    fprintf(stderr,"%d %d %d %d\n",
                            asym_fifo_depth,n_pairs,pairs[n_pairs],idx_skip[n_pairs]);
#endif
                    n_pairs++;
                    i = i + 4;
                } else {
                    i++;
                }
            }

            fprintf(stderr,"asym.st-FIND3: %d %d\n",n_pairs,asym_fifo_depth);

            beam_sync_pairs = n_pairs-1;
            pvPut(beam_sync_pairs);
            pvPut(asym_fifo_depth);
        } state get_asym
    }


   state get_asym {
       when() {
           printf( "asym.st:  GET ASYM (delay=%dwindows)\n",n_dly_cycle);
           sprintf(seq_status,"GETASYM");
           pvPut(seq_status);
           for (i_chan = 0; i_chan < NCHAN; i_chan++) {
               if (asym_chan[i_chan]) {
                   sprintf(tmp_name,"asym_calc_enable_%i",i_chan);
                   pvAssign(tmp_short, tmp_name);
                   pvGet(tmp_short);
                   asym_calc_enable[i_chan] = tmp_short;
               }
           }

#ifdef FULLDEBUG
           printf("Delayed by %d cycles \n", n_dly_cycle );
           printf("Settle time is %f \n", hls_setl_time*10.0 );
           printf("Stable time is %f \n", hls_stbl_time*10.0 );
           printf("n_fifo_used is %d \n", nfifo_used ); 
           printf("n_pairs is %d \n", n_pairs );
#endif
          for (i_chan = 0; i_chan < NCHAN; i_chan++) {
             if (asym_chan[i_chan] && asym_calc_enable[i_chan]) {
               if (i_chan != 0) {
	             sprintf(tmp_name,"asym_%i.READ",i_chan);
	             pvAssign(tmp_short, tmp_name);
	             tmp_short = 1;
	             pvPut(tmp_short);
               }
 
               sprintf(tmp_name,"asym_%i",i_chan);
               pvAssign(tmp_fifo, tmp_name);
               pvGet(tmp_fifo);

               sum[0] = 0;
               sum[1] = 0;
               for (i_pair=0; i_pair<n_pairs-1; i_pair++) {
                   if ( ( pairs[i_pair] + n_dly_cycle*2 ) < ( nfifo_used - LOCAL_DEPTH ) ) {
                       i_skip =  idx_skip[i_pair];


                       for (i=i_skip; i<4; i=i+2) { 
                           raw_value    = tmp_fifo[pairs[i_pair]+i];
                           raw_value_d  = tmp_fifo[pairs[i_pair]+i + n_dly_cycle*2];
                           sync_bit     = getbits(raw_value,31,1);   /* sync bit */ 
                           helicity_bit = getbits(raw_value_d,30,1);  /* helicity bit */
                           value        = getbits(raw_value,23,24);  /* value */

                           if ( i==(i_skip+0) ) hls_1 = helicity_bit ;
                           if ( i==(i_skip+2) ) hls_2 = helicity_bit ;	

                           sum[helicity_bit] += value;
         
#ifdef DOSLMPEDESTAL
                           // pedestal-subtraction for SLM:
                           if (i_chan==slm_index) {
                               raw_value = clock_fifo[pairs[i_pair]+i];
                               value = getbits(raw_value,23,24);
                               sum[helicity_bit] -= slm_offset*value/1e7;
                           }
#endif

                       }
                       if ( hls_1 == hls_2 ) {
                           printf(" Illegal in pair #  %d , FIFO #  %d  : %d  %d \n", 
                                   i_pair, pairs[i_pair], hls_1, hls_2 );
                       }

                   }
               }

               sum_plus = sum[1];
               sum_minus = sum[0];

               tmp_float = sum_plus;
               sprintf(tmp_name,"sum_plus_%i",i_chan);
               pvAssign(tmp_float, tmp_name);
               pvPut(tmp_float);             

               tmp_float = sum_minus;
               sprintf(tmp_name,"sum_minus_%i",i_chan);
               pvAssign(tmp_float, tmp_name);
               pvPut(tmp_float);             

               q_asym = 100.*(sum_plus - sum_minus)/(sum_plus + sum_minus + 0.1);

               dq_asym = 100. * sqrt( ( 1. - (q_asym*q_asym)/(100.*100.) ) / (sum_plus + sum_minus + 0.1) );  

               tmp_float = q_asym;
               sprintf(tmp_name,"q_asym_%i",i_chan);
               pvAssign(tmp_float, tmp_name);
               pvPut(tmp_float);             

               // just set error to zero if we didn't really measure anything:
               if (sum_plus+sum_minus>0) tmp_float = dq_asym;
               else                      tmp_float = 0;

               sprintf(tmp_name,"d_asym_%i",i_chan);
               pvAssign(tmp_float, tmp_name);
               pvPut(tmp_float);             

             }
          }

          // update feedback timestamp if beam:
          pvGet(slm_minus_cnts);
          pvGet(slm_plus_cnts);
          pvGet(clk_minus_cnts);
          pvGet(clk_plus_cnts);
          pvGet(coinc_plus_cnts);
          pvGet(coinc_minus_cnts);
          pvGet(accid_plus_cnts);
          pvGet(accid_minus_cnts);
          if (clk_minus_cnts + clk_plus_cnts > 0 && slm_slope > 0) {
              beam_current = (slm_minus_cnts + slm_plus_cnts)/(clk_minus_cnts + clk_plus_cnts);
              beam_current = (beam_current - slm_offset)/slm_slope;
              if (beam_current > current_cut) { 
                  pvGet(unix_stamp);	
                  asym_fdbk_stamp = unix_stamp;
                  pvPut(asym_fdbk_stamp);
              }
          }
               
         
          printf("%d %d %d %d %d %d\n",
                  coinc_plus_cnts,coinc_minus_cnts,
                  accid_plus_cnts,accid_minus_cnts,
                  slm_plus_cnts,slm_minus_cnts
                  );


       } state init
   }
}



/* end of states, what follows are C functions used by states */
%{
int getbits(unsigned x, int p, int n) {
	return (x >> (p+1-n)) & ~(~0 << n);
}


/* this function looks for a good sync pair and returns the 
   index where the pair starts
   in the array */

int find_pair(int index) {
     int sync[LOCAL_DEPTH];
     int clock[LOCAL_DEPTH];
     int slm[LOCAL_DEPTH];
     int hls[LOCAL_DEPTH];
     int i1;
     int local_index;
     int next_pair;
     int beam_on;
     float min_slm_count;

     next_pair = -1;
     local_index = index;

     while( ( ( local_index + n_dly_cycle*2 ) < ( nfifo_used - LOCAL_DEPTH ) ) && 
             (next_pair == -1) ) {
         for (i1 = 0; i1 < LOCAL_DEPTH; i1++) {
             sync[i1]  = getbits(clock_fifo[local_index+i1],31,1);  /* sync bit */
             hls[i1]   = getbits(clock_fifo[local_index+i1+n_dly_cycle*2],30,1);  /* helicity bit */
             clock[i1] = getbits(clock_fifo[local_index+i1],23,24);  /* 10MHz clock counts */
             slm[i1]   = getbits(slm_fifo[local_index+i1],23,24);  /* slm counts */
         }

         beam_on = 1;

         if (SLMMINIMUM>0) {
             min_slm_count = (float)SLMMINIMUM /  hls_flip_freq ; 
             for (i1=1; i1<LOCAL_DEPTH; i1=i1+2) {
                 if (slm[i1] < min_slm_count ) {  
                     beam_on = 0;     
                 } 
             }
         }

         //printf(" s: "); for ( i1 = 0; i1 < LOCAL_DEPTH; i1++ ) printf(" %8d ", sync[i1] ) ; printf("\n");
         //printf(" h: "); for ( i1 = 0; i1 < LOCAL_DEPTH; i1++ ) printf(" %8d ", hls[i1] );   printf("\n");
         //printf(" c: "); for ( i1 = 0; i1 < LOCAL_DEPTH; i1++ ) printf(" %8d ", clock[i1] ); printf("\n");
         //printf(" m: "); for ( i1 = 0; i1 < LOCAL_DEPTH; i1++ ) printf(" %8d ", slm[i1] );   printf("\n");

         if ( 1 && 

                 ( ( hls[1]  == hls[2]   && 
                     hls[0]  == hls[3] ) ||
                   ( hls[0]  == hls[1]   && 
                     hls[2]  == hls[3] ) ) &&
                 hls[1] != hls[3]    && 

                 /*
                    sync[0] == sync[1]  &&
                    sync[2] == sync[3]  &&
                    */
                 /*
                    sync[0] == sync[3]  &&
                    sync[1] == sync[2]  &&

                    ( ( hls[1]  == hls[2]   && 
                    hls[3]  == hls[4] ) ||
                    ( hls[0]  == hls[1]   && 
                    hls[2]  == hls[3] ) ) &&   
                    hls[1] != hls[3]    && 
                    sync[1] != sync[3]  && 
                    */

             /* These cuts are here because time interval can vary at ~ 0.1% level */
             abs( clock[1] - clock[3] ) < ( 0.005 * abs( clock[1] + clock[3] ) ) && 
             abs( clock[0] - clock[2] ) < ( 0.005 * abs( clock[0] + clock[2] ) ) && 

                 beam_on == 1)  {
                     next_pair = local_index;
                 } else {
                     local_index++;
                 }

     }
     if (next_pair == -1) next_pair = NFIFO;
     return next_pair;
}


/* Returns 0 if the long time interval is first and */ 
/* returns 1 if the long time interval is second */
int get_idx_skip( unsigned idx ) {
    int i_long;
    long clock0;
    long clock1;
    clock0 = getbits(clock_fifo[idx+0],23,24);  /* 10MHz on first  interval */
    clock1 = getbits(clock_fifo[idx+1],23,24);  /* 10MHz on second interval */
#ifdef FULLDEBUG
    printf("get_idx_skip: clock0/1 = %i/%i\n",clock0,clock1);
#endif
    i_long = (clock0>clock1) ? 0 : 1; 
    return i_long;
}


int dumpbits(unsigned ival) {
  int i;
  unsigned bit[32];

  for (i=31; i>-1; i--) {
    bit[i] = getbits(ival,i,1);
    printf("%u ",bit[i]);
  }
  printf("\n");
  return 1;
}


/* Function to find the number of helicty states delayed */
/* Based on the info provided from Scot Higgins */
int get_delay( int delay_rec ) {
  int delay = 0;
  switch( delay_rec ) {
      case 0:
        delay = 0;
        break;
      case 1:
        delay = 1;
        break;
      case 2:
        delay = 2;
        break;
      case 3:
        delay = 4;
        break;
      case 4:
        delay = 8;
        break;
      case 5:
        delay = 12;
        break;
      case 6:
        delay = 16;
        break;
      case 7:
        delay = 24;
        break;
      case 8:
        delay = 32;
        break;
      case 9:
        delay = 40;
        break;
      case 10:
        delay = 48;
        break;
      case 11:
        delay = 64;
        break;
      case 12:
        delay = 72;
        break;
      case 13:
        delay = 96;
        break;
      case 14:
        delay = 112;
        break;
      case 15:
        delay = 128;
        break;
      default:
	delay = 0;
	break;
  }
  return delay;
}


}%


