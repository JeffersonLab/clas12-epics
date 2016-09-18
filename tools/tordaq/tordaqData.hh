//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Mon Aug 22 14:24:33 2016 by ROOT version 5.34/21
// from TTree VT6/WF2 records
// found on file: torus_20160818_114059.root
//////////////////////////////////////////////////////////

#ifndef __TORDAQDATA_HH__
#define __TORDAQDATA_HH__

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TH1.h>
#include <TNtupleD.h>
#include <iostream>

class tordaqData {
public :
 
   static const int NVT=22;
   static const int FREQUENCY=3846;
   static const int WFLENGTH=2000;

   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   Long64_t        record_tsec;
   Long64_t        record_tnsec;
   Float_t         record_data[WFLENGTH];

   // List of branches
   TBranch        *b_record;   //!

   //tordaqData(TTree *tree=0);
   //virtual ~tordaqData();
   //virtual Int_t    Cut(Long64_t entry);
   //virtual Int_t    GetEntry(Long64_t entry);
   //virtual Long64_t LoadTree(Long64_t entry);
   //virtual void     Init(TTree *tree);
   //virtual void     Loop();
   //virtual Bool_t   Notify();
   //virtual void     Show(Long64_t entry = -1);
   //Double_t getTime(Long64_t sec,Long64_t nsec,Int_t wfLength,Int_t iSample);
   //Double_t getTime(Int_t iSample);

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
Double_t getTime(Int_t iSample)
{
    return getTime(record_tsec,record_tnsec,WFLENGTH,iSample);
}

tordaqData(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("torus_20160818_114059.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("torus.root");
      }
      f->GetObject("VT6",tree);

   }
   Init(tree);
}

~tordaqData()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("record", &record_tsec, &b_record);
   Notify();
}

Bool_t Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}

void Loop()
{
//   In a ROOT session, you can do:
//      Root > .L tordaq.C
//      Root > tordaq t
//      Root > t.GetEntry(12); // Fill t data members with entry number 12
//      Root > t.Show();       // Show values of entry 12
//      Root > t.Show(16);     // Read and show values of entry 16
//      Root > t.Loop();       // Loop on all entries
//

//     This is the loop skeleton where:
//    jentry is the global entry number in the chain
//    ientry is the entry number in the current Tree
//  Note that the argument to GetEntry must be:
//    jentry for TChain::GetEntry
//    ientry for TTree::GetEntry and TBranch::GetEntry
//
//       To read only selected branches, Insert statements like:
// METHOD1:
//    fChain->SetBranchStatus("*",0);  // disable all branches
//    fChain->SetBranchStatus("branchname",1);  // activate branchname
// METHOD2: replace line
//    fChain->GetEntry(jentry);       //read all branches
//by  b_branchname->GetEntry(ientry); //read only this branch
   if (fChain == 0) return;

   Long64_t nentries = fChain->GetEntriesFast();

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;

      std::cout<<record_tsec<<" "<<record_tnsec<<" "<<std::endl<<std::endl;
      for (int ii=0; ii<WFLENGTH; ii++)
          std::cout<<record_data[ii]<<" ";
      std::cout<<std::endl;
      getchar();
   }
}
};
#endif
