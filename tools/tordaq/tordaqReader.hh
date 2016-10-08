
#ifndef __TORDAQREADER__HH
#define __TORDAQREADER__HH

#include "tordaqData.hh"

#include <TNtupleD.h>
#include <TGProgressBar.h>

#include <map>

class tordaqReader {
public:
    const char* separator=",";
    tordaqReader(){};
    ~tordaqReader(){};
    TFile *inFile=NULL;
    TString inFilename="";
    TString outAsciiFilename="";
    TString outRootFilename="";
    Long64_t maxSamples=-1;
    Long64_t startTime=-1;
    Long64_t endTime=-1;
    bool rubenTime=0;
    bool makeHistos=false;
    bool makeNtuple=false;
    FILE *outAsciiFile=NULL;
    TNtupleD *outTree=NULL;
    TFile *outRootFile=NULL;
    TGHProgressBar *progressMeter=NULL;
  
    tordaqData tdData;

    std::vector <tordaqData*> inTrees;
    std::vector <TH1*> outHistos;

    void ProgressMeter(const double total,const double current,const int starttime=0)
    {
        static const int maxdots=40;
        double frac = current/total;
        if (frac>1) frac=1;
        int ii=0;  printf("%3.0f%% [",frac*100);
        for ( ; ii < frac*maxdots; ii++) printf("=");
        for ( ; ii < maxdots;      ii++) printf(" ");
        int timeRemain=-1;
        if (starttime>0) {
            time_t now=time(0);
            timeRemain=float(time(0)-starttime)*(1/frac-1);
        }
        if (frac>0.2)
        {
            if (timeRemain>0) printf("]  %d sec          \r",timeRemain);
            else              printf("]                  \r");
        }
        else                  printf("]  ?? sec          \r");
        fflush(stdout);
        if (progressMeter)
        {
            progressMeter->SetPosition(progressMeter->GetMin() +
                    (progressMeter->GetMax()-progressMeter->GetMin()) *frac);
        }
    }
    
    static void WriteRemainingHistos()
    {
        TObject *oo;
        TIter itoo(gDirectory->GetList());
        while ((oo=(TObject*)itoo()))
        {
            if (!oo) continue;
            if (!oo->IsA()->InheritsFrom(TH1::Class())) continue;
            oo->Write();
        }
    }

