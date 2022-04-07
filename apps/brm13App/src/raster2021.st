/* uitfraster.st
 * 
 * A sequencer for the control of uitf raster.
 */

program uitfraster

option +c; /* Wait for all database connections */


%% #include <stdio.h>
%% #include <math.h>
%% #include <string.h>


/* constants */
#define MIN_RASTER_CURRENT 0.2  /* minimum current */
#define MAX_RASTER_CURRENT 5.0  /* maximum current */
#define RAMP_DELTA 0.1          /* volts per interval */
#define RAMP_TIME  1.0          /* 1 second interval */
#define MIN_VOLT  0.01          /* minimum voltage written to A33500 */

/* Sequence Status */
string raster_status;
assign raster_status to "ITFRA_STATUSW";

/* reset BRM board FSD */
short fsd_reset;
assign fsd_reset to "ITFRA_FSDRESET";
monitor fsd_reset;
evflag effsd_reset;
sync fsd_reset effsd_reset;

short zero_go;
assign zero_go to "ITFRA_WOFF";
monitor zero_go;
evflag efzero_go;
sync zero_go efzero_go;

short waveform_go;
assign waveform_go to "ITFRA_WGO";
monitor waveform_go;
evflag efwaveform_go;
sync waveform_go efwaveform_go;

float brm_ipeak;
assign brm_ipeak to "ITFRA_IPEAK";

float brm_x_voltage;
assign brm_x_voltage to "ITFRA_VOLTAGE.D";

float brm_y_voltage;
assign brm_y_voltage to "ITFRA_VOLTAGE.E";

/*******************************/
/*            BRM PVs          */
/*******************************/

float brm_ixpeak;
assign brm_ixpeak to "ITFRA_IXPEAK";

float brm_iypeak;
assign brm_iypeak to "ITFRA_IYPEAK";

/* FSD Clear on BRM */
long brm_a_fsdcon;
assign brm_a_fsdcon to "ITFRA_FSDCONLO";

float brm_a_ximax_a;
assign brm_a_ximax_a to "ITFRA_XIMAX.A";

float brm_a_ximin_a;
assign brm_a_ximin_a to "ITFRA_XIMIN.A";

float brm_a_yimax_a;
assign brm_a_yimax_a to "ITFRA_YIMAX.A";

float brm_a_yimin_a;
assign brm_a_yimin_a to "ITFRA_YIMIN.A";

float brm_a_ximax;
assign brm_a_ximax to "ITFRA_XIMAX";
monitor brm_a_ximax;
evflag efbrm_ximax;
sync brm_a_ximax efbrm_ximax;

float brm_a_ximin;
assign brm_a_ximin to "ITFRA_XIMIN";
monitor brm_a_ximin;
evflag efbrm_ximin;
sync brm_a_ximin efbrm_ximin;

float brm_a_yimax;
assign brm_a_yimax to "ITFRA_YIMAX";
monitor brm_a_yimax;
evflag efbrm_yimax;
sync brm_a_yimax efbrm_yimax;

float brm_a_yimin;
assign brm_a_yimin to "ITFRA_YIMIN";
monitor brm_a_yimin;
evflag efbrm_yimin;
sync brm_a_yimin efbrm_yimin;

/*******************************/
/*            A33500 PVs          */
/*******************************/
/* horizontal Fundamental Amplitude */
float wg_xampl;
assign wg_xampl to "ITFRA_WG_XAMPL";

/* Horizontal Fundamental Amplitude */
float wg_yampl;
assign wg_yampl to "ITFRA_WG_YAMPL";

/* horizontal Fundamental Amplitude readback */
float wg_xampl_readback;
assign wg_xampl_readback to "ITFRA_WG_XAMPl";
monitor wg_xampl_readback;

/* Horizontal Fundamental Amplitude readback */
float wg_yampl_readback;
assign wg_yampl_readback to "ITFRA_WG_YAMPl";
monitor wg_yampl_readback;

/* horizontal output control */
short wg_xoutput;
assign wg_xoutput to "ITFRA_WG_XOUTPUT";

/* Horizontal output control */
short wg_youtput;
assign wg_youtput to "ITFRA_WG_YOUTPUT";

/* horizontal output readback */
short wg_xoutput_readback;
assign wg_xoutput_readback to "ITFRA_WG_XOUTPUt";
monitor wg_xoutput_readback;

/* Horizontal output readback */
short wg_youtput_readback;
assign wg_youtput_readback to "ITFRA_WG_YOUTPUt";
monitor wg_youtput_readback;

