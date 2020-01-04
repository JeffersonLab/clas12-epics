#define WaveformTree_cxx

#include <iostream>
#include <iomanip>

#include "WaveformTree.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TTimeStamp.h>

using namespace std;

void WaveformTree::Loop()
{
//   In a ROOT session, you can do:
//      Root > .L WaveformTree.C
//      Root > WaveformTree t
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

   Double_t waveformIncrement = 1.0e-06;
//   Double_t waveformIncrement = 1.1e-06;
   Double_t nextNumberExpected = 0;
   Double_t errToler  =    1.0e-08;

   ULong_t  waveformPatternPeriod = 100;

   Long64_t nentries = fChain->GetEntriesFast();

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      if( jentry % 100000 == 0 ) {
    	  cout << "Looking at entry " << jentry << endl;
      }
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      TTimeStamp rootTS( (time_t)record_tsec,  (Int_t)record_tnsec );
//      rootTS.Add( -TTimeStamp::GetZoneOffset() );
//      cout << "Entry #" << ientry << " taken at " << rootTS.AsString("lc") << " has data : " << endl;
      for ( int iData = 0; iData < 2048; iData++ ) {
//     	  if( iData % waveformPatternPeriod == 0 ) {
// //    		  cout << setiosflags(ios::fixed) << setprecision(7) << record_data[iData] << " " ;
//         	  if( iData == 0 ) nextNumberExpected = record_data[iData];
//         	  else nextNumberExpected += waveformIncrement;
//     	  }
	  cout << "Recorded point " << iData << " has value " << record_data[iData] << " at " << rootTS.AsString("lc") << endl;
// 	  if( TMath::Abs( record_data[iData] - nextNumberExpected ) > errToler ) {
// 	    cout << " Wrong data : Entry taken at " << rootTS.AsString("lc") << " is expected to be " <<
// 	      setiosflags(ios::fixed) << setprecision(7) << nextNumberExpected << " but is " <<
// 	      record_data[iData] << endl ;
// 	  }
      }
//       cout << endl << endl;
      // if (Cut(ientry) < 0) continue;
   }
}
