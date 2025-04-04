#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>
#include <vector>
#include "bom.h"

#include "richfpga_io.c"

//#undef JSCALER_DEBUG
//#define JSCALER_DEBUG

#define DGSPORTNO 6102
#define MAXNPORTS 10 // maximum number of ports to try before failure

using namespace std;
void *crateThread(void *);
int Dsc2ReadScalers(VmeChassis *ptr_c, map<int, JlabBoard *>::iterator &it, int &nchannels);
int Fadc250ReadScalers(VmeChassis *ptr_c, map<int, JlabBoard *>::iterator &it, int &nchannels);
int SSPReadScalers(VmeChassis *ptr_c, map<int, JlabBoard *>::iterator &it);
ScalersSlowControl::ScalersSlowControl(){}
map<int, VmeChassis*> *ScalersSlowControl::GetChassisMap(){ return &vmecrates; }

VmeChassis::VmeChassis(int id, string &hostname) : HOSTNAME(hostname){

	int n, val;
	sockfd_reg = open_socket(6102);
	/* Send endian test header */
	val = 0x12345678;
	write(sockfd_reg, &val, 4);
	val = 0;
	n = read(sockfd_reg, &val, 4);
	printf("n = %d, val = 0x%08X\n", n, val);

   
	rich_test_regs(400);
	rich_set_pulser(10000000.0, 0.5, 0xFFFFFFFF);					// freq, dutycycle, repetition (0= disable,0xffffffff = infinite)
	rich_write32(&pRICH_regs->MAROC_Cfg.DACAmplitude, 1000);

	// Setup FPGA version of MAROC OR (note: this OR is formed in the FPGA from the MAROC hits and does not use the MAROC_OR signal)
	rich_setmask_fpga_or(0x00000001, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000);

	rich_write32(&pRICH_regs->Sd.OutSrc[0], SD_SRC_SEL_PULSER_DLY0);			// output pulser to TTL outputs for probing/scope trigger
	rich_write32(&pRICH_regs->Sd.OutSrc[1], SD_SRC_SEL_PULSER_DLY1);
	rich_write32(&pRICH_regs->Sd.CTestSrc, 0);//SD_SRC_SEL_PULSER_DLY1_N);	// internal pulser fires test charge injection
	rich_write32(&pRICH_regs->Sd.PulserDelay, (0<<16) | (0<<8) | (0<<0));
	
	/* Set trig source to disabled */
	rich_write32(&pRICH_regs->Sd.TrigSrc, 0);
	rich_write32(&pRICH_regs->EvtBuilder.TrigDelay, 128);				//128*8ns = 1024ns trigger delay
	
	int hold_dly = 5;
	SetupMAROC_ADC(hold_dly, hold_dly, MAROC_ADC_RESOLUTION_12b, MAROC_MASK_3ASIC);

	/* Soft pulse sync */
	rich_write32(&pRICH_regs->Sd.SyncSrc, 1);
	rich_write32(&pRICH_regs->Sd.SyncSrc, 0);

	rich_fifo_reset();
	rich_fifo_status();
	rich_setup_readout(1200/8, 400/8);			// lookback 1.2us, capture 400ns
	
	rich_disable_all_tdc_channels();
	rich_enable_all_tdc_channels();
	
	/* Set trig source to pulser when ready to take events */
	rich_write32(&pRICH_regs->Sd.TrigSrc, SD_SRC_SEL_PULSER_DLY0);		// trigger source is pulser (delayed by TrigDelay)

    int thr = 300;
    rich_test_regs(thr);
  
    rich_write32(&pRICH_regs->MAROC_Cfg.DACAmplitude, 4095);
   


    pthread_mutex_init(&IOmutex, NULL);
    
    int rval;

    fprintf(stderr,"Making thread\n");
    rval = pthread_create(&threadC, NULL, crateThread, (void *) this );
    fprintf(stderr,"Made thread\n");
    if (rval != 0) {
        perror("Creating the Server Analysis Thread failed");
        exit(3);
    }
    fprintf(stderr,"Thread Created.\n");
/*
    while (1) {
        sleep(SCALERS_READ_INTERVAL);
        pthread_mutex_lock(&IOmutex);
        fprintf(stderr,"loop\n");
        printf("(((((((((((((((((((((((((((((((((((((((((((((((((((\n");
        rich_dump_scalers(bomScalers);
        pthread_mutex_unlock(&IOmutex);
    }
*/
}


