/**

V.Sytnik 07/2014

*/
#include "jscalers.h"


ScalersSlowControl *scalersslowcontrol;

///================================================
///================================================
///================== IOC part ====================
///================================================
///================================================


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
        else if (command==JLAB_SET_READ_MODE) {
            if (dynamic_cast<JlabDisc2Board *>(sc))
                ((JlabDisc2Board *) ((scalersslowcontrol->vmecrates[crate])->crateBoards[slot]))->SetReadMode(channel, values);
        }

        pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
        //((scalersslowcontrol.vmecrates[crate])->crateBoards[slot])->genericSetBoards.push_back(gsb);

        return 0;
    }

#ifdef __cplusplus
}
#endif
///================================================

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
        else if (command==JLAB_SET_READ_MODE) {
            if (dynamic_cast<JlabDisc2Board *>(sc))
                ((JlabDisc2Board *) ((scalersslowcontrol->vmecrates[crate])->crateBoards[slot]))->GetReadMode(channel,values);
        }

        pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
        //((scalersslowcontrol.vmecrates[crate])->crateBoards[slot])->genericSetBoards.push_back(gsb);

        return 0;
    }



#ifdef __cplusplus
}
#endif

#ifdef __cplusplus
extern "C" {
#endif

    void IocReadWaveform(int crate, int slot, int channel, int len, double values[]){
        if(scalersslowcontrol->vmecrates.count(crate)<=0) return;
        pthread_mutex_lock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));

        for(int i=0;i<(len);i++){
            values[i]=(((scalersslowcontrol->vmecrates[crate])->crateBoards[slot])->scalerCountsHz[channel])[i];
        }

        //((scalersslowcontrol.vmecrates[crate])->crateBoards[slot])->genericSetBoards.push_back(gsb);
        pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
    }

#ifdef __cplusplus
}
#endif
///================================================

#ifdef __cplusplus
extern "C" {
#endif

    int IocGetWaveformLength(int crate, int slot, int channel, int *len){
        int slot_status=0;
        if (scalersslowcontrol->vmecrates.count(crate)<=0) {
            *len=0;
            return CRATE_NOT_PRESENT;
        }
        pthread_mutex_lock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
        if (!((scalersslowcontrol->vmecrates[crate])->crateBoards[slot])) {
            (*len)=0;
            slot_status=BOARD_NOT_PRESENT;
        }
        else (*len) = (((scalersslowcontrol->vmecrates[crate])->crateBoards[slot])->scalerCountsHz[channel]).size();
        pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
        return slot_status;
    }

#ifdef __cplusplus
}
#endif

///================================================

#ifdef __cplusplus
extern "C" {
#endif

    void IocReadWaveformSSPData(int crate, int slot, int channel, int len, double values[]){
        if (scalersslowcontrol->vmecrates.count(crate)<=0) return;
        JlabSSPBoard *board;
        if (!dynamic_cast<JlabSSPBoard*> (scalersslowcontrol->vmecrates[crate]->crateBoards[slot])) 
            return;
        else
            board=(JlabSSPBoard*)(scalersslowcontrol->vmecrates[crate]->crateBoards[slot]); 
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
        int slot_status=0;
        if (scalersslowcontrol->vmecrates.count(crate)<=0) {
            *len=0;
            return CRATE_NOT_PRESENT;
        }
        JlabSSPBoard *board;
        if (!dynamic_cast<JlabSSPBoard*> (scalersslowcontrol->vmecrates[crate]->crateBoards[slot])) 
            return BOARD_NOT_PRESENT;
        else
            board=(JlabSSPBoard*)(scalersslowcontrol->vmecrates[crate]->crateBoards[slot]); 
        pthread_mutex_lock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
        if (!board) {
            (*len)=0;
            slot_status=BOARD_NOT_PRESENT;
        }
        else (*len) = (board->SSPData[channel]).size();
        pthread_mutex_unlock(&((scalersslowcontrol->vmecrates[crate])->IOmutex));
        return slot_status;
    }
 
#ifdef __cplusplus
}
#endif
        
 
///================================================
#ifdef __cplusplus
extern "C" {
#endif
    void block_until_crate_read(int crate){ ///my:
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

///================================================
///================================================
///================================================
///================================================
///================================================
///================================================
///================================================

