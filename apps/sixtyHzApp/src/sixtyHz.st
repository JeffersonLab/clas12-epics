/* --------------------------------------------- */
program sixtyHz
/* --------------------------------------------- */
option +c;

%%#include <math.h>
#include "sixtyHz.h"

short stop;
assign stop to "sixtyHz_0.STOP";

short erase_start;
assign erase_start to "sixtyHz_0.ERST";

short acqg;
assign acqg to "sixtyHz_0.ACQG";
monitor acqg;

double dwel;
assign dwel to "sixtyHz_0.DWEL";

int i;
int i_chan;
int j;

char  tmp_name[128];

unsigned int fifo_all[NCHAN][NFIFO];
assign fifo_all to { "sixtyHz_0",  "sixtyHz_1",  "sixtyHz_2",  "sixtyHz_3", 
                     "sixtyHz_4",  "sixtyHz_5",  "sixtyHz_6",  "sixtyHz_7", 
                     "sixtyHz_8",  "sixtyHz_9", "sixtyHz_10", "sixtyHz_11",
                    "sixtyHz_12", "sixtyHz_13", "sixtyHz_14", "sixtyHz_15",
                    "sixtyHz_16", "sixtyHz_17", "sixtyHz_18", "sixtyHz_19",
                    "sixtyHz_20", "sixtyHz_21", "sixtyHz_22", "sixtyHz_23",
                    "sixtyHz_24", "sixtyHz_25", "sixtyHz_26", "sixtyHz_27",
                    "sixtyHz_28", "sixtyHz_29", "sixtyHz_30", "sixtyHz_31"}; 

short sub_fifo[2048];
assign sub_fifo to "";

float copy_fifo[NFIFO];
assign copy_fifo to "";

unsigned int null_fifo[NFIFO];

float tmp_fft_real[NFIFO];
float tmp_fft_img[NFIFO];

float power[HALF_FIFO];
assign power to "";

float phase[HALF_FIFO];
assign phase to "";

float power_0Hz;
assign power_0Hz to "";

float power_60Hz;
assign power_60Hz to "";

float power_max;
assign power_max to "";

float power_max_freq;
assign power_max_freq to "";

float total_rate;
assign total_rate to "";

float cw_to_total;
assign cw_to_total to "";

float peak_to_peak;
assign peak_to_peak to "";

float rms;
assign rms to "";

float average;
assign average to "";

float sixtyHz_debug;
assign sixtyHz_debug to "sixtyHz_debug";

int sixtyHz_bin;
int power_max_bin;

float fft_real[HALF_FIFO];
assign fft_real to "";

float fft_img[HALF_FIFO];
assign fft_img to "";

short tmp_short;
assign tmp_short to "";

float tmp_float;
assign tmp_float to "";

float time_2_fill_fifo;
float rat;
float c_0;
float c_1;
float sum;
float sumsum;
float sum_power;
float sum_cw_power;

float min_val;
float max_val;

float ang;
float test_data;
float sync_data;

%%extern void fft_float(unsigned  NumSamples, int InverseTransform, unsigned int *RealIn, unsigned int *ImagIn, float *RealOut, float *ImagOut);

