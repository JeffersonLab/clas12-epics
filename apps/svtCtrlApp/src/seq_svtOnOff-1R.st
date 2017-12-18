program seq_svtOnOff_1R

// N. Baltzell

option -c;
option +r;
option -s;

%%#include <stdlib.h>

// Duration (seconds) between between repeated checks (and rewrites):
#define CHECKPERIOD 2

// Duration (seconds) between initial write and first rewrite attempt:
#define FIXDELAY 11

// Duration (seconds) after which to abort state if checks unsucessfull:
#define TIMEOUT 120

// Number of PVs to write consecutively without delay:
#define NCONSECWRITES 8

// Delay (seconds) after writing NCONSECWRITES PVs:
#define WRITEDELAY 1

// Voltage thresholds for considering a channel ON (LARGE) or OFF (SMALL):
#define HVSMALL 0.2
#define HVLARGE 1.0
#define LVSMALL 0.1
#define LVLARGE 1.0

// These are just for initializing PV names:
#define NREGIONS 4
#define NSIDES 2
string sides[NSIDES]={"T","B"};
int nModulesPerRegion[NREGIONS]={10,14,18,24};
int hv_slotsPerRegion[NREGIONS][4]={ { 7,8,9,10}, { 9,10,0,0}, { 8, 9,10,0}, { 8, 9,10,0} };
int hv_nChansPerSlot[NREGIONS][4] ={ {16,4,0, 0}, {16,12,0,0}, {16,16, 4,0}, {16,16,16,0} };

// Static PVs (i.e. count known at compile-time):
#define NPVSTATIC 7
string msg;    assign msg      to "B_SVT_R{R}_SEQ:msg";
short btnOff;  assign btnOff   to "B_SVT_R{R}_SEQ:btnOff";  monitor btnOff;
short btnOn;   assign btnOn    to "B_SVT_R{R}_SEQ:btnOn";   monitor btnOn;
short btnAbt;  assign btnAbt   to "B_SVT_R{R}_SEQ:btnAbt";  monitor btnAbt;
int lv_isOn;   assign lv_isOn  to "B_SVT_LV_R{R}:isOn";     monitor lv_isOn; 
int lv_isOff;  assign lv_isOff to "B_SVT_LV_R{R}:isOff";    monitor lv_isOff;
int hv_isOn;   assign hv_isOn  to "B_SVT_HV_R{R}:isOn";     monitor hv_isOn;
int hv_isOff;  assign hv_isOff to "B_SVT_HV_R{R}:isOff";    monitor hv_isOff;

// Dynamic PVs (i.e. count defined at run-time)
#define NCHANS 96
double hv_vmon[NCHANS];   assign hv_vmon to {};
double lva_vmon[NCHANS];  assign lva_vmon to {};
double lvd_vmon[NCHANS];  assign lvd_vmon to {};
int hv_switchOn[NCHANS];  assign hv_switchOn to {};
int lv_switchOn[NCHANS];  assign lv_switchOn to {};
int hv_switchOff[NCHANS]; assign hv_switchOff to {};
int lv_switchOff[NCHANS]; assign lv_switchOff to {};

// These should be "const":
string prefix="B_SVT";
string hv_vmonSuff=":outputMeasSenseV";
string lv_vmonSuff=":outputMeasSenseV";
string hv_switchSuff=":HVPB_";
string lv_switchSuff=":PB_";
string hv_switchOffSuff=":outSwitch";
string lv_switchOffSuff=":onOff";

// Region# for this sequencer instance:
int iRegion;

// Number of hv/lv channels (region-dependent):
int hv_nChan, lv_nChan;

// Number of connected PVs (region-dependent):
int nPVs;

// Temporary variables:
string stmp, sRegion;
int t0, doFix, hv_iSlot, hv_nChanSlot;
int ii, jj, kk, slot, exitError, allGood;

