//
// automoller.st - Automated Moller Run Setup
//
// automoller.db (and automoller-sim.db) contain associated records
//
// N. Baltzell, 2018
//
program automoller ("P=B_MOLLER:,SIMTAG=,SIMQUAD=,SIMHELM=SIMDET=")

// not reentrant (only one instance allowed):
option -r;

// safe mode:
option +s;

#include "automoller.h"

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

// CODA run number:
int coda_runno; assign coda_runno to "B_DAQ:run_number";

// Quadrupole Controls:
int quadB_isOn;    assign quadB_isOn    to "{SIMQUAD}DYNABPSON";
int quadC_isOn;    assign quadC_isOn    to "{SIMQUAD}DYNACPSON";
int quadB_on;      assign quadB_on      to "{SIMQUAD}DYNABON";
int quadC_on;      assign quadC_on      to "{SIMQUAD}DYNACON";
int quadB_off;     assign quadB_off     to "{SIMQUAD}DYNABOFF";
int quadC_off;     assign quadC_off     to "{SIMQUAD}DYNACOFF";
int quadB_reverse; assign quadB_reverse to "{SIMQUAD}DYNABREVERSE";
int quadB_forward; assign quadB_forward to "{SIMQUAD}DYNABFORWARD";
float quadB_iset;  assign quadB_iset    to "{SIMQUAD}DYNABSETI";
float quadC_iset;  assign quadC_iset    to "{SIMQUAD}DYNACSETI";
float quadB_imon;  assign quadB_imon    to "{SIMQUAD}hallb_sf_xy560_0_14"; monitor quadB_imon;
float quadC_imon;  assign quadC_imon    to "{SIMQUAD}hallb_sf_xy560_0_18"; monitor quadC_imon;
int quadB_reset;   assign quadB_reset   to "{SIMQUAD}DYNABRESET";
int quadC_reset;   assign quadC_reset   to "{SIMQUAD}DYNACRESET";
int quadB_revmon;  assign quadB_revmon  to "{SIMQUAD}DYNABRC";
int quadB_fwdmon;  assign quadB_fwdmon  to "{SIMQUAD}DYNABFC";

// Helmholtz Controls:
int helm_state;     assign helm_state   to "{SIMHELM}B_MOLLER_HELMHOLTZ_STATE";
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
float tgt_left;   assign tgt_left     to "moller_target_left";
float tgt_right;  assign tgt_right    to "moller_target_right";
float tgt_empty;  assign tgt_empty    to "moller_target_empty"; monitor tgt_empty;
float tgt_moving; assign tgt_moving   to "moeller_target.MOVN"; monitor tgt_moving;

// High Voltage Controls:
float hv_slm_onoff;   assign hv_slm_onoff   to "B_DET_BLINE_HV_SLM:pwonoff";
float hv_slm_vsetrbk; assign hv_slm_vsetrbk to "B_DET_BLINE_HV_SLM:vsetrbk"; monitor hv_slm_vsetrbk;
float hv_slm_vset;    assign hv_slm_vset    to "B_DET_BLINE_HV_SLM:vset";    monitor hv_slm_vset;
float hv_slm_stat;    assign hv_slm_stat    to "B_DET_BLINE_HV_SLM:stat";    monitor hv_slm_stat;
float hv_dc_off;      assign hv_dc_off      to "{SIMDET}B_DET_DC_HV:OFF";
float hv_svt_off;     assign hv_svt_off     to "{SIMDET}B_SVT_SEQ:btnOff";
float hv_bmt_off;     assign hv_bmt_off     to "{SIMDET}B_DET_BMT_HV:pwoff";
float hv_ftc_off;     assign hv_ftc_off     to "{SIMDET}B_DET_FTC_HV:OFF";
float hv_fth_off;     assign hv_fth_off     to "{SIMDET}B_DET_FTH_HV:OFF";
float hv_ftt_off;     assign hv_ftt_off     to "{SIMDET}B_DET_FTT_HV:OFF";
float hv_ctof_off;    assign hv_ctof_off    to "{SIMDET}B_DET_CTOF_HV:OFF";
int hv_svt_stat;      assign hv_svt_stat    to "{SIMDET}B_SVT:status";            monitor hv_svt_stat;
int hv_bmt_stat;      assign hv_bmt_stat    to "{SIMDET}B_DET_BMT_HV:stat";       monitor hv_bmt_stat;
int hv_dc_stat;       assign hv_dc_stat     to "{SIMDET}B_DET_DC_HV:isOff";       monitor hv_dc_stat;