///=========================================================================================================
int VmeChassis::GetNumberOfSlots() { return numberOfSlots; }
int VmeChassis::getPortFromDb(string &HOSTNAME) { return DGSPORTNO; }
map<int, JlabBoard*> *VmeChassis::GetBoardMap() { return &crateBoards; }

///=========================================================================================================
void *crateThread(void *ptr) {

    fprintf(stderr,"crateThread\n");

    VmeChassis *ptr_c=NULL;
    
    while (!ptr || !ptr_c) {
        sleep(1);
        ptr_c=(VmeChassis*)ptr;
    }

    fprintf(stderr,"got chassis\n");
        sleep(1);
    
    while (1) {
        sleep(SCALERS_READ_INTERVAL);
//        if (!(ptr_c->IOmutex)) continue;
        fprintf(stderr,"threadA\n");
        pthread_mutex_lock(&(ptr_c->IOmutex));
        fprintf(stderr,"thread\n");
        fprintf(stderr,"&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n");
        rich_dump_scalers(ptr_c->bomScalers);
        pthread_mutex_unlock(&(ptr_c->IOmutex));
    }
    return NULL;
}

///==================================================================================================================


int Fadc250ReadScalers(VmeChassis *ptr_c, map<int, JlabBoard *>::iterator &it, int &nchannels){
    int len=0;
    unsigned int *buf[1];
    int ret=0;
    (*buf)=0;
    /*
    if (strcmp(ptr_c->getHostname().c_str(),"ADCECAL1")==0) { 
        fprintf(stderr,"Fadc250ReadScalersA\n");
        if (!ptr_c->crateMsgClient) {
            fprintf(stderr,"Fadc250ReadScalers: found null pointer\n");
            return 0;
        }
        if (!(ptr_c->crateMsgClient->IsValid())) {
            fprintf(stderr,"Fadc250ReadScalers: found invalid\n");
            return 0;
        }
        if (!(ptr_c->crateMsgClient->CheckConnection("foo"))) {
            fprintf(stderr,"Fadc250ReadScalers: found bad conn\n");
            return 0;
        }
    }
    */
    // NABO:  THREAD CRASHES HERE IF DGS IS KILLED
    if (ptr_c && ptr_c->crateMsgClient && ptr_c->crateMsgClient->IsValid() && ptr_c->crateMsgClient->CheckConnection("foo"))
    ret = ptr_c->crateMsgClient->ReadScalers(it->first, buf, &len);
    /*
    if (strcmp(ptr_c->getHostname().c_str(),"ADCECAL1")==0) 
        fprintf(stderr,"Fadc250ReadScalersB\n");
    */
    (void)ret;
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
            it->second->scalerCounts[ii].clear();
            it->second->scalerCounts[ii].push_back((*buf)[ii]);
            it->second->scalerCountsHz[ii].clear();
            it->second->scalerCountsHz[ii].push_back((*buf)[ii]*ref);
        }
    }
    if (*buf) delete *buf;
    return 0;
}

