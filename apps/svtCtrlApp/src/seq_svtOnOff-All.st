program seq_svtOnOff_All

option -c;
option -r;
option -s;

%%#include <stdlib.h>

#define NREGIONS 4
#define REGIONDELAY 20

string msg;      assign msg       to "B_SVT_SEQ:msg";
short btnOffAll; assign btnOffAll to "B_SVT_SEQ:btnOff"; monitor btnOffAll;
short btnOnAll;  assign btnOnAll  to "B_SVT_SEQ:btnOn";  monitor btnOnAll;
short btnAbtAll; assign btnAbtAll to "B_SVT_SEQ:btnAbt"; monitor btnAbtAll;

short btnOff[NREGIONS];  assign btnOff to {};
short btnOn[NREGIONS];   assign btnOn  to {};

//int lv_isOn[NREGIONS];   assign lv_isOn  to {};
//int lv_isOff[NREGIONS];  assign lv_isOff to {};
//int hv_isOn[NREGIONS];   assign hv_isOn  to {};
//int hv_isOff[NREGIONS];  assign hv_isOff to {};

// temporary variables:
string stmp;
int ii,iRegion;

int orderOn[NREGIONS]={4,3,2,1};
int orderOff[NREGIONS]={1,2,3,4};

ss seq_svtOnOff_All {

    state start {
        
        entry {
            for (ii=0; ii<NREGIONS; ii++) {
                sprintf(stmp,"B_SVT_R%d_SEQ:btnOff",ii+1);
                pvAssign(btnOff[ii],stmp);
                sprintf(stmp,"B_SVT_R%d_SEQ:btnOn",ii+1);
                pvAssign(btnOn[ii],stmp);
                sprintf(stmp,"B_SVT_HV_R%d:isOn",ii+1);
                
                //pvAssign(hv_isOn[ii],stmp);
                //sprintf(stmp,"B_SVT_HV_R%d:isOff",ii+1);
                //pvAssign(hv_isOff[ii],stmp);
                //sprintf(stmp,"B_SVT_LV_R%d:isOn",ii+1);
                //pvAssign(lv_isOn[ii],stmp);
                //sprintf(stmp,"B_SVT_LV_R%d:isOff",ii+1);
                //pvAssign(lv_isOff[ii],stmp);

                //pvMonitor(hv_isOn[ii]);
                //pvMonitor(lv_isOn[ii]);
                //pvMonitor(hv_isOff[ii]);
                //pvMonitor(lv_isOff[ii]);
            }
        }
        
        when (pvConnectCount() < pvChannelCount())
        {
            sprintf(msg,"start: Waiting for PVs (%d/%d)",pvConnectCount(),pvChannelCount());
            printf("seq_svtOnOff_All() - %s\n",msg);
            pvPut(msg);
            epicsThreadSleep(1);
        } state start

        when () {} state listen
    }

    state listen {
       
        entry {
            sprintf(msg,"listen ...");
            printf("seq_svtOnOff_All() - %s\n",msg);
            pvPut(msg);
        }
        
        when (pvConnectCount() < pvChannelCount())
        {
            sprintf(msg,"listen: Waiting for PVs (%d/%d)",pvConnectCount(),pvChannelCount());
            printf("seq_svtOnOff_All() - %s\n",msg);
            pvPut(msg);
            epicsThreadSleep(1);
        } state listen
        
        when (btnOffAll) { btnOffAll=0; pvPut(btnOffAll); } state off
        
        when (btnOnAll)  { btnOnAll=0;  pvPut(btnOnAll);  } state on
    }


    state on {
        option -t;
        entry {
            iRegion=0;
            btnOn[orderOn[iRegion]-1]=1;
            pvPut(btnOn[orderOn[iRegion]-1]);
            iRegion+=1;
        }
        
        when (iRegion>=NREGIONS) {} state listen
        
        when (btnAbtAll) { btnAbtAll=0; pvPut(btnAbtAll); } state listen
        when (btnOffAll) { btnOffAll=0; pvPut(btnOffAll); } state off
        when (btnOnAll)  { btnOnAll=0;  pvPut(btnOnAll);  } state on

        when (delay(REGIONDELAY*1) && iRegion==1) {
            btnOn[orderOn[iRegion]-1]=1;
            pvPut(btnOn[orderOn[iRegion]-1]);
            iRegion+=1;
        } state on
        
        when (delay(REGIONDELAY*2) && iRegion==2) {
            btnOn[orderOn[iRegion]-1]=1;
            pvPut(btnOn[orderOn[iRegion]-1]);
            iRegion+=1;
        } state on

        when (delay(REGIONDELAY*3) && iRegion==3) {
            btnOn[orderOn[iRegion]-1]=1;
            pvPut(btnOn[orderOn[iRegion]-1]);
            iRegion+=1;
        } state listen
    }

    state off {
        option -t;
        entry {
            iRegion=0;
            btnOff[orderOff[iRegion]-1]=1;
            pvPut(btnOn[orderOff[iRegion]-1]);
            iRegion+=1;
        }
        
        when (iRegion>=NREGIONS) {} state listen
        
        when (btnAbtAll) { btnAbtAll=0; pvPut(btnAbtAll); } state listen
        when (btnOnAll)  { btnOnAll=0;  pvPut(btnOnAll);  } state on
        when (btnOffAll) { btnOffAll=0; pvPut(btnOffAll); } state off

        when (delay(REGIONDELAY*1) && iRegion==1) {
            btnOn[orderOff[iRegion]-1]=1;
            pvPut(btnOff[orderOff[iRegion]-1]);
            iRegion+=1;
        } state off
        
        when (delay(REGIONDELAY*2) && iRegion==2) {
            btnOn[orderOff[iRegion]-1]=1;
            pvPut(btnOff[orderOff[iRegion]-1]);
            iRegion+=1;
        } state off

        when (delay(REGIONDELAY*3) && iRegion==3) {
            btnOn[orderOff[iRegion]-1]=1;
            pvPut(btnOff[orderOff[iRegion]-1]);
            iRegion+=1;
        } state listen
    }
}


