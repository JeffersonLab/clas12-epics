program seq_svtOnOff_1R

option -c;
option +r;
option -s;

%%#include <stdlib.h>

// Refrain from checking for this long:
#define CHECKDELAY 16 // units=seconds

// Delay between repeated checks in a single on/off state:
#define RECHECKDELAY 2 // units=seconds

// Abort on/off state if checks still uncessfull after this long:
#define TIMEOUT 60 // units=seconds

// Voltage thresholds for considering a channel ON (LARGE) or OFF (SMALL):
#define HVSMALL 0.1
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

// These are "static" PVs (i.e. count known at compile-time):
#define NPVSTATIC 7
string msg;    assign msg      to "B_SVT_R{R}_SEQ:msg";
short btnOff;  assign btnOff   to "B_SVT_R{R}_SEQ:btnOff";  monitor btnOff;
short btnOn;   assign btnOn    to "B_SVT_R{R}_SEQ:btnOn";   monitor btnOn;
int lv_isOn;   assign lv_isOn  to "B_SVT_LV_R{R}:isOn";     monitor lv_isOn; 
int lv_isOff;  assign lv_isOff to "B_SVT_LV_R{R}:isOff";    monitor lv_isOff;
int hv_isOn;   assign hv_isOn  to "B_SVT_HV_R{R}:isOn";     monitor hv_isOn;
int hv_isOff;  assign hv_isOff to "B_SVT_HV_R{R}:isOff";    monitor hv_isOff;
//int watchdog;  assign watchdog to "B_SVT_R{R}_SEQ:heartbeat";

// These are dynamically assigned PVs (i.e. count is defined at run-time)
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

// temporary variables:
string stmp,sRegion;
int hv_nChan,lv_nChan,nPVs;
int hv_iSlot,hv_nChanSlot,allGood;
int ii,jj,kk,slot,iRegion,exitError;