int SSPReadScalers(VmeChassis *ptr_c, map<int, JlabBoard *>::iterator &it){
    int len=0,ret=0;
    unsigned int *buf[1];
    int thisLen,thisFiber,ii,jj,marocID,pixelID,pmtID,fiberPixelID;
    double hz,thisRef;

    JlabSSPBoard *ssp=NULL;
    if (dynamic_cast <JlabSSPBoard*> (it->second))
        ssp=(JlabSSPBoard*)it->second;
    else {
        printf("SSPReadScalers:  NOT an SSP board");
        return 0;
    }
    
    // clear fiber# vectors:
    ssp->scalerFibers.clear();
    ssp->dataFibers.clear();

    // initialize data vectors to error values:
    for (ii=0; ii<ssp->MAXFIBERS; ii++) {
        for (jj=0; jj<(int)ssp->scalerCounts[ii].size(); jj++)
            ssp->scalerCounts[ii][jj]=NOT_PRESENT_VALUE;
        for (jj=0; jj<(int)ssp->scalerCountsHz[ii].size(); jj++)
            ssp->scalerCountsHz[ii][jj]=NOT_PRESENT_VALUE;
        for (jj=0; jj<(int)ssp->SSPData[ii].size(); jj++)
            ssp->SSPData[ii][jj]=NOT_PRESENT_VALUE;
    }

    // read scalers:::::::::::::::::::::::::::::::::::::::::::
    (*buf)=0;
    ret = ptr_c->crateMsgClient->ReadScalers(it->first, buf, &len);
/*
    if (len > ssp->MAXSCALERLEN) {
        printf("SSPReadScalers:  Invalid Scaler Array length:%d\n",len);
        if (*buf) delete *buf;
        return 1; 
    }
*/
    ii=0;
    while (1) {
    
        if (ii>=len) break;
        
        // read header for this fiber:
        thisLen = (*buf)[ii];
        if (ii+thisLen > len) {
            printf("SSPReadScalers:  Invalid scaler lengths.\n");
            break;
        }
        
        // non-RICH SSP boards:
        if (thisLen==0) break;

        if (thisLen <= ssp->SCALERHEADEROFFSET) {
            printf("SSPReadScalers:  Bad Scaler length:  %d/%d\n",len,thisLen);
        }
        else {
            thisFiber = (*buf)[ii+1];
            thisRef = (*buf)[ii+2];
            if (thisFiber<0 || thisFiber>=ssp->MAXFIBERS)
                printf("SSPReadScalers:  Invalid Scaler Fiber #:  %d\n",thisFiber);
            else {
                // read scalers for this fiber:
                ssp->scalerFibers.push_back(thisFiber);
                
                // without maroc<->pixel remapping:
                //ssp->scalerCounts[thisFiber].clear();
                //ssp->scalerCountsHz[thisFiber].clear();

                // with maroc<->pixel remapping (FIXME):
                for (jj=ssp->scalerCounts[thisFiber].size(); jj<ssp->SCALERSPERFIBER; jj++)
                    ssp->scalerCounts[thisFiber].push_back(NOT_PRESENT_VALUE);
                for (jj=ssp->scalerCountsHz[thisFiber].size(); jj<ssp->SCALERSPERFIBER; jj++)
                    ssp->scalerCountsHz[thisFiber].push_back(NOT_PRESENT_VALUE);

                for (jj=ii+ssp->SCALERHEADEROFFSET; jj<ii+thisLen; jj++) {
                    hz=(*buf)[jj]*(ssp->CLOCKFREQ/thisRef);
                   
                    // without maroc<->pixel remapping:
                    //ssp->scalerCounts[thisFiber].push_back((*buf)[jj]);
                    //ssp->scalerCountsHz[thisFiber].push_back(hz);
                   
                    // with maroc<->pixel remapping:
                    pmtID = (jj-ii-ssp->SCALERHEADEROFFSET) / ssp->SCALERSPERPMT;
                    marocID = (jj-ii-ssp->SCALERHEADEROFFSET) % ssp->SCALERSPERPMT;
                    pixelID = ssp->Maroc2Pixel(marocID);
                    fiberPixelID = pixelID + pmtID * ssp->SCALERSPERPMT;
                    // sanity checks (maybe mathematically impossible to fail):
                    if (pmtID<0        || pmtID>=ssp->PMTSPERFIBER ||
                        marocID<0      || marocID>=ssp->SCALERSPERPMT ||
                        pixelID<0      || pixelID>=ssp->SCALERSPERPMT ||
                        fiberPixelID<0 || fiberPixelID>ssp->SCALERSPERFIBER) {
                        printf("SSPReadScalers:  Invalid Maroc\n");
                    }
                    else {
                        ssp->scalerCounts[thisFiber][fiberPixelID]=(*buf)[jj];
                        ssp->scalerCountsHz[thisFiber][fiberPixelID]=hz;
                    }
                    //printf("%d %d %d %d %f\n",len,thisLen,thisFiber,jj,hz);
                    //printf("%d %d %d %d ---- %d %d %d %d ---- %f\n",len,thisLen,thisFiber,jj,pmtID,marocID,pixelID,pixelID+pmtID*64,hz);
                }
            }
        }

        // move to next fiber:
        ii+=thisLen;
    }
    if (*buf) delete *buf;
    
    // read data::::::::::::::::::::::::::::::::::::::::::::::
    (*buf)=0;
    len=0;
    ret = ptr_c->crateMsgClient->ReadData(it->first, buf, &len);
/*
    if (len > ssp->MAXDATALEN) {
        printf("SSPReadScalers:  Invalid Scaler Array length:%d\n",len);
        if (*buf) delete *buf;
        return 1; 
    }
*/    
    ii=0;
    while (1) {
    
        if (ii>=len) break;

        // reader header for this fiber:
        thisLen = (*buf)[ii];
        if (ii+thisLen > len) {
            printf("SSPReadScalers:  Invalid scaler lengths.\n");
            break;
        }
        
        // non-RICH ssp boards:
        if (thisLen==0) break;

        if (thisLen != ssp->DATAPERFIBER+ssp->DATAHEADEROFFSET)
            printf("SSPReadScalers:  Odd Data length:  %d\n",thisLen);
        if (thisLen <= ssp->DATAHEADEROFFSET) {
            printf("SSPReadScalers:  Bad Data length:  %d\n",thisLen);
        }
        else {
            thisFiber = (*buf)[ii+1];
            thisRef = (*buf)[ii+2];
            if (thisFiber<0 || thisFiber>=ssp->MAXFIBERS)
                printf("SSPReadScalers:  Invalid Data Fiber #:  %d\n",thisFiber);
            else {
                // read data for this fiber:
                ssp->dataFibers.push_back(thisFiber);
                ssp->SSPData[thisFiber].clear();
                for (int jj=ii+ssp->DATAHEADEROFFSET; jj<ii+thisLen; jj++) {
                    ssp->SSPData[thisFiber].push_back((float)(*buf)[jj]);
//                    printf("%d %d %d %d %f\n",len,thisLen,thisFiber,jj,(float)(*buf)[jj]);
                }
            }
        }

        // move to next fiber:
        ii+=thisLen;
    }
    if (*buf) delete *buf;

/*
    // print warnings if # of fibers changed:
    if ((int)ssp->scalerFibers.size() != ssp->numberOfChannels) {
        printf("SSPReadScalers:  Number of Fibers Changed: %d -> %d\n",
                ssp->numberOfChannels,(int)ssp->scalerFibers.size());
        ssp->numberOfChannels = ssp->scalerFibers.size();
    }
    if ((int)ssp->dataFibers.size() != ssp->numOfSSPDataChannels) {
        printf("SSPReadScalers:  Number of Fibers Changed: %d -> %d\n",
                ssp->numOfSSPDataChannels,(int)ssp->dataFibers.size());
        ssp->numOfSSPDataChannels = ssp->dataFibers.size();
    }
*/

    (void)ret;
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

    if (ret <=0 ) printf("error in scaler reading\n");
    else{

        for(int i10=0;i10 < len; i10++){

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

                    int in11=0;
                    int inn=0;
                    for(int in10=0;in10< ((j/nchannels)+1);in10++ ) {
                        inn=0;
                        for(uint in=in11;in<SCALER_NUMBER_OF_SUBGROUPS;in++){
                            in11=in+1;
                            if(bit[in]==0)inn++;
                            else {break;}
                        }
                    }
                    for(int in=0;in<inn;in++)
                        ( it->second->scalerCounts[j10] ).push_back(NOT_PRESENT_VALUE);
                    ( it->second->scalerCounts[j10] ).push_back((*buf)[i10+1+j]);
                }

                uint ref_gr1=(*buf)[i10+scaler_len-ref_num+1];
                uint ref_gr2=(*buf)[i10+scaler_len-ref_num+2];
                uint ref_prescale=((*buf)[i10+scaler_len+1]) + 1; /* prescale reported starting from 0 */
#ifdef JSCALER_DEBUG
                printf("ref_prescale=%u, ref=%u %u\n",ref_prescale,ref_gr1,ref_gr2);
#endif
                uint ref;
                (it->second->scalerClocks).clear();
                (it->second->scalerClocks).push_back(ref_gr1);
                (it->second->scalerClocks).push_back(ref_gr2);
                for(int j10=0; j10< (it->second)->numberOfChannels; j10++){
                    for(uint j=0; j< SCALER_NUMBER_OF_SUBGROUPS-(it->second->scalerCounts[j10]).size(); j++){
                        ( it->second->scalerCounts[j10] ).push_back(NOT_PRESENT_VALUE);
                    }
                }

                for(int j10=0; j10< (it->second)->numberOfChannels; j10++){
                    (it->second->scalerCountsHz[j10] ).clear();
                    for(uint j=0; j< (it->second->scalerCounts[j10]).size(); j++){
                        ref = (ref_gr1 > ref_gr2) ? ref_gr1 : ref_gr2;
                        if(ref!=0 && (it->second->scalerCounts[j10])[j] >=0 )(it->second->scalerCountsHz[j10] ).push_back((it->second->scalerCounts[j10])[j] / (ref*ref_prescale/ScalerDsc2ClockFrequecy));
                        else (it->second->scalerCountsHz[j10] ).push_back(NOT_PRESENT_VALUE);
                    }
                }
                break;
            }
        }
    }
    if(*buf)delete *buf;
    return 0;
}

