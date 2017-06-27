
/**

V.Sytnik 07/2014

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>
#include <vector>
#include "jscalers.h"


#undef JSCALER_DEBUG
//#define JSCALER_DEBUG


using namespace std;
void *crateThread(void *);
int Dsc2ReadScalers(VmeChassis *ptr_c, map<int, JlabBoard *>::iterator &it, int &nchannels);
int Fadc250ReadScalers(VmeChassis *ptr_c, map<int, JlabBoard *>::iterator &it, int &nchannels);
///=========================================================================================================
ScalersSlowControl::ScalersSlowControl(){

}
///=========================================================================================================
map<int, VmeChassis*> *ScalersSlowControl::GetChassisMap(){

    return &vmecrates;

}
///=========================================================================================================
///=========================================================================================================
/// this constructor is called in the IOC init macro (one macro per crate)
/// then the chassis pbject is added in the vmecrates
///--------------------------------------------------------------------
//VmeChassis::VmeChassis(int id, string &hostname, int slots_number, int *board_types) : HOSTNAME(hostname){  /// id is to talk from record
VmeChassis::VmeChassis(int id, string &hostname) : HOSTNAME(hostname){  /// id is to talk from record

    int *board_types;
    int len=0;
    unsigned int *buf[1];
    int ret;

    //this->hostname=hostname;
    //IOmutex = PTHREAD_MUTEX_INITIALIZER;
    pthread_mutex_init(&IOmutex, NULL);

    is_crate_read=0;
    port=getPortFromDb(HOSTNAME);
    printf("1==  %s %d \n", HOSTNAME.c_str(), port);
    numberOfSlots=0;

    crateMsgClient= new CrateMsgClient((const char*) HOSTNAME.c_str(), port);
#ifndef SIMULATION 

    if(crateMsgClient->IsValid())
    {
        printf("Connected %p\n",crateMsgClient);
    }
    else
    {
        printf("NOT CONNECTED - RETURN\n");
        return; 
    }
#endif


    (*buf)=0;
    ret = crateMsgClient->GetCrateMap(buf, &len);
    printf("boards len=%d\n",len);
    if(ret){
        for(int ii=0; ii<len; ii++) printf("slot %2d, boardID 0x%08x\n",ii,(*buf)[ii]);
        board_types=(int *) (*buf);
        numberOfSlots=len;

        /*
           if(slots_number==0){

        // slots_number=getBoards(board_types);  /// talks to hardware to get array of board_types of slots_number length (hall d)
        int ret = crateMsgClient->GetCrateMap(buf, &len);
        printf("boards len=%d\n",len);
        //for(int ii=0; ii<len; ii++) printf("slot %2d, boardID 0x%08x\n",ii,(*buf)[ii]);

        }
        */

        for(int i=0;i< numberOfSlots;i++){
            //printf("boards slot=%d\n",i);
            if(board_types[i]==SCALER_TYPE_DSC2)crateBoards[i]= (new JlabDisc2Board(crateMsgClient, i, board_types[i] ));
            else if(board_types[i]==SCALER_TYPE_FADC250)crateBoards[i]=(new JlabFadc250Board(crateMsgClient, i, board_types[i] ));
            else if(board_types[i]==JLAB_SLOT_IS_EMPTY )crateBoards[i]=0;
            else {printf("unknown board!\n");exit(1);} /// 

        }
    }
    if(*buf)delete (*buf);

    int rval = pthread_create(&threadC, NULL, crateThread, (void *) this );
    if (rval != 0) {
        perror("Creating the Server Analysis Thread failed");
        exit(3);
    }

    //delete (*buf);

}
///=========================================================================================================
int VmeChassis::GetNumberOfSlots(){

 return numberOfSlots;

}

///=========================================================================================================

int VmeChassis::getPortFromDb(string &HOSTNAME){ /// get port fron db

 int port=6102;

 return port;

}

///=========================================================================================================
///=========================================================================================================
///=========================================================================================================

int JlabBoard::GetNumberOfChannels(){

 return numberOfChannels;


}
///=========================================================================================================

