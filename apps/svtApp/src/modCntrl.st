program modCntrl("MODULE=R1S1,LS=1,HS=7")
option -c;
option +r;

short lvon[2];
short lvoff[2];
assign lvon[0] to "{MODULE}T:PB_ON";
assign lvon[1] to "{MODULE}B:PB_ON";
assign lvoff[0] to "{MODULE}T:PB_OFF";
assign lvoff[1] to "{MODULE}B:PB_OFF";
monitor lvon;
monitor lvoff;
evflag ef_lvon;
sync lvon ef_lvon;
evflag ef_lvoff;
sync lvoff ef_lvoff;
short hvon[2];
short hvoff[2];
assign hvon[0] to "{MODULE}T:HVPB_ON";
assign hvon[1] to "{MODULE}B:HVPB_ON";
assign hvoff[0] to "{MODULE}T:HVPB_OFF";
assign hvoff[1] to "{MODULE}B:HVPB_OFF";
monitor hvon;
monitor hvoff;
evflag ef_hvon;
sync hvon ef_hvon;
evflag ef_hvoff;
sync hvoff ef_hvoff;

int HVONOFF[2];
assign HVONOFF[0] to "B_SVT_HV_{MODULE}T_Slot{HS}:outSwitch";
assign HVONOFF[1] to "B_SVT_HV_{MODULE}B_Slot{HS}:outSwitch";
int LV_VDONOFF[2];
assign LV_VDONOFF[0] to "B_SVT_LV_VD_{MODULE}T_Slot{LS}:onOff";
assign LV_VDONOFF[1] to "B_SVT_LV_VD_{MODULE}B_Slot{LS}:onOff";
int LV_VAONOFF[2];
assign LV_VAONOFF[0] to "B_SVT_LV_VA_{MODULE}T_Slot{LS}:onOff";
assign LV_VAONOFF[1] to "B_SVT_LV_VA_{MODULE}B_Slot{LS}:onOff";

int lvarb[2];
assign lvarb[0] to "B_SVT_LV_VA_{MODULE}T_Slot{LS}:outputStatuslong";
assign lvarb[1] to "B_SVT_LV_VA_{MODULE}B_Slot{LS}:outputStatuslong";
monitor lvarb;
int lvdrb[2];
assign lvdrb[0] to "B_SVT_LV_VD_{MODULE}T_Slot{LS}:outputStatuslong";
assign lvdrb[1] to "B_SVT_LV_VD_{MODULE}B_Slot{LS}:outputStatuslong";
monitor lvdrb;
double hvrb[2];
assign hvrb[0] to "B_SVT_HV_{MODULE}T_Slot{HS}:outputMeasSenseV";
assign hvrb[1] to "B_SVT_HV_{MODULE}B_Slot{HS}:outputMeasSenseV";
monitor hvrb;

int hvst[2];
assign hvst[0] to "B_SVT_HV_{MODULE}T_Slot{HS}:outswitchRlong";
assign hvst[1] to "B_SVT_HV_{MODULE}B_Slot{HS}:outswitchRlong";
monitor hvst;

int humAlarm;
assign humAlarm to "B_SVT_V450_Humidity_Master.SEVR";
monitor humAlarm;
int tmpAlarm;
assign tmpAlarm to "B_SVT_V450_Ambient_Master.SEVR";
monitor tmpAlarm;

string message[2];
assign message[0] to "{MODULE}T:MODSTAT";
assign message[1] to "{MODULE}B:MODSTAT";

#define LVON 0x80
#define HVOFF 0.10

%%#include <string.h>

int i;
int allhvoff;
int lvcmdoff[2];

ss modCntrl {
   state init {
/***********************************************************
 *  Init:                                                  *
 ***********************************************************/
    when(){
        efClear(ef_hvon);
        efClear(ef_lvon);
        efClear(ef_hvoff);
        efClear(ef_lvoff);
        for( i=0; i<2; i++ ) {
           strcpy( message[i], "             ");
           pvPut( message[i],SYNC );
           lvcmdoff[i]=0;
        }
       allhvoff = 0;
    } state wait4cmd
   }
/***********************************************************
 *  wait4cmd: wait for HVPB_ON/OFF or LVPB_ON/OFF          *
 ***********************************************************/
   state wait4cmd {
      when( efTestAndClear(ef_hvoff) ) {
        for( i=0; i<2; i++ ) {
           if( hvoff[i] > 0 ) {
              HVONOFF[i] = 0;
              pvPut(HVONOFF[i]);
              strcpy(message[i],"Turning HV off");
              pvPut(message[i]);
           }
        }
      } state wait4cmd

      when( humAlarm <= 1 && tmpAlarm <=1 && efTestAndClear(ef_lvon) ) {
        for(i=0;i<2;i++) {
         if( lvon[i] > 0 ) {
            LV_VAONOFF[i] = 1;
            pvPut(LV_VAONOFF[i]);
            LV_VDONOFF[i] = 1;
            pvPut(LV_VDONOFF[i]);
            strcpy(message[i],"Turning LV on");
            pvPut(message[i]);
         }
        }
      } state wait4cmd
      
      when( humAlarm <= 1 && tmpAlarm <=1 && efTestAndClear(ef_hvon) ) {
        for(i=0; i<2 ; i++){
         if( hvon[i] > 0 ) {
            if( ((lvarb[i] & LVON)>0) && ((lvdrb[i] & LVON)>0) ){
                HVONOFF[i] = 1;
                pvPut(HVONOFF[i]);
                strcpy(message[i],"Turning HV on");
                pvPut(message[i]);
             } else {
                strcpy(message[i],"LV must be on");
                pvPut(message[i]);
             }
          }
        }
      } state wait4cmd

      when( efTestAndClear(ef_lvoff) ) { 
            allhvoff=0;
            for(i=0;i<2;i++) if(hvst[i]==0)lvcmdoff[i] = lvoff[i];
      } state checkHvOff 
   }
/***********************************************************
 *  checkHvOff:  Hv must be off before we turn LV off      *
 ***********************************************************/
   state checkHvOff {
      when( delay(0.5) && (allhvoff == 0)){
        allhvoff = 1;  /* assume all off */
        for(i=0;i<2;i++){
           if( (lvcmdoff[i] > 0) && (hvrb[i] >= HVOFF) ){
             strcpy(message[i],"Waiting for HV off");
             pvPut(message[i]);
             allhvoff = 0;
           }
        }
      } state checkHvOff

      when(allhvoff) {
         allhvoff = 0; /* Reset for next time */
      } state turnLvOff
   }        
/***********************************************************
 *  turnLvOff:  Turn LV modules off                        *
 ***********************************************************/
   state turnLvOff {
      when( ) {
         for(i=0;i<2;i++){
           if( (lvcmdoff[i] > 0) && (hvrb[i] < HVOFF) && (hvst[i] == 0)) {
              printf("::lvoff %d, hvrb %f, hvst %ld\n",lvcmdoff[i],hvrb[i],hvst[i]);
              strcpy ( message[i], "Turn off LV" );
              pvPut(message[i]);
              printf("Turn off %d LV\n",i);
              LV_VDONOFF[i] = 0;
              pvPut(LV_VDONOFF[i]);
              LV_VAONOFF[i] = 0;
              pvPut(LV_VAONOFF[i]);
              lvcmdoff[i] = 0;
           }
         } 
      }state wait4cmd
   }
 }