/* Button for generator initialization */
short wg_init_proc;
assign wg_init_proc to "ITFRA_WG_INIT.PROC";

/* variables */
float ramp_goal;
float ramp_x_goal;
float ramp_y_goal;
float ramp_x;
float ramp_y;


ss uitf_raster {
  state init {
    when () {
      /* reset A33500 to defaults */
/*      wg_init_proc = 1;
      pvPut(wg_init_proc); */
      /* turn A33500 output off */
      wg_xoutput = 0;
      pvPut(wg_xoutput);
      wg_youtput = 0;
      pvPut(wg_youtput);

      /* set low limit */
      brm_a_ximin_a = MIN_RASTER_CURRENT;
      pvPut(brm_a_ximin_a);
      brm_a_yimin_a = MIN_RASTER_CURRENT;
      pvPut(brm_a_yimin_a);

      /* set high limit */
      brm_a_ximax_a = MAX_RASTER_CURRENT;
      pvPut(brm_a_ximax_a);
      brm_a_yimax_a = MAX_RASTER_CURRENT;
      pvPut(brm_a_yimax_a);
    
      /* init BRM FSD to write the limits to DAC */
      brm_a_fsdcon = 1;
      pvPut(brm_a_fsdcon);
      /* clear BRM FSD bits */
      brm_a_fsdcon = 2;
      pvPut(brm_a_fsdcon);

      sprintf(raster_status, "Write current limits to BRM");
      pvPut(raster_status);

      /* clear event flags */
      efClear(efzero_go);
      efClear(efwaveform_go);
      efClear(effsd_reset);
      efClear(efbrm_ximax);
      efClear(efbrm_yimax);
      efClear(efbrm_ximin);
      efClear(efbrm_yimin);
    } state wait_actions
  }

  /* wait for user to push buttons */
  state wait_actions {
    /* Ramp To Zero button */
    when (efTestAndClear(efzero_go) && zero_go == 1) {
    } state ramp_zero
    
    /* Send Current button */
    when (efTestAndClear(efwaveform_go) && waveform_go == 1) {
    } state send_waveform

    /* FSD reset button */
    when (efTestAndClear(effsd_reset) && fsd_reset == 1) {
      sprintf(raster_status, "Reset BRM FSD");
      pvPut(raster_status);
      brm_a_fsdcon = 2;
      pvPut(brm_a_fsdcon);
    } state wait_actions

    /* current limit is written */
    when (efTestAndClear(efbrm_ximax) || efTestAndClear(efbrm_yimax) ||
          efTestAndClear(efbrm_ximin) || efTestAndClear(efbrm_yimin)) {
    } state write_limits
  }

  /* set A33500 amplitude and output waveform */
  state send_waveform {
    when () {
        sprintf(raster_status, "Sending current to magnets");
        pvPut(raster_status);

        /* open limits to avoid FSD durning the current change */
        /* set low limit */
        brm_a_ximin_a = MIN_RASTER_CURRENT;
        pvPut(brm_a_ximin_a);
        brm_a_yimin_a = MIN_RASTER_CURRENT;
        pvPut(brm_a_yimin_a);

        /* set high limit */
        brm_a_ximax_a = MAX_RASTER_CURRENT;
        pvPut(brm_a_ximax_a);
        brm_a_yimax_a = MAX_RASTER_CURRENT;
        pvPut(brm_a_yimax_a);
    
        /* init BRM FSD to write the limits to DAC */
        brm_a_fsdcon = 1;
        pvPut(brm_a_fsdcon);
        /* clear BRM FSD bits */
        brm_a_fsdcon = 2;
        pvPut(brm_a_fsdcon);

        sprintf(raster_status, "Write current limits to BRM");
        pvPut(raster_status);
	
        if (wg_xoutput_readback == 0 || wg_youtput_readback == 0) {
          if (wg_xoutput_readback == 0) {
            wg_xampl = MIN_VOLT;
            pvPut(wg_xampl);
            wg_xoutput = 1;
            pvPut(wg_xoutput);
          }
          if (wg_youtput_readback == 0) {
            wg_yampl = MIN_VOLT;
            pvPut(wg_yampl);
            wg_youtput = 1;
            pvPut(wg_youtput);
          }
          epicsThreadSleep(RAMP_TIME);
        }
        pvGet(brm_x_voltage);
        ramp_x_goal = brm_x_voltage;
        pvGet(brm_y_voltage);
        ramp_y_goal = brm_y_voltage;
        ramp_x = wg_xampl_readback;
        ramp_y = wg_yampl_readback;
        while (1) {
          if (ramp_x < ramp_x_goal) {
            ramp_x += RAMP_DELTA;
            if (ramp_x > ramp_x_goal) {
              ramp_x = ramp_x_goal;
            }
            wg_xampl = ramp_x;
            pvPut(wg_xampl);
          }
          else if (ramp_x > ramp_x_goal) {
            ramp_x -= RAMP_DELTA;
            if (ramp_x < ramp_x_goal) {
              ramp_x = ramp_x_goal;
            }
            wg_xampl = ramp_x;
            pvPut(wg_xampl);
          }

          if (ramp_y < ramp_y_goal) {
            ramp_y += RAMP_DELTA;
            if (ramp_y > ramp_y_goal) {
              ramp_y = ramp_y_goal;
            }
            wg_yampl = ramp_y;
            pvPut(wg_yampl);
          }
          else if (ramp_y > ramp_y_goal) {
            ramp_y -= RAMP_DELTA;
            if (ramp_y < ramp_y_goal) {
              ramp_y = ramp_y_goal;
            }
            wg_yampl = ramp_y;
            pvPut(wg_yampl);
          }
          if (ramp_x == ramp_x_goal && ramp_y == ramp_y_goal) break;
          epicsThreadSleep(RAMP_TIME);
        }

        /* Set limits to +/-10% of the initial current value */
	epicsThreadSleep(3);
	pvGet(brm_ixpeak);
	brm_a_ximin_a = brm_ixpeak * 0.9;
	pvPut(brm_a_ximin_a);
	brm_a_ximax_a = brm_ixpeak * 1.1;
	pvPut(brm_a_ximax_a);
	pvGet(brm_iypeak);
	brm_a_yimin_a = brm_iypeak * 0.9;
	pvPut(brm_a_yimin_a);
	brm_a_yimax_a = brm_iypeak * 1.1;
	pvPut(brm_a_yimax_a);

        /* init BRM FSD to write the limits to DAC */
        brm_a_fsdcon = 1;
        pvPut(brm_a_fsdcon);
        /* clear BRM FSD bits */
        brm_a_fsdcon = 2;
        pvPut(brm_a_fsdcon);

        sprintf(raster_status, "Sending current complete");
        pvPut(raster_status);
    } state wait_actions
  }

  /* voltage ramps down to zero */
  state ramp_zero {
    when () {
      sprintf(raster_status, "Ramping current down to zero");
      pvPut(raster_status);
      ramp_goal = MIN_VOLT;
      ramp_x = wg_xampl_readback;
      ramp_y = wg_yampl_readback;
      while (1) {
        if (ramp_x < ramp_goal) {
          ramp_x = ramp_goal;
          wg_xampl = ramp_x;
          pvPut(wg_xampl);
        }
        else if (ramp_x > ramp_goal) {
          ramp_x -= RAMP_DELTA;
          if (ramp_x < ramp_goal) {
            ramp_x = ramp_goal;
          }
          wg_xampl = ramp_x;
          pvPut(wg_xampl);
        }

        if (ramp_y < ramp_goal) {
          ramp_y = ramp_goal;
          wg_yampl = ramp_y;
          pvPut(wg_yampl);
        }
        else if (ramp_y > ramp_goal) {
          ramp_y -= RAMP_DELTA;
          if (ramp_y < ramp_goal) {
            ramp_y = ramp_goal;
          }
          wg_yampl = ramp_y;
          pvPut(wg_yampl);
        }
        if (ramp_x == ramp_goal && ramp_y == ramp_goal) break;
        epicsThreadSleep(RAMP_TIME);
      }
      wg_xoutput = 0;
      pvPut(wg_xoutput);
      wg_youtput = 0;
      pvPut(wg_youtput);
      sprintf(raster_status, "Ramping current down complete");
      pvPut(raster_status);
    } state wait_actions
  }

  state write_limits {
    when () {
      /* init BRM FSD to write the limits to DAC */
      brm_a_fsdcon = 1;
      pvPut(brm_a_fsdcon);
      /* clear BRM FSD bits */
      brm_a_fsdcon = 2;
      pvPut(brm_a_fsdcon);

      sprintf(raster_status, "Write current limits to BRM");
      pvPut(raster_status);
    } state wait_actions
  }
}	