ss seq_svtOnOff_1R {

    state start { // check R macro and wait for static PVs
        
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

    state init { // initialize and wait for dynamically-assigned PVs
        
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

    state wait {
        when (pvConnectCount() < nPVs) {
            sprintf(msg,"wait: Waiting for PVs (%d/%d)",pvConnectCount(),nPVs);
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            epicsThreadSleep(2);
        } state listen
        when () { epicsThreadSleep(2); } state wait
    }

    //
    // STATE FLOWCHART:
    //
    // listen --> lvOn --> hvOn --> listen
    //            |           |
    //            |-> hvOff   |-> hvOff
    //
    // listen --> hvOff --> lvOff --> listen
    //            |           |
    //            |-> lvOn    |-> lvOn
    //
    
    state listen {
        
        entry {
            sprintf(msg,"listen ...");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
        }

        when (pvConnectCount() < nPVs) {} state wait
        
        when (btnOff) {
            btnOff=0;  pvPut(btnOff);
            btnOn=0;   pvPut(btnOn);
        } state hvOff

        when (btnOn) {
            btnOn=0;   pvPut(btnOn);
        } state lvOn

        when () { epicsThreadSleep(1); } state listen
    }

    state lvOn {

        // do not reset timer unless previous state is different:
        option -t;

        entry {
            allGood=0;
            sprintf(msg,"lvOn ...");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            for (ii=0; ii<lv_nChan; ii++) {
                lv_switchOn[ii]=1;
                pvPut(lv_switchOn[ii]);
                if ((ii+1)%10==0) epicsThreadSleep(1);
            }
        }
        
        when (btnOff) {
            btnOff=0; pvPut(btnOff);
            btnOn=0;  pvPut(btnOn);
        } state hvOff

        when (btnOn) { btnOn=0; pvPut(btnOn); } state lvOn

        when (allGood) {} state hvOn

        when (delay(TIMEOUT)) {
            sprintf(msg,"lvOn:  TIMEOUT");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
        } state listen

        when (delay(CHECKDELAY)) {
            if (lv_isOn) {
                allGood=1;
                printf("lvOn: checking ... ");
                for (ii=0; ii<lv_nChan; ii++) {
                    pvGet(lva_vmon[ii]);
                    pvGet(lvd_vmon[ii]);
                    if (lva_vmon[ii]<LVLARGE || lvd_vmon[ii]<LVLARGE) {
                        printf("%d ",ii);
                        allGood=0;
                        lv_switchOn[ii]=1;
                        pvPut(lv_switchOn[ii]);
                    }
                }
                printf("\n");
            }
            epicsThreadSleep(RECHECKDELAY);
        } state lvOn
    }

    state hvOn {
        
        // do not reset timer unless previous state is different:
        option -t;

        entry {
            allGood=0;
            sprintf(msg,"hvOn ...");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            for (ii=0; ii<hv_nChan; ii++) {
                hv_switchOn[ii]=1;
                pvPut(hv_switchOn[ii]);
                if ((ii+1)%10==0) epicsThreadSleep(1);
            }
        }
        
        when (btnOff) {
            btnOff=0;  pvPut(btnOff);
            btnOn=0;   pvPut(btnOn);
        } state hvOff

        when (btnOn) { btnOn=0; pvPut(btnOn); } state hvOn

        when (allGood) {} state listen

        when (delay(TIMEOUT)) {
            sprintf(msg,"hvOn:  TIMEOUT");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
        } state listen

        when (delay(CHECKDELAY)) {
            if (hv_isOn) {
                allGood=1;
                printf("hvOn: checking ... ");
                for (ii=0; ii<hv_nChan; ii++) {
                    pvGet(hv_vmon[ii]);
                    if (hv_vmon[ii] < HVLARGE) {
                        printf("%d ",ii);
                        allGood=0;
                        hv_switchOn[ii]=1;
                        pvPut(hv_switchOn[ii]);
                    }
                }
                printf("\n");
            }
            epicsThreadSleep(RECHECKDELAY);
        } state hvOn
    }

    state hvOff {
        
        // do not reset timer unless previous state is different:
        option -t;

        entry {
            allGood=0;
            sprintf(msg,"hvOff ...");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            for (ii=0; ii<hv_nChan; ii++) {
                hv_switchOff[ii]=1;
                pvPut(hv_switchOff[ii]);
                if ((ii+1)%10==0) epicsThreadSleep(1);
            }
        }
        when (btnOff) { btnOff=0; pvPut(btnOff); } state hvOff

        when (btnOn) { btnOn=0; pvPut(btnOn); } state lvOn

        when (allGood) {} state lvOff

        when (delay(TIMEOUT)) {
            sprintf(msg,"hvOff:  TIMEOUT");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
        } state listen

        when (delay(CHECKDELAY)) {
            if (hv_isOff) {
                allGood=1;
                printf("hvOff: checking ... ");
                for (ii=0; ii<hv_nChan; ii++) {
                    pvGet(hv_vmon[ii]);
                    if (hv_vmon[ii] > HVSMALL) {
                        printf("%d ",ii);
                        allGood=0;
                        hv_switchOff[ii]=1;
                        pvPut(hv_switchOff[ii]);
                    }
                }
                printf("\n");
            }
            epicsThreadSleep(RECHECKDELAY);
        } state hvOff
    }
    
    state lvOff {
        
        // do not reset timer unless previous state is different:
        option -t;

        entry {
            allGood=0;
            sprintf(msg,"lvOff ...");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
            for (ii=0; ii<lv_nChan; ii++) {
                printf("%d\n",ii);
                lv_switchOff[ii]=1;
                pvPut(lv_switchOff[ii]);
                if ((ii+1)%10==0) epicsThreadSleep(1);
            }
            epicsThreadSleep(0.2);
        }

        when (btnOff) { btnOff=0; pvPut(btnOff); } state lvOff
        
        when (btnOn) { btnOn=0; pvPut(btnOn); } state lvOn

        when (allGood) {} state listen
        
        when (delay(TIMEOUT)) {
            sprintf(msg,"lvOff:  TIMEOUT");
            printf("seq_svtOnOff_1R(%d) - %s\n",iRegion,msg);
            pvPut(msg);
        } state listen

        when (delay(CHECKDELAY)) {
            if (lv_isOff) {
                allGood=1;
                printf("hvOff: checking ... ");
                for (ii=0; ii<lv_nChan; ii++) {
                    pvGet(lva_vmon[ii]);
                    pvGet(lvd_vmon[ii]);
                    if (lva_vmon[ii]>LVSMALL || lvd_vmon[ii]>LVSMALL) {
                        printf("%d ",ii);
                        allGood=0;
                        lv_switchOff[ii]=1;
                        pvPut(lv_switchOff[ii]);
                    }
                }
                printf("\n");
            }
            epicsThreadSleep(RECHECKDELAY);
        } state lvOff
    }

}

