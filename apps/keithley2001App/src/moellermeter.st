program seqMoellermeter ("P=moellermeter")

option -c;  // donot wait on pv connections
option -r;  // donot allow multiple instances

%{
FILE* fd=NULL;
void openFile(char* basename)
{
    static const int datelen=18;
    static const char* dir="/usr/clas12/DATA/moeller/calib/";

    time_t now;
    struct tm *nowloc;
    char sdate[datelen];
    char filepath[150];

    time(&now);
    nowloc=localtime(&now);

    strftime(&sdate[0],datelen,"%m-%d-%y_%H:%M:%S", nowloc);
    strcpy(basename,"emf-");
    strcat(basename,sdate);
    strcat(basename,".txt");

    strcpy(filepath,dir);
    strcat(filepath,basename);

    fd=fopen(filepath,"w");
}
int writeFile(float data[1000],float aperture,float current,int nsamp)
{
    int ii;
    fprintf(fd,"%.8f %.8f %8d\n",current,aperture,nsamp);
    for (ii=0; ii<nsamp; ii++)
    {
        fprintf(fd,"%e\n",data[ii]);
    }
    fclose(fd);
    return 1;
}
}%

char cfilename[1024];
float current=0;
int counter=0;
short failure=0;
short success=0;
short configured=0;
int readoutTimeout=120;
short autoTrigger=0;

string msg;            assign msg           to "{P}:msg";
float daqDelay;        assign daqDelay      to "{P}:daqdelay";
float readoutDelay;    assign readoutDelay  to "{P}:readoutdelay";
short opc;             assign opc           to "{P}:opc";
short setopc;          assign setopc        to "{P}:setopc";
int nsamples;          assign nsamples      to "{P}:tracpoints";
float aperture;        assign aperture      to "{P}:aperture";
//float sampleno[1000];  assign sampleno      to "{P}:sampleno";
float readoutData[1000];   assign readoutData       to "{P}:data";
short readoutActive;   assign readoutActive to "{P}:data.PACT";
short goreadout;       assign goreadout     to "{P}:data.PROC";
short pvReset;         assign pvReset       to "{P}:reset";
short pvConfig;        assign pvConfig      to "{P}:config";
short pvReadConfig;    assign pvReadConfig  to "{P}:getcfg";
string sfilename;      assign sfilename     to "{P}:filename";

short zerodata;       assign zerodata       to "{P}:zerodata";
short trigger1;       assign trigger1       to "{P}:trigger1";
short trigger2;       assign trigger2       to "{P}:trigger2";

short flipAndTrigBtn; assign flipAndTrigBtn to "{P}:flipAndTrigBtn"; monitor flipAndTrigBtn;
short flipBtn;        assign flipBtn        to "{P}:flipBtn";        monitor flipBtn;
short cfgBtn;         assign cfgBtn         to "{P}:cfgBtn";         monitor cfgBtn;
short readCfgBtn;     assign readCfgBtn     to "{P}:readCfgBtn";     monitor readCfgBtn;
short fileBtn;        assign fileBtn        to "{P}:fileBtn";        monitor fileBtn;
short trigBtn;        assign trigBtn        to "{P}:trigBtn";        monitor trigBtn;
short resetBtn;       assign resetBtn       to "{P}:resetBtn";       monitor resetBtn;
short zeroBtn;        assign zeroBtn        to "{P}:zeroBtn";        monitor zeroBtn;
short display; assign display to"{P}:display";

// simulator:
float iSet;            assign iSet          to "moellerPS:iset";
float iMon;            assign iMon          to "moellerPS:imon";

// real:
//float iMon; assign iMon to "B_DET_MOELLER1_CURRENT";
//float iSet; assign iSet to "B_DET_MOELLER1_CRNT_SET";
//float iSetRbk; assign iSetRbk to "B_DET_MOELLER_CRNT_SP";

