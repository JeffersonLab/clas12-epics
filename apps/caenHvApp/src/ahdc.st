program ahdc

option -c;
option -r;

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

float bpm;
float fcup;
float bpms[60]; assign bpms to "ahdc:seq:bpm";
float fcups[60]; assign fcups to "ahdc:seq:fcup";
float threshold; assign threshold to "ahdc:seq:thresh";

float stat[27]; assign stat to {};
float vmon[27]; assign vmon to {};
float vset[27]; assign vset to {};
float vsetrbk[27]; assign vsetrbk to {};

int depth=0;
int dwell; assign dwell to "ahdc:seq:dwell";
float vhi; assign vhi to "ahdc:seq:vhi";
float vlo; assign vlo to "ahdc:seq:vlo";
int status; assign status to "ahdc:seq:stat";
string enable; assign enable to "ahdc:seq:enable";
string msg; assign msg to "ahdc:seq:msg";

int i,j;
string stmp;

ss ahdc {

    state start {

        when () {
            MESSAGE(Assigning PVs ...);
            for (i=0; i<9; ++i) {
                for (j=0; j<3; ++j) {
                    sprintf(stmp,"B_DET_AHDC_HV_S%d-%d:stat",i+1,j+1);
                    pvAssign(stat[3*i+j],stmp);
                    sprintf(stmp,"B_DET_AHDC_HV_S%d-%d:vmon",i+1,j+1);
                    pvAssign(vmon[3*i+j],stmp);
                    sprintf(stmp,"B_DET_AHDC_HV_S%d-%d:vset",i+1,j+1);
                    pvAssign(vset[3*i+j],stmp);
                    sprintf(stmp,"B_DET_AHDC_HV_S%d-%d:vsetrbk",i+1,j+1);
                    pvAssign(vsetrbk[3*i+j],stmp);
                }
            }
        } state init
    }

    state init {

        when (pvConnectCount() < pvChannelCount()) {
            sprintf(msg,"Waiting for PVs (%d/%d)",pvConnectCount(),pvChannelCount());
            printf("%s\n",msg);
            pvPut(msg);
            status=1;
            pvPut(status);
            epicsThreadSleep(2);
        } state init
        
        when () {
            status=0;
            pvPut(status);
            MESSAGE(Running ...);
        } state acquire
    }

    state acquire {

        when (pvConnectCount() < pvChannelCount()) {} state init

        when () {
            pvGet(bpms);
            pvGet(fcups);
            for (i=0; i<27; ++i) {
                pvGet(stat[i]);
                pvGet(vmon[i]);
                pvGet(vset[i]);
                pvGet(vsetrbk[i]);
            }
            pvGet(threshold);
            pvGet(dwell);
            pvGet(vlo);
            pvGet(vhi);
        } state analyze
    }

    state analyze {
        entry {
            fcup,bpm = 999,999
            for (i=0; i<dwell; ++i) {
                bmp = min(bpms[i],bpm)
                fcup = min(fcups[i],fcup)
            }
        }
        when (bpm < threshold  && fcup <  threshold) { } state low
        when (bpm >= threshold || fcup >= threshold) { } state high
    }

    state high {
        when (pvConnectCount() < pvChannelCount()) {} state init
        when () {
            for (i=0; i<27; ++i) {
                vset[i] = vhi;
                pvPut(vset[i]);
            }
        } state fix
    }

    state low {
        when (pvConnectCount() < pvChannelCount()) {} state init
        when () {
            for (i=0; i<27; ++i) {
                vset[i] = vlo;
                pvPut(vset[i]);
            }
        } state fix
    }

    state fix {
        when (pvConnectCount() < pvChannelCount()) {} state init
        when () {
            for (i=0; i<27; ++i) {
                if (vsetrbk[i] != vset[i]) {
                    vset[i] = vsetrbk[i];
                    pvPut(vset[i]);
                }
            }
        } state acquire
    }

}

