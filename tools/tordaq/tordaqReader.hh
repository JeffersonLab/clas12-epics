
#ifndef __TORDAQREADER__HH
#define __TORDAQREADER__HH

#include "tordaqData.hh"

#include <TNtupleD.h>
#include <TGProgressBar.h>
#include <iomanip>

class tordaqReader {
private:
    const char* asciiDelimiter=",";
    TFile *inFile=NULL;
    std::vector <tordaqData*> inTrees;

public:
    tordaqReader(){};
    ~tordaqReader(){};
    TString inFilename="";
    TString outAsciiFilename="";
    TString outRootFilename="";
    Long64_t maxSamples=-1;
    Long64_t startTime=-1;
    Long64_t endTime=-1;
    bool rubenTime=false;
    bool makeHistos=false;
    bool makeNtuple=false;
    FILE *outAsciiFile=NULL;
    TNtupleD *outTree=NULL;
    TFile *outRootFile=NULL;
    TGHProgressBar *progressMeter=NULL;
    bool doSynchroAna=false;
    bool forceSynchro=false;
    bool removeJitter=false;
    bool saveSynchroPlots=false;
    bool isTorus=true;
    bool isSolenoid=true;
    tordaqData tdData;
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
        if (frac>0.15)
        {
            if (timeRemain>0) printf("]  ETA:  %d sec          \r",timeRemain);
            else              printf("]                  \r");
        }
        else                  printf("]  ETA:  ?? sec          \r");
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
        // open the input file:
        if (inFilename!="") {
            if (gSystem->AccessPathName(inFilename))
            {
                std::cerr<<"Missing input file:  "<<inFilename<<std::endl;
                return false;
            }
            if (inFile) inFile->Close();
            std::cout<<"tordaqReader:  Reading "+inFilename+" ....."<<std::endl;
            inFile=new TFile(inFilename,"READ");
        }

        // stop leaking memory upon opening another file:
        for (unsigned int ii=0; ii<outHistos.size(); ii++) 
            if (outHistos[ii]) delete outHistos[ii];

        // determine the variable names based on file contents:
        tdData.setTreeNames();

        //std::vector <std::string> VARNAMES=tdData.getTreeNames();
        
        // find the input TTrees:
        inTrees.clear();
        outHistos.clear();
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
                std::string sep="";
                std::string varnames="";
                for (unsigned int ii=0; ii<tdData.VARNAMES.size(); ii++)
                {
                    varnames += sep+"t"+tdData.VARNAMES[ii];
                    varnames += ":"+tdData.VARNAMES[ii];
                    sep=":";
                }
                std::cerr<<varnames<<std::endl;
                outTree=new TNtupleD("tordaq","",varnames.c_str());
            }
        }