map<int, JlabBoard*> *VmeChassis::GetBoardMap(){

 return &crateBoards;

}

///=========================================================================================================
void *crateThread(void *ptr) {

    VmeChassis *ptr_c=(VmeChassis *)ptr;

    int len=0;
    unsigned int *buf[1];
    int partype;

#ifdef JSCALER_DEBUG
    unsigned int niter=0;
#endif

    while(1){

#ifdef JSCALER_DEBUG
        fprintf(stderr,"CrateThreadBegin %d\n",niter);
#endif

        sleep(SCALERS_READ_INTERVAL);
        //usleep(100000);
        //fprintf(stderr,"CrateThreadBegin1 %d\n",niter);
        pthread_mutex_lock(&(ptr_c->IOmutex));
        //fprintf(stderr,"CrateThreadBegin2 %d\n",niter);
        int ret=0;
        ///----------------------------- read part--------------------------------------

        for( map<int, JlabBoard *>::iterator it=ptr_c->crateBoards.begin() ; it!= ptr_c->crateBoards.end();  ++it){

            //printf("%d addr=%p\n",it->first,it->second);
            if(!(it->second))continue;
            int nchannels = (it->second)->numberOfChannels;

            ///----------------------------------------------------------

            if((it->second)->boardType==SCALER_TYPE_DSC2){
#ifdef JSCALER_DEBUG
                fprintf(stderr,"ioc:Dsc2ReadScalersA\n");
#endif
                Dsc2ReadScalers(ptr_c, it, nchannels);
#ifdef JSCALER_DEBUG
                fprintf(stderr,"ioc:Dsc2ReadScalersB\n");
#endif
            }

            else if((it->second)->boardType==SCALER_TYPE_FADC250){
#ifdef JSCALER_DEBUG
                fprintf(stderr,"ioc:Fadc250ReadScalerA\n");
#endif
                Fadc250ReadScalers(ptr_c, it, nchannels);
#ifdef JSCALER_DEBUG
                fprintf(stderr,"ioc:Fadc250ReadScalerB\n");
#endif
            }

            ///-------------------  thresholds ------------------------------------

            for(int i=0;i<it->second->numberOfChannels;i++){ 
                it->second->scalerThresholds[i].clear();
            }

            (*buf)=0;
            partype = SCALER_PARTYPE_THRESHOLD;
            //printf("ioc:GetBoardParams\n");
            ret = ptr_c->crateMsgClient->GetBoardParams(it->first, partype, buf, &len);
/*
            if ((it->second)->boardType==SCALER_TYPE_DSC2)
                printf("DSC2 Read Thresholdsd:  ");
            else if ((it->second)->boardType==SCALER_TYPE_FADC250)
                printf("FADC Read Thresholdsd:  ");
            else
                printf("???? Read Thresholdsd:  ");
            if (ret) for (int i=0; i<len; i++) printf(" %d",(*buf)[i]); printf("\n");
*/
            //printf("ioc:GetBoardParams2\n");
            if(ret)
                for(int i=0;i<len;i++){ /// len is number of channels
                    ( it->second->scalerThresholds[i] ).push_back((*buf)[i]);
                }
            if(*buf)delete *buf;
            (*buf)=0;
            partype = SCALER_PARTYPE_THRESHOLD2;
            //printf("ioc:GetBoardParams_2\n");
            ret = ptr_c->crateMsgClient->GetBoardParams(it->first, partype, buf, &len);
            //printf("ioc:GetBoardParams_22\n");
            if(ret)
                for(int i=0;i<len;i++){ /// len is number of channels
                    ( it->second->scalerThresholds[i] ).push_back((*buf)[i]);
                }
            if(*buf)delete *buf;


#ifdef JSCALER_DEBUG 
            for(int i=0;i<it->second->numberOfChannels;i++){  
                int size1=( it->second->scalerThresholds[i] ).size();
                for(int i8=0;i8<size1;i8++){
                    printf("slot=%d size=%d  =%f \n", it->first, size1, ( it->second->scalerThresholds[i] )[i8]);
                }
            }
#endif
            ///----------------------------------------------------------

        } // for( map<int, JlabBoard *>::iterator it=ptr_c->crateBoards.begin() ; it!= ptr_c->crateBoards.end();  ++it)

        ///-----------------------------------------------------------------------------
        ///-------------------------- request part -----------------------------------------

        unsigned int buffer[100];
        for( map<int, JlabBoard *>::iterator it=ptr_c->crateBoards.begin() ; it!= ptr_c->crateBoards.end();  ++it){
            if(!(it->second))continue;

            for(unsigned int j=0;j<(it->second)->genericSetBoards.size();j++){

                if((it->second)->genericSetBoards[j].command==JLAB_SET_THRESHOLD){
                    (*buf)=0;
                    len=1;

                    partype = (int) ((it->second)->genericSetBoards[j].values[0]);

                    buffer[0]=(uint)(it->second)->genericSetBoards[j].values[1];

#ifdef JSCALER_DEBUG
                    printf("QWERasdf partype=%d buffer[0]=%d \n",partype,buffer[0]);
#endif

                    ret = ptr_c->crateMsgClient->SetChannelParams((it->second)->slotNumber, (it->second)->genericSetBoards[j].channelNumber,
                            partype, buffer, len );
                    if(ret <=0 ){
                        printf("error in thresh set\n");
                    }
                    if(*buf)delete *buf;
                }
                else if((it->second)->genericSetBoards[j].command==JLAB_SET_READ_MODE){




                }
                (it->second)->genericSetBoards[j].values.clear();

            } // for j

            (it->second)->genericSetBoards.clear();

        } // for i

        ///-----------------------------------------------------------------------------
        pthread_mutex_unlock(&(ptr_c->IOmutex));

        ptr_c->is_crate_read=1;

#ifdef JSCALER_DEBUG
        fprintf(stderr,"CrateThreadEnd %d\n",niter++);
#endif

    } // while

    return NULL;
}