///==================================================================================================================

void JlabBoard::SetThresholds( int threshType, double threshold){ 
 for (int i=0; i<numberOfChannels; i++) SetThreshold( i, threshType, threshold );
}
void JlabBoard::SetThreshold(  int chanNumber, int threshType, double threshold  ){
    GenericSetBoard gsb;
    gsb.command=JLAB_SET_THRESHOLD;
    gsb.values.push_back(threshType); // type of threshold: low or high
    gsb.values.push_back(threshold); 
    gsb.channelNumber=chanNumber;
    genericSetBoards.push_back(gsb);

}

///==================================================================================================================

void JlabBoard::GetThresholds( int threshType, double thresholds[] ){ 
    double threshold;
    for(int i=0;i<numberOfChannels;i++){
        GetThreshold( i, threshType, threshold  );
        thresholds[i]=threshold;
    }
}
void JlabBoard::GetThreshold( int chanNumber, int threshType, double & threshold  ){
    const unsigned int nn=scalerThresholds[chanNumber].size();
    if (threshType < (int)nn) {
        if (boardType == SCALER_TYPE_DSC2 && nn==NUMBER_OF_SCALER_THRESHOLDS) {
            threshold=(scalerThresholds[chanNumber])[threshType];
        }
        else if (boardType == SCALER_TYPE_FADC250 && nn==1) {
            threshold=(scalerThresholds[chanNumber])[threshType];
        }
    }
}

