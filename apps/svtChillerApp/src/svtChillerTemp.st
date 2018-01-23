program seqsvtChillerTemp

// N. Baltzell

// Set chiller temperature based on whether SVT is ON or OFF.
// Done in sequencer instead of records for future flexibility.

option -c;
option -r;

// update period (seconds): 
int delay=1;

int lvOnR1; assign lvOnR1 to "B_SVT_LV_R1:isOn";
int lvOnR2; assign lvOnR2 to "B_SVT_LV_R2:isOn";
int lvOnR3; assign lvOnR3 to "B_SVT_LV_R3:isOn";

float chillTemp;    assign chillTemp    to "B_SVT_CHILLER:GetSP00";
float chillSetTemp; assign chillSetTemp to "B_SVT_CHILLER:SetSP00";

float chillOnTemp;  assign chillOnTemp  to "B_SVT_CHILLER:onTemp";
float chillOffTemp; assign chillOffTemp to "B_SVT_CHILLER:offTemp";

string seqMessage; assign seqMessage to "B_SVT_CHILLER:seqMessage";
int seqStatus;     assign seqStatus  to "B_SVT_CHILLER:seqStatus";
int seqDisable;    assign seqDisable to "B_SVT_CHILLER:seqDisable";

%%#include "math.h"

ss seqsvtChillerTemp {

    state start
    {   
        when ()
        { 
            seqStatus=-1;
            pvPut(seqStatus);
            printf("** start state **************************\n");
            sprintf(seqMessage,"INIT - Assigning PVs");
            pvPut(seqMessage);
        } state init
    }

    state init
    {
        entry
        {
            seqStatus=-1;
            pvPut(seqStatus);
            printf("** init state ****************************\n");
        }
        when (pvConnectCount() < pvChannelCount())
        {
            seqStatus=-1;
            pvPut(seqStatus);
            printf("Waiting for PVs (%d/%d)\n",pvConnectCount(),pvChannelCount());
            sprintf(seqMessage,"ERROR - Waiting for PVs (%d/%d)",pvConnectCount(),pvChannelCount());
            pvPut(seqMessage);
            epicsThreadSleep(2);
        } state init
        when () {} state run
    }

    state run
    {
        entry
        {
            printf("** run state ****************************\n");
            sprintf(seqMessage,"OK - Running");
            pvPut(seqMessage);
        }

        when (pvConnectCount() < pvChannelCount()) {} state init

        when ()
        {
            seqStatus=0;
            sprintf(seqMessage,"Monitoring ...");
            pvPut(seqMessage);

            pvGet(seqDisable);
            pvGet(lvOnR1);
            pvGet(lvOnR2);
            pvGet(lvOnR3);
            pvGet(chillTemp);
            pvGet(chillOffTemp);
            pvGet(chillOnTemp);

            if (seqDisable==0) {
                if (lvOnR1 || lvOnR2 || lvOnR3) {
                    if (fabs(chillTemp-chillOnTemp)>0.1) {
                        seqStatus=1;
                        sprintf(seqMessage,"Setting Chiller Temp for SVT ON ...");
                        pvPut(seqMessage);
                        chillSetTemp = chillOnTemp;
                        pvPut(chillSetTemp);
                    }
                }
                else {
                    if (fabs(chillTemp-chillOffTemp)>0.1) {
                        seqStatus=1;
                        sprintf(seqMessage,"Setting Chiller Temp for SVT OFF ...");
                        pvPut(seqMessage);
                        chillSetTemp = chillOffTemp;
                        pvPut(chillSetTemp);
                    }
                }
            }

            pvPut(seqStatus);

            epicsThreadSleep(delay);

        } state run
    }

}