///==================================================================================================================


int Fadc250ReadScalers(VmeChassis *ptr_c, map<int, JlabBoard *>::iterator &it, int &nchannels){
    int len=0;
    unsigned int *buf[1];
    int ret=0;

    (*buf)=0;
    ret = ptr_c->crateMsgClient->ReadScalers(it->first, buf, &len);
    (void)ret;

    //printf("\n\n**************************AAA BoardType = %d\n",(it->second)->boardType);
    //printf("222 slot=%d msgclient_addr=%p buf_addr=%p len=%d\n",it->first,ptr_c->crateMsgClient, &buf, len);

    if (len!=17) {
        printf("Fadc250ReadScalers:  odd length:  %d.\n",len);
    }
    else if ((*buf)[16]<=0) {
        printf("Fadc250ReadScalers:  odd normalization:  %d\n",(*buf)[16]);
    }
    else {
        static const double ref1=488281.25f;
        static const double ref2=1;
        const double ref=ref1/(*buf)[16]/ref2;
        for (int ii=0; ii<len-1; ii++)
        {
            //printf("A%d = %d\n",ii,(*buf)[ii]);
            //printf("BBBB = %d %d\n",ii,it->second->scalerCounts[ii].size());
            it->second->scalerCounts[ii].clear();
            it->second->scalerCounts[ii].push_back((*buf)[ii]);
            it->second->scalerCountsHz[ii].clear();
            it->second->scalerCountsHz[ii].push_back((*buf)[ii]*ref);
            //printf("CCCC = %.2f\n",it->second->scalerCounts[ii][0]);
        }
    }
    if(*buf)delete *buf;
    return 0;
}

