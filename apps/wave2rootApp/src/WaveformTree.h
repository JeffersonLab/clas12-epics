//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Mon Dec 17 09:48:45 2012 by ROOT version 5.34/01
// from TTree halld-pxi:array:vtt7/PXI records
// found on file: /local/scratch/PXI_DATA/ROOT/pxi_2012-12-14_16:02:11.root
//////////////////////////////////////////////////////////

#ifndef WaveformTree_h
#define WaveformTree_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

// Fixed size dimensions of array or collections stored in the TTree if any.

class WaveformTree {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   Long64_t        record_tsec;
   Long64_t        record_tnsec;
   Float_t         record_data[2048];

   // List of branches
   TBranch        *b_record;   //!

   WaveformTree(TTree *tree=0);
   virtual ~WaveformTree();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef WaveformTree_cxx
WaveformTree::WaveformTree(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("/usr/clas12/hps/DATA/waveforms/w2r_20141215_185715.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("/usr/clas12/hps/DATA/waveforms/w2r_20141215_185715.root");
      }
      f->GetObject("sixtyHz_raw_14",tree);

   }
   Init(tree);
}

WaveformTree::~WaveformTree()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t WaveformTree::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t WaveformTree::LoadTree(Long64_t entry)
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

void WaveformTree::Init(TTree *tree)
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

Bool_t WaveformTree::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void WaveformTree::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t WaveformTree::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef WaveformTree_cxx
