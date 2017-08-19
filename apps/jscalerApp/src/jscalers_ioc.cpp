
#include "jscalers.h"

ScalersSlowControl *scalersslowcontrol;

#ifdef __cplusplus
extern "C" {
#endif

    int IocSetValue(int crate, int slot, int channel, int command, double values[]){
        if(scalersslowcontrol->vmecrates.count(crate)<=0) return 1;
        pthread_mutex_lock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));

        JlabBoard *sc = ((scalersslowcontrol->vmecrates[crate])->crateBoards[slot]); 
        if (!sc) {
            pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
            return 1;
        }

        if (command==JLAB_SET_THRESHOLD) {
            if (dynamic_cast<JlabDisc2Board *>(sc))
                ( (JlabDisc2Board *) ((scalersslowcontrol->vmecrates[crate])->crateBoards[slot]) )->SetThreshold(channel, (int)values[0],(int) values[1]);
            else if (dynamic_cast<JlabFadc250Board *>(sc))
                ( (JlabDisc2Board *) ((scalersslowcontrol->vmecrates[crate])->crateBoards[slot]) )->SetThreshold(channel, (int)values[0],(int) values[1]);
        }
        //else if (command==JLAB_SET_READ_MODE) {
        //    if (dynamic_cast<JlabDisc2Board *>(sc))
        //        ((JlabDisc2Board *) ((scalersslowcontrol->vmecrates[crate])->crateBoards[slot]))->SetReadMode(channel, values);
        //}
        pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
        return 0;
    }

#ifdef __cplusplus
}
#endif

#ifdef __cplusplus
extern "C" {
#endif

    int IocGetValue(int crate, int slot, int channel, int command, double values[]){
        if (scalersslowcontrol->vmecrates.count(crate)<=0) return 1;
        pthread_mutex_lock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));

        JlabBoard *sc = ((scalersslowcontrol->vmecrates[crate])->crateBoards[slot]); 
        if (!sc) {
            pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
            return 1;
        }

        if (command==JLAB_SET_THRESHOLD) {
            if (dynamic_cast<JlabDisc2Board *>(sc)) {
                ( (JlabDisc2Board *) ((scalersslowcontrol->vmecrates[crate])->crateBoards[slot]) )->GetThreshold(channel,SCALER_PARTYPE_THRESHOLD, values[0]);
                ( (JlabDisc2Board *) ((scalersslowcontrol->vmecrates[crate])->crateBoards[slot]) )->GetThreshold(channel,SCALER_PARTYPE_THRESHOLD2, values[1]);
            }
            else if (dynamic_cast<JlabFadc250Board *>(sc))
                ( (JlabFadc250Board *) ((scalersslowcontrol->vmecrates[crate])->crateBoards[slot]) )->GetThreshold(channel,SCALER_PARTYPE_THRESHOLD, values[0]);
        }
        //else if (command==JLAB_SET_READ_MODE) {
        //    if (dynamic_cast<JlabDisc2Board *>(sc))
        //        ((JlabDisc2Board *) ((scalersslowcontrol->vmecrates[crate])->crateBoards[slot]))->GetReadMode(channel,values);
        //}
        else if (command==JLAB_GET_NFIBERS) {
            if (dynamic_cast<JlabSSPBoard *>(sc)) {
                values[0]=((JlabSSPBoard *) ((scalersslowcontrol->vmecrates[crate])->crateBoards[slot]))->scalerFibers.size();
                values[1]=((JlabSSPBoard *) ((scalersslowcontrol->vmecrates[crate])->crateBoards[slot]))->dataFibers.size();
            }
        }
        else printf("IocGetValue:  unknown command i%d/%d/%d/%d\n",crate,slot,channel,command);

        pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
        return 0;
    }

#ifdef __cplusplus
}
#endif

#ifdef __cplusplus
extern "C" {
#endif

    void IocReadWaveform(int crate, int slot, int channel, int len, double values[]){
        pthread_mutex_lock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
        if (scalersslowcontrol->vmecrates.count(crate)<=0) {
            //|| channel>=((scalersslowcontrol->vmecrates[crate])->crateBoards[slot])->numberOfChannels)  {
            for (int i=0; i<len; i++) values[i]=NOT_PRESENT_VALUE;
        } else {
            for(int i=0;i<(len);i++) {
                if (i>= (int)(((scalersslowcontrol->vmecrates[crate])->crateBoards[slot])->scalerCountsHz[channel]).size()) 
                    values[i]=NOT_PRESENT_VALUE;
                else
                    values[i]=(((scalersslowcontrol->vmecrates[crate])->crateBoards[slot])->scalerCountsHz[channel])[i];
            }
        }
        pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
    }

#ifdef __cplusplus
}
#endif