// Low-level asym DAQ:
int moller_accumulate; assign moller_accumulate to "moller_accumulate";
int moller_reset;      assign moller_reset      to "moller_reset";
string filename;       assign filename          to "asym_filename";
float polarization;    assign polarization      to "beam_polarization";
float epolarization;   assign epolarization     to "beam_polarization_error";
float slmbca;          assign slmbca            to "q_asym_3";
float slmebca;         assign slmebca           to "d_asym_3";

%{
extern void makeLogEntry(char*,float,float,float,float,float,float,float,float,float,int,int,char*,char*,int,int,char*,char*);
extern double fabs(double);
int equals(float x1,float x2,float tolerance) { return fabs(x1-x2) < tolerance; }
}%

ss automoller {

    // intializations and connect to pvs:
    state start {

        entry {
            sprintf(msg,"Connecting ...");
            printf("%s\n",msg); pvPut(msg);
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
            sprintf(msg,"Non-Moller Configuration.");
            printf("%s\n",msg); pvPut(msg);
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
        } state listen
    }

///////////////////////////////////////////////////

    state logentry {
        
        when () {
            pvGet(logusers);
            // require logbook users to be defined:
            if (strcmp(logusers,"")==0) {
                sprintf(stmp,msg);
                sprintf(msg,"Must define Entry Makers for Logbook.");
                pvPut(msg);
            }
            else {
                sprintf(msg,"Generating Logbook Entry ...");
                pvPut(msg);
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
                epicsThreadSleep(4);
                makeLogEntry(filename,polarization,epolarization,slmbca,slmebca,beamEnergy,hv_slm_vsetrbk,quadB_imon,quadC_imon,helm_imon,tgt_cfg,halfwaveplate,logcomments,logusers,runno,coda_runno,runStartTime,runEndTime);
                epicsThreadSleep(2);
                sprintf(msg,"Check Logbook for New Entry!");
                pvPut(msg);
                sprintf(logcomments,"None");
                pvPut(logcomments);
            }
        } state listen
    }

	state reconfigure {

		entry {
            // require stopping run before reconfigure:
			if (isMollerRunning) {
                sprintf(stmp,"%s",msg);
				sprintf(msg,"No Reconfigure.  Stop Moller Run First.");
                printf("%s\n",msg); pvPut(msg);
                epicsThreadSleep(2);
                sprintf(msg,"%s",stmp);
                printf("%s\n",msg); pvPut(msg);
			}
			else {
				sprintf(msg,"Reconfiguring ...");
                printf("%s\n",msg); pvPut(msg);
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
            sprintf(msg,"Moller Reconfiguration Complete.");
            printf("%s\n",msg); pvPut(msg);
            status=CONFIGURED;
            pvPut(status);
		} state listen
	}

    state enterMoller {
		entry {
			status=CONFIGURING;
			pvPut(status);
            sprintf(msg,"Entering Moller Configuration ...");
            printf("%s\n",msg);
            pvPut(msg);
            epicsThreadSleep(1);
		}
        when () {} state checkTagger
    }

    state checkTagger {
        entry {
            sprintf(msg,"Checking Tagger ...");
            printf("%s\n",msg);
            pvPut(msg);
            epicsThreadSleep(1);
        }
        when (tagger_irbk < TAGGER_TOLERANCE) {
            sprintf(msg,"ERROR:  Tagger is Off.  Aborted Moller Run.");
            printf("%s\n",msg);
            pvPut(msg);
			status=NOT_CONFIGURED;
			pvPut(status);
        } state listen
        when () {} state hvOff
    }

    state hvOff {
      
		// execute entry block even if previous state was the same:
		option -e;

        // only reset timer if previous state was different:
        option -t;

        entry {
            if (hv_svt_stat!=0) {
                sprintf(msg,"Turning SVT HV Off ...");
                printf("%s\n",msg);
                pvPut(msg);
                hv_svt_off=1;
                pvPut(hv_svt_off);
                epicsThreadSleep(1);
            }
            if (hv_dc_stat!=1) {
                sprintf(msg,"Turning DC HV Off ...");
                printf("%s\n",msg);
                pvPut(msg);
                hv_dc_off=1;
                pvPut(hv_dc_off);
                epicsThreadSleep(1);
            }
            if (hv_bmt_stat!=0) {
                sprintf(msg,"Turning BMT HV Off ...");
                printf("%s\n",msg);
                pvPut(msg);
                hv_bmt_off=1;
                pvPut(hv_bmt_off);
                epicsThreadSleep(1);
            }
            sprintf(msg,"Confirming HV Off ...");
            printf("%s\n",msg);
            pvPut(msg);
            hv_ftc_off=1;
            hv_fth_off=1;
            hv_ftt_off=1;
            pvPut(hv_ftc_off);
            pvPut(hv_fth_off);
            pvPut(hv_ftt_off);
            epicsThreadSleep(5);
        }

        when (delay(5) &&
			  hv_dc_stat==1 &&
			  hv_svt_stat==0 &&
			  hv_bmt_stat==0) {} state setSlm
        
        when (delay(90)) {
			status=NOT_CONFIGURED;
			pvPut(status);
            if (hv_dc_stat!=1) {
				status=DC_ALARM;
                sprintf(msg,"ERROR on DC HV Off.  Aborted Moller Run.");
            }
            else if (hv_svt_stat!=0) {
				status=SVT_ALARM;
                sprintf(msg,"ERROR on SVT HV Off.  Aborted Moller Run.");
            }
            else if (hv_bmt_stat!=0) {
				status=MVT_ALARM;
                sprintf(msg,"ERROR on BMT HV Off.  Aborted Moller Run.");
            }
            printf("%s\n",msg);
			pvPut(status);
            pvPut(msg);
        } state listen
        
        when (delay(30) && hv_bmt_stat!=0) {} state hvOff
        when (delay(30) && hv_dc_stat!=1)  {} state hvOff
        when (delay(60) && hv_svt_stat!=0) {} state hvOff
    }

    state setSlm {

        entry {
            sprintf(msg,"Setting SLM HV ...");
            printf("%s\n",msg);
            pvPut(msg);
            hv_slm_onoff=1;
            pvPut(hv_slm_onoff);
            pvGet(hv_slm_vsetrbk);
            pvGet(hv_slm_vcfg);
            hv_slm_default=hv_slm_vsetrbk;
            hv_slm_vset=hv_slm_vcfg;
            pvPut(hv_slm_vset);
        }
        
        when (hv_slm_vsetrbk==hv_slm_vcfg && hv_slm_stat==1) {} state quadsCalc
        
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

        when (delay(90)) {
			status=NOT_CONFIGURED;
			pvPut(status);
            sprintf(msg,"ERROR setting SLM HV.  Aborted Moller Run.");
            printf("%s\n",msg); pvPut(msg);
        } state listen

    }

    state quadsCalc {

        // only reset timer if previous state was different:
        option -t;

        entry {
            pvGet(quad_icfg);
            pvGet(quad_icfg_auto);
            itmp=0;
            if (quad_icfg_auto) {
                sprintf(msg,"Calculating Quadrupole Current ...");
                printf("%s\n",msg); pvPut(msg);
                epicsThreadSleep(1);
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
            }
        }
        
        when (itmp!=0) {
            sprintf(msg,"ERROR on #Passes for Quad Current.");
            printf("%s\n",msg); pvPut(msg);
        } state listen

        when () {
            pvPut(quad_icfg);
        } state quadsOn
    }

    state quadsOn {

        // only reset timer if previous state was different:
        option -t;

        entry {
            sprintf(msg,"Energizing Quadrupoles ...");
            printf("%s\n",msg); pvPut(msg);
            epicsThreadSleep(1);
            quadB_reset = 1;
            quadC_reset = 1;
            // critical that resets complete before we do ON:
            sprintf(msg,"Resetting Quadrupoles ...");
            printf("%s\n",msg); pvPut(msg);
            pvPutComplete(quadB_reset);
            pvPutComplete(quadC_reset);
            sprintf(msg,"Turning ON Quadrupoles ...");
            printf("%s\n",msg); pvPut(msg);
            quadB_on = 1;
            quadC_on = 1;
            pvPut(quadB_on);
            pvPut(quadC_on);
            epicsThreadSleep(1);
            sprintf(msg,"Settting Quadrupole Current ...");
            printf("%s\n",msg); pvPut(msg);
            pvGet(quad_icfg);
            quadB_iset = quad_icfg;
            quadC_iset = quad_icfg;
            pvPut(quadB_iset);
            pvPut(quadC_iset);
            epicsThreadSleep(1);
        }

        when (delay(3) &&
              equals(quadB_imon,quadB_iset,QUAD_TOLERANCE) &&
              equals(quadC_imon,quadC_iset,QUAD_TOLERANCE) ) {
        } state helmholtzOn
/*
        // check that Quads succeeded:
        when (delay(30) && !equals(quadB_imon,quadB_iset,QUAD_TOLERANCE)) {
            quadB_iset=0;
            pvPut(quadB_iset);
            quadB_off=1;
            pvPut(quadB_off);
            quadB_reset=1;
            pvPut(quadB_reset);
            quadB_on=1;
            pvPut(quadB_on);
            quadB_iset=quad_icfg;
            pvPut(quadB_iset);
        } state quadsOn
        when (delay(30) && !equals(quadC_imon,quadC_iset,QUAD_TOLERANCE)) {
            quadC_iset=0;
            pvPut(quadC_iset);
            quadC_off=1;
            pvPut(quadC_off);
            quadC_reset=1;
            pvPut(quadC_reset);
            quadC_on=1;
            pvPut(quadC_on);
            quadC_iset=quad_icfg;
            pvPut(quadC_iset);
        } state quadsOn
*/
        when (delay(90)) {
			status=QUAD_ALARM;
			pvPut(status);
            sprintf(msg,"ERROR energizing Quads.  Aborted Moller Run.");
            printf("%s\n",msg);
            pvPut(msg);
        } state listen
    }

    state helmholtzOn {
        
        // only reset timer if previous state was different:
        option -t;

        entry {
            sprintf(msg,"Energizing Helmholtz Coils ...");
            printf("%s\n",msg);
            pvPut(msg);
            pvGet(helm_icfg);
            pvGet(helm_polcfg);
            helm_iset = helm_icfg*(2*helm_polcfg-1);
            helm_on = 1;
            pvPut(helm_on);
            epicsThreadSleep(1);
            pvPut(helm_iset);
            epicsThreadSleep(1);
        }
        
        when (delay(3) && equals(helm_imon,helm_iset,HELM_TOLERANCE)) {
        } state insertTarget

        when (delay(20)) {
			status=HELM_ALARM;
			pvPut(status);
            sprintf(msg,"ERROR energizing Helmholtz.  Aborted Moller Run.");
            printf("%s\n",msg);
            pvPut(msg);
        } state listen
    }

    state insertTarget {
        entry {
            sprintf(msg,"Inserting Moller Target ...");
            printf("%s\n",msg);
            pvPut(msg);
            pvGet(tgt_cfg);
            tgt_cmd = tgt_cfg;
            pvPut(tgt_cmd);
        }

        when (delay(10) && tgt_moving==0) {
            isMollerConfigured=1;
            sprintf(msg,"Moller Configuration Ready.");
			status=CONFIGURED;
			pvPut(status);
            printf("%s\n",msg);
            pvPut(msg);
        } state listen

        when (delay(90)) {
			status=TGT_ALARM;
			pvPut(status);
            sprintf(msg,"ERROR inserting target.  Aborted Moller Run.");
            printf("%s\n",msg);
            pvPut(msg);
        } state listen

    }


///////////////////////////////////////////////////

    state startDaq {

        when (isMollerConfigured==0) {
            sprintf(stmp,msg);
            sprintf(msg,"Enter Moller Config before starting DAQ.");
            printf("%s\n",msg);
            pvPut(msg);
            epicsThreadSleep(5);
            sprintf(msg,stmp);
            pvPut(msg);
        } state listen

        when () {
            isMollerRunning=1;
            sprintf(msg,"Starting DAQ  ...");
            printf("%s\n",msg);
            pvPut(msg);
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
            sprintf(msg,"New Run Number and File ...");
            printf("%s\n",msg);
            pvPut(msg);
            epicsThreadSleep(1);
            sprintf(msg,"Moller Run in Progress ...");
            printf("%s\n",msg);
            pvPut(msg);
			status=RUN_IN_PROGRESS;
			pvPut(status);
        } state listen
    }
    
    state stopDaq {
		when (!isMollerRunning) {
            sprintf(stmp,msg);
            sprintf(msg,"Moller run is already stopped.");
            printf("%s\n",msg);
            pvPut(msg);
            epicsThreadSleep(5);
            sprintf(msg,stmp);
            pvPut(msg);
		} state listen
        when () {
            isMollerRunning=0;
            sprintf(msg,"Stopping DAQ  ...");
            printf("%s\n",msg);
            pvPut(msg);
            moller_accumulate=STOPDAQ;
            pvPut(moller_accumulate);
            epicsTimeGetCurrent(&timeStamp);
            epicsTimeToStrftime(runEndTime,40,"%m/%d/%Y %H:%M:%S",&timeStamp);
            epicsThreadSleep(1);
            sprintf(msg,"DAQ Stopped.");
            printf("%s\n",msg);
            pvPut(msg);
			status=CONFIGURED;
			pvPut(status);
        } state listen
    }
   
///////////////////////////////////////////////////
    state exitMoller {
        entry {
            sprintf(msg,"Exiting Moller Configuration ...");
            printf("%s\n",msg);
            pvPut(msg);
            epicsThreadSleep(1);
            isMollerRunning=0;
            isMollerConfigured=0;
            sprintf(msg,"Stopping DAQ  ...");
            printf("%s\n",msg);
            pvPut(msg);
            moller_accumulate=STOPDAQ;
            pvPut(moller_accumulate);
			status=CONFIGURED;
			pvPut(status);
            epicsThreadSleep(2);
            sprintf(msg,"Restoring non-Moller configuration ...");
            printf("%s\n",msg);
            pvPut(msg);
			status=NOT_CONFIGURED;
			pvPut(status);
			epicsThreadSleep(1);
        }
        when (delay(1)) {} state quadsOff
    }

    state quadsOff {
        entry {
            sprintf(msg,"De-energizing Quadrupoles ...");
            printf("%s\n",msg);
            pvPut(msg);
            quadB_iset = 0;
            quadC_iset = 0;
            quadB_off = 0;
            quadC_off = 0;
            pvPut(quadB_iset);
            pvPut(quadC_iset);
            pvPut(quadB_off);
            pvPut(quadC_off);
        }
        when (delay(5)) {} state helmholtzOff
    }

    state helmholtzOff {
        entry {
            sprintf(msg,"De-energizing Helmholtz ...");
            printf("%s\n",msg);
            pvPut(msg);
            helm_iset=0;
            pvPut(helm_iset);
            helm_off=1;
            pvPut(helm_off);
        }
        when (delay(5)) {} state restoreSlm
    }
    
	state restoreSlm {
        entry {
            sprintf(msg,"Restoring SLM settings ...");
            printf("%s\n",msg);
            pvPut(msg);
            hv_slm_vset=hv_slm_default;
            pvPut(hv_slm_vset);
        }
        when (delay(2)) {} state retractTarget
    }
    
    state retractTarget {
        entry {
            sprintf(msg,"Retracting Moller Target ...");
            printf("%s\n",msg);
            pvPut(msg);
            tgt_go_empty=1;
            pvPut(tgt_go_empty);
        }
        when (delay(10) && tgt_moving==0 && tgt_empty==1) {
            sprintf(msg,"Non-Moller Configuration Restored.");
            printf("%s\n",msg);
            pvPut(msg);
        } state listen
        
        when (delay(90)) {
            sprintf(msg,"ERROR retracting target.");
            printf("%s\n",msg);
            pvPut(msg);
            status=TGT_ALARM;
            pvPut(status);
        } state listen
    }


}