ss seqMoellermeter 
{
    state init {
        when (pvConnectCount() < pvChannelCount()) {
            sprintf(msg,"Waiting for PVs (%d/%d)",pvConnectCount(),pvChannelCount());
            pvPut(msg);
        } state idle
        when () {
            sprintf(msg,"Connected.  Not Configured.");
            pvPut(msg);
            epicsThreadSleep(1);
        } state idle
    }

    state idle {
        entry {
            printf("seqMoellermeter:  idle state\n");
            sprintf(msg,"Idle State");
            autoTrigger=0;
            pvPut(display);
            pvPut(msg);
            cfgBtn=0;
            flipBtn=0;
            flipAndTrigBtn=0;
            fileBtn=0;
            resetBtn=0;
            zeroBtn=0;
            pvPut(cfgBtn);
            pvPut(flipBtn);
            pvPut(flipAndTrigBtn);
            pvPut(fileBtn);
            pvPut(resetBtn);
            pvPut(zeroBtn);
        }
        when (readCfgBtn) {
            readCfgBtn=0;
            pvPut(readCfgBtn);
        } state readcfg
        when (cfgBtn) {
            cfgBtn=0;
            pvPut(cfgBtn);
        } state setcfg
        when (flipAndTrigBtn) {
            autoTrigger=1;
            flipBtn=0;
            pvPut(flipBtn);
        } state flip
        when (flipBtn) {
            flipBtn=0;
            pvPut(flipBtn);
        } state flip
        when (fileBtn) {
            fileBtn=0;
            pvPut(fileBtn);
        } state writeout
        when (trigBtn) {
            trigBtn=0;
            pvPut(trigBtn);
        } state trigger
        when (resetBtn) {
            resetBtn=0;
            pvPut(resetBtn);
        } state reset
        when (zeroBtn) {
            zeroBtn=0;
            pvPut(zeroBtn);
        } state zero
        when () {
            // .PACT field doesnt monitor
            pvGet(readoutActive);
            if (readoutActive) {
                sprintf(msg,"Reading Out Data ...");
                pvPut(msg);
                epicsThreadSleep(1);
            }
            else {
                sprintf(msg,"Idle.");
                pvPut(msg);
            }
        } state idle
    }

    state reset {
        when () {
            sprintf(msg,"Resetting to Defaults ...");
            pvPut(msg);
            pvPut(pvReset);
            epicsThreadSleep(1);
        } state readcfg
    }
    state zero {
        when () {
            sprintf(msg,"Clearing DMM Readout Memory ...");
            pvPut(msg);
            pvPut(zerodata);
            epicsThreadSleep(1);
            sprintf(msg,"Zeroing EPICS Waveform ...");
            pvPut(msg);
            counter=0;
            while (counter<1000)
            {
                readoutData[counter]=0.;
                counter++;
            }
            pvPut(readoutData);
            epicsThreadSleep(1);
        } state idle
    }
    
    state setcfg {
        when () {
            printf("seqMoellermeter:  setcfg state\n");
            sprintf(msg,"Configuring Multimeter ...");
            pvPut(msg);
//            pvPut(pvReset);
            pvPut(pvConfig);
            epicsThreadSleep(1);
/*
            counter=0;
            while (counter<1000)
            {
                readoutData[counter]=0.;
                sampleno[counter]=counter;
                counter++;
            }
            pvPut(sampleno);
            //pvPut(readoutData);
*/
            pvGet(aperture);
            pvGet(nsamples);
            pvPut(display);
        } state readcfg
    }

    state readcfg {
        when () {
            printf("seqMoellermeter:  readcfg state\n");
            sprintf(msg,"Reading Back Configuration ...");
            pvPut(msg);
            epicsThreadSleep(1);
            pvPut(pvReadConfig);

            // load these now, instead of when triggering:
            pvGet(daqDelay);
            pvGet(readoutDelay);
            
            epicsThreadSleep(2);
            sprintf(msg,"Done Reading Configuration.");
            pvPut(msg);
            epicsThreadSleep(1);
            pvGet(iSet);
            pvGet(aperture);
            pvGet(nsamples);
            current=iSet;
            configured=1;
            pvPut(display);
        } state idle
    }
    
    state flip {
        entry {
            printf("seqMoellermeter:  flip state\n");
            sprintf(msg,"Reversing Polarity ...");
            pvPut(msg);
            pvGet(iSet);
            pvGet(aperture);
            pvGet(nsamples);

            // store pre-flip current for writing to file:
            current=iSet;

            // flip current:
            iSet=-iSet;
            pvPut(iSet);

            sprintf(msg,"Polarity Reversed.");
            pvPut(msg);
            pvPut(display);
        }
        when (autoTrigger) {} state trigger
        when () {} state idle
    }

    state trigger {
        when (!configured) {
            sprintf(msg,"Trigger aborted.  Not configured.");
            pvPut(msg);
        } state idle
        when () {
            sprintf(msg,"Triggering Multimeter ...");
            pvPut(msg);
            printf("seqMoellermeter:  trigger state\n");

            //pvPut(trigger1);
            pvPut(trigger2);

            // wait expected amount of time:
            counter=daqDelay;
            while (counter>0) {
                sprintf(msg,"Waiting on Post Processing (%d seconds) ...",counter);
                pvPut(msg);
                epicsThreadSleep(1);
                counter--;
            }
/*
            // Test if done post processing:
            pvPut(setopc);
            opc=1;
            counter=0;
            while (!opc) {
                pvGet(opc);
                epicsThreadSleep(1);
                counter++;
                if (counter>120) break;
            }
*/
        } state readout
    }

    state readout {
        
        entry {
            printf("seqMoellermeter:  readout state\n");
            sprintf(msg,"Reading Out Multimeter ...");
            pvPut(display);
            pvPut(msg);
            epicsThreadSleep(1);
            failure=0;
            success=0;
        }
        
        when (success) {
            sprintf(msg,"Readout Done.");
            pvPut(msg);
            epicsThreadSleep(1);
        } state writeout

        when (failure) {
            sprintf(msg,"Readout Timeout.");
            pvPut(msg);
        } state idle

        when () {

            goreadout=1;
            pvPut(goreadout);

            // wait expected amount of time for readout:
            counter=readoutDelay;
            while (counter>0) {
                sprintf(msg,"Waiting on Readout (%d seconds) ...",counter);
                pvPut(msg);
                epicsThreadSleep(1);
                counter--;
            }

            // wait for .PACT field to be ready:
            sprintf(msg,"Waiting on Readout ...");
            pvPut(msg);
            counter=readoutTimeout;
            while (counter>0) {
                pvGet(readoutActive);
                if (!readoutActive) break;
                sprintf(msg,"Checking Readout:  %d",readoutActive);
                pvPut(msg);
                epicsThreadSleep(1);
                counter--;
            }
            if (counter>0) success=1;
            else           failure=1;
            pvPut(display);

        } state readout
    }

    state writeout {
        when () {
            sprintf(msg,"Writing Output File ...");
            pvPut(msg);
            epicsThreadSleep(2);
            fprintf(stderr,"seqMoellermeter:  writeout state\n");
            openFile(&cfilename);
            strcpy(sfilename,cfilename);
            pvPut(sfilename);
            epicsThreadSleep(2);
            pvGet(readoutData);
            fprintf(stderr,"seqMoellermeter:  writing file with %d points ...\n",nsamples);
            writeFile(readoutData,aperture,current,nsamples);
            pvPut(display);
        } state idle
    }
}


// comment this out when going to real power supply:
ss seqMollersimulator {
    state init {
        when (pvConnectCount() == pvChannelCount()) {} state idle
    }
    state idle {
        when () {
            epicsThreadSleep(4);
            pvGet(iSet);
            iMon=iSet;
            pvPut(iMon);
        } state idle
    }
}

