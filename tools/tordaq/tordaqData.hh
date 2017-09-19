#ifndef __TORDAQDATA_HH__
#define __TORDAQDATA_HH__
#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TKey.h>
#include <TH1.h>
#include <iostream>
#include <vector>
#include <string>

// (will keep them in this order, and then numerical order)
static const char* VARSTUBS[]={"VT","IDCCT",NULL};

class tordaqData {
private:

public :
   
   std::vector <std::string> varnames;
   std::vector <std::string> varstubs;

   // Frequency (Hz) of samples in EPICS waveform: 
   static const int FREQUENCY=10000;
   
   // EPICS waveform length:
   static const int WFLENGTH=2000;

   // EPICS update period (nanoseconds):
   static const Long64_t UPDATEPERIOD = 1e9*WFLENGTH/FREQUENCY;

   TTree          *fChain=NULL;
   Int_t           fCurrent;
   Long64_t        record_tsec;
   Long64_t        record_tnsec;
   Float_t         record_data[WFLENGTH];
   TBranch        *b_record;
   Long64_t        first_sec; 
   Long64_t        first_nsec; 

   tordaqData() {
       varstubs = getTreeStubs();
   }

   tordaqData(TTree *tree) : fChain(0) 
   {
       varstubs = getTreeStubs();

       if (tree)
       {
           fChain = tree;
           fCurrent = -1;
           fChain->SetMakeClass(1);
           fChain->SetBranchAddress("record", &record_tsec, &b_record);
       }
       else std::cerr<<"tordaqData:: Error Reading tree"<<std::endl;
       
       storeFirstTimestamp();
   }

   Double_t getTime(Long64_t sec,Long64_t nsec,Int_t iSample)
   {
       // Reported timestamp corresponds to first sample of waveform.
       // Assume time between waveform samples is 1/FREQUENCY.
       return sec + nsec/1e9 + (Double_t)iSample/FREQUENCY;
   }
   
   Double_t getTime(Int_t iSample)
   {
       return getTime(record_tsec,record_tnsec,iSample);
   }

   // getJitterlessTime
   //
   // Assume the first timestamp in the file to be exact,
   // and use it to remove jitter from all future timestamps,
   // based on assumption that period between readouts is
   // always a fixed multiple of UPDATEPERIOD.
   //
   // This jitter correction only needs to operate on the
   // nanosecond portion of the timestamp.
   //
   Double_t getJitterlessTime(Long64_t sec,Long64_t nsec,Int_t iSample)
   {
       // relative time since first reading, offset by a number of periods:
       const Long64_t relative_nsec = nsec - first_nsec + 10*UPDATEPERIOD;

       // take modulus to get jitter (with half-periods to wrap properly):
       const Long64_t jitter = (relative_nsec + UPDATEPERIOD/2) % UPDATEPERIOD - UPDATEPERIOD/2;

       // correct time for jitter:
       const Long64_t jitterless_nsec = nsec - jitter;

       return getTime(sec,jitterless_nsec,iSample);
   }
   Double_t getJitterlessTime(Int_t iSample)
   {
       return getJitterlessTime(record_tsec,record_tnsec,iSample);
   }
   
   void storeFirstTimestamp()
   {
       LoadTree(0);
       fChain->GetEntry(0);
       first_sec = record_tsec;
       first_nsec = record_tnsec;
   }

   static std::vector <std::string> getTreeNames()
   {
       int ii=0;
       std::vector <std::string> ss;
       while (VARSTUBS[ii])
       {
           for (int jj=0; jj<100; jj++)
               if (gDirectory->Get(Form("%s%d",VARSTUBS[ii],jj)))
                   ss.push_back(Form("%s%d",VARSTUBS[ii],jj));
           ii++;
       }
       return ss;
   }
   
   static std::vector <std::string> getTreeStubs()
   {
       int ii=0;
       std::vector <std::string> ss;
       while (VARSTUBS[ii])
       {
           ss.push_back(Form("%s",VARSTUBS[ii]));
           ii++;
       }
       return ss;
   }

   void setTreeNames() { varnames=getTreeNames(); }

   ~tordaqData()
   {
       if (fChain) delete fChain->GetCurrentFile();
   }

   Long64_t LoadTree(Long64_t entry)
   {
       if (!fChain) return -5;
       Long64_t centry = fChain->LoadTree(entry);
       if (centry < 0) return centry;
       if (fChain->GetTreeNumber() != fCurrent) fCurrent = fChain->GetTreeNumber();
       return centry;
   }

   // this is for manually testing input wf2root files:
   void Loop()
   {
       if (fChain == 0) return;
       Long64_t nentries = fChain->GetEntriesFast();
       Long64_t nbytes = 0, nb = 0;
       for (Long64_t jentry=0; jentry<nentries;jentry++) {
           Long64_t ientry = LoadTree(jentry);
           if (ientry < 0) break;
           nb = fChain->GetEntry(jentry);   nbytes += nb;
           std::cout<<record_tsec<<" "<<record_tnsec<<" "<<std::endl<<std::endl;
           //for (int ii=0; ii<WFLENGTH; ii++)
           //    std::cout<<record_data[ii]<<" ";
           std::cout<<std::endl;
           getchar();
       }
   }

   TH1* getHisto()
   {
       if (fChain == 0) return NULL;
       fChain->LoadTree(0);
       fChain->GetEntry(0);
       const double tMin=getTime(0);
       fChain->LoadTree(fChain->GetEntriesFast()-1);
       fChain->GetEntry(fChain->GetEntriesFast()-1);
       const double tMax=getTime(WFLENGTH-1);
       const int nBins=(tMax-tMin)/FREQUENCY;
       TH1F *hh=new TH1F(Form("h%d",fChain->GetName()),"",nBins,tMin,tMax);
       for (Long64_t jentry=0; jentry<fChain->GetEntriesFast(); jentry++) {
           if (LoadTree(jentry)) break;
           fChain->GetEntry(jentry);
           for (int ii=0; ii<WFLENGTH; ii++)
           {
               const Double_t tt=getTime(ii);
               hh->SetBinContent(hh->GetXaxis()->FindBin(tt),record_data[ii]);
           }
       }
       return hh;
   }

};
#endif
