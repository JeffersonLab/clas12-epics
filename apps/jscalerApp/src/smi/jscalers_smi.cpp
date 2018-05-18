/**

V.Sytnik 07/2014

*/
#ifdef USE_SMI

#include "jscalers.h"
#include "smiuirtl.hxx"

extern ScalersSlowControl *scalersslowcontrol;
///======================================================================================
//#ifdef __cplusplus
extern "C" {
//#endif
int ScalerBoardSmiMonitor( int is_init, char *epics_name,
unsigned int crate, unsigned int slot, unsigned int first_channel, unsigned int chs_number)
{

 string smi_command;
 string smi_obj_name;
 
// printf("===crate===%d %s\n",crate, epics_name);
if(scalersslowcontrol->vmecrates.count(crate)<=0) return 1;
pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));

 JlabBoard *sc = ((scalersslowcontrol->vmecrates[crate])->crateBoards[slot]); 
 if(!sc){pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));return 1;}

 if(is_init){
  sc->part_epics_names.push_back(epics_name);
 }


 if(sc->smi_state != sc->smi_state_prev || sc->smi_state_prev==SMI_STATE_UNDEFINED){
 //printf("1\n");
  if(sc->smi_state_prev==SMI_STATE_UNDEFINED)sc->smi_state=SMI_STATE_OFF; /// this should be removed if we get status (sc->smi_state) from hardware
  
  if((sc->smi_state_prev==SMI_STATE_UNDEFINED) || (sc->smi_state_prev==SMI_STATE_UNDEFINED_2)){
   /// sc->smi_state= reading status from hardware
  }
 
  if(sc->smi_state==SMI_STATE_ON)smi_command=("SET_ON");
  else if(sc->smi_state==SMI_STATE_OFF)smi_command=("SET_OFF");
  else if(sc->smi_state==SMI_STATE_ERROR)smi_command=("SET_ERROR");

  for(int i=0;i<sc->part_epics_names.size();i++){
  ///  smi_obj_name = string("CLAS12::")+string(epics_name);
     smi_obj_name=string("CLAS12::")+sc->part_epics_names[i];
  //char t1[100];
 // char t2[100]; 
//smiui_send_command(t1, t2);
// ccompiled_callto_
//printf("1 %s %s\n",smi_obj_name.c_str(),smi_command.c_str());
    smiui_send_command((char *) smi_obj_name.c_str(), (char *) smi_command.c_str());
  }

  
  sc->smi_state_prev=sc->smi_state;
 }

pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
 //((scalersslowcontrol.vmecrates[crate])->crateBoards[slot])->genericSetBoards.push_back(gsb);


 return 0;

}

//#ifdef __cplusplus
}
//#endif

///======================================================================================
int ScalerBoardSmiControl ///  my: smi
(char *smi_obj_name, unsigned int crate, unsigned int slot, 
unsigned int first_channel, unsigned int chs_number, unsigned int onoff){
if(scalersslowcontrol->vmecrates.count(crate)<=0) return 1;
 pthread_mutex_lock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));

 JlabBoard *sc = ((scalersslowcontrol->vmecrates[crate])->crateBoards[slot]); 
 if(!sc){pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));return 1;}

 //if(sc->smi_state != sc->smi_state_prev){
 
  if(onoff)sc->smi_state=SMI_STATE_ON;
  else sc->smi_state=SMI_STATE_OFF;

 //}

pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
 //((scalersslowcontrol.vmecrates[crate])->crateBoards[slot])->genericSetBoards.push_back(gsb);

 return 0;


}

///=======================================================================================

int ScalerCrateSmiInit ///  my: smi  my_n_smi
(char *smi_obj_name, unsigned int crate){
if(scalersslowcontrol->vmecrates.count(crate)<=0) return 1;
pthread_mutex_lock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));

 VmeChassis *vme=(scalersslowcontrol->vmecrates[crate]);
 if(!vme){pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));return 1;}

  for(int i=0;i< vme->numberOfSlots;i++){
    if(vme->crateBoards[i])(vme->crateBoards[i])->smi_state_prev=SMI_STATE_UNDEFINED_2;
  }

pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));

return 0;
}


///=======================================================================================

#else

void
jscalers_smi_dummy()
{
  return;
}

#endif