///==================================================================================================================
/*
void JlabBoard::SetReadModes( double par[]){ 
    for (int i=0; i<numberOfChannels; i++) SetReadMode( i, par);
}
void JlabBoard::SetReadMode( const unsigned chanNumber, double par[]){
    GenericSetBoard gsb;
    gsb.command=JLAB_SET_READ_MODE;
    gsb.values.push_back(par[0]); /// read mode itself
    gsb.values.push_back(par[1]); /// additional parameter (interval ???)
    gsb.values.push_back(par[2]); /// additional parameter ???
    gsb.channelNumber=chanNumber; 
    genericSetBoards.push_back(gsb);
}

void JlabBoard::GetReadModes( double pars[]) { 
    for (int i=0; i<numberOfChannels; i++)
        GetReadMode(i, pars+i*MODE_PARS_NUMBER);
}
void JlabBoard::GetReadMode( const unsigned chanNumber, double par[]){

    if ( (scalerModes[chanNumber]).size() >= MODE_PARS_NUMBER) {
        for (int i=0; i<MODE_PARS_NUMBER; i++)
            par[i]=(scalerModes[chanNumber])[i];
    }
}

int JlabBoard::GetNumberOfChannels(){
 return numberOfChannels;
}
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

vector<double> *JlabBoard::GetScalerCounts
( int chanNumber, bool inHz ){ 
    if (inHz) return &(scalerCountsHz[chanNumber]);
    else      return &(scalerCounts[chanNumber]);
}

uint JlabBoard::GetClockCounts( int type ){  
    if      (type==SCALER_GROUP_1) return  scalerClocks[0];
    else if (type==SCALER_GROUP_2) return  scalerClocks[1];
    return -1;
}
///==================================================================================================================
*/