    bool process()
    {
        if (inFilename!="") {
            if (gSystem->AccessPathName(inFilename))
            {
                std::cerr<<"Missing input file:  "<<inFilename<<std::endl;
                return false;
            }
            inFile=new TFile(inFilename,"READ");
        }
        
        // find the input TTrees:
        std::vector <std::string> missingTrees;
        for (unsigned int ii=0; ii<tdData.VARNAMES.size(); ii++)
        {
            TTree *tt=(TTree*)gDirectory->Get(tdData.VARNAMES[ii].c_str());
            if (tt) inTrees.push_back(new tordaqData(tt));
            else missingTrees.push_back(tdData.VARNAMES[ii]);
        }
        for (unsigned int ii=0; ii<missingTrees.size(); ii++)
            std::cerr<<"Missing Tree:   "<<missingTrees[ii]<<std::endl;
        if (missingTrees.size()>0) return false;
        if (tdData.VARNAMES.size() != inTrees.size())
        {
            std::cerr<<"Unkown missing trees (this should be impossible)."<<std::endl;
            return false;
        }

        // open output ascii file:
        if (outAsciiFilename=="stdout") outAsciiFile=stdout;
        else if (outAsciiFilename!="")
        {
            outAsciiFile=fopen(outAsciiFilename,"w");
            if (!outAsciiFile)
            {
                std::cerr<<"Error Opening Output File:  "<<outAsciiFilename<<std::endl;
                std::cerr<<"Probably you don't have permissions to write to that directory"<<std::endl;
                return false;
            }
        }


        // open output ROOT file and TNtupleD:
        if (outRootFilename!="")
        {
            outRootFile=new TFile(outRootFilename,"CREATE");
            if (makeNtuple)
            {
                std::string separator="";
                std::string varnames="";
                for (unsigned int ii=0; ii<tdData.VARNAMES.size(); ii++)
                {
                    varnames += separator+"t"+tdData.VARNAMES[ii];
                    varnames += ":"+tdData.VARNAMES[ii];
                    separator=":";
                }
                std::cerr<<varnames<<std::endl;
                outTree=new TNtupleD("tordaq","",varnames.c_str());
            }
        }


        if (makeHistos)
        {
            for (unsigned int ii=0; ii<inTrees.size(); ii++)
            {
                Double_t time0=-1,time1=-1;
                if (inTrees[ii]->LoadTree(0) < 0) continue;
                else
                {
                    inTrees[ii]->fChain->GetEntry(0);
                    time0 = inTrees[ii]->getTime(0);
                }
                if (inTrees[ii]->LoadTree(inTrees[ii]->fChain->GetEntries()-1) < 0) continue;
                else
                {
                    inTrees[ii]->fChain->GetEntry(inTrees[ii]->fChain->GetEntries()-1);
                    time1 = inTrees[ii]->getTime(tordaqData::WFLENGTH-1);
                }
                if (time0>0 && time1>0)
                {
                    const Double_t t0 = time0 - 0.5/tordaqData::FREQUENCY;
                    const Double_t t1 = time1 + 0.5/tordaqData::FREQUENCY;
                    const int nBins=(t1-t0)*tordaqData::FREQUENCY;
                    const TString vn=inTrees[ii]->fChain->GetName();
                    outHistos.push_back(new TH1F("h"+vn,";;"+vn,nBins,t0,t1));
                }
                else
                {
                    std::cerr<<"Error Reading TTree:  "<<inTrees[ii]->fChain->GetName()<<std::endl;
                    return false;
                }
            }
        }

        std::vector <bool> skipVars;
        for (unsigned int ii=0; ii<inTrees.size(); ii++) skipVars.push_back(false);

        static const int ASCIITIMELENGTH=26;
        char stime[ASCIITIMELENGTH];

        Double_t ntupleVars[1000];

        Long64_t jentry=-1;
        Long64_t nSamples=0;
        bool tooManySamples=0;

        // just for progress meter:
        const int nev = maxSamples>0 && maxSamples<inTrees[0]->fChain->GetEntries()
                      ? maxSamples/tordaqData::WFLENGTH
                      : inTrees[0]->fChain->GetEntries();
        const time_t runStartTime=time(0);

        while (1)
        {
            jentry++;

            if (jentry%(int)(nev/50)==0) ProgressMeter(nev,jentry,runStartTime);

            bool allEarly=1;
            bool allLate=1;

            // load the entries for all TTrees:
            for (unsigned int iVar=0; iVar<inTrees.size(); iVar++)
            {
                skipVars[iVar]=false;
                if (inTrees[iVar]->LoadTree(jentry) < 0) skipVars[iVar]=true;
                else
                {
                    inTrees[iVar]->fChain->GetEntry(jentry);
                    const Double_t time = inTrees[iVar]->getTime(0);
                    if (endTime<0   || time<endTime)   allLate=0;
                    if (startTime<0 || time>startTime) allEarly=0;
                }
            }

            // all times are too late, we can just stop reading:
            if (allLate) break;

            // all times are too early, skip to next entry:
            if (allEarly) continue;


            for (int iSamp=0; iSamp<tordaqData::WFLENGTH; iSamp++)
            {
                char sep[1]="";
                for (unsigned int iVar=0; iVar<inTrees.size(); iVar++)
                {
                    strcpy(stime,"0000:00:00 00:00:00: 0.0000");
                    Double_t time=0,data=0;
                    ntupleVars[2*iVar]=ntupleVars[2*iVar+1]=0;
                    if (!skipVars[iVar])
                    {
                        data = inTrees[iVar]->record_data[iSamp];
                        time = inTrees[iVar]->getTime(iSamp);
                        ntupleVars[2*iVar]=time;
                        ntupleVars[2*iVar+1]=data;
                        if (rubenTime)
                        {
                            const time_t timet=(int)time;
                            const struct tm* structtm=localtime(&timet);
                            strftime(stime,ASCIITIMELENGTH,"%Y:%m:%d %H:%M:%S",structtm);
                            sprintf(stime,"%s %.4f",stime,time-(int)time);
                        }
                        if (makeHistos)
                        {
                            const int bin=outHistos[iVar]->FindBin(time);
                            
                            /*
                            if (iVar==18)
                            {
                                if (fabs(outHistos[iVar]->GetBinContent(bin))>1e-8)
                                {
                                    std::cerr<<"Overlapping Data:"<<inTrees[iVar]->fChain->GetName();
                                    fprintf(stderr," (%d,%d,%d) ",jentry,iSamp,bin);
                                    fprintf(stderr," (%20f,%f) ",time,data);
                                    std::cerr<<outHistos[iVar]->GetBinContent(bin)<<std::endl;
                                    getchar();
                                }
                                else
                                {
                                    fprintf(stderr," (%d,%d,%d) ",jentry,iSamp,bin);
                                    fprintf(stderr,"  (%20f,%f)\n",time,data);
                                }
                            }
                            */
                            outHistos[iVar]->SetBinContent(bin,data);
                        }
                    }
                    if (outAsciiFile)
                    {
                        if (rubenTime) fprintf(outAsciiFile,"%s%s%s%12f",sep,stime,separator,data);
                        else           fprintf(outAsciiFile,"%s%18.4f%s%12f",sep,time,separator,data);
                    }
                    strcpy(sep,separator);
                }
                if (outAsciiFile) fprintf(outAsciiFile,"\n");
                if (outTree) outTree->Fill(ntupleVars);
                if (++nSamples>=maxSamples && maxSamples>0)
                {
                    tooManySamples=1;
                    break;
                }
            }
            if (tooManySamples) break;
        }
        return true;
    }
};
#endif

