#include <unistd.h> 
#include <stdio.h>
#include <vector>
#include <string>
#include <time.h>

#include <TSystem.h>
#include <TNtupleD.h>

#include "tordaqData.h"

/*
#define FREQUENCY 3846

Double_t getTime(Long64_t sec,Long64_t nsec,Int_t wfLength,Int_t iSample)
{
    // assume the waveform is sampled at wfLength Hz
    // and updated at 1 Hz, i.e. no deadtime
    // return sec + nsec/1e9 + (Double_t)iSample/wfLength;
  
    // Nope, there's known deadtime:
    // Consecutive samples are recorded at 3.846 kHz, or once per 260 us.
    // 2000 samples are then reported to EPICS, but only once every 800 ms.
    // So that leaves a contiguous 279 ms of every 1 second with no data.
    return sec + nsec/1e9 + (Double_t)iSample/FREQUENCY;
}
Double_t getTime(tordaqData* td,Int_t iSample)
{
    return getTime(td->record_tsec,td->record_tnsec,td->WFLENGTH,iSample);
}
*/

int main(int argc,char **argv)
{
    // for input arguments:
    const char* timeFormat="%Y-%m-%d_%H:%M:%S";

    // for Ruben's output file:
    const char* separator=",";
    
    TString inFilename="torus.root";
    TString outAsciiFilename="";
    TString outRootFilename="";
    Long64_t maxSamples=-1;
    Long64_t startTime=-1;
    Long64_t endTime=-1;
    bool rubenTime=0;
    bool makeHistos=false;
    bool makeNtuple=false;
    std::string sStartTime="";
    std::string sEndTime="";

    TString usage="\ntordaq [options]\n"
        "\t  -i input wf2root filename\n"
        "\t  -o output ascii filename\n"
        "\t  -t output ROOT filename with ntuple\n"
        "\t  -H output ROOT filename with histos\n"
        "\t  -s first epoch second or YYYY-MM-DD_HH:MM:SS\n"
        "\t  -e last  epoch second or YYYY-MM-DD_HH:MM:SS\n"
        "\t  -n max # samples\n"
        "\t  -R (output Ruben's ascii time format)\n"
        "\t  -h (print usage)\n";
   
    int itmp;
    while ( (itmp=getopt(argc,argv,"i:o:t:s:e:H:n:Rh")) != -1 )
    {
        switch (itmp)
        {
            case 'i':
                inFilename=optarg;
                break;
            case 'o':
                outAsciiFilename=optarg;
                break;
            case 't':
                outRootFilename=optarg;
                makeNtuple=true;
                break;
            case 'H':
                outRootFilename=optarg;
                makeHistos=true;
                break;
            case 's':
                sStartTime=optarg;
                break;
            case 'e':
                sEndTime=optarg;
                break;
            case 'n':
                maxSamples=std::stoi(optarg);
                break;
            case 'R':
                rubenTime=1;
                break;
            case 'h':
                std::cout<<usage<<std::endl;
                exit(0);
            default:
                std::cout<<usage<<std::endl;
                exit(1);
        }
    }

    // interpret time arguments:
    if (sStartTime!="")
    {
        if (sStartTime.find(":")==std::string::npos)
            startTime=std::stoi(sStartTime.c_str());
        else
        {
            struct tm tm;
            strptime(sStartTime.c_str(),timeFormat,&tm);
            startTime=mktime(&tm);
        }
    }
    if (sEndTime!="")
    {
        if (sEndTime.find(":")==std::string::npos)
            endTime=std::stoi(sEndTime.c_str());
        else
        {
            struct tm tm;
            strptime(sEndTime.c_str(),timeFormat,&tm);
            endTime=mktime(&tm);
        }
    }

    // check filesystem for input/output files:
    if (gSystem->AccessPathName(inFilename))
    {
        std::cerr<<"Input File Does Not Exist:  "<<inFilename<<std::endl;
        std::cerr<<usage<<std::endl;
        exit(1);
    }
    if (outAsciiFilename!="" && !gSystem->AccessPathName(outAsciiFilename))
    {
        if (outAsciiFilename!="stdout")
        {
            std::cerr<<"Output File Already Exists:  "<<outAsciiFilename<<std::endl;
            std::cerr<<usage<<std::endl;
            exit(1);
        }
    }
    if (outRootFilename!="" && !gSystem->AccessPathName(outRootFilename))
    {
        std::cerr<<"Output File Already Exists:  "<<outRootFilename<<std::endl;
        std::cerr<<usage<<std::endl;
        exit(1);
    }

    // find the input TTrees:
    std::vector <tordaqData*> tordaqs;
    TFile *inFile=new TFile(inFilename,"READ");
    int itree=1;
    while (1)
    {
        TTree *tt=(TTree*)inFile->Get(Form("VT%d",itree++));
        if (tt) tordaqs.push_back(new tordaqData(tt));
        else break;
    }
    if (tordaqs.size()<1)
    {
        std::cerr<<"Found No Trees"<<std::endl<<std::endl;
        std::cerr<<usage<<std::endl;
        exit(1);
    }
    std::cout<<"Found "<<tordaqs.size()<<" Variables."<<std::endl;
    

    // print requested time range:
    if (startTime>0 || endTime>0)
    {
        std::cout<<"Time Span:  "<<startTime<<" >< "<<endTime<<std::endl;
        std::cout<<"Time Span:  "<<sStartTime<<" >< "<<sEndTime<<std::endl;
    }

    // open output ascii file:
    FILE *outAsciiFile=NULL;
    if (outAsciiFilename=="stdout") outAsciiFile=stdout;
    else if (outAsciiFilename!="")  outAsciiFile=fopen(outAsciiFilename,"w");
    
    // open output ROOT file and TNtupleD:
    TNtupleD *outTree=NULL;
    TFile *outRootFile=NULL;
    if (outRootFilename!="")
    {
        outRootFile=new TFile(outRootFilename,"CREATE");
        if (makeNtuple)
        {
            TString vars="t1:x1";
            for (unsigned int ii=1; ii<tordaqs.size(); ii++)
                vars+=Form(":t%d:x%d",ii+1,ii+1);
            outTree=new TNtupleD("tordaq","",vars);
        }
    }
    
    // determine available time range:
    Double_t time0=-1,time1=-1;
    for (unsigned int ii=0; ii<tordaqs.size(); ii++)
    {
        if (tordaqs[ii]->LoadTree(0) < 0) continue;
        else
        {
            tordaqs[ii]->fChain->GetEntry(0);
            const Double_t t0 = tordaqs[ii]->getTime(0);
            //const Double_t t0 = getTime(tordaqs[ii],0);
            if (time0<0 || t0<time0) time0=t0;
        }
        if (tordaqs[ii]->LoadTree(tordaqs[ii]->fChain->GetEntries()-1) < 0) continue;
        else
        {
            tordaqs[ii]->fChain->GetEntry(tordaqs[ii]->fChain->GetEntries()-1);
            const Double_t t1 = tordaqs[ii]->getTime(tordaqs[ii]->WFLENGTH-1);
            //const Double_t t1 = getTime(tordaqs[ii],tordaqs[ii]->WFLENGTH-1);
            if (time1<0 || t1>time1) time1=t1;
        }
    }
    
    std::vector <TH1*> htordaqs;
    if (makeHistos)
    {
        const Double_t sec0=floor(time0);
        const Double_t sec1=floor(time1)+1;
        const int nSeconds=floor(time1)+1-floor(time0);
        const int nBins=nSeconds*tordaqData::FREQUENCY;
        std::cerr<<std::endl<<nBins<<" "<<time0<<" "<<time1<<std::endl<<std::endl;
        for (unsigned int ii=0; ii<tordaqs.size(); ii++)
            htordaqs.push_back(new TH1F(Form("h%d",ii+1),Form(";;VT%d",ii+1),nBins,sec0,sec1));
    }
   
    std::vector <bool> skipVars;
    for (unsigned int ii=0; ii<tordaqs.size(); ii++) skipVars.push_back(false);

    static const int ASCIITIMELENGTH=26;
    char stime[ASCIITIMELENGTH];

    Double_t vars[1000];

    Long64_t jentry=-1;
    Long64_t nSamples=0;
    bool tooManySamples=0;

    // just for progress meter:
    const int nev = maxSamples>0 && maxSamples<tordaqs[0]->fChain->GetEntries() ?
        maxSamples/tordaqs[0]->WFLENGTH : tordaqs[0]->fChain->GetEntries();
    const time_t runStartTime=time(0);

    while (1)
    {
        jentry++;

        if (jentry%(int)(nev/50)==0) ProgressMeter(nev,jentry,runStartTime);

        bool allEarly=1;
        bool allLate=1;

        // load the entries for all TTrees:
        for (unsigned int iVar=0; iVar<tordaqs.size(); iVar++)
        {
            skipVars[iVar]=false;
            if (tordaqs[iVar]->LoadTree(jentry) < 0) skipVars[iVar]=true;
            else
            {
                tordaqs[iVar]->fChain->GetEntry(jentry);
                const Double_t time = tordaqs[iVar]->getTime(0);
                //const Double_t time = getTime(tordaqs[iVar]->record_tsec,
                //                              tordaqs[iVar]->record_tnsec,
                //                              tordaqs[iVar]->WFLENGTH,
                //                              0);
                if (endTime<0   || time<endTime)   allLate=0;
                if (startTime<0 || time>startTime) allEarly=0;
            }
        }
       
        if (allLate) break;
        if (allEarly) continue;

        for (int iSamp=0; iSamp<tordaqs[0]->WFLENGTH; iSamp++)
        {
            char sep[1]="";
            for (unsigned int iVar=0; iVar<tordaqs.size(); iVar++)
            {
                strcpy(stime,"0000:00:00 00:00:00: 0.0000");
                Double_t time=0,data=0;
                vars[2*iVar]=vars[2*iVar+1]=0;
                if (!skipVars[iVar])
                {
                    data = tordaqs[iVar]->record_data[iSamp];
                    time = tordaqs[iVar]->getTime(iSamp);
//                    time = getTime(tordaqs[iVar]->record_tsec,
//                                   tordaqs[iVar]->record_tnsec,
//                                   tordaqs[iVar]->WFLENGTH,
//                                   iSamp);
                    vars[2*iVar]=time;
                    vars[2*iVar+1]=data;
                    if (rubenTime)
                    {
                        const time_t timet=(int)time;
                        const struct tm* structtm=localtime(&timet);
                        strftime(stime,ASCIITIMELENGTH,"%Y:%m:%d %H:%M:%S",structtm);
                        sprintf(stime,"%s %.4f",stime,time-(int)time);
                    }
                    if (makeHistos)
                        htordaqs[iVar]->SetBinContent(htordaqs[iVar]->FindBin(time),data);
                }
                if (outAsciiFile)
                {
                    if (rubenTime) fprintf(outAsciiFile,"%s%s%s%12f",sep,stime,separator,data);
                    else           fprintf(outAsciiFile,"%s%18.4f%s%12f",sep,time,separator,data);
                }
                strcpy(sep,separator);
            }
            if (outAsciiFile) fprintf(outAsciiFile,"\n");
            if (outTree) outTree->Fill(vars);
            if (++nSamples>=maxSamples && maxSamples>0)
            {
                tooManySamples=1;
                break;
            }
        }
        if (tooManySamples) break;
    }

    std::cout<<std::endl<<"Closing Files ..."<<std::endl<<std::endl;
    if (outAsciiFile) fclose(outAsciiFile);
    if (outRootFile) 
    {
        if (outTree) outTree->AutoSave();
        WriteRemainingHistos();
        outRootFile->Close();
    }
}

