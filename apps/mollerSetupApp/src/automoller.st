program automoller

// not reentrant (only one instance allowed):
option -r;

// safe mode:
option +s;

#define DC_ALARM 1
#define SVT_ALARM 2
#define MVT_ALARM 3
#define QUAD_ALARM 4
#define HELM_ALARM 5

int isMollerRunning;
int turnDetectorsOff;
float hv_slm_default;

string stmp;
string msg;   assign msg   to "{P}ctrl:msg";
int alarm;    assign alarm to "{P}ctrl:alarm";
int logentry; assign logentry to "{P}ctrl:logentry"; monitor logentry;

// User Controls:
int moller_enter; assign moller_enter to "{P}ctrl:enter"; monitor moller_enter;
int moller_exit;  assign moller_exit  to "{P}ctrl:exit";  monitor moller_exit;
int moller_recfg; assign moller_recfg to "{P}ctrl:recfg"; monitor moller_recfg;
int daq_start; assign daq_start to "{P}ctrl:start"; monitor daq_start;
int daq_stop;  assign daq_stop  to "{P}ctrl:stop";  monitor daq_stop;

// User Configurations:
float quad_icfg;   assign quad_icfg     to "{P}cfg:quad:iset";
float helm_icfg;   assign helm_icfg     to "{P}cfg:helm:iset";
int helm_polcfg;   assign helm_polcfg   to "{P}cfg:helm:pol";
int tgt_cfg;       assign tgt_cfg       to "{P}cfg:tgt:pos";
float hv_slm_vcfg; assign hv_slm_vcfg   to "{P}cfg:slm:vset";

monitor quad_icfg;    evflag ev_quad_icfg;    sync quad_icfg   ev_quad_icfg;
monitor helm_icfg;    evflag ev_helm_icfg;    sync helm_icfg   ev_helm_icfg;
monitor helm_polcfg;  evflag ev_helm_polcfg;  sync helm_polcfg ev_helm_polcfg;
monitor tgt_cfg;      evflag ev_tgt_cfg;      sync tgt_cfg     ev_tgt_cfg;

// Tagger Current: 
float tagger_irbk; assign tagger_irbk to "{S}TMIRBCK";  monitor tagger_irbk;

// Beam Energy:
float beamEnergy; assign beamEnergy to "{S}MBSY2C_energy";

int halfwaveplate; assign halfwaveplate to "IGL1I00DI24_24M";

// Quadrupoles:
int quadB_on;      assign quadB_on to "{S}DYNABON";
int quadC_on;      assign quadC_on to "{S}DYNACON";
int quadB_off;     assign quadB_off to "{S}DYNABOFF";
int quadC_off;     assign quadC_off to "{S}DYNACOFF";
int quadB_reverse; assign quadB_reverse to "{S}DYNABREVERSE";
int quadB_forward; assign quadB_forward to "{S}DYNABFORWARD";
float quadB_iset;  assign quadB_iset to "{S}DYNABSETI";
float quadC_iset;  assign quadC_iset to "{S}DYNACSETI";
float quadB_imon;  assign quadB_imon to "{S}hallb_sf_xy560_0_14";
float quadC_imon;  assign quadC_imon to "{S}hallb_sf_xy560_0_18";

// Helmholtz:
int helm_state;     assign helm_state   to "{S}B_MOLLER_HELMHOLTZ_STATE";
float helm_iset;    assign helm_iset    to "{S}B_MOLLER_HELMHOLTZ_CURRENT_SET";
float helm_isetrbk; assign helm_isetrbk to "{S}B_MOLLER_HELMHOLTZ_CURRENT_SP";
float helm_irbk;    assign helm_irbk    to "{S}B_MOLLER_HELMHOLTZ_CURRENT";
int helm_on;        assign helm_on      to "{S}B_MOLLER_HELMHOLTZ_OPER";
int helm_off;       assign helm_off     to "{S}B_MOLLER_HELMHOLTZ_OFF";

// Target Motor:
int tgt_go_left;  assign tgt_go_left  to "moller_target_go_left";
int tgt_go_right; assign tgt_go_right to "moller_target_go_right";
int tgt_go_empty; assign tgt_go_empty to "moller_target_go_empty";
float tgt_calib;  assign tgt_calib    to "moller_target_calib";
float tgt_cmd;    assign tgt_cmd      to "moller_target_command";
float tgt_left;   assign tgt_left     to "moller_target_left";
float tgt_right;  assign tgt_right    to "moller_target_right";
float tgt_empty;  assign tgt_empty    to "moller_target_empty"; monitor tgt_empty;
float tgt_moving; assign tgt_moving   to "moeller_target.MOVN"; monitor tgt_moving;

