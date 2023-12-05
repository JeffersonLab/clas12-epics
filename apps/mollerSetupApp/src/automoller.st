//
// automoller.st - Automated Moller Run Setup
//
// automoller.db (and automoller-sim.db) contain associated records
//
// N. Baltzell, 2018
//
program automoller ("P=B_MOLLER:,SIMTAG=,SIMQUAD=,SIMHELM=,SIMDET=")

// not reentrant (only one instance allowed):
option -r;

// safe mode:
option +s;

// whether to use Brian's quad calculation:
#define USE_BRIANS_QUADS 1

#include "automoller.h"

#define MESSAGE(MSG) \
    sprintf(msg,#MSG);\
    printf("%s\n",msg);\
    pvPut(msg);

#define TMPMESSAGE(MSG) \
    sprintf(stmp,msg);\
    sprintf(msg,#MSG);\
    printf("%s\n",msg);\
    pvPut(msg);\
    epicsThreadSleep(2);\
    sprintf(msg,stmp);\
    pvPut(msg);

%{epicsTimeStamp timeStamp;}%
string runStartTime;
string runEndTime;

int isMollerRunning;
int isMollerConfigured;
float hv_slm_default;
int itmp;
string stmp;

// Sequencer Status:
string msg; assign msg    to "{P}ctrl:msg";
int status; assign status to "{P}ctrl:status";
int runno;  assign runno  to "{P}ctrl:runno";

// Logbook Entry:
string logcomments; assign logcomments to "{P}ctrl:logcomments";
string logusers;    assign logusers    to "{P}ctrl:logusers";
int    logentry;    assign logentry    to "{P}ctrl:logentry"; monitor logentry;

// User Controls:
int moller_enter; assign moller_enter to "{P}ctrl:enter"; monitor moller_enter;
int moller_exit;  assign moller_exit  to "{P}ctrl:exit";  monitor moller_exit;
int moller_recfg; assign moller_recfg to "{P}ctrl:recfg"; monitor moller_recfg;
int daq_start;    assign daq_start    to "{P}ctrl:start"; monitor daq_start;
int daq_stop;     assign daq_stop     to "{P}ctrl:stop";  monitor daq_stop;

// User Configurations:
float quad_icfg;   assign quad_icfg     to "{P}cfg:quad:iset";
float helm_icfg;   assign helm_icfg     to "{P}cfg:helm:iset";
int helm_polcfg;   assign helm_polcfg   to "{P}cfg:helm:pol";
int tgt_cfg;       assign tgt_cfg       to "{P}cfg:tgt:pos";
float hv_slm_vcfg; assign hv_slm_vcfg   to "{P}cfg:slm:vset"; monitor hv_slm_vcfg;
int   quad_icfg_auto;  assign quad_icfg_auto  to "{P}cfg:quad:iset:auto";
float quad_icfg_1pass; assign quad_icfg_1pass to "{P}cfg:quad:iset:1pass";
float quad_icfg_2pass; assign quad_icfg_2pass to "{P}cfg:quad:iset:2pass";
float quad_icfg_3pass; assign quad_icfg_3pass to "{P}cfg:quad:iset:3pass";
float quad_icfg_4pass; assign quad_icfg_4pass to "{P}cfg:quad:iset:4pass";
float quad_icfg_5pass; assign quad_icfg_5pass to "{P}cfg:quad:iset:5pass";

// Tagger Current: 
float tagger_irbk; assign tagger_irbk to "{SIMTAG}TMIRBCK";  monitor tagger_irbk;

// Beam Energy:
float beamEnergy; assign beamEnergy to "MBSY2C_energy";
int   beamPasses; assign beamPasses to "MMSHLBPASS";

// Half-Wave Plate:
int halfwaveplate; assign halfwaveplate to "IGL1I00DI24_24M";

// Wien Angles:
float vwienangle; assign vwienangle to "PWF1I04:spinCalc";
float hwienangle; assign hwienangle to "PWF1I06:spinCalc";

// CODA run number:
int coda_runno; assign coda_runno to "B_DAQ:run_number";

// Quadrupole Controls:
int quadB_isOn;    assign quadB_isOn    to "{SIMQUAD}DYNAB:stat:on"; monitor quadB_isOn;
//int quadB_isOn;    assign quadB_isOn    to "{SIMQUAD}DYNABPSON"; monitor quadB_isOn;
int quadC_isOn;    assign quadC_isOn    to "{SIMQUAD}DYNACPSON"; monitor quadC_isOn;
int quadB_on;      assign quadB_on      to "{SIMQUAD}DYNAB:on";
//int quadB_on;      assign quadB_on      to "{SIMQUAD}DYNABON";
int quadC_on;      assign quadC_on      to "{SIMQUAD}DYNACON";
int quadB_off;     assign quadB_off     to "{SIMQUAD}DYNAB:off";
//int quadB_off;     assign quadB_off     to "{SIMQUAD}DYNABOFF";
int quadC_off;     assign quadC_off     to "{SIMQUAD}DYNACOFF";
float quadB_iset;  assign quadB_iset    to "{SIMQUAD}DYNAB:i:ramp";
//float quadB_iset;  assign quadB_iset    to "{SIMQUAD}DYNABSETI";
float quadC_iset;  assign quadC_iset    to "{SIMQUAD}DYNACSETI";
float quadB_imon;  assign quadB_imon    to "{SIMQUAD}DYNAB:i:rbk"; monitor quadB_imon;
//float quadB_imon;  assign quadB_imon    to "{SIMQUAD}hallb_sf_xy560_0_14"; monitor quadB_imon;
float quadC_imon;  assign quadC_imon    to "{SIMQUAD}hallb_sf_xy560_0_18"; monitor quadC_imon;
int quadB_reset;   assign quadB_reset   to "{SIMQUAD}DYNAB:reset";
//int quadB_reset;   assign quadB_reset   to "{SIMQUAD}DYNABRESET";
int quadC_reset;   assign quadC_reset   to "{SIMQUAD}DYNACRESET";

// Helmholtz Controls:
float helm_iset;    assign helm_iset    to "{SIMHELM}B_MOLLER_HELMHOLTZ_CURRENT_SET";
float helm_isetrbk; assign helm_isetrbk to "{SIMHELM}B_MOLLER_HELMHOLTZ_CURRENT_SP";
float helm_imon;    assign helm_imon    to "{SIMHELM}B_MOLLER_HELMHOLTZ_CURRENT"; monitor helm_imon;
int helm_on;        assign helm_on      to "{SIMHELM}B_MOLLER_HELMHOLTZ_OPER";
int helm_off;       assign helm_off     to "{SIMHELM}B_MOLLER_HELMHOLTZ_OFF";

// Target Motor Controls:
int tgt_go_left;  assign tgt_go_left  to "moller_target_go_left";
int tgt_go_right; assign tgt_go_right to "moller_target_go_right";
int tgt_go_empty; assign tgt_go_empty to "moller_target_go_empty";
float tgt_calib;  assign tgt_calib    to "moller_target_calib";
float tgt_cmd;    assign tgt_cmd      to "moller_target_command";
float tgt_left;   assign tgt_left     to "moller_target_left";  monitor tgt_left;
float tgt_right;  assign tgt_right    to "moller_target_right"; monitor tgt_right;
float tgt_empty;  assign tgt_empty    to "moller_target_empty"; monitor tgt_empty;
float tgt_alum;   assign tgt_alum     to "moller_target_al";    monitor tgt_alum;
float tgt_moving; assign tgt_moving   to "moeller_target.MOVN"; monitor tgt_moving;

// Collimator Motor Controls:
int   colli_blank; assign colli_blank to "collimator_at_b";  monitor colli_blank;
float colli_move;  assign colli_move  to "collimator.VAL";

// High Voltage Controls:
float hv_slm_onoff;   assign hv_slm_onoff   to "B_DET_BLINE_HV_SLM:pwonoff";
float hv_slm_vsetrbk; assign hv_slm_vsetrbk to "B_DET_BLINE_HV_SLM:vsetrbk"; monitor hv_slm_vsetrbk;
float hv_slm_vset;    assign hv_slm_vset    to "B_DET_BLINE_HV_SLM:vset";    monitor hv_slm_vset;
float hv_slm_stat;    assign hv_slm_stat    to "B_DET_BLINE_HV_SLM:stat";    monitor hv_slm_stat;
float hv_dc_off;      assign hv_dc_off      to "{SIMDET}B_DET_DC_HV:OFF";
float hv_svt_off;     assign hv_svt_off     to "{SIMDET}B_SVT_HV:OFF";
float hv_bmt_off;     assign hv_bmt_off     to "{SIMDET}B_DET_BMT_HV:safe";
float hv_ftc_off;     assign hv_ftc_off     to "{SIMDET}B_DET_FTC_HV:OFF";
float hv_fth_off;     assign hv_fth_off     to "{SIMDET}B_DET_FTH_HV:OFF";
float hv_ftt_off;     assign hv_ftt_off     to "{SIMDET}B_DET_FTT_HV:OFF";
float hv_band_off;    assign hv_band_off    to "{SIMDET}B_DET_BAND_HV:OFF";
float hv_ctof_off;    assign hv_ctof_off    to "{SIMDET}B_DET_CTOF_HV:OFF";
float hv_cnd_off;     assign hv_cnd_off     to "{SIMDET}B_DET_CND_HV:OFF";
float hv_rich_off;    assign hv_rich_off    to "{SIMDET}B_DET_RICH_ALL_HV:OFF";
int hv_htcc_off;      assign hv_htcc_off    to "{SIMDET}B_DET_HTCC_HV:OFF";
int hv_ltcc_off;      assign hv_ltcc_off    to "{SIMDET}B_DET_LTCC_HV:OFF";
int hv_ecal_off;      assign hv_ecal_off    to "{SIMDET}B_DET_ECAL_HV:OFF";
int hv_pcal_off;      assign hv_pcal_off    to "{SIMDET}B_DET_PCAL_HV:OFF";
int hv_ftof_off;      assign hv_ftof_off    to "{SIMDET}B_DET_FTOF_HV:OFF";
int hv_svt_stat;      assign hv_svt_stat    to "{SIMDET}B_SVT_HV:isOff";          monitor hv_svt_stat;
int hv_bmt_stat;      assign hv_bmt_stat    to "{SIMDET}B_DET_BMT_HV:safe:stat";  monitor hv_bmt_stat;
int hv_dc_stat;       assign hv_dc_stat     to "{SIMDET}B_DET_DC_HV:isOff";       monitor hv_dc_stat;
int hv_left_onoff;    assign hv_left_onoff  to "B_DET_BLINE_HV_MollerLeft:pwonoff";
int hv_right_onoff;   assign hv_right_onoff to "B_DET_BLINE_HV_MollerRight:pwonoff";

// Low-level asym DAQ:
float moller_acqtime;  assign moller_acqtime    to "asym_acqg_time";
int moller_accumulate; assign moller_accumulate to "moller_accumulate";
int moller_reset;      assign moller_reset      to "moller_reset";
string filename;       assign filename          to "asym_filename";
int filedisable;       assign filedisable       to "asym_file_disable";
float polarization;    assign polarization      to "beam_polarization";
float epolarization;   assign epolarization     to "beam_polarization_error";
float slmbca;          assign slmbca            to "q_asym_3";
float slmebca;         assign slmebca           to "d_asym_3";

%{
extern void makeLogEntry(char*,float,float,float,float,float,float,float,float,float,int,int,char*,char*,int,int,char*,char*,float,float);
extern double calcQuadCurrent(float);
extern double fabs(double);
int equals(float x1,float x2,float tolerance) { return fabs(x1-x2) < tolerance; }
}%

ss automoller {

    // intializations and connect to pvs:
    state start {

        entry {
            MESSAGE(Connecting ...);
            isMollerRunning=0;
            isMollerConfigured=0;
        }

        when (pvConnectCount() < pvChannelCount())
        {
            sprintf(msg,"Waiting for PVs (%d/%d)",pvConnectCount(),pvChannelCount());
            printf("%s\n",msg); pvPut(msg);
            epicsThreadSleep(1);
        } state start

        when () {
            moller_accumulate=STOPDAQ;
            pvPut(moller_accumulate);
            moller_reset=1;
            pvPut(moller_reset);
			status=NOT_CONFIGURED;
			pvPut(status);
            MESSAGE(Non-Moller Configuration.);
        } state listen

    }

    // wait for user input:
    state listen {

        when (pvConnectCount() < pvChannelCount())
        {
            sprintf(stmp,"%s",msg);
            sprintf(msg,"Waiting for PVs (%d/%d)",pvConnectCount(),pvChannelCount());
            pvPut(msg);
            epicsThreadSleep(1);
            sprintf(msg,stmp);
            pvPut(msg);
        } state listen
        
		when (moller_recfg) {
			moller_recfg=0;
			pvPut(moller_recfg);
		} state reconfigure
        when (moller_enter) {
            moller_enter=0;
            pvPut(moller_enter);
        } state enterMoller
        when (moller_exit) {
            moller_exit=0;
            pvPut(moller_exit);
        } state exitMoller
        when (daq_start) {
            daq_start=0;
            pvPut(daq_start);
        } state startDaq
        when (daq_stop) {
            daq_stop=0;
            pvPut(daq_stop);
        } state stopDaq
        when (logentry) {
            logentry=0;
            pvPut(logentry);
        } state logentry

        // alarm on magnet currents:
        when (isMollerConfigured) {
            if (!equals(quadB_imon,quadB_iset,QUAD_TOLERANCE) ||
                !equals(quadC_imon,quadC_iset,QUAD_TOLERANCE) ) {
                status=QUAD_ALARM;
                pvPut(status);
            }
            else if (status==QUAD_ALARM) {
                if (isMollerRunning) status=RUN_IN_PROGRESS;
                else                 status=CONFIGURED;
                pvPut(status);
            }
            if (!equals(helm_imon,helm_iset,HELM_TOLERANCE)) {
                status=HELM_ALARM;
                pvPut(status);
            }
            else if (status==HELM_ALARM) {
                if (isMollerRunning) status=RUN_IN_PROGRESS;
                else                 status=CONFIGURED;
                pvPut(status);
            }
            if (!colli_blank) {
                status=COLLI_ALARM;
                pvPut(status);
            }
            else if (status==COLLI_ALARM) {
                if (isMollerRunning) status=RUN_IN_PROGRESS;
                else                 status=CONFIGURED;
                pvPut(status);
            }
            if (tgt_moving!=0) {
                status=TGT_ALARM;
                pvPut(status);
            }
            else if (status==TGT_ALARM) {
                if (isMollerRunning) status=RUN_IN_PROGRESS;
                else                 status=CONFIGURED;
                pvPut(status);
            }
            epicsThreadSleep(1);
        } state listen

        when () {
            epicsThreadSleep(1);
        } state listen
    }

///////////////////////////////////////////////////

    state logentry {

        entry {
            pvGet(logusers);
            pvGet(moller_accumulate);
        }

        when (moller_accumulate!=STOPDAQ) {
            TMPMESSAGE(Must stop DAQ before Logbook Entry.)
        } state listen
        
        when (strcmp(logusers,"")==0) {
            TMPMESSAGE(Must define Entry Makers for Logbook.);
        } state listen

        when () {
            MESSAGE(Generating Logbook Entry ...);
            pvGet(filename);
            pvGet(beamEnergy);
            pvGet(halfwaveplate);
            pvGet(polarization);
            pvGet(epolarization);
            pvGet(logcomments);
            pvGet(runno);
            pvGet(coda_runno);
            pvGet(slmbca);
            pvGet(slmebca);
            pvGet(vwienangle);
            pvGet(hwienangle);
            epicsThreadSleep(4);
            makeLogEntry(filename,polarization,epolarization,slmbca,slmebca,beamEnergy,hv_slm_vsetrbk,quadB_imon,quadC_imon,helm_imon,tgt_cfg,halfwaveplate,logcomments,logusers,runno,coda_runno,runStartTime,runEndTime,vwienangle,hwienangle);
            epicsThreadSleep(2);
            MESSAGE(Check Logbook for New Entry!);
            sprintf(logcomments,"None");
            pvPut(logcomments);
        } state listen

        exit {
            strcpy(logusers,"");
            pvPut(logusers);
        }
    }

	state reconfigure {

		entry {
            // require stopping run before reconfigure:
			if (isMollerRunning) {
                sprintf(stmp,"%s",msg);
                MESSAGE(No Reconfigure.  Stop Moller Run First.);
                epicsThreadSleep(2);
                sprintf(msg,"%s",stmp);
                printf("%s\n",msg); pvPut(msg);
			}
			else {
                MESSAGE(Reconfiguring ...);
				status=CONFIGURING;
				pvPut(status);
                pvGet(quad_icfg);
                pvGet(helm_icfg);
                pvGet(helm_polcfg);
                pvGet(tgt_cfg);
                quadB_iset = quad_icfg;
				quadC_iset = quad_icfg;
				helm_iset = helm_icfg*(2*helm_polcfg-1);
				hv_slm_vset = hv_slm_vcfg;
				tgt_cmd = tgt_cfg;
				pvPut(quadB_iset);
				pvPut(quadC_iset);
				pvPut(helm_iset);
				pvPut(hv_slm_vset);
				pvPut(tgt_cmd);
				epicsThreadSleep(5);
			}
		}

		when (delay(10) && tgt_moving==0) {
            MESSAGE(Moller Reconfiguration Complete.);
            status=CONFIGURED;
            pvPut(status);
		} state listen
	}

    state enterMoller {
		entry {
			status=CONFIGURING;
			pvPut(status);
            MESSAGE(Entering Moller Configuration ...);
            filedisable=0;
            pvPut(filedisable);
            epicsThreadSleep(1);
		}
        when () {} state checkTagger
    }

    state checkTagger {
        entry {
            MESSAGE(Checking Tagger ...);
            epicsThreadSleep(1);
        }
        when (tagger_irbk < TAGGER_TOLERANCE) {
            MESSAGE(ERROR:  Tagger is Off.  Aborted Moller Run.);
            status=NOT_CONFIGURED;
	        pvPut(status);
        } state listen
        when () {} state insertCollimator
    }

    state insertCollimator {
        entry {
            MESSAGE(Inserting Collimator ...);
            colli_move=COLLIMATOR_POSITION;
            pvPut(colli_move);
        }

        when (colli_blank==1) {} state hvOff
        
        when (delay(60)) {
            status=COLLI_ALARM;
            pvPut(status);
            MESSAGE(ERROR Inserting Collimator.  Aborted Moller Run.)
        } state listen
    }

    state hvOff {
      
		// execute entry block even if previous state was the same:
		option -e;

        // only reset timer if previous state was different:
        option -t;

        entry {
            MESSAGE(Turning HV Off. May Generate Alarms ...);
            epicsThreadSleep(1);
            if (hv_svt_stat!=1) {
                MESSAGE(Turning SVT HV Off ...);
                hv_svt_off=1;
                pvPut(hv_svt_off);
                epicsThreadSleep(1);
            }
            if (hv_bmt_stat!=1) {
                MESSAGE(Setting BMT HV Safe ...);
                hv_bmt_off=1;
                pvPut(hv_bmt_off);
                epicsThreadSleep(1);
            }
            if (hv_dc_stat!=1) {
                MESSAGE(Turning DC HV Off ...);
                hv_dc_off=1;
                pvPut(hv_dc_off);
                epicsThreadSleep(1);
            }
            hv_ftc_off=1;
            hv_fth_off=1;
            hv_ftt_off=1;
            hv_band_off=1;
            hv_ctof_off=1;
            hv_cnd_off=1;
            hv_rich_off=1;
            hv_ecal_off=1;
            hv_pcal_off=1;
            hv_ftof_off=1;
            hv_htcc_off=1;
            hv_ltcc_off=1;
            pvPut(hv_ftc_off);
            pvPut(hv_fth_off);
            pvPut(hv_ftt_off);
            pvPut(hv_band_off);
            pvPut(hv_ctof_off);
            pvPut(hv_cnd_off);
            pvPut(hv_rich_off);
            pvPut(hv_ecal_off);
            pvPut(hv_pcal_off);
            pvPut(hv_ftof_off);
            pvPut(hv_htcc_off);
            pvPut(hv_ltcc_off);
            MESSAGE(Confirming HV Off ...);
            epicsThreadSleep(5);
        }

        when (delay(5) &&
			  hv_dc_stat==1 &&
			  hv_svt_stat==1 &&
			  hv_bmt_stat==1) {} state setSlm
        when (delay(90)) {
            if (hv_dc_stat!=1) {
				status=DC_ALARM;
                MESSAGE(ERROR on DC HV Off.  Aborted Moller Run.);
            }
            else if (hv_svt_stat!=1) {
				status=SVT_ALARM;
                MESSAGE(ERROR on SVT HV Off.  Aborted Moller Run.);
            }
            else if (hv_bmt_stat!=1) {
				status=MVT_ALARM;
                MESSAGE(ERROR on BMT HV Safe.  Aborted Moller Run.);
            }
			pvPut(status);
        } state listen
        
        when (delay(30) && hv_dc_stat!=1)  {} state hvOff
        when (delay(30) && hv_bmt_stat!=1) {} state hvOff
        when (delay(60) && hv_svt_stat!=1) {} state hvOff
    }

    state setSlm {

        entry {
            MESSAGE(Setting SLM HV ...);
            hv_slm_onoff=1;
            pvPut(hv_slm_onoff);
            pvGet(hv_slm_vsetrbk);
            hv_slm_default=hv_slm_vsetrbk;
            hv_slm_vset=hv_slm_vcfg;
            pvPut(hv_slm_vset);
        }
        
        when (hv_slm_vsetrbk==hv_slm_vcfg && hv_slm_stat==1) {} state mollerHvOn
        
        when (delay(90)) {
			status=NOT_CONFIGURED;
			pvPut(status);
            MESSAGE(ERROR setting SLM HV.  Aborted Moller Run.);
        } state listen

        when (delay(20) && hv_slm_stat!=1) {
            hv_slm_onoff=1;
            pvPut(hv_slm_onoff);
            epicsThreadSleep(5);
        } state setSlm

        when (delay(20) && hv_slm_vsetrbk!=hv_slm_vcfg) {
            hv_slm_vset=hv_slm_vcfg;
            pvPut(hv_slm_vset);
            epicsThreadSleep(5);
        } state setSlm

    }

    state mollerHvOn {
        entry {
            MESSAGE(Setting Moller L/R HV ON ...);
            hv_left_onoff=1;
            hv_right_onoff=1;
            pvPut(hv_left_onoff);
            pvPut(hv_right_onoff);
        }

        when (delay(5)) {
        } state quadsCalc
    }


    state quadsCalc {

        // only reset timer if previous state was different:
        option -t;

        entry {
            pvGet(quad_icfg);
            pvGet(quad_icfg_auto);
            itmp=0;
            if (quad_icfg_auto) {
                MESSAGE(Calculating Quadrupole Current ...);
#if USE_BRIANS_QUADS
                pvGet(beamEnergy);
                quad_icfg = calcQuadCurrent(beamEnergy/1000);
#else
                pvGet(beamPasses);
                if (beamPasses==1) {
                    pvGet(quad_icfg_1pass);
                    quad_icfg = quad_icfg_1pass;
                }
                else if (beamPasses==2) {
                    pvGet(quad_icfg_2pass);
                    quad_icfg = quad_icfg_2pass;
                }
                else if (beamPasses==3) {
                    pvGet(quad_icfg_3pass);
                    quad_icfg = quad_icfg_3pass;
                }
                else if (beamPasses==4) {
                    pvGet(quad_icfg_4pass);
                    quad_icfg = quad_icfg_4pass;
                }
                else if (beamPasses==5) {
                    pvGet(quad_icfg_5pass);
                    quad_icfg = quad_icfg_5pass;
                }
                else {
                    itmp=1;
                }
#endif
            }
        }
        
        when (itmp!=0) {
            MESSAGE(ERROR on #Passes for Quad Current.);
        } state listen

        when (quad_icfg>3300) {
            MESSAGE(ERROR on Quad Current above 3300 A.);
        } state listen

        when () {
            pvPut(quad_icfg);
            MESSAGE(Turning ON Quadrupoles ...);
        } state quadsOn
    }

    state quadsOn {

        // only reset timer if previous state was different:
        option -t;

        entry {
            // reset:
            quadB_reset = 1;
            quadC_reset = 1;
            pvPut(quadB_reset);
            pvPut(quadC_reset);
            epicsThreadSleep(1);
            // on:
            quadB_on = 1;
            quadC_on = 1;
            pvPut(quadB_on);
            pvPut(quadC_on);
            epicsThreadSleep(1);
        }

        when (delay(5) && quadB_isOn==1 && quadC_isOn==1) {
        } state quadsRampUp

        when (delay(30)) {
			status=QUAD_ALARM;
			pvPut(status);
            MESSAGE(ERROR turning on Quads.  Aborted Moller Run.);
            pvPut(msg);
        } state listen
        
        when (delay(5)) {
            if (quadB_isOn==0)  pvPut(quadB_on);
            if (quadC_isOn==0)  pvPut(quadC_on);
            epicsThreadSleep(2);
        } state quadsOn

    }

    state quadsRampUp {

        // only reset timer if previous state was different:
        option -t;

        entry {
            quadB_iset = quad_icfg;
            quadC_iset = quad_icfg;
            pvPut(quadB_iset);
            pvPut(quadC_iset);
            epicsThreadSleep(1);
        }

        when (delay(5) &&
              equals(quadB_imon,quadB_iset,QUAD_TOLERANCE) &&
              equals(quadC_imon,quadC_iset,QUAD_TOLERANCE) ) {
        } state helmholtzOn

        when (delay(40)) {
			status=QUAD_ALARM;
			pvPut(status);
            MESSAGE(ERROR energizing Quads.  Aborted Moller Run.);
            pvPut(msg);
        } state listen
        
        when (delay(5)) {
            pvPut(quadB_iset);
            pvPut(quadC_iset);
            epicsThreadSleep(2);
        } state quadsRampUp
        
    }

    state helmholtzOn {
        
        // only reset timer if previous state was different:
        option -t;

        entry {
            MESSAGE(Energizing Helmholtz Coils ...);
            pvGet(helm_icfg);
            pvGet(helm_polcfg);
            helm_iset = helm_icfg*(2*helm_polcfg-1);
            helm_on=1;
            pvPut(helm_on);
            pvPut(helm_iset);
            epicsThreadSleep(1);
        }
        
        when (delay(3) && equals(helm_imon,helm_iset,HELM_TOLERANCE)) {
        } state insertTarget

        when (delay(25)) {
			status=HELM_ALARM;
			pvPut(status);
            MESSAGE(ERROR energizing Helmholtz.  Aborted Moller Run.);
        } state listen
        
        when (delay(15)) {
            pvPut(helm_on);
            pvPut(helm_iset);
            epicsThreadSleep(7);
        } state helmholtzOn
    }

    state insertTarget {
        entry {
            MESSAGE(Inserting Moller Target ...);
            pvGet(tgt_cfg);
            tgt_cmd = tgt_cfg;
            pvPut(tgt_cmd);
        }

        when (delay(120)) {
			status=TGT_ALARM;
			pvPut(status);
            MESSAGE(ERROR inserting target.  Aborted Moller Run.);
        } state listen

        when (delay(10) && tgt_moving==0 &&
             ( (tgt_cfg==TGT_LEFT  && tgt_left==1) ||
               (tgt_cfg==TGT_RIGHT && tgt_right==1) ||
               (tgt_cfg==TGT_EMPTY && tgt_empty==1) ||
               (tgt_cfg==TGT_ALUM  && tgt_alum==1)) ) {
            isMollerConfigured=1;
            status=CONFIGURED;
            pvPut(status);
            MESSAGE(Moller Configuration Ready.);
        } state listen
    }


///////////////////////////////////////////////////

    state startDaq {

        when (isMollerConfigured==0) {
            sprintf(stmp,msg);
            MESSAGE(Enter Moller Config before starting DAQ.);
            epicsThreadSleep(5);
            sprintf(msg,stmp);
            pvPut(msg);
        } state listen

        when () {
            isMollerRunning=1;
            MESSAGE(Starting DAQ  ...);
            epicsTimeGetCurrent(&timeStamp);
            epicsTimeToStrftime(runStartTime,40,"%m/%d/%Y %H:%M:%S",&timeStamp);
            sprintf(runEndTime,"N/A");
            moller_accumulate=STARTDAQ;
            pvPut(moller_accumulate);
            moller_reset=1;
            pvPut(moller_reset);
            epicsThreadSleep(1);
            pvGet(runno);
            runno=runno+1;
            pvPut(runno);
            MESSAGE(New Run Number and File ...);
            epicsThreadSleep(1);
            MESSAGE(Moller Run in Progress ...);
			status=RUN_IN_PROGRESS;
			pvPut(status);
        } state listen
    }
    
    state stopDaq {
		when (!isMollerRunning) {
            sprintf(stmp,msg);
            MESSAGE(Moller run is already stopped.);
            epicsThreadSleep(5);
            sprintf(msg,stmp);
            pvPut(msg);
		} state listen
        when () {
            isMollerRunning=0;
            MESSAGE(Stopping DAQ  ...);
            moller_accumulate=STOPDAQ;
            pvPut(moller_accumulate);
            epicsTimeGetCurrent(&timeStamp);
            epicsTimeToStrftime(runEndTime,40,"%m/%d/%Y %H:%M:%S",&timeStamp);
            epicsThreadSleep(1);
            MESSAGE(DAQ Stopped);
			status=CONFIGURED;
			pvPut(status);
        } state listen
    }
   
///////////////////////////////////////////////////
    state exitMoller {
        entry {
            MESSAGE(Exiting Moller Configuration ...);
            epicsThreadSleep(1);
            isMollerRunning=0;
            isMollerConfigured=0;
			status=CONFIGURED;
			pvPut(status);
            MESSAGE(Restoring DAQ ...);
            moller_accumulate=STOPDAQ;
            pvPut(moller_accumulate);
            filedisable=1;
            pvPut(filedisable);
            epicsThreadSleep(1);
            moller_acqtime=60;
            pvPut(moller_acqtime);
            moller_accumulate=STARTDAQ;
            pvPut(moller_accumulate);
            epicsThreadSleep(1);
            MESSAGE(Restoring non-Moller configuration ...);
			status=NOT_CONFIGURED;
			pvPut(status);
			epicsThreadSleep(1);
        }
        when (delay(1)) {} state quadsRampDown
    }

    state quadsRampDown {

        // only reset timer if previous state was different:
        option -t;

        entry {
            quadB_iset = 0;
            quadC_iset = 0;
            pvPut(quadB_iset);
            pvPut(quadC_iset);
            epicsThreadSleep(1);
        }

        when (delay(5) && quadB_imon < 50 && quadC_imon < 50) {
        } state quadsOff

        when (delay(30)) {
			status=QUAD_ALARM;
			pvPut(status);
            MESSAGE(ERROR denergizing Quads.  Aborted Moller Run.);
            pvPut(msg);
        } state listen

        when (delay(5)) {
            pvPut(quadB_iset);
            pvPut(quadC_iset);
            epicsThreadSleep(2);
        } state quadsRampDown

    }

    state quadsOff {

        // only reset timer if previous state was different:
        option -t;

        entry {
            quadB_off = 1;
            quadC_off = 1;
            pvPut(quadB_off);
            pvPut(quadC_off);
            epicsThreadSleep(1);
        }

        when (delay(5) && quadB_isOn==0 && quadC_isOn==0) {
        } state helmholtzOff

        when (delay(30)) {
			status=QUAD_ALARM;
			pvPut(status);
            MESSAGE(ERROR turning off Quads.  Aborted Moller Run.);
            pvPut(msg);
        } state listen
        
        when (delay(5)) {
            if (quadB_isOn!=0)  pvPut(quadB_off);
            if (quadC_isOn!=0)  pvPut(quadC_off);
            epicsThreadSleep(2);
        } state quadsOff

    }

    state helmholtzOff {

        // only reset timer if previous state was different:
        option -t;

        entry {
            MESSAGE(De-energizing Helmholtz ...);
            helm_iset=0;
            pvPut(helm_iset);
            helm_off=1;
            pvPut(helm_off);
        }

        when (delay(3) && fabs(helm_imon)<0.2) {} state restoreSlm

        when (delay(30)) {
			status=HELM_ALARM;
			pvPut(status);
            MESSAGE(ERROR de-energizing Helmholtz.);
        } state restoreSlm

        when (delay(10)) {
            helm_iset=0;
            pvPut(helm_iset);
            helm_off=1;
            pvPut(helm_off);
        } state helmholtzOff
    }
    
	state restoreSlm {
        entry {
            MESSAGE(Restoring SLM settings ...);
            hv_slm_vset=hv_slm_default;
            pvPut(hv_slm_vset);
        }
        when (delay(2)) {} state mollerHvOff
    }
    
    state mollerHvOff {
        entry {
            MESSAGE(Setting Moller L/R HV OFF ...);
            hv_left_onoff=0;
            hv_right_onoff=0;
            pvPut(hv_left_onoff);
            pvPut(hv_right_onoff);
        }

        when (delay(5)) {
        } state retractTarget
    }

    
    state retractTarget {
        entry {
            MESSAGE(Retracting Moller Target ...);
            tgt_go_empty=1;
            pvPut(tgt_go_empty);
        }

        when (delay(90)) {
            MESSAGE(ERROR retracting target.);
            status=TGT_ALARM;
            pvPut(status);
        } state listen
        
        when (delay(10) && tgt_moving==0 && tgt_empty==1) {
            MESSAGE(Non-Moller Configuration Restored.);
        } state listen
    }
}