int Dsc2ReadScalers(VmeChassis *ptr_c, map<int, JlabBoard *>::iterator &it, int &nchannels){

    int len=0;
    unsigned int *buf[1];
    int ret=0;

    (*buf)=0;
    ret = ptr_c->crateMsgClient->ReadScalers(it->first, buf, &len);
#ifdef JSCALER_DEBUG
    printf("\n\n**************************AAA BoardType = %d\n",(it->second)->boardType);
    printf("111  slot=%d  msgclient_addr=%p buf_addr=%p len=%d\n",it->first, ptr_c->crateMsgClient, &buf,len);
#endif
    ///  printf("len=%d\n",len);

#ifndef SIMULATION
    if(ret <=0 ){
        printf("error in scaler reading\n");
    }
    else{
#endif

        //printf("len=%d\n", len);
        for(int i10=0;i10 < len; i10++){ /// ???

            /*sergey: fixed in DiagServer   (*buf)[i10]=SCALERS_LSWAP((*buf)[i10]); */

            int type=(*buf)[i10] >> 31;
            int bit[8];
            type=(((*buf)[i10]) >> 27) & 0x0f;
#ifdef JSCALER_DEBUG
            printf("word type=%d %u\n",type,*buf[0]);
#endif

            if(type==4){ /// scaler header
                int scaler_len= ((*buf)[i10]) & 0x0ff; 
                //(it->second)->numberOfChannels;

                int flags=(((*buf)[i10]) & 0x0ff00) >> 8;
                bit[0]=flags & 0x1 >> 0;
                bit[1]=flags & 0x2 >> 1;
                bit[2]=flags & 0x4 >> 2;
                bit[3]=flags & 0x8 >> 3;
                bit[4]=flags & 0x10 >> 4;
                bit[5]=flags & 0x20 >> 5;
                int ref_num= bit[4]+bit[5];

                //   int received_ngroups=0;
                //   for(int j=0;j<SCALER_NUMBER_OF_SUBGROUPS;j++){
                //    received_ngroups+=bit[j];
                //   }

#ifdef JSCALER_DEBUG
                printf("scaler_len%d\n",scaler_len);
#endif
                for(int j=0; j< (scaler_len-ref_num); j++){
                    int j10=j%nchannels; /// channel number in the group
                    if(!(j/nchannels))
                    {
                        it->second->scalerCounts[j10].clear();
                        it->second->scalerCountsHz[j10].clear();
                    }
                    //double d=(double)(*buf)[i10];
                    // printf("j=%d i10=%d 0x%08x\n",j,i10, (*buf)[i10]);

                    int in11=0;
                    int inn=0;
                    for(int in10=0;in10< ((j/nchannels)+1);in10++ ) {
                        inn=0;
                        for(uint in=in11;in<SCALER_NUMBER_OF_SUBGROUPS;in++){
                            //if(bit[in]==0 && ( it->second->scalerCounts[j10] ).size() <= ( (j%16)+1)  ){
                            in11=in+1;
                            if(bit[in]==0)inn++;
                            else {break;}
                        }
                    }
                    for(int in=0;in<inn;in++){
                        ( it->second->scalerCounts[j10] ).push_back(NOT_PRESENT_VALUE);
                    }

                    ( it->second->scalerCounts[j10] ).push_back((*buf)[i10+1+j]);

                        //     if(((j/16)+1)==received_ngroups)
                        //     for(uint in=0;in<SCALER_NUMBER_OF_SUBGROUPS-received_ngroups;in++){
                        //      ( it->second->scalerCounts[j10] ).push_back(-1);
                        //     }      

                } // for j

                uint ref_gr1=(*buf)[i10+scaler_len-ref_num+1];
                uint ref_gr2=(*buf)[i10+scaler_len-ref_num+2];
                uint ref_prescale=((*buf)[i10+scaler_len+1]) + 1; /* prescale reported starting from 0 */
#ifdef JSCALER_DEBUG
                printf("ref_prescale=%u, ref=%u %u\n",ref_prescale,ref_gr1,ref_gr2);
#endif
                //ref_prescale=1;
                uint ref;
                (it->second->scalerClocks).clear();
                (it->second->scalerClocks).push_back(ref_gr1);
                (it->second->scalerClocks).push_back(ref_gr2);
                //    printf("%08x %08x %d\n",ref_gr1,ref_gr2, i10+scaler_len+1);
                for(int j10=0; j10< (it->second)->numberOfChannels; j10++){
                    //     printf("=== %d %d\n",j10, (it->second->scalerCounts[j10]).size());
                    for(uint j=0; j< SCALER_NUMBER_OF_SUBGROUPS-(it->second->scalerCounts[j10]).size(); j++){
                        ( it->second->scalerCounts[j10] ).push_back(NOT_PRESENT_VALUE);
                        //             printf("%d %08x\n",j, (it->second->scalerCounts[j10] )[j]);
                    }
                }

                for(int j10=0; j10< (it->second)->numberOfChannels; j10++){
                    //     printf("=== %d %d\n",j10, (it->second->scalerCounts[j10]).size());
                    (it->second->scalerCountsHz[j10] ).clear();
                    for(uint j=0; j< (it->second->scalerCounts[j10]).size(); j++){

                        /*sergey: always use ungated(biggest0 reference for normalization
                          if(j < 2)ref=ref_gr1;
                          else ref=ref_gr2;
                          */
                        ref = (ref_gr1 > ref_gr2) ? ref_gr1 : ref_gr2;


                        //int count_int=(int)(it->second->scalerCounts[j10])[j];
                        if(ref!=0 && (it->second->scalerCounts[j10])[j] >=0 )(it->second->scalerCountsHz[j10] ).push_back((it->second->scalerCounts[j10])[j] / (ref*ref_prescale/ScalerDsc2ClockFrequecy));
                        else (it->second->scalerCountsHz[j10] ).push_back(NOT_PRESENT_VALUE);

                        //            printf("%d %08x\n",j, (it->second->scalerCounts[j10] )[j]);

                    }
                }

                break;
            }
        } // for(int i10=0;i10 < len; i10++)
    } // else i.e. ret>0


    if(*buf)delete *buf;

    return 0;
}
///==================================================================================================================