#ifdef __cplusplus
extern "C" {
#endif

    int IocGetWaveformLength(int crate, int slot, int channel, int *len){
        if (scalersslowcontrol->vmecrates.count(crate)<=0) {
            *len=0;
            return CRATE_NOT_PRESENT;
        }
        if (slot >= scalersslowcontrol->vmecrates[crate]->numberOfSlots) {
            (*len)=0;
            return BOARD_NOT_PRESENT;
        }
        if (!((scalersslowcontrol->vmecrates[crate])->crateBoards[slot])) {
            (*len)=0;
            return BOARD_NOT_PRESENT;
        }
        //if (channel>=((scalersslowcontrol->vmecrates[crate])->crateBoards[slot])->numberOfChannels)  {
        //    *len=0;
        //    fprintf(stderr,"::D  %d %d\n",channel,((scalersslowcontrol->vmecrates[crate])->crateBoards[slot])->numberOfChannels);
        //    return NOT_PRESENT_VALUE;
        //}
        pthread_mutex_lock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
        (*len) = (((scalersslowcontrol->vmecrates[crate])->crateBoards[slot])->scalerCountsHz[channel]).size();
        pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
        if ((*len)<=0) return NOT_PRESENT_VALUE;
        return 0;
    }

#ifdef __cplusplus
}
#endif

#ifdef __cplusplus
extern "C" {
#endif
    void IocReadWaveformSSPData(int crate, int slot, int channel, int len, double values[]){
        if (scalersslowcontrol->vmecrates.count(crate)<=0) {
            for (int i=0; i<len; i++) values[i]=BOARD_NOT_PRESENT;
            return;
        }
        JlabSSPBoard *board;
        if (!dynamic_cast<JlabSSPBoard*> (scalersslowcontrol->vmecrates[crate]->crateBoards[slot])) {
            for (int i=0; i<len; i++) values[i]=NOT_PRESENT_VALUE;
            return;
        }
        else board=(JlabSSPBoard*)(scalersslowcontrol->vmecrates[crate]->crateBoards[slot]); 
        //if (channel >= board->numOfSSPDataChannels)  {
        //    for (int i=0; i<len; i++) values[i]=NOT_PRESENT_VALUE;
        //    return;
        //}
        pthread_mutex_lock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
        for (int i=0; i<(len); i++) values[i]=((board->SSPData[channel]))[i];
        pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
    }
#ifdef __cplusplus
}
#endif

#ifdef __cplusplus
extern "C" {
#endif
    int IocGetWaveformLengthSSPData(int crate, int slot, int channel, int *len){
        if (scalersslowcontrol->vmecrates.count(crate)<=0) {
            *len=0;
            return CRATE_NOT_PRESENT;
        }
        JlabSSPBoard *board;
        if (!dynamic_cast<JlabSSPBoard*> (scalersslowcontrol->vmecrates[crate]->crateBoards[slot])) { 
            *len=0;
            return BOARD_NOT_PRESENT;
        }
        else board=(JlabSSPBoard*)(scalersslowcontrol->vmecrates[crate]->crateBoards[slot]); 
        if (!board) {
            (*len)=0;
            return BOARD_NOT_PRESENT;
        }
        //if (channel>=board->numOfSSPDataChannels)  {
        //    *len=0;
        //    return NOT_PRESENT_VALUE;
        //}
        pthread_mutex_lock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
        (*len) = (board->SSPData[channel]).size();
        pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
        return 0;
    }
 
#ifdef __cplusplus
}
#endif
        
#ifdef __cplusplus
extern "C" {
#endif
    void block_until_crate_read(int crate){
        if (scalersslowcontrol->vmecrates.count(crate)<=0) return;
        VmeChassis *co = ((scalersslowcontrol->vmecrates[crate])); 
        while (!(co->is_crate_read)) {  
            sleep(5);
            printf("is_mainframe_read wait (crate=%d)\n",crate);
        }
    }
#ifdef __cplusplus
}
#endif


