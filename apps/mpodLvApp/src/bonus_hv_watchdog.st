program bonus_hv_watchdog

option -r;
option +s;

#define NCHAN 7

#define MESSAGE(MSG) \
    sprintf(msg,#MSG);\
    printf("seq: %s\n",msg);\
    pvPut(msg);

#define TMPMESSAGE(MSG) \
    sprintf(stmp,msg);\
    sprintf(msg,#MSG);\
    printf("seq: %s\n",msg);\
    pvPut(msg);\
    epicsThreadSleep(2);\
    sprintf(msg,stmp);\
    pvPut(msg);

string NAMES[NCHAN]={"GEM3_IN","GEM3_OUT","GEM2_IN","GEM2_OUT","GEM1_IN","GEM1_OUT","CATHODE"};

string msg; assign msg to "B_BONUS_HV:watchdog:msg";

int onbtn;  assign onbtn  to "B_BONUS_HV:onbtn";  monitor onbtn;
int offbtn; assign offbtn to "B_BONUS_HV:offbtn"; monitor offbtn;

int off;      assign off      to "B_BONUS_HV:off";
int allclear; assign allclear to "hvbonus2:clearEvent";

int isError; assign isError to "B_BONUS_HV:isError"; monitor isError;
int isOn;    assign isOn    to "B_BONUS_HV:isOn";    monitor isOn;
//int isOff;   assign isOff   to "B_BONUS_HV:isOff";   monitor isOff;

#define NINTLK 6
string intlkNames[NINTLK] = {"GEM1CAT","GEM12","GEM23","GEM1","GEM2","GEM3"};
int intlkReset[NINTLK]; assign intlkReset to {};

int dly[NCHAN];  assign dly to {};
int pw[NCHAN];   assign pw to {};

string stmp;
int changed,tmp,iseq,ii,jj;
int sequence[NCHAN]={0,1,2,3,4,5,6};

ss bonus_hv_watchdog {

    state start {
    
        entry {
            MESSAGE(Connecting ...);
            for (ii=0; ii<NCHAN; ii++) {
                sprintf(stmp,"B_BONUS_HV_%s:dly",NAMES[ii]);
                pvAssign(dly[ii],stmp);
                sprintf(stmp,"B_BONUS_HV_%s:outSwitch",NAMES[ii]);
                pvAssign(pw[ii],stmp);
            }
            for (jj=0; jj<NINTLK; jj++) {
                sprintf(stmp,"B_BONUS_INTLK_%s:dv:reset",intlkNames[jj]);
                printf(stmp);
                printf("\n");
                pvAssign(intlkReset[jj],stmp);
            }
        }

        when (pvConnectCount() < pvChannelCount()) {
            sprintf(msg,"Waiting for PVs (%d/%d)",pvConnectCount(),pvChannelCount());
            printf("%s\n",msg); pvPut(msg);
            epicsThreadSleep(1);
        } state start

        when (!pvArrayConnected(dly,NCHAN)) {
            MESSAGE(Waiting for delay PVs ...);
        } state start

        when (!pvArrayConnected(pw,NCHAN)) {
            MESSAGE(Waiting for power PVs ...);
        } state start

        when () {} state watch

    }

    state watch {
        entry { MESSAGE(Waiting for user input ...); }
        when (onbtn) {} state on
        when (offbtn) {} state off
        when (isError) {
            MESSAGE(HW ERROR - Offing);
            epicsThreadSleep(2);
        } state off
    }

    state off {
        entry {
            MESSAGE(Turning HV Off ...);
            offbtn=0;
            pvPut(offbtn);
            off=1;
            pvPut(off);
        }
        when(delay(2)) {} state watch
    }

    state on {

        // do not reset timer unless entering from a different state:
        option -t;

        entry {
            onbtn=0;
            pvPut(onbtn);
            offbtn=0;
            pvPut(offbtn);
            MESSAGE(Clearing All inhibits ...);
            allclear=10;
            pvPut(allclear);

            for (jj=0; jj<NINTLK; jj++) {
                printf("Resetting Interlock:  %s\n",intlkNames[jj]);
                intlkReset[jj]=0;
                pvPut(intlkReset[jj]);
            }
            offbtn=0;
            pvPut(offbtn);
            epicsThreadSleep(2);
            offbtn=0;
            pvPut(offbtn);

            MESSAGE(Sorting Delays ...);
            for (ii=0; ii<NCHAN; ii++) {
                pvGet(dly[ii]);
            }
            
            // bubble-sort indices by delay:
            while (1) {
                changed=0;
                for (ii=1; ii<NCHAN; ii++) {
                    if (dly[sequence[ii]]<dly[sequence[ii-1]]) {
                        tmp=sequence[ii-1];
                        sequence[ii-1]=sequence[ii];
                        sequence[ii]=tmp;
                        changed=1;
                        break;
                    }
                }
                if (changed==0) break;
            }
            for (ii=0; ii<NCHAN; ii++) {
                printf("%d ",dly[ii]);
            }
            printf("\n");
            for (ii=0; ii<NCHAN; ii++) {
                printf("%d:%d ",sequence[ii],dly[sequence[ii]]);
            }
            printf("\n");
            iseq=0;
            
            epicsThreadSleep(2);
        }
       
        when (offbtn) {} state off

        when (onbtn) {} state watch
      
        when (isError) {
            MESSAGE(HW ERROR - Aborting);
            epicsThreadSleep(1);
        } state off

        when (iseq>=NCHAN && isOn) {
            MESSAGE(Complete -  All channels ON);
            epicsThreadSleep(2);
        } state watch

        when (iseq>=NCHAN) {
            sprintf(msg,"Waiting for ramping ...");
            pvPut(msg);
        } state on

        when (delay(dly[sequence[iseq]]+2)) {
            sprintf(msg,"Powering #%d: %s",iseq+1,NAMES[sequence[iseq]]);
            printf("seq: %s\n",msg); pvPut(msg);
            pw[sequence[iseq]]=1;
            pvPut(pw[sequence[iseq]]);
            iseq++;
        } state on

    }

}