// High Voltage:
float hv_dc_off;    assign hv_dc_off    to "{S}B_DET_DC_HV:OFF";
float hv_svt_off;   assign hv_svt_off   to "{S}B_SVT_SEQ:btnOff";
float hv_bmt_off;   assign hv_bmt_off   to "{S}B_DET_BMT_HV:pwoff";

float hv_slm_onoff;   assign hv_slm_onoff to   "B_DET_BLINE_HV_SLM:pwonoff";
float hv_slm_vsetrbk; assign hv_slm_vsetrbk to "B_DET_BLINE_HV_SLM:vsetrbk"; monitor hv_slm_vsetrbk;
float hv_slm_vset;    assign hv_slm_vset to    "B_DET_BLINE_HV_SLM:vset"; monitor hv_slm_vset;
float hv_slm_stat;    assign hv_slm_stat to    "B_DET_BLINE_HV_SLM:stat"; monitor hv_slm_stat;

int hv_svt_stat; assign hv_svt_stat to "{S}B_SVT:status"; // 0=ALLOFF,1=ALLON,2=MIXED
int hv_bmt_stat; assign hv_bmt_stat to "{S}B_DET_BMT_HV:stat";
int hv_dc_stat;  assign hv_dc_stat to "{S}B_DET_DC_HV:isOff";

// asym DAQ:
int moller_accumulate; assign moller_accumulate to "moller_accumulate";
int moller_reset;      assign moller_reset      to "moller_reset";
string filename;       assign filename      to "asym_filename";
float polarization;    assign polarization  to "beam_polarization";
float epolarization;   assign epolarization to "beam_polarization_error";

%{
void makeLogEntry(
        char* filename,
        float pol,
        float epol,
        float energy,
        float hv,
        float quad,
        float helm,
        int tgt,
        int hwp) {
    char *dir="/home/epics/DATA/MOELLER";
    char cmd[1000];
    char body[1000];
    sprintf(body,
            "Polarization = %.1f +/- %.1f<br>"
            "Half Wave Plate = %d<br>"
            "Target Position = %d<br>"
            "Beam Energy = %.1f<br>"
            "Quad Current = %.1f<br>"
            "Helmholtz Current = %.1f<br>"
            "SLM Voltage = %.1f<br>"
            "Filename = %s/%s<br>",
            pol,epol,hwp,tgt,energy,quad,helm,hv,dir,filename);
    sprintf(cmd,"echo '%s' | logentry --html -l TLOG -t 'Test Run' -a %s/%s -b -",body,dir,filename);
    fprintf(stderr,cmd);
	system(cmd);
}
}%

