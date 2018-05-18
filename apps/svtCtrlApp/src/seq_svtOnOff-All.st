program seq_svtOnOff_All

// N. Baltzell

option -c;
option -r;
option -s;

%%#include <stdlib.h>

#define NREGIONS 3

// Duration (seconds) between regions:
#define REGIONDELAY 20

// Region ordering:
int orderOn[NREGIONS]={3,2,1};
int orderOff[NREGIONS]={1,2,3};

// seq_svtOnOff_All buttons:
string msg;      assign msg       to "B_SVT_SEQ:msg";
short btnOffAll; assign btnOffAll to "B_SVT_SEQ:btnOff"; monitor btnOffAll;
short btnOnAll;  assign btnOnAll  to "B_SVT_SEQ:btnOn";  monitor btnOnAll;
short btnAbtAll; assign btnAbtAll to "B_SVT_SEQ:btnAbt"; monitor btnAbtAll;

// seq_svtOnOff_1R buttons:
short btnOff[NREGIONS];  assign btnOff to {};
short btnOn[NREGIONS];   assign btnOn  to {};

string stmp;
int ii,iRegion;

ss seq_svtOnOff_All {

    state start {
        
        entry {
            sprintf(msg,"start:");
            printf("seq_svtOnOff_All() - %s\n",msg);
            pvPut(msg);
            for (ii=0; ii<NREGIONS; ii++) {
                sprintf(stmp,"B_SVT_R%d_SEQ:btnOff",ii+1);
                pvAssign(btnOff[ii],stmp);
                sprintf(stmp,"B_SVT_R%d_SEQ:btnOn",ii+1);
                pvAssign(btnOn[ii],stmp);
                sprintf(stmp,"B_SVT_HV_R%d:isOn",ii+1);
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
        
        when (btnAbtAll) { btnAbtAll=0; pvPut(btnAbtAll); } state listen
        when (btnOffAll) { btnOffAll=0; pvPut(btnOffAll); } state off
        when (btnOnAll)  { btnOnAll=0;  pvPut(btnOnAll);  } state on
    }


    state on {
        
        option -t;
        entry {
            iRegion=0;
            sprintf(msg,"on:");
            printf("seq_svtOnOff-All - %s\n",msg);
            pvPut(msg);
        }
        
        when (pvConnectCount() < pvChannelCount()) {} state listen
        
        when (iRegion>=NREGIONS) {} state listen
        
        when (btnAbtAll) { btnAbtAll=0; pvPut(btnAbtAll); } state listen
        when (btnOffAll) { btnOffAll=0; pvPut(btnOffAll); } state off
        when (btnOnAll)  { btnOnAll=0;  pvPut(btnOnAll);  } state on

        when (iRegion==0 && delay(REGIONDELAY*iRegion)) {
            sprintf(msg,"on:  R%d",orderOn[iRegion]);
            printf("seq_svtOnOff-All - %s\n",msg);
            pvPut(msg);
            btnOn[orderOn[iRegion]-1]=1;
            pvPut(btnOn[orderOn[iRegion]-1]);
            iRegion+=1;
        } state on
        
        when (iRegion==1 && delay(REGIONDELAY*iRegion)) {
            sprintf(msg,"on:  R%d",orderOn[iRegion]);
            printf("seq_svtOnOff-All - %s\n",msg);
            pvPut(msg);
            btnOn[orderOn[iRegion]-1]=1;
            pvPut(btnOn[orderOn[iRegion]-1]);
            iRegion+=1;
        } state on
        
        when (iRegion==2 && delay(REGIONDELAY*iRegion)) {
            sprintf(msg,"on:  R%d",orderOn[iRegion]);
            printf("seq_svtOnOff-All - %s\n",msg);
            pvPut(msg);
            btnOn[orderOn[iRegion]-1]=1;
            pvPut(btnOn[orderOn[iRegion]-1]);
            iRegion+=1;
        } state listen
    }

    state off {
        
        option -t;
        entry {
            iRegion=0;
            sprintf(msg,"off:");
            printf("seq_svtOnOff-All - %s\n",msg);
            pvPut(msg);
        }
        
        when (pvConnectCount() < pvChannelCount()) {} state listen
        
        when (iRegion>=NREGIONS) {} state listen
        
        when (btnAbtAll) { btnAbtAll=0; pvPut(btnAbtAll); } state listen
        when (btnOnAll)  { btnOnAll=0;  pvPut(btnOnAll);  } state on
        when (btnOffAll) { btnOffAll=0; pvPut(btnOffAll); } state off
        
        when (iRegion==0 && delay(REGIONDELAY*iRegion)) {
            sprintf(msg,"off:  R%d",orderOff[iRegion]);
            printf("seq_svtOnOff-All - %s\n",msg);
            pvPut(msg);
            btnOff[orderOff[iRegion]-1]=1;
            pvPut(btnOff[orderOff[iRegion]-1]);
            iRegion+=1;
        } state off

        when (iRegion==1 && delay(REGIONDELAY*iRegion)) {
            sprintf(msg,"off:  R%d",orderOff[iRegion]);
            printf("seq_svtOnOff-All - %s\n",msg);
            pvPut(msg);
            btnOff[orderOff[iRegion]-1]=1;
            pvPut(btnOff[orderOff[iRegion]-1]);
            iRegion+=1;
        } state off
        
        when (iRegion==2 && delay(REGIONDELAY*iRegion)) {
            sprintf(msg,"off:  R%d",orderOff[iRegion]);
            printf("seq_svtOnOff-All - %s\n",msg);
            pvPut(msg);
            btnOff[orderOff[iRegion]-1]=1;
            pvPut(btnOff[orderOff[iRegion]-1]);
            iRegion+=1;
        } state listen
    }
}