ss seq_svtOnOff_1R {

    state start { // Check R macro, assign region#, wait for static PVs
        
        entry {
            exitError = 0;
            nPVs = NPVSTATIC;
            sprintf(sRegion,"%s",macValueGet("R"));
            if (strcmp(sRegion,"1")!=0 &&
                strcmp(sRegion,"2")!=0 &&
                strcmp(sRegion,"3")!=0 &&
                strcmp(sRegion,"4")!=0) {
                exitError=1;
                sprintf(msg,"start: Invalid Region (%s), EXITING.",sRegion);
                printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
                pvPut(msg);
            } else { 
                iRegion=atoi(sRegion);
            }
        }

        when (exitError) {} exit

        when (pvConnectCount() < nPVs) {
            sprintf(msg,"start: Waiting for PVs (%d/%d)",pvConnectCount(),nPVs);
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            epicsThreadSleep(1);
        } state start

        when () {} state init
    }

    state init { // Assign and wait for dynamic PVs
        
        entry {
            sprintf(msg,"init: Assigning PVs ...");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            hv_nChan=0;
            lv_nChan=0;
            hv_iSlot=0;
            hv_nChanSlot=0;
            for (ii=0; ii<nModulesPerRegion[iRegion-1]; ii++) {
                
                for (jj=0; jj<NSIDES; jj++) {
               
                    // HV:
                    // slot mapping defined by global arrays above
                    slot = hv_slotsPerRegion[iRegion-1][hv_iSlot];
                    
                    sprintf(stmp,"%s_HV_R%dS%d%s_Slot%d%s",prefix,
                            iRegion,ii+1,sides[jj],slot,hv_vmonSuff);
                    pvAssign(hv_vmon[hv_nChan],stmp);
                    
                    sprintf(stmp,"R%dS%d%s%sOFF",
                            iRegion,ii+1,sides[jj],hv_switchSuff);
                    pvAssign(hv_switchOff[hv_nChan],stmp);
                    
                    sprintf(stmp,"R%dS%d%s%sON",
                            iRegion,ii+1,sides[jj],hv_switchSuff);
                    pvAssign(hv_switchOn[hv_nChan],stmp);

                    hv_nChan++;
                    nPVs += 3;
                    
                    // LV:
                    // slot mapping just starts at 1, with 8 channels per slot,
                    // except R4 starts over after Slot6
                    slot = (ii*4+jj*2)/8+1;
                    if (iRegion==4 && slot>6) slot-=6;

                    sprintf(stmp,"R%dS%d%s%sOFF",
                             iRegion,ii+1,sides[jj],lv_switchSuff);
                    pvAssign(lv_switchOff[lv_nChan],stmp);
                    
                    sprintf(stmp,"R%dS%d%s%sON",
                             iRegion,ii+1,sides[jj],lv_switchSuff);
                    pvAssign(lv_switchOn[lv_nChan],stmp);
                        
                    sprintf(stmp,"%s_LV_VA_R%dS%d%s_Slot%d%s",prefix,
                            iRegion,ii+1,sides[jj],slot,lv_vmonSuff);
                    pvAssign(lva_vmon[lv_nChan],stmp);

                    sprintf(stmp,"%s_LV_VD_R%dS%d%s_Slot%d%s",prefix,
                            iRegion,ii+1,sides[jj],slot,lv_vmonSuff);
                    pvAssign(lvd_vmon[lv_nChan],stmp);

                    lv_nChan++;
                    nPVs += 4;

                }
                
                hv_nChanSlot += 2;
                if (hv_nChanSlot >= hv_nChansPerSlot[iRegion-1][hv_iSlot])
                {
                    hv_iSlot++;
                    hv_nChanSlot=0;
                }
            }
        }
        
        when (pvConnectCount() < nPVs) {
            sprintf(msg,"init: Waiting for PVs (%d/%d)",pvConnectCount(),nPVs);
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            epicsThreadSleep(2);
        } state init

        when () {} state listen
    }

    state wait { // Wait for disconnected PVs

        when (pvConnectCount() < nPVs) {
            sprintf(msg,"wait: Waiting for PVs (%d/%d)",pvConnectCount(),nPVs);
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            epicsThreadSleep(2);
        } state wait
        
        when () {} state listen
    }

    //
    // Normal State Flow:
    //
    // listen --> lvOn --> hvOn --> listen
    //
    // listen --> hvOff --> lvOff --> listen
    //
    //
    
    state listen {
        
        entry {
            sprintf(msg,"listen ...");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
        }

        when (pvConnectCount() < nPVs) {} state wait

        when (btnOff) { btnOff=0; pvPut(btnOff); } state hvOff
        when (btnOn)  { btnOn=0;  pvPut(btnOn);  } state lvOn

        when () { epicsThreadSleep(1); } state listen
    }

    state lvOn {

        // Only reset timer if previous state is different:
        option -t;

        // Initialize state variables and write all on/off PVs:
        entry {
            t0=0;
            doFix=0;
            allGood=0;
            sprintf(msg,"lvOn ...");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            for (ii=0; ii<lv_nChan; ii++) {
                lv_switchOn[ii]=1;
                pvPut(lv_switchOn[ii]);
                if ((ii+1)%NCONSECWRITES==0) {
                    epicsThreadSleep(WRITEDELAY);
                    t0 += WRITEDELAY;
                }
            }
        }
       
        // Abort if lost PV connections: 
        when (pvConnectCount() < nPVs) {} state wait

        // Honor user-intervention:
        when (btnAbt) { btnAbt=0; pvPut(btnAbt); } state listen
        when (btnOff) { btnOff=0; pvPut(btnOff); } state hvOff
        when (btnOn)  { btnOn=0;  pvPut(btnOn);  } state lvOn

        // Success, proceed to next state:
        when (allGood) {} state hvOn

        // Abort if no timely success:
        when (delay(t0+TIMEOUT)) {
            sprintf(msg,"lvOn:  TIMEOUT");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            epicsThreadSleep(5);
        } state listen

        // Enable rewriting: 
        when (delay(t0+FIXDELAY) && !doFix) { doFix=1; } state lvOn

        // Confirm results:
        when () {

            allGood=1;
            sprintf(msg,"lvOn: checking ... ");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);

            // Check monitored voltages:
            for (ii=0; ii<lv_nChan; ii++) {
                
                pvGet(lva_vmon[ii]);
                pvGet(lvd_vmon[ii]);
                
                if (lva_vmon[ii]<LVLARGE || lvd_vmon[ii]<LVLARGE) {
                    allGood=0;
                  
                    // Rewrite, if enabled:
                    if (doFix) {
                        printf("%d ",ii);
                        lv_switchOn[ii]=1;
                        pvPut(lv_switchOn[ii]);
                    }

                }
            }
            
            // Require confirmation from global status PV:
            if (!lv_isOn) allGood=0;
            
            // Failure, delay before next check: 
            if (!allGood) {
                if (doFix) printf("\n");
                epicsThreadSleep(CHECKPERIOD);
            }

        } state hvOn
    }

    state hvOn {
        
        option -t;

        entry {
            t0=0;
            doFix=0;
            allGood=0;
            epicsThreadSleep(5); t0+=5;
            sprintf(msg,"hvOn ...");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            for (ii=0; ii<hv_nChan; ii++) {
                hv_switchOn[ii]=1;
                pvPut(hv_switchOn[ii]);
                if ((ii+1)%NCONSECWRITES==0) {
                    epicsThreadSleep(WRITEDELAY);
                    t0 += WRITEDELAY;
                }
            }
        }
        
        when (pvConnectCount() < nPVs) {} state wait

        when (btnAbt) { btnAbt=0; pvPut(btnAbt); } state listen
        when (btnOff) { btnOff=0; pvPut(btnOff); } state hvOff
        when (btnOn)  { btnOn=0;  pvPut(btnOn);  } state hvOn

        when (allGood) {} state listen

        when (delay(t0+TIMEOUT)) {
            sprintf(msg,"hvOn:  TIMEOUT");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            epicsThreadSleep(5);
        } state listen

        when (delay(t0+FIXDELAY) && !doFix) { doFix=1; } state hvOn

        when () {
            allGood=1;
            sprintf(msg,"hvOn: checking ... ");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            for (ii=0; ii<hv_nChan; ii++) {
                pvGet(hv_vmon[ii]);
                if (hv_vmon[ii] < HVLARGE) {
                    allGood=0;
                    if (doFix) {
                        printf("%d ",ii);
                        hv_switchOn[ii]=1;
                        pvPut(hv_switchOn[ii]);
                    }
                }
            }
            if (!hv_isOn) allGood=0;
            if (!allGood) {
                printf("\n");
                epicsThreadSleep(CHECKPERIOD);
            }
        } state hvOn
    }

    state hvOff {
        
        option -t;

        entry {
            t0=0;
            doFix=0;
            allGood=0;
            sprintf(msg,"hvOff ...");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            for (ii=0; ii<hv_nChan; ii++) {
                hv_switchOff[ii]=1;
                pvPut(hv_switchOff[ii]);
                if ((ii+1)%NCONSECWRITES==0) {
                    epicsThreadSleep(WRITEDELAY);
                    t0 += WRITEDELAY;
                }
            }
        }
        
        when (pvConnectCount() < nPVs) {} state wait

        when (btnAbt) { btnAbt=0; pvPut(btnAbt); } state listen
        when (btnOff) { btnOff=0; pvPut(btnOff); } state hvOff
        when (btnOn)  { btnOn=0;  pvPut(btnOn);  } state lvOn

        when (allGood) {} state lvOff

        when (delay(t0+TIMEOUT)) {
            sprintf(msg,"hvOff:  TIMEOUT");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            epicsThreadSleep(5);
        } state listen

        when (delay(t0+FIXDELAY) && !doFix) { doFix=1; } state hvOff

        when () {
            allGood=1;
            sprintf(msg,"hvOff: checking ... ");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            for (ii=0; ii<hv_nChan; ii++) {
                pvGet(hv_vmon[ii]);
                if (hv_vmon[ii] > HVSMALL) {
                    allGood=0;
                    if (doFix) {
                        printf("%d ",ii);
                        hv_switchOff[ii]=1;
                        pvPut(hv_switchOff[ii]);
                    }
                }
            }
            if (!hv_isOff) allGood=0;
            if (!allGood) {
                printf("\n");
                epicsThreadSleep(CHECKPERIOD);
            }
        } state hvOff
    }
    
    state lvOff {
        
        option -t;

        entry {
            t0=0;
            doFix=0;
            allGood=0;
            epicsThreadSleep(3); t0+=3;
            sprintf(msg,"lvOff ...");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            for (ii=0; ii<lv_nChan; ii++) {
                lv_switchOff[ii]=1;
                pvPut(lv_switchOff[ii]);
                if ((ii+1)%NCONSECWRITES==0) {
                    epicsThreadSleep(WRITEDELAY);
                    t0 += WRITEDELAY;
                }
            }
        }

        when (pvConnectCount() < nPVs) {} state wait

        when (btnAbt) { btnAbt=0; pvPut(btnAbt); } state listen
        when (btnOff) { btnOff=0; pvPut(btnOff); } state lvOff
        when (btnOn)  { btnOn=0;  pvPut(btnOn);  } state lvOn

        when (allGood) {} state listen

        when (delay(t0+TIMEOUT)) {
            sprintf(msg,"lvOff:  TIMEOUT");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            epicsThreadSleep(5);
        } state listen

        when (delay(t0+FIXDELAY) && !doFix) { doFix=1; } state lvOff
        
        when () {
            allGood=1;
            sprintf(msg,"lvOff: checking ... ");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            for (ii=0; ii<lv_nChan; ii++) {
                pvGet(lva_vmon[ii]);
                pvGet(lvd_vmon[ii]);
                if (lva_vmon[ii]>LVSMALL || lvd_vmon[ii]>LVSMALL) {
                    allGood=0;
                    if (doFix) {
                        printf("%d ",ii);
                        lv_switchOff[ii]=1;
                        pvPut(lv_switchOff[ii]);
                    }
                }
            }
            if (!lv_isOff) allGood=0;
            if (!allGood) {
                printf("\n");
                epicsThreadSleep(CHECKPERIOD);
            }
        } state lvOff
    }

}