ss automoller {

    // just connect to pvs:
    state start {
        entry {
            turnDetectorsOff=0;
            isMollerRunning=0;
            sprintf(msg,"connecting ...");
            printf("%s\n",msg);
            pvPut(msg);
        }
        when (pvConnectCount() < pvChannelCount())
        {
            sprintf(msg,"start: Waiting for PVs (%d/%d)",pvConnectCount(),pvChannelCount());
            printf("%s\n",msg);
            pvPut(msg);
            epicsThreadSleep(1);
        } state start

        when () {} state init
    }

    // clear events:
    state init {
        entry {
            efClear(ev_quad_icfg);
            efClear(ev_helm_icfg);
            efClear(ev_helm_polcfg);
            efClear(ev_tgt_cfg);
            //efClear(ev_moller_accumulate);
        }
        when () {
            sprintf(msg,"Non-Moller Configuration.");
            printf("%s\n",msg);
            pvPut(msg);
        } state listen
    }

    // listen for user input:
    state listen {

        when (pvConnectCount() < pvChannelCount())
        {
            sprintf(stmp,"%s",msg);
            sprintf(msg,"listen: Waiting for PVs (%d/%d)",pvConnectCount(),pvChannelCount());
            pvPut(msg);
            epicsThreadSleep(1);
        } state init

        when (efTestAndClear(ev_quad_icfg) && isMollerRunning) {
            sprintf(stmp,"%s",msg);
            sprintf(msg,"Ignoring Quad Reconfigure Mid-Run ...");
            pvPut(msg);
            epicsThreadSleep(1);
            sprintf(msg,"%s",stmp);
            pvPut(msg);
        } state listen

        when (efTestAndClear(ev_helm_icfg) && isMollerRunning) {
            sprintf(stmp,"%s",msg);
            sprintf(msg,"Ignoring Helmholtz Reconfigure Mid-Run ...");
            pvPut(msg);
            epicsThreadSleep(1);
            sprintf(msg,"%s",stmp);
            pvPut(msg);
        } state listen

        when (efTestAndClear(ev_helm_polcfg) && isMollerRunning) {
            sprintf(stmp,"%s",msg);
            sprintf(msg,"Ignoring Helmhotz Reconfigure Mid-Run ...");
            pvPut(msg);
            epicsThreadSleep(1);
            sprintf(msg,"%s",stmp);
            pvPut(msg);
        } state listen

        when (efTestAndClear(ev_tgt_cfg) && isMollerRunning) {
            sprintf(stmp,"%s",msg);
            sprintf(msg,"Ignoring Target Reconfigure Mid-Run ...");
            pvPut(msg);
            epicsThreadSleep(1);
            sprintf(msg,"%s",stmp);
            pvPut(msg);
        } state listen
		
		when (moller_recfg) {
			moller_recfg=0;
			pvPut(moller_recfg);
		} state reconfigure

        when (moller_enter) {
            sprintf(msg,"Entering Moller Configuration ...");
            printf("%s\n",msg);
            pvPut(msg);
            moller_enter=0;
            pvPut(moller_enter);
        } state enterMoller

        when (moller_exit) {
            sprintf(msg,"Exiting Moller Configuration ...");
            printf("%s\n",msg);
            pvPut(msg);
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
            if (isMollerRunning) {
                sprintf(msg,"Moller Run in Progress.  Stop it to make Log Entry.");
                printf("%s\n",msg);
                pvPut(msg);
            }
            else {
                sprintf(msg,"Generating Logbook Entry ...");
                pvPut(msg);
                logentry=0;
                pvPut(logentry);
                pvGet(filename);
                pvGet(beamEnergy);
                pvGet(halfwaveplate);
                pvGet(polarization);
                pvGet(epolarization);
                epicsThreadSleep(5);
                makeLogEntry(filename,polarization,epolarization,beamEnergy,hv_slm_vsetrbk,quad_icfg,helm_icfg,tgt_cfg,halfwaveplate);
                sprintf(msg,"Check logbook for new entry.");
                pvPut(msg);
            }
        } state listen

        when () {
            epicsThreadSleep(1);
        } state listen
    }

///////////////////////////////////////////////////

	state reconfigure {

		entry {
			sprintf(stmp,"%s",msg);
			if (isMollerRunning) {
				sprintf(msg,"Ignoring Reconfigure Mid-Run ...");
				pvPut(msg);
			}
			else {
				sprintf(stmp,"%s",msg);
				sprintf(msg,"Reconfiguring ...");
				pvPut(msg);
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

		when (delay(1) && tgt_moving==0) {
		} state listen
		
		exit {
			sprintf(msg,"%s",stmp);
			pvPut(msg);
		}
	}

    state enterMoller {
		entry {
            sprintf(msg,"Entering Moller Configuration ...");
            printf("%s\n",msg);
            pvPut(msg);
		}
        when (delay(2)) {} state checkTagger
    }

    state checkTagger {

        when (tagger_irbk < 200) {
            sprintf(msg,"ERROR:  Tagger is Off.  Aborted Moller Run.");
            printf("%s\n",msg);
            pvPut(msg);
        } state listen

        when () {} state hvOff
    }

    state hvOff {
      
		// execute entry block even if previous state was the same:
		option -e;

        entry {
            if (turnDetectorsOff) {
				sprintf(msg,"Turning HV Off ...");
				printf("%s\n",msg);
				pvPut(msg);
				if (hv_dc_stat!=0) {
					hv_dc_off=1;
					pvPut(hv_dc_off);
				}
				if (hv_svt_stat!=0) {
					hv_svt_off=1;
					pvPut(hv_svt_off);
				}
				if (hv_bmt_stat!=0) {
					hv_bmt_off=1;
					pvPut(hv_bmt_off);
				}
            }
        }

        when (delay(2) && !turnDetectorsOff) {} state setSlm

        when (delay(5) &&
			  hv_dc_stat==0 &&
			  hv_svt_stat==0 &&
			  hv_bmt_stat==0) {} state setSlm
        
        when (delay(20) && hv_bmt_stat!=0) {} state hvOff
        when (delay(30) && hv_dc_stat!=0)  {} state hvOff
        when (delay(60) && hv_svt_stat!=0) {} state hvOff
        
        when (delay(90)) {
            if (hv_dc_stat!=0) {
				alarm=DC_ALARM;
                sprintf(msg,"ERROR turning DC HV Off.  Aborted Moller Run.");
            }
            else if (hv_svt_stat!=0) {
				alarm=SVT_ALARM;
                sprintf(msg,"ERROR turning SVT HV Off.  Aborted Moller Run.");
            }
            else if (hv_bmt_stat!=0) {
				alarm=MVT_ALARM;
                sprintf(msg,"ERROR turning BMT HV Off.  Aborted Moller Run.");
            }
            printf("%s\n",msg);
			pvPut(alarm);
            pvPut(msg);
        } state listen
        
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
        
        when (hv_slm_vsetrbk==hv_slm_vcfg && hv_slm_stat==1) {} state quadsOn
        
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
            sprintf(msg,"ERROR setting SLM HV.  Aborted Moller Run.");
            printf("%s\n",msg);
            pvPut(msg);
        } state listen

    }

    state quadsOn {
        entry {
            sprintf(msg,"Energizing Quadrupoles ...");
            printf("%s\n",msg);
            pvPut(msg);
            quadB_iset = quad_icfg;
            pvPut(quadB_iset);
            quadC_iset = quad_icfg;
            pvPut(quadC_iset);
            quadB_on = 1;
            pvPut(quadB_on);
            quadC_on = 1;
            pvPut(quadC_on);
            epicsThreadSleep(5);
        }

        when () {} state helmholtzOn

        when (delay(90)) {
            sprintf(msg,"ERROR energizing Quadrupoles.  Aborted Moller Run.");
            printf("%s\n",msg);
            pvPut(msg);
        } state listen
    }

    state helmholtzOn {
        entry {
            sprintf(msg,"Energizing Helmholtz Coils ...");
            printf("%s\n",msg);
            pvPut(msg);
            helm_iset = helm_icfg*(2*helm_polcfg-1);
            pvPut(helm_iset);
            helm_on = 1;
            pvPut(helm_on);
            epicsThreadSleep(5);
        }
        
        when () {} state insertTarget

        when (delay(90)) {
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
            tgt_cmd = tgt_cfg;
            pvPut(tgt_cmd);
        }

        when (delay(10) && tgt_moving==0) {
        } state startDaq

        when (delay(90)) {
            sprintf(msg,"ERROR inserting target.  Aborted Moller Run.");
            printf("%s\n",msg);
            pvPut(msg);
        } state listen

    }


///////////////////////////////////////////////////

    state startDaq {
        entry {
            isMollerRunning=1;
            sprintf(msg,"Starting DAQ  ...");
            printf("%s\n",msg);
            pvPut(msg);
            moller_accumulate=0;
            pvPut(moller_accumulate);
            epicsThreadSleep(2);
            sprintf(msg,"Moller Run in Process ...");
            printf("%s\n",msg);
            pvPut(msg);
        }
        when () {} state listen
    }
    
    state stopDaq {
        entry {
            isMollerRunning=0;
            sprintf(msg,"Stopping DAQ  ...");
            printf("%s\n",msg);
            pvPut(msg);
            moller_accumulate=1;
            pvPut(moller_accumulate);
            epicsThreadSleep(2);
            sprintf(msg,"DAQ Stopped.");
            printf("%s\n",msg);
            pvPut(msg);
        }
        when () {} state listen
    }
   
///////////////////////////////////////////////////
    state exitMoller {
        entry {
            isMollerRunning=0;
            sprintf(msg,"Stopping DAQ  ...");
            printf("%s\n",msg);
            pvPut(msg);
            moller_accumulate=1;
            pvPut(moller_accumulate);
            epicsThreadSleep(2);
            sprintf(msg,"Restoring non-Moller configuration ...");
            printf("%s\n",msg);
            pvPut(msg);
        }
        when (delay(1)) {} state quadsOff
    }

    state quadsOff {
        entry {
            sprintf(msg,"De-energizing Quadrupoles ...");
            printf("%s\n",msg);
            pvPut(msg);
            quadB_iset = 0;
            pvPut(quadB_iset);
            quadC_iset = 0;
            pvPut(quadC_iset);
            quadB_off = 0;
            pvPut(quadB_off);
            quadC_off = 0;
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
        } state listen
    }


}

