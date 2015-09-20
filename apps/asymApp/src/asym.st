/* --------------------------------------------- */
program asym
/* --------------------------------------------- */
option +c;

#include "asym.h"

%%extern int getbits(unsigned , int, int);
%%extern int get_idx_skip( unsigned idx );
%%extern int dumpbits(unsigned ival);
%%extern int find_pair(int index);
%%extern float sqrt( float );

short   harp_tagger_scan_flag;
assign  harp_tagger_scan_flag  to "harp_tagger_scan_flag.VAL";
monitor harp_tagger_scan_flag;

short   harp_2c21_scan_flag;
assign  harp_2c21_scan_flag  to "harp_2c21_scan_flag.VAL";
monitor harp_2c21_scan_flag;

short   harp_2H02A_scan_flag;
assign  harp_2H02A_scan_flag  to "harp_2H02A_scan_flag.VAL";
monitor harp_2H02A_scan_flag;

long current_cut;
assign current_cut to "HB:Q_THRESHOLD";

double  slm_offset;
assign slm_offset to "slm_offset";

double slm_slope;
assign slm_slope to "slm_slope";

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

unsigned int slm_fifo[NFIFO];
assign slm_fifo to "asym_3";

/* Reporting Delay in helicity cycles  */
unsigned int hls_rptg_scheme; 
/* assign hls_rptg_scheme to "HELG0DELAYd"; */
assign hls_rptg_scheme to "HELDELAYd";

/* T_Stable in usec  */
double hls_stbl_time;
assign hls_stbl_time to "HELTSTABLEd";

/* T_Settle in usec  */ 
double hls_setl_time;
assign hls_setl_time to "HELTSETTLEd";

/* Rate of possible helicty flips */ 
double hls_flip_freq;
assign hls_flip_freq to "HELFREQ";

double asym_acqg_time;
assign asym_acqg_time to "asym_acqg_time";
monitor asym_acqg_time;

double beam_sync_pairs;
assign beam_sync_pairs to "beam_sync_pairs";

double asym_fifo_depth;
assign asym_fifo_depth to "asym_fifo_depth";

double unix_stamp;
assign unix_stamp to "classc1:unixtime";

double asym_fdbk_stamp;
assign asym_fdbk_stamp to "HB:Q_STAMP"; 

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
char  asym_name[128];
char  d_asym_name[128];
char  sum_plus_name[128];
char  sum_minus_name[128];

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

int i_skip;

/* float complete_fifo[NFIFO,NCHAN]; */

