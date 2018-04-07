#ifndef JSCALERS_DOT_H
#define JSCALERS_DOT_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>

#include <vector>
#include <iostream>
#include <string>
#include <map>
#include <pthread.h>

#include "common.h"

#include "cratemsgclient.h"

using namespace std;

///============================================================================

struct GenericSetBoard {
    int command; /// e.g. setthresholds, set_some_mode_for_channel
    vector<double> values; /// values to set
    int channelNumber; /// negative (-1) means to ussue a command for a whole board
};

///============================================================================
class JlabBoard {

    private:

    protected:
        // Prevent copying boards
        JlabBoard(const JlabBoard& board);
        JlabBoard& operator=(const JlabBoard& board);
    public:

        CrateMsgClient* crateMsgClient;

        vector<string> part_epics_names;

        int commsStatus;
        int slotNumber;
        int boardType;
        int numberOfChannels;
        vector<GenericSetBoard> genericSetBoards;   
        vector< double > *scalerCounts;
        vector< double > *scalerCountsHz;
        vector< uint > scalerClocks;
        vector< double > *scalerThresholds;
        vector< double > *scalerModes;

        JlabBoard(CrateMsgClient *msgClient, int slot, int type ) : crateMsgClient(msgClient), slotNumber(slot), boardType(type){
            unsigned int *buf[1];
            int len;
            int partype = SCALER_PARTYPE_NCHANNELS;
            (*buf)=0;
            int ret = msgClient->GetBoardParams(slotNumber, partype, buf, &len);
            if (ret) numberOfChannels=((*buf)[0]);
            printf("numberOfChannels===========%d slot=%d\n", numberOfChannels, slot);
            if (*buf) delete (*buf);
            if (numberOfChannels>0) {
                scalerCounts=new vector< double >[numberOfChannels];
                scalerCountsHz=new vector< double >[numberOfChannels];
                scalerThresholds=new vector< double >[numberOfChannels];
                scalerModes=new vector< double >[numberOfChannels];
            }
            commsStatus=1;
        }
        virtual ~JlabBoard(){};

        virtual void SetThresholds( int threshType, double threshold  );
        virtual void SetThreshold( int chanNumber, int threshType, double threshold  );
        virtual void GetThresholds( int threshType, double threshold[]   );
        virtual void GetThreshold( int chanNumber, int threshType, double & threshold  );

        //virtual int GetNumberOfChannels();
        //virtual vector<double> *GetScalerCounts( int chanNumber, bool inHz = true );
        //virtual double GetScalerCount( int chanNumber, int type, bool inHz = true );
        //virtual uint GetClockCounts( int type );
        //virtual void SetReadModes(double values[]); // not implemented completely
        //virtual void SetReadMode(const unsigned chanNumber, double values[]); // not implemented completely
        //virtual void GetReadModes(double values[]); // not implemented completely
        //virtual void GetReadMode(const unsigned chanNumber, double values[]); // not implemented completely
};

///============================================================================
class JlabDisc2Board : public JlabBoard {
    protected:
        // Prevent copying boards
        JlabDisc2Board(const JlabDisc2Board& board);
        JlabDisc2Board& operator=(const JlabDisc2Board& board);
    public:
        JlabDisc2Board(CrateMsgClient *crateMsgClient, int slot, int type ) : JlabBoard(crateMsgClient, slot, type){}
        virtual ~JlabDisc2Board(){};

};
///============================================================================
class JlabFadc250Board : public JlabBoard {
    protected:
        // Prevent copying boards
        JlabFadc250Board(const JlabFadc250Board& board);
        JlabFadc250Board& operator=(const JlabFadc250Board& board);
    public:
        static const double CLOCKFREQ=488281.25f;
        JlabFadc250Board(CrateMsgClient *crateMsgClient, int slot, int type ) : JlabBoard(crateMsgClient,slot,type){}
        virtual ~JlabFadc250Board(){};

};
///============================================================================
class JlabSSPBoard : public JlabBoard {
    protected:
        // Prevent copying boards
        JlabSSPBoard(const  JlabSSPBoard& board);
        JlabSSPBoard& operator=(const  JlabSSPBoard& board);
    public:
        static const int MAXFIBERS=32;
        static const int PMTSPERFIBER=3;
        static const int SCALERSPERPMT=64;
        static const int SCALERSPERFIBER=PMTSPERFIBER*SCALERSPERPMT;//192
        static const int DATAPERFIBER=9;
        static const int SCALERHEADEROFFSET=3;
        static const int DATAHEADEROFFSET=2;
        static const double CLOCKFREQ=125E6;

        static const int MAXSCALERLEN = MAXFIBERS * (SCALERSPERFIBER+SCALERHEADEROFFSET); 
        static const int MAXDATALEN = MAXFIBERS * (DATAPERFIBER+DATAHEADEROFFSET); 

        int numOfSSPDataChannels;
        vector< double > *SSPData;
        vector< int > scalerFibers;
        vector< int > dataFibers;

        JlabSSPBoard(CrateMsgClient *crateMsgClient, int slot, int type ) : JlabBoard(crateMsgClient,slot,type){
            // use max possible number of fibers to create vectors::
            scalerCounts=new vector< double >[MAXFIBERS];
            scalerCountsHz=new vector< double >[MAXFIBERS];
            SSPData=new vector< double >[MAXFIBERS];
        }
        virtual ~JlabSSPBoard(){};

        static const int Maroc2Pixel(const int maroc) {
            static const int m2p[SCALERSPERPMT]={
                60,58,59,57,52,50,51,49,
                44,42,43,41,36,34,35,33,
                28,26,27,25,20,18,19,17,
                12,10,11, 9, 4, 2, 3, 1,
                5, 7, 6, 8,13,15,14,16,
                21,23,22,24,29,31,30,32,
                37,39,38,40,45,47,46,48,
                53,55,54,56,61,63,62,64};
            return (maroc<0 || maroc>=SCALERSPERPMT) ? -1 : m2p[maroc]-1;
        }

};
///============================================================================
class VmeChassis {
    private:

    protected:
        // Prevent copying boards
        VmeChassis(const VmeChassis& chassis);
        VmeChassis& operator=(const VmeChassis& chassis);

    public:
        string HOSTNAME;

        int commsStatus;
        string getHostname() {return HOSTNAME;}
        int port;  /// should be gotten from the databses (not used at the moment)
        CrateMsgClient* crateMsgClient;
        pthread_mutex_t IOmutex;// = PTHREAD_MUTEX_INITIALIZER;
        map<int, JlabBoard *> crateBoards; // key is slot
        pthread_t threadC,threadCmon;
        int is_crate_read;
        int numberOfSlots;
        VmeChassis(int id, string &hostname );  /// id is to talk from record
        bool IsCrateRead(){return is_crate_read;}
        int getPortFromDb(string &hostname); /// get port from db (not used now)
        int GetNumberOfSlots();
        map<int, JlabBoard*> *GetBoardMap(); // key is slot
};
///===========================================================================

class ScalersSlowControl{
    public:
        ScalersSlowControl();
        map<int, VmeChassis* > vmecrates;
        map<int, VmeChassis*> *GetChassisMap();
};

///============================================================================


#endif