ss sixtyHz_calc {
   state init {
        when () {
	  stop = 1;
          pvPut(stop);
          printf("sixtyHz init state done...waiting for HV to init...\n");
        } state  wait
   }
   state wait {
      when (delay(4)) {
         erase_start = 1;
         pvPut(erase_start);
         pvGet(dwel);
         time_2_fill_fifo = dwel*(NFIFO+10);
         sixtyHz_bin = 60.*NFIFO*dwel+0.499999;
         printf("sixtyHz....here we go data in  %f secs %i\n", time_2_fill_fifo, sixtyHz_bin);
      } state stop
   }
   state stop{
	when(delay(time_2_fill_fifo))  {
	  stop = 1;
          pvPut(stop);
        } state pause
   } 
   state pause {
         when () {
         ;
         } state read
   }
   state read {
	when(acqg == 0 ) {
	  for (i=0; i<NCHAN; i++) {
            sprintf(tmp_name,"sixtyHz_%i.READ",i);
            pvAssign(tmp_short, tmp_name);
            tmp_short = 1;
            pvPut(tmp_short);
          }
        } state get_fifo
   }
   state get_fifo {
	when() {
        pvGet(sixtyHz_debug); 
/*        printf("sixtyHz debug value %f\n", sixtyHz_debug); */
	if (sixtyHz_debug) {
             for (j=0; j< 4096; j++) {
      	       ang = j*(60.*2.*3.14159/4096.);
               test_data = 50. + 5.*cos(ang + 3.14159/8);
	       ang = j*(120.*2.*3.14159/4096.);
               test_data += 0.5*cos(ang + 7*3.14159/12.);
	       ang = j*(180.*2.*3.14159/4096.);
               test_data += 0.3*cos(ang + 5*3.14159/12.);
                     
      	       ang = j*(60.*2.*3.14159/4096.);
               sync_data = 6. + 5.*cos(ang + 3.14159/17);

               for (i_chan = 0; i_chan < NCHAN; i_chan++) {
                 if (i_chan != 10) {
                   fifo_all[i_chan][j]  = test_data;
                 } else {
                   fifo_all[i_chan][j]  = sync_data;
                 }
               }
             } 
           } else {
             for (i_chan = 0; i_chan < NCHAN; i_chan++) {
               pvGet(fifo_all[i_chan]); 
             }
           }
        } state erase_start
   }
   state erase_start {
        when() {
            pvGet(dwel);
            time_2_fill_fifo = dwel*(NFIFO+10);
            sixtyHz_bin = 60.*NFIFO*dwel+0.4999999;
            if (dwel >= 0.001) {
              erase_start = 1;
              pvPut(erase_start);
            }
        } state process_data
   }
   state process_data {
      when() {
          for (i_chan = 0; i_chan < NCHAN; i_chan++) {

               i=0;
               sum = 0.0;
               sumsum = 0.0;
               sum_power = 0.0;
               min_val = 99999999.0;
               max_val = 0.0;

               for (j=0; j < NFIFO; j++) {
                 sum = sum + fifo_all[i_chan][j];
                 sumsum = sumsum + fifo_all[i_chan][j]*fifo_all[i_chan][j];
                 if (fifo_all[i_chan][j] > 0) {
                   i++;
                   if (fifo_all[i_chan][j] < min_val) {
                      min_val = fifo_all[i_chan][j];
                   }
                   if (fifo_all[i_chan][j] > max_val) {
                      max_val = fifo_all[i_chan][j];
                   }
                 }
	         if (j >2047) {
                      sub_fifo[j-2047] = fifo_all[i_chan][j];
                 }
                 copy_fifo[j] = fifo_all[i_chan][j];                 
               }

               rat = (100.*i)/NFIFO;
               if (rat >= 1) {
                  power_max = 0;
                  power_max_bin = 0;
                  fft_float(NFIFO, 0, &fifo_all[i_chan][0], null_fifo, tmp_fft_real, tmp_fft_img);

%%                power[0] = (float) sqrt(tmp_fft_real[0]*tmp_fft_real[0] + tmp_fft_img[0]*tmp_fft_img[0]);
                  phase[0] = 0;
                  sum_power = power[0];
                  sum_cw_power = power[0];
                  if (power[0] > 0.0) {
                    for (j=1; j < (NFIFO-1)/2; j++) {
                      fft_real[j] = tmp_fft_real[j];
                      fft_img[j] = tmp_fft_img[j];
%%                    power[j] = ((float) sqrt(fft_real[j]*fft_real[j] + fft_img[j]*fft_img[j]));
                      if (fft_real[j] != 0) {
%%                       phase[j] = ((float) atan2(fft_img[j],fft_real[j]));
                      } else {
                         phase[j] = 3.14159/2.;
                      }
	              sum_power = sum_power + power[j];
                      if ((j/(NFIFO*dwel))<6) {
                         sum_cw_power = sum_cw_power + power[j];
                      }
                      power[j] = power[j]/power[0];
                      if (power[j] > power_max) {
                        power_max = power[j];
                        power_max_bin = j;
                      }
                    }
                  } else {
                    for (j=1; j < (NFIFO-1)/2; j++) {
                      fft_real[j] = tmp_fft_real[j];
                      fft_img[j] = tmp_fft_img[j];
%%                    power[j] = ((float) sqrt(fft_real[j]*fft_real[j] + fft_img[j]*fft_img[j]));
                      sum_power = sum_power + power[j];
                      power[j] = power[j]/power[0];
                      if (power[j] > power_max) {
                        power_max = power[j];
                        power_max_bin = j;
                      }
                    }
                  } 
                  power_0Hz = power[0];
                  power[0] = power[1];
                  sprintf(tmp_name,"power_0Hz_%i",i_chan);
                  pvAssign(power_0Hz, tmp_name);
                  pvPut(power_0Hz);

                  power_60Hz = power[sixtyHz_bin];
                  sprintf(tmp_name,"power_60Hz_%i",i_chan);
                  pvAssign(power_60Hz, tmp_name);
                  pvPut(power_60Hz);

                  sprintf(tmp_name,"power_max_%i",i_chan);
                  pvAssign(power_max, tmp_name);
                  pvPut(power_max);

                  power_max_freq = power_max_bin/(NFIFO*dwel);
                  sprintf(tmp_name,"power_max_freq_%i",i_chan);
                  pvAssign(power_max_freq, tmp_name);
                  pvPut(power_max_freq);

                  total_rate = sum/(NFIFO*dwel);
                  sprintf(tmp_name,"sixtyHz_total_rate_%i",i_chan);
                  pvAssign(total_rate, tmp_name);
                  pvPut(total_rate);

                  average = sum/NFIFO;
                  if (average > 0) {
                    peak_to_peak = 100.*(max_val - min_val)/(2.*average);
/*		    printf("------ debug NFIFO = %d sum = %f average = %f sumsum = %f ", NFIFO, sum, average, sumsum);
		    printf("sumsum/NFIFO = %f average^2 = %f ", sumsum/NFIFO, average*average); */
/*		    printf("delta = %f ", sumsum/NFIFO - average*average); */
%%                  rms = 100.*sqrt(fabs(sumsum/NFIFO - average*average))/average;
/*		    printf("rms = %f\n", rms); */
                  } else {
                    peak_to_peak = 0.0;
                    rms = 0.0;
                  }

                  sprintf(tmp_name,"peak2peak_%i",i_chan);
                  pvAssign(peak_to_peak, tmp_name);
                  pvPut(peak_to_peak);

                  sprintf(tmp_name,"sixtyHz_average_%i",i_chan);
                  pvAssign(average, tmp_name);
                  pvPut(average);

                  sprintf(tmp_name,"sixtyHz_rms_%i",i_chan);
                  pvAssign(rms, tmp_name);
                  pvPut(rms);

                  sprintf(tmp_name,"sixtyHz_raw_%i",i_chan);
                  pvAssign(sub_fifo, tmp_name);
                  pvPut(sub_fifo);

                  sprintf(tmp_name,"sixtyHz_copy_%i",i_chan);
                  pvAssign(copy_fifo, tmp_name);
                  pvPut(copy_fifo);

                  if (sum_power > 0.0) {
                     cw_to_total = sum_cw_power/sum_power;  
/*                     cw_to_total = power_0Hz/sum; */
                  } else {
                     cw_to_total = 0.0;
                  }
                  sprintf(tmp_name,"cw_to_total_ratio_%i",i_chan);
                  pvAssign(cw_to_total, tmp_name);
                  pvPut(cw_to_total);

                  sprintf(tmp_name,"fft_%i",i_chan);
                  pvAssign(fft_real, tmp_name);
                  pvPut(fft_real);

                  sprintf(tmp_name,"fft_img_%i",i_chan);
                  pvAssign(fft_img, tmp_name);
                  pvPut(fft_img);

                  sprintf(tmp_name,"power_%i",i_chan);
                  pvAssign(power, tmp_name);
                  pvPut(power);

                  sprintf(tmp_name,"phase_%i",i_chan);
                  pvAssign(phase, tmp_name);
                  pvPut(phase);
               }
/*
   else {
                  printf("chan %i   rat %f \n", i_chan, rat);
               }
*/
            }
            if (dwel < 0.001) {
              erase_start = 1;
              pvPut(erase_start);
            }
        } state stop
   }
}