/*
        // bin each histo independently based on its channels' min/max times:
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
                    outHistos.push_back(new TH1F("h"+vn,";;"+vn,nBins,t0,t0+(double)nBins/tordaqData::FREQUENCY));
                }
                else
                {
                    std::cerr<<"tordaqReader:  Error Reading TTree:  "<<inTrees[ii]->fChain->GetName()<<std::endl;
                    return false;
                }
            }
        }
*/       
        // use the same binning for all histos:
        // NABO:  MODIFY TO USE ONLY inTrees[0]'s TIMESTAMPS IF forceSynchro=true
        if (makeHistos)
        {
            // choose time limits:
            Double_t time0=-1,time1=-1;
            for (unsigned int ii=0; ii<inTrees.size(); ii++)
            {
                if (inTrees[ii]->LoadTree(0) < 0) continue;
                else
                {
                    inTrees[ii]->fChain->GetEntry(0);
                    if (time0<0 || inTrees[ii]->getTime(0)<time0)
                        time0 = inTrees[ii]->getTime(0);
                }
                if (inTrees[ii]->LoadTree(inTrees[ii]->fChain->GetEntries()-1) < 0) continue;
                else
                {
                    inTrees[ii]->fChain->GetEntry(inTrees[ii]->fChain->GetEntries()-1);
                    if (time1<0 || inTrees[ii]->getTime(tordaqData::WFLENGTH-1)>time1)
                        time1 = inTrees[ii]->getTime(tordaqData::WFLENGTH-1);
                }
            }

            // make histos for raw data:
            if (time0>0 && time1>0)
            {
              for (unsigned int ii=0; ii<inTrees.size(); ii++)
              {
                const Double_t t0 = time0 - 0.5/tordaqData::FREQUENCY;
                const Double_t t1 = time1 + 0.5/tordaqData::FREQUENCY;
                const int nBins=(t1-t0)*tordaqData::FREQUENCY+1;
                const TString vn=inTrees[ii]->fChain->GetName();
                outHistos.push_back(new TH1F("h"+vn,";;"+vn,nBins,t0,t0+(double)nBins/tordaqData::FREQUENCY));
              }
            }
            else
            {
              std::cerr<<"tordaqReader:  Error Reading TTrees:  (no good times)."<<std::endl;
              return false;
            }
        }

        // print warning messages about synchronization:
        if (doSynchroAna) std::cout<<std::endl<<"Performing synchronization analysis.  MEMORY INTENSIVE!"<<std::endl;
        if (forceSynchro) std::cout<<std::endl<<"FORCING SYNCHRONIZATION!"<<std::endl;
        if (removeJitter) std::cout<<std::endl<<"REMOVING JITTER!"<<std::endl;
        std::cout<<std::endl;

        // setup dynamically allocated stuff:
        std::vector <double> lastUpdateTime;
        std::vector <bool> skipVars;
        std::vector < std::vector <int> > sampleFills;
        std::vector < TH1* > updatePeriod;
        for (unsigned int ii=0; ii<inTrees.size(); ii++) 
        {
            skipVars.push_back(false);
            if (doSynchroAna)
            {
                // this is memory-intensive:
                std::vector <int> mm;
                for (int jj=0; jj<outHistos[ii]->GetNbinsX(); jj++) mm.push_back(0);
                sampleFills.push_back(mm);
                // this is harmless:
                double kk=-1;
                lastUpdateTime.push_back(kk);
                updatePeriod.push_back(new TH1D(Form("hUpdatePeriod%s",inTrees[ii]->fChain->GetName()),"",200000,-100,100));
            }
        }

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

        /*
        // print a header row in the ascii file:
        if (outAsciiFile)
        {
            for (unsigned int iVar=0; iVar<inTrees.size(); iVar++)
            {
                fprintf(outAsciiFile,"%s%s%s%12f",inTrees[iVar].GetName());
            }
        }
        */

        // the loop over all the data:
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
                    if (doSynchroAna)
                    {
                        if (lastUpdateTime[iVar]>0)
                            updatePeriod[iVar]->Fill(time-lastUpdateTime[iVar]);
                        lastUpdateTime[iVar]=time;
                    }
                }
            }

            // all times are too late, we can just stop reading:
            if (allLate) break;

            // all times are too early, skip to next entry:
            if (allEarly) continue;

            for (int iSamp=0; iSamp<tordaqData::WFLENGTH; iSamp++)
            {
                // if forcing synchronization, require that all trees are good:
                if (forceSynchro)
                    for (unsigned int iVar=0; iVar<inTrees.size(); iVar++)
                        if (skipVars[iVar]) continue;

                char sep[1]="";
                for (unsigned int iVar=0; iVar<inTrees.size(); iVar++)
                {
                    strcpy(stime,"0000:00:00 00:00:00: 0.0000");
                    Double_t time=0,data=0;
                    ntupleVars[2*iVar]=ntupleVars[2*iVar+1]=0;
                    if (!skipVars[iVar])
                    {
                        // get time and data for this sample:
                        data = inTrees[iVar]->record_data[iSamp];
                        if (removeJitter) {
                            if (forceSynchro) time = inTrees[0]->getJitterlessTime(
                                                                 inTrees[iVar]->record_tsec,
                                                                 inTrees[iVar]->record_tnsec,
                                                                 iSamp);
                            else              time = inTrees[iVar]->getJitterlessTime(iSamp);
                        }
                        else {
                            if (forceSynchro) time = inTrees[0]->getTime(iSamp);
                            else              time = inTrees[iVar]->getTime(iSamp);
                        }

                        ntupleVars[2*iVar]=time;
                        ntupleVars[2*iVar+1]=data;

                        // convert to Ruben's time format:
                        if (rubenTime)
                        {
                            const time_t timet=(int)time;
                            const struct tm* structtm=localtime(&timet);
                            strftime(stime,ASCIITIMELENGTH,"%Y:%m:%d %H:%M:%S",structtm);
                            sprintf(stime,"%s %.4f",stime,time-(int)time);
                        }

                        // fill histograms:
                        if (makeHistos)
                        {
                            const int bin=outHistos[iVar]->FindBin(time);
                            outHistos[iVar]->SetBinContent(bin,data);
                            if (doSynchroAna) sampleFills[iVar][bin-1]++;
                        }
                    }

                    // print to the pointless ascii file:
                    if (outAsciiFile)
                    {
                        if (rubenTime) fprintf(outAsciiFile,"%s%s%s%12f",sep,stime,asciiDelimiter,data);
                        else           fprintf(outAsciiFile,"%s%18.4f%s%12f",sep,time,asciiDelimiter,data);
                    }
                    strcpy(sep,asciiDelimiter);
                }

                // end-of-event closures:
                if (outAsciiFile) fprintf(outAsciiFile,"\n");
                if (outTree) outTree->Fill(ntupleVars);

                // call it quits:
                if (++nSamples>=maxSamples && maxSamples>0)
                {
                    tooManySamples=1;
                    break;
                }
            }
            if (tooManySamples) break;
        }



        if (doSynchroAna)
        {
            // print out duplicates and missing samples info:
            std::cout<<std::endl<<std::endl<<std::endl;
            std::cout<<"*###########################################################################"<<std::endl;
            std::cout<<"*###########################################################################"<<std::endl;
            std::cout<<"*################# Syncrhonization Analysis Report #########################"<<std::endl;
            std::cout<<"*"<<std::endl;
            std::cout<<"* Output format:  (Number of Occurences / Fraction of Total)"<<std::endl;
            std::cout<<"*"<<std::endl;
            std::cout<<"*###################### Timestamps #########################################"<<std::endl;
            std::cout<<"* "<<std::endl;
            std::cout<<"* These should all be exactly zero.  Anything non-zero is a problem."<<std::endl;
            std::cout<<"* "<<std::endl;
            for (unsigned int ii=0; ii<updatePeriod.size(); ii++)
            {
                TH1* h=updatePeriod[ii];
                const double total=h->GetEntries();
                const double duplicates=h->Integral(h->FindBin(-0.1),h->FindBin(0.1));
                const double misses=h->Integral(h->FindBin(0.3),h->GetNbinsX());
                fprintf(stdout,"*%7s:   Duplicates = (%.1E / %.2f%%)    Missed = (%.1E / %.2f%%)\n",
                        inTrees[ii]->fChain->GetName(),
                        duplicates,100*duplicates/total,
                        misses,100*misses/total);
            }
            std::cout<<"* "<<std::endl;
            std::cout<<"* "<<std::endl;
            std::cout<<"*####################### Samples ###########################################"<<std::endl;
            std::cout<<"* "<<std::endl;
            std::cout<<"* Here if Missed and Overlaps are similar and small,"<<std::endl;
            std::cout<<"*\tthen that *can* be due just to timestamp jitter."<<std::endl;
            std::cout<<"*"<<std::endl;
            for (unsigned int ii=0; ii<sampleFills.size(); ii++)
            {
                int nDuplicates=0,nMissing=0;
                for (unsigned int jj=0; jj<sampleFills[ii].size(); jj++)
                {
                    if      (sampleFills[ii][jj]>1) nDuplicates++;
                    else if (sampleFills[ii][jj]<1) nMissing++;
                }
                if (nDuplicates>0 || nMissing>0)
                {
                    const double fracDuplicates=100*(double)nDuplicates/outHistos[ii]->GetNbinsX();
                    const double fracMissing   =100*(double)nMissing   /outHistos[ii]->GetNbinsX();
                    fprintf(stdout,"*%7s:   Overlaps = (%.1E / %.2f%%)    Missed = (%.1E / %.2f%%)\n",
                            inTrees[ii]->fChain->GetName(),
                            (float)nDuplicates,fracDuplicates,
                            (float)nMissing,fracMissing);
                }                
            }
            std::cout<<"*"<<std::endl;
            std::cout<<"*###########################################################################"<<std::endl;
            std::cout<<"*###########################################################################"<<std::endl;
            std::cout<<std::endl;

            // free up memory:
            for (unsigned int ii=0; ii<sampleFills.size(); ii++) 
              sampleFills[ii].resize(0);
            sampleFills.resize(0);
            
            // write out synchro analysis plots:
            if (saveSynchroPlots)
            {
              TFile *fout=new TFile("tordaqSynchroAna.root","RECREATE");
              if (fout)
              {
                for (unsigned int ii=0; ii<updatePeriod.size(); ii++)
                {
                  updatePeriod[ii]->SetDirectory(fout);
                  updatePeriod[ii]->Write();
                }
                fout->Close();
              }
            }
        }
        
        std::cout<<std::endl<<"tordaqReader:  Finished Reading File."<<std::endl;

        if (true && makeHistos)
        {
          std::cout<<"tordaqReader:  Making Comparators ... ";
          TH1 *hh[100];
          bool foundComparatorInputs=true;
          for (unsigned int ii=0; ii<outHistos.size(); ii++)
          {
            for (int jj=1; jj<22; jj++)
            {
              if (strcmp(outHistos[ii]->GetName(),Form("hVT%d",jj))==0)
              {
                hh[jj]=outHistos[ii];
                break;
              }
            }
          }
          for (int ii=1; ii<22; ii++)
          {
            if (!hh[ii])
            {
              std::cerr<<std::endl<<"tordaqReader:  Error finding comparator input:  "<<Form("VT%d",ii)<<std::endl;
              foundComparatorInputs=false;
            }
          }
          if (!foundComparatorInputs)
          {
            std::cerr<<std::endl<<"tordaqReader:  Proceeding without making comparators."<<std::endl;
          }
          else
          {

              // !!!!we need to be able to delete this upon opening new file!!!!!!

            if (isTorus) {

                std::cout<<" C4"<<std::flush;

                TH1* hV1 =(TH1*)hh[5] ->Clone("hV1"); hV1->Add(hh[6]);  hV1->Add(hh[7]);
                TH1* hV2 =(TH1*)hh[7] ->Clone("hV2"); hV2->Add(hh[8]);  hV2->Add(hh[9]);
                TH1* hV3 =(TH1*)hh[9] ->Clone("hV3"); hV3->Add(hh[10]); hV3->Add(hh[11]);
                TH1* hV4 =(TH1*)hh[11]->Clone("hV4"); hV4->Add(hh[12]); hV4->Add(hh[13]);

                //TH1* hV5 =(TH1*)hh[13]->Clone("hV5"); hV4->Add(hh[14]); hV4->Add(hh[15]);
                //TH1* hV6 =(TH1*)hh[15]->Clone("hV6"); hV4->Add(hh[16]); hV4->Add(hh[17]);
                //TH1* hV7 =(TH1*)hh[3] ->Clone("hV7"); hV7->Add(hh[4]);  hV7->Add(hh[5]);
                //TH1* hV15=(TH1*)hh[17]->Clone("hV15");hV15->Add(hh[18]);hV15->Add(hh[19]);

                TH1* hV12 =(TH1*)hV1->Clone("hV12"); hV12->Add(hV2);
                TH1* hV34 =(TH1*)hV3->Clone("hV34"); hV34->Add(hV4);
                //TH1* hV56 =(TH1*)hV5->Clone("hV56"); hV56->Add(hV6);

                //TH1* hC1 =(TH1*)hV1->Clone("hC1");  hC1->Add(hV2,-1);
                //TH1* hC2 =(TH1*)hV3->Clone("hC2");  hC2->Add(hV4,-1);
                //TH1* hC3 =(TH1*)hV5->Clone("hC3");  hC3->Add(hV6,-1);
                TH1* hC4 =(TH1*)hV12->Clone("hC4"); hC4->Add(hV34,-1);
                //TH1* hC5 =(TH1*)hV34->Clone("hC5"); hC5->Add(hV56,-1);
                //TH1* hC6 =(TH1*)hV56->Clone("hC6"); hC6->Add(hV12,-1);
                //TH1* hC7 =(TH1*)hV7->Clone("hC7");  hC7->Add(hV15,-1);

                //TH1* hC8  =(TH1*)hh[3]->Clone("hC8");  hC8->Add(hh[19],-1);
                //TH1* hC9  =(TH1*)hh[2]->Clone("hC9");  hC9->Add(hh[20],-1);
                //TH1* hC10 =(TH1*)hh[1]->Clone("hC10"); hC10->Add(hh[21],-1);

                tdData.VARNAMES.push_back("C4");
                outHistos.push_back(hC4);
            }

/*
               Sol_QD1 : -(VT5_DAQ+VT6_DAQ+VT7_DAQ+VT8_DAQ+VT9_DAQ+VT10_DAQ) + (VT11_DAQ+VT12_DAQ+VT13_DAQ+VT14_DAQ)
               Sol_QD2 : (VT5_DAQ+VT6_DAQ+VT7_DAQ+VT8_DAQ ) - (VT9_DAQ+VT10_DAQ+VT11_DAQ+VT12_DAQ+VT13_DAQ+VT14_DAQ)
               Sol_QD3 : (VT15_DAQ+VT16_DAQ+VT17_DAQ+VT18_DAQ+VT19_DAQ)
               Sol_QD4 : (VT17_DAQ+VT18_DAQ+VT19_DAQ)
               Sol_QD5 : (VT5_DAQ+VT4_DAQ+VT3_DAQ+VT2_DAQ+VT1_DAQ)
               Sol_QD6 : (VT3_DAQ+VT2_DAQ+VT1_DAQ)
               Sol_QD7 : (VT5_DAQ+VT4_DAQ+VT3_DAQ+VT2_DAQ)
               Sol_QD8 : (VT15_DAQ+VT16_DAQ+VT17_DAQ+VT18_DAQ)
*/

            if (isSolenoid) {
                std::cout<<" QD1"<<std::flush;
                TH1* hQD1=(TH1*)hh[11]->Clone("hQD1");
                hQD1->Add(hh[12]);
                hQD1->Add(hh[13]);
                hQD1->Add(hh[14]);
                hQD1->Add(hh[5],-1);
                hQD1->Add(hh[6],-1);
                hQD1->Add(hh[7],-1);
                hQD1->Add(hh[8],-1);
                hQD1->Add(hh[9],-1);
                hQD1->Add(hh[10],-1);
                std::cout<<",QD2"<<std::flush;
                TH1* hQD2=(TH1*)hh[5]->Clone("hQD2");
                hQD2->Add(hh[6]);
                hQD2->Add(hh[7]);
                hQD2->Add(hh[8]);
                hQD2->Add(hh[9], -1);
                hQD2->Add(hh[10], -1);
                hQD2->Add(hh[11],-1);
                hQD2->Add(hh[12],-1);
                hQD2->Add(hh[13],-1);
                hQD2->Add(hh[14],-1);
                std::cout<<",QD3"<<std::flush;
                TH1* hQD3=(TH1*)hh[15]->Clone("hQD3");
                hQD3->Add(hh[16]);
                hQD3->Add(hh[17]);
                hQD3->Add(hh[18]);
                hQD3->Add(hh[19]);
                std::cout<<",QD4"<<std::flush;
                TH1* hQD4=(TH1*)hh[17]->Clone("hQD4");
                hQD4->Add(hh[18]);
                hQD4->Add(hh[19]);
                std::cout<<",QD5"<<std::flush;
                TH1* hQD5=(TH1*)hh[1]->Clone("hQD5");
                hQD5->Add(hh[2]);
                hQD5->Add(hh[3]);
                hQD5->Add(hh[4]);
                hQD5->Add(hh[5]);
                std::cout<<",QD6"<<std::flush;
                TH1* hQD6=(TH1*)hh[1]->Clone("hQD6");
                hQD6->Add(hh[2]);
                hQD6->Add(hh[3]);
                std::cout<<",QD7";
                TH1* hQD7=(TH1*)hh[2]->Clone("hQD7");
                hQD7->Add(hh[3]);
                hQD7->Add(hh[4]);
                hQD7->Add(hh[5]);
                std::cout<<",QD8"<<std::flush;
                TH1* hQD8=(TH1*)hh[15]->Clone("hQD8");
                hQD8->Add(hh[16]);
                hQD8->Add(hh[17]);
                hQD8->Add(hh[18]);

                tdData.VARNAMES.push_back("QD1");  outHistos.push_back(hQD1);
                tdData.VARNAMES.push_back("QD2");  outHistos.push_back(hQD2);
                tdData.VARNAMES.push_back("QD3");  outHistos.push_back(hQD3);
                tdData.VARNAMES.push_back("QD4");  outHistos.push_back(hQD4);
                tdData.VARNAMES.push_back("QD5");  outHistos.push_back(hQD5);
                tdData.VARNAMES.push_back("QD6");  outHistos.push_back(hQD6);
                tdData.VARNAMES.push_back("QD7");  outHistos.push_back(hQD7);
                tdData.VARNAMES.push_back("QD8");  outHistos.push_back(hQD8);
            }

            std::cout<<std::endl<<"tordaqReader:  Finished Making Comparators."<<std::endl;
          }
        }

      
        if (inFile) inFile->Close();
        if (outAsciiFile) fclose(outAsciiFile);
        return true;
    }
};
#endif