ss asym_calc {
   state init {
        when () {
	  pvGet( hls_setl_time );
	  pvGet( hls_stbl_time );
	  for (i=0; i<NCHAN; i++) {
	    if (asym_chan[i]) {
              sprintf(tmp_name,"asym_%i.ERAS",i);
              pvAssign(tmp_short, tmp_name);
              tmp_short = 1;
              pvPut(tmp_short);
	 /* find number of delayed cycles  */ 
	 /* for helicty signals versus real data */
  	      pvGet( hls_rptg_scheme ) ;
	      n_dly_cycle = get_delay( hls_rptg_scheme );
            }
          }
        } state  start
   }
   state start{
	when()  {
	  start = 1;
          pvPut(start);
        } state stop

   } 
   state stop{
	when(delay(asym_acqg_time))  {
	  stop = 1;
          pvPut(stop);
          pvGet(asym_acqg_time);
/*          nfifo_used = asym_acqg_time*60; */
	  pvGet( hls_flip_freq ) ;
	  nfifo_used = asym_acqg_time * hls_flip_freq * 2.0;
          if (nfifo_used > NFIFO - LOCAL_DEPTH) {
            nfifo_used = NFIFO - LOCAL_DEPTH;
          }
        } state pause

   } 
   state pause {
         when (delay(1)) { 
         ;
         } state read
   }
   state read {
	when(acqg == 0) {
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

           pvGet(current_cut);   
           pvGet(slm_slope);   
           pvGet(slm_offset);   
           pvGet(slm_fifo);   
           pvGet(clock_fifo);   

	   i = 0;
           n_pairs = 0;
           while (i < nfifo_used-LOCAL_DEPTH) {
/*             printf("looking for pairs..index at: %i out of %i\n",i,nfifo_used); */
             i = find_pair(i);
	     if (i < nfifo_used-LOCAL_DEPTH) {
               asym_fifo_depth = i+3;
               pairs[n_pairs] = i;
	       idx_skip[n_pairs] = get_idx_skip( i );
               n_pairs++;
               i = i + 4;
             } else {
               i++;
             }
           }
           beam_sync_pairs = n_pairs-1;
           pvPut(beam_sync_pairs);
           pvPut(asym_fifo_depth);
        } state get_asym
   }
   state get_asym {
	when() {
          for (i_chan = 0; i_chan < NCHAN; i_chan++) {
            if (asym_chan[i_chan]) {
              sprintf(tmp_name,"asym_calc_enable_%i",i_chan);
              pvAssign(tmp_short, tmp_name);
              pvGet(tmp_short);
	      asym_calc_enable[i_chan] = tmp_short;
            }
	  }

/*
	printf("Delayed by %d cycles \n", n_dly_cycle );
	printf("Settle time is %f \n", hls_setl_time*10.0 );
	printf("Stable time is %f \n", hls_stbl_time*10.0 );
	printf("n_fifo_used is %d \n", nfifo_used ); 
	printf("n_pairs is %d \n", n_pairs );
*/

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

                      sum[helicity_bit] = sum[helicity_bit] + value;
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

/*	       dq_asym = 100./ sqrt( (1. - q_asym*q_asym) / (sum[1]+ sum[0] +1.) ) ; */
/*               dq_asym = 100./(sqrt(sum[1]+ sum[0] +1)); */
/*	printf( "Asymetry for chan %d is %f +- %f \n", i_chan,  q_asym, dq_asym );  */

               tmp_float = q_asym;
               sprintf(tmp_name,"q_asym_%i",i_chan);
               pvAssign(tmp_float, tmp_name);
               pvPut(tmp_float);             

               tmp_float = dq_asym;
               sprintf(tmp_name,"d_asym_%i",i_chan);
               pvAssign(tmp_float, tmp_name);
               pvPut(tmp_float);             

            }
          }
          pvGet(slm_minus_cnts);
          pvGet(slm_plus_cnts);
          pvGet(clk_minus_cnts);
          pvGet(clk_plus_cnts);
          if (clk_minus_cnts + clk_plus_cnts > 0 && slm_slope > 0) {
            beam_current = (slm_minus_cnts + slm_plus_cnts)/(clk_minus_cnts + clk_plus_cnts);
            beam_current = (beam_current - slm_offset)/slm_slope;
            if (beam_current > current_cut) { 
                pvGet(unix_stamp);	
                asym_fdbk_stamp = unix_stamp;
                pvPut(asym_fdbk_stamp);
/*	        printf("updating values: unix_stamp %f fdbk_stamp %f\n",unix_stamp, asym_fdbk_stamp); */
            }
          }
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

/* #define LOCAL_DEPTH (16)     	 */
int find_pair(int index) {
     int sync[LOCAL_DEPTH];
     int clock[LOCAL_DEPTH];
     int slm[LOCAL_DEPTH];
     int hls[LOCAL_DEPTH];
     int i1;
     int local_index;
     int next_pair;
     int beam_on;
     float  min_slm_count;

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

/*       printf("find_pair: local_index: %i slm[1]: %i\n",local_index,slm[1]); */

       beam_on = 1;
/* The minimum counts is normalized to 20 at 240 Hz assuming ~5nA beam*/ 
       min_slm_count = 20. * 240. /  hls_flip_freq ; 
/*       min_slm_count = 0.0;	*/
       for (i1=1; i1<LOCAL_DEPTH; i1=i1+2) {
          if (slm[i1] < min_slm_count ) {  
              beam_on = 0;     
          } 
       } 

/*
	printf(" s: ");
	for ( i1 = 0; i1 < LOCAL_DEPTH; i1++ )
	  printf(" %8d ", sync[i1] );
	printf("\n");

	printf(" h: ");
	for ( i1 = 0; i1 < LOCAL_DEPTH; i1++ )
	  printf(" %8d ", hls[i1] );
	printf("\n");
     
	printf(" c: ");
	for ( i1 = 0; i1 < LOCAL_DEPTH; i1++ )
	  printf(" %8d ", clock[i1] );
	printf("\n");

	printf(" m: ");
	for ( i1 = 0; i1 < LOCAL_DEPTH; i1++ )
	  printf(" %8d ", slm[i1] );
	printf("\n");
*/

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
     if (next_pair == -1) {
       next_pair = NFIFO;
     }
/*	printf("Next pair is : %d \n", next_pair ); */
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
	if( clock0 > clock1 ) {
	   i_long = 0;
	} else {
	   i_long = 1;
	}
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


