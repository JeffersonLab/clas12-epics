#ifndef __TORDAQREADER__HH
#define __TORDAQREADER__HH

#include "tordaqData.hh"

class tordaqReader {
    private:

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
        std::vector <tordaqData*> inTrees;
        std::vector <TH1*> outHistos;

        static void ProgressMeter(const double total,const double current,const int starttime=0)
        {
            static const int maxdots=40;
            const double frac = current/total;
            int ii=0;  printf("%3.0f%% [",frac*100);
            for ( ; ii < frac*maxdots; ii++) printf("=");
            for ( ; ii < maxdots;      ii++) printf(" ");
            int timeRemain=-1;
            if (starttime>0) {
                time_t now=time(0);
                timeRemain=float(time(0)-starttime)*(1/frac-1);
            }
            if (frac>0.1 && timeRemain>0) printf("]  %d sec          \r",timeRemain);
            else                          printf("]                  \r");
            fflush(stdout);
        }
        static void WriteRemainingHistos()
        {
            TObject *oo;
            TIter noo(gDirectory->GetList());
            while ((oo=(TObject*)noo()))
            {
                if (!oo) continue;
                if (!oo->IsA()->InheritsFrom(TH1::Class())) continue;
                oo->Write();
            }
        }

        void process()
        {

            if (inFilename!="") {
                if (gSystem->AccessPathName(inFilename))
                {
                    std::cerr<<"Missing input file:  "<<inFilename<<std::endl;
                    return;
                }
                inFile=new TFile(inFilename,"READ");
            }

            // find the input TTrees:
            int itree=1;
            while (1)
            {
                //TTree *tt=(TTree*)inFile->Get(Form("VT%d",itree++));
                TTree *tt=(TTree*)gDirectory->Get(Form("VT%d",itree++));
                if (tt) inTrees.push_back(new tordaqData(tt));
                else break;
            }
            if (inTrees.size()<1)
            {
                std::cerr<<"Found No Trees"<<std::endl<<std::endl;
                return;
            }
            if (inTrees.size()!=tordaqData::NVT)
            {
                std::cerr<<"Missing Trees"<<std::endl<<std::endl;
                return;
            }

            // open output ascii file:
            if (outAsciiFilename=="stdout") outAsciiFile=stdout;
            else if (outAsciiFilename!="")  outAsciiFile=fopen(outAsciiFilename,"w");

            // open output ROOT file and TNtupleD:
            if (outRootFilename!="")
            {
                outRootFile=new TFile(outRootFilename,"CREATE");
                if (makeNtuple)
                {
                    TString vars="t1:x1";
                    for (unsigned int ii=1; ii<inTrees.size(); ii++)
                        vars+=Form(":t%d:x%d",ii+1,ii+1);
                    outTree=new TNtupleD("tordaq","",vars);
                }
            }

            // determine available time range:
            Double_t time0=-1,time1=-1;
            for (unsigned int ii=0; ii<inTrees.size(); ii++)
            {
                if (inTrees[ii]->LoadTree(0) < 0) continue;
                else
                {
                    inTrees[ii]->fChain->GetEntry(0);
                    const Double_t t0 = inTrees[ii]->getTime(0);
                    if (time0<0 || t0<time0) time0=t0;
                }
                if (inTrees[ii]->LoadTree(inTrees[ii]->fChain->GetEntries()-1) < 0) continue;
                else
                {
                    inTrees[ii]->fChain->GetEntry(inTrees[ii]->fChain->GetEntries()-1);
                    const Double_t t1 = inTrees[ii]->getTime(inTrees[ii]->WFLENGTH-1);
                    if (time1<0 || t1>time1) time1=t1;
                }
            }

            if (makeHistos)
            {
                const Double_t sec0=floor(time0);
                const Double_t sec1=floor(time1)+1;
                const int nSeconds=floor(time1)+1-floor(time0);
                const int nBins=nSeconds*tordaqData::FREQUENCY;
                //std::cerr<<std::endl<<nBins<<" "<<time0<<" "<<time1<<std::endl<<std::endl;
                for (unsigned int ii=0; ii<inTrees.size(); ii++)
                    outHistos.push_back(new TH1F(Form("h%d",ii+1),Form(";;VT%d",ii+1),nBins,sec0,sec1));
            }

            std::vector <bool> skipVars;
            for (unsigned int ii=0; ii<inTrees.size(); ii++) skipVars.push_back(false);

            static const int ASCIITIMELENGTH=26;
            char stime[ASCIITIMELENGTH];

            Double_t vars[1000];

            Long64_t jentry=-1;
            Long64_t nSamples=0;
            bool tooManySamples=0;

            // just for progress meter:
            const int nev = maxSamples>0 && maxSamples<inTrees[0]->fChain->GetEntries() ?
                maxSamples/inTrees[0]->WFLENGTH : inTrees[0]->fChain->GetEntries();
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

                if (allLate) break;
                if (allEarly) continue;

                for (int iSamp=0; iSamp<inTrees[0]->WFLENGTH; iSamp++)
                {
                    char sep[1]="";
                    for (unsigned int iVar=0; iVar<inTrees.size(); iVar++)
                    {
                        strcpy(stime,"0000:00:00 00:00:00: 0.0000");
                        Double_t time=0,data=0;
                        vars[2*iVar]=vars[2*iVar+1]=0;
                        if (!skipVars[iVar])
                        {
                            data = inTrees[iVar]->record_data[iSamp];
                            time = inTrees[iVar]->getTime(iSamp);
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
                                outHistos[iVar]->SetBinContent(outHistos[iVar]->FindBin(time),data);
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
        }
};
#endif