//int command; /// e.g. setthresholds, set_some_mode_for_channel
//vector<double> values; /// value to set
//int channelNumber;
///==================================================================================================================

// Set thresholds for particlular type of thresholds for all channels
// type range: SCALER_PARTYPE_THRESHOLD (), SCALER_PARTYPE_THRESHOLD2()
void JlabBoard::SetThresholds( int threshType, double threshold){ 

 for(int i=0;i<numberOfChannels;i++){
   SetThreshold( i, threshType, threshold  );
 }

}

///==================================================================================================================

// Set thresholds for particular type of threshold for a single channel
// type range: SCALER_PARTYPE_THRESHOLD (), SCALER_PARTYPE_THRESHOLD2()
void JlabBoard::SetThreshold(  int chanNumber, int threshType, double threshold  ){
    GenericSetBoard gsb;
    gsb.command=JLAB_SET_THRESHOLD;
    gsb.values.push_back(threshType); // type of threshold: low or high
    gsb.values.push_back(threshold); 
    gsb.channelNumber=chanNumber;
    genericSetBoards.push_back(gsb);

}
///==================================================================================================================

void JlabBoard::SetReadModes( double par[]){ 

    for(int i=0;i<numberOfChannels;i++){
        SetReadMode( i, par);
    }

}

///==================================================================================================================

void JlabBoard::SetReadMode( const unsigned chanNumber, double par[]){
    GenericSetBoard gsb;
    gsb.command=JLAB_SET_READ_MODE;
    gsb.values.push_back(par[0]); /// read mode itself
    gsb.values.push_back(par[1]); /// additional parameter (interval ???)
    gsb.values.push_back(par[2]); /// additional parameter ???
    gsb.channelNumber=chanNumber; 
    genericSetBoards.push_back(gsb);
}

///==================================================================================================================
///==================================================================================================================

// Get thresholds of particlular type of thresholds for all channels
// type range: SCALER_PARTYPE_THRESHOLD (), SCALER_PARTYPE_THRESHOLD2()
void JlabBoard::GetThresholds( int threshType, double thresholds[] ){ 

    double threshold;
    for(int i=0;i<numberOfChannels;i++){
        GetThreshold( i, threshType, threshold  );
        thresholds[i]=threshold;
    }

}