/*
    state on {
        
        entry {
            nGood=0;
            //nIter=0;
            sprintf(msg,"on ...");
            printf("seq_svtOnOff_All() - %s\n\n",msg);
            pvPut(msg);
        }

        when (btnOffAll) {
            btnOffAll=0; pvPut(btnOffAll);
            btnOnAll=0;  pvPut(btnOnAll);
        } state off

        when (btnOnAll) { btnOnAll=0; pvPut(btnOnAll); } state on

        when (nGood==NREGIONS) {} state listen
        
        when () {
            nGood=0;
            for (ii=0; ii<NREGIONS; ii++) {
                iReg=orderOn[ii]-1;
                if (lv_isOn[iReg] && hv_isOn[iReg]) {
                    nGood++;
                    continue;
                }
                btnOn[iReg]=1;
                pvPut(btnOn[iReg]);
                break;
            }
        } state on
    }
    
    state off {
        
        entry {
            nGood=0;
            sprintf(msg,"off ...");
            printf("\nseq_svtOnOff_All() - %s\n\n",msg);
            pvPut(msg);
        }

        when (btnOffAll) { btnOffAll=0; pvPut(btnOffAll); } state off
        
        when (btnOnAll) { btnOnAll=0; pvPut(btnOnAll); } state on

        when (nGood==NREGIONS) {} state listen
        
        when () {
            nGood=0;
            for (ii=0; ii<NREGIONS; ii++) {
                iReg=orderOff[ii]-1;
                if (lv_isOff[iReg] && hv_isOff[iReg]) {
                    nGood++;
                    continue;
                }
                btnOff[iReg]=1;
                pvPut(btnOff[iReg]);
                break;
            }
        } state off
    }
*/