///==================================================================================================================

// Get threshold of particular type of threshold for a single channel
// type range: SCALER_PARTYPE_THRESHOLD (), SCALER_PARTYPE_THRESHOLD2()
void JlabBoard::GetThreshold(  int chanNumber, int threshType, double & threshold  ){

    const unsigned int nn=scalerThresholds[chanNumber].size();

    if (threshType < (int)nn) {
        if (boardType == SCALER_TYPE_DSC2 && nn==NUMBER_OF_SCALER_THRESHOLDS) {
            threshold=(scalerThresholds[chanNumber])[threshType];
        }
        else if (boardType == SCALER_TYPE_FADC250 && nn==1) {
            threshold=(scalerThresholds[chanNumber])[threshType];
        }
    }
/*
    //printf("%d %d %f \n",chanNumber,threshType,(scalerThresholds[chanNumber])[threshType]); 
    if((int)(scalerThresholds[chanNumber]).size() == NUMBER_OF_SCALER_THRESHOLDS){
        threshold=(scalerThresholds[chanNumber])[threshType];
    }
*/

}
///==================================================================================================================

void JlabBoard::GetReadModes( double pars[]){ 
    for(int i=0;i<numberOfChannels;i++){
        GetReadMode(i, pars+i*MODE_PARS_NUMBER);
    } 


}

///==================================================================================================================

void JlabBoard::GetReadMode( const unsigned chanNumber, double par[]){

    if( (scalerModes[chanNumber]).size() >= MODE_PARS_NUMBER){
        for(int i=0;i<MODE_PARS_NUMBER;i++){
            par[i]=(scalerModes[chanNumber])[i];
        }
    }
}

///==================================================================================================================
// type range: ScalerThreshTrig_Gr1, ScalerThreshTDC_Gr1, ScalerThreshTrig_Gr2, ScalerThreshTDC_Gr2
double JlabBoard::GetScalerCount
( int chanNumber, int type, bool inHz ){ 

    double ret;
    if(scalerCountsHz[chanNumber].size()<SCALER_NUMBER_OF_SUBGROUPS)ret=-1;
    if(inHz){
        if(type==ScalerThreshTrig_Gr1){
            ret=scalerCountsHz[chanNumber][0];
        }
        else if(type==ScalerThreshTrig_Gr1){
            ret=scalerCountsHz[chanNumber][1];  
        }
        if(type==ScalerThreshTrig_Gr2){
            ret=scalerCountsHz[chanNumber][2];
        }
        else if(type==ScalerThreshTrig_Gr2){
            ret=scalerCountsHz[chanNumber][3]; 
        }
        else ret=-1;
    }
    else{
        if(type==ScalerThreshTrig_Gr1){
            ret=scalerCounts[chanNumber][0];
        }
        else if(type==ScalerThreshTrig_Gr1){
            ret=scalerCounts[chanNumber][1];  
        }
        if(type==ScalerThreshTrig_Gr2){
            ret=scalerCounts[chanNumber][2];
        }
        else if(type==ScalerThreshTrig_Gr2){
            ret=scalerCounts[chanNumber][3]; 
        }
        else ret=-1;
    }

    return ret;

}
///==================================================================================================================
// type range: ScalerThreshTrig_Gr1, ScalerThreshTDC_Gr1, ScalerThreshTrig_Gr2, ScalerThreshTDC_Gr2
vector<double> *JlabBoard::GetScalerCounts
( int chanNumber, bool inHz ){ 

    if(inHz){
        return &(scalerCountsHz[chanNumber]);
    }
    else{
        return &(scalerCounts[chanNumber]);
    }
}

///==================================================================================================================
// type range: SCALER_PARTYPE_THRESHOLD, SCALER_PARTYPE_THRESHOLD2
uint JlabBoard::GetClockCounts( int type ){  

    if(type==SCALER_GROUP_1){
        return  scalerClocks[0];
    }
    else  if(type==SCALER_GROUP_2){
        return  scalerClocks[1];
    }

    return -1;

}
///==================================================================================================================



