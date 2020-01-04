#include <TH1D.h>
#include <TH2D.h>
#include <TFile.h>
#include <TTree.h>
#include <TMath.h>
#include <TMath.h>
#include <TGraph.h>
#include <iostream>
#include <TCanvas.h>
#include <TRandom.h>
#include <TTimeStamp.h>

#include <string>
#include <fstream>

using namespace std;

struct scaler_record
{
  Long64_t record_tsec;
  Long64_t record_nsec;
  //Float_t record_data[2048];
  Float_t record_data[60000];
};

bool check_beam_trip(Float_t *, int);
bool check_beam_recover(Float_t *, int);

int main( int argc, char** argv )
{
  string file_name;
  string file_init_part;
  if( argc == 2 )
    {
      file_name = argv[1];
      file_init_part = file_name.substr(0, 19);
    }
  else
    {
      cout<<"Please specify file_name"<<endl;
      cout<<"The program is exiting"<<endl;
      exit(1);
    }
  cout<<"Filename initial part = "<<file_init_part<<endl;

  const int n_trees = 5;  // number of trees in the file
  //const int n_max_graphi_points = 200000; 
  const int buf_size = 60000;
  //const int n_train_groups = n_max_graphi_points/60000;
  //const int n_for_averaging = 200; // Will calculate average rates of the 1st n_for_averaging events
  const int NSA = 100; // number of buffer readings befor the suspecious event
  const int NSB = 300; // number of buffer readings after the suspecious event
  //  const double dwel = 15000./1.e9;
  const double dwel = 15000.;
  //const double min_av_rate = 10; // We assume that average rate on counters should be higher than this number
  const double microsec = 1.e3;

  //TRandom *rand1 = new TRandom();

  TTimeStamp t_stamp;

  string tree_names_[n_trees] = {"struckDaq_copy_0", "struckDaq_copy_1", "struckDaq_copy_2", "struckDaq_copy_3", "struckDaq_copy_4"};

  TCanvas *c_trip = new TCanvas("c_trip", "", 750, 750);
  TCanvas *c_recover = new TCanvas("c_recover", "", 750, 750);

  TFile *file_in = new TFile(Form("/usr/clas12/hps/DATA/waveforms/%s", file_name.c_str()), "Read");
  //TFile *file_out = new TFile(Form("skim_%s",file_name.c_str() ), "Recreate");

    // Define tree variables
  TBranch *br_record;
  //Long64_t tsec, tnsec;
  //double data[buf_size];

  scaler_record record;

  TTree *tr1_[n_trees];

  c_trip->Print(Form("Beam_trips_%s.ps[", file_init_part.c_str()));
  c_recover->Print(Form("Beam_recovers_%s.ps[", file_init_part.c_str()));
  
  // Lets loop over trees, one tree is one channel of Struk Scaler
  for( int i = 0; i < n_trees; i++ )
    {
      cout<<"Preocessing Tree "<<i<<endl;
      tr1_[i] = (TTree*)file_in->Get(Form("%s", tree_names_[i].c_str()));
      tr1_[i]->SetBranchAddress("record", &record.record_tsec,  &br_record);

      int nev = tr1_[i]->GetEntries();   // Number of entries for that particular Scaler channel
                                         // One tree event represent one Buffer (train) with a size buf_size
      
      //double average_rate = 0;
      //double average_sigma = 0;
      for( int jentry = 0; jentry < nev; jentry++ )
	{
	  tr1_[i]->GetEntry(jentry);
	  
	  TTimeStamp rootTS( (time_t)record.record_tsec,  (Int_t)record.record_nsec );
	  
	  Double_t sec = rootTS.GetSec();
	  Double_t nanosec = rootTS.GetNanoSec();
	  
	  // =============== Simulate Beam trip ===================
// 	  if( i == 2 && jentry < 10 )
// 	  {
// 	    cout<<"Simulating Beam tripp for event "<<jentry<<endl;
// 	    for( int i_buf = 0; i_buf < buf_size; i_buf++ )
// 	      {
// 		double mc_count = rand1->Gaus(45, sqrt(45.));
// 		if( i_buf > 4125 && i_buf <  4130)
// 		  {
// 		    mc_count = rand1->Gaus((45. + 45*(i_buf - 4125)), sqrt(45.));
// 		  }
// 		else if (i_buf > 9915 && i_buf < 15120)
// 		  {
// 		    mc_count = 0.;
// 		  }
// 		record.record_data[i_buf] = mc_count;
// 	      }
// 	  }
	  
	  int i_trip = 0; // just a counter that will calculate trpis in the this train
	  int i_recover = 0; // just a counter that will calculate trpis in the this train
	  // ========== Loop over the buffer ==================
	  for( int i_buf = 0; i_buf < buf_size; i_buf++ )
	    {
	      double counts = record.record_data[i_buf];
	      //double counts_1bef = record.record_data[TMath::Max(0, i_buf - 1)];  // counts of previous index in the buffer
	      //double counts_2bef = record.record_data[TMath::Max(0, i_buf - 2)];  // counts of 2 index before in the buffer
	      //double counts_1aft = record.record_data[TMath::Min(buf_size - 1, i_buf + 1)];  // counts of previous index in the buffer
	      //double counts_2aft = record.record_data[TMath::Min(buf_size - 1, i_buf + 2)];  // counts of 2 index before in the buffer
	      
	      
	      if( counts == 0 )
		{
		  bool trip = check_beam_trip( record.record_data, i_buf );

		  if( trip )
		    {
		      string timestamp1 = rootTS.AsString("lc");
		      TGraph *gr1 = new TGraph();
		      gr1->SetMarkerStyle(24);
		      gr1->SetMarkerSize(0.15);
		      gr1->SetMarkerColor(4);
		      //gr1->SetTitle(Form("%d ; time #mu s ; counts", month));
		      gr1->SetTitle(Form("channel %s , %s ; time #mu s ; counts",tree_names_[i].c_str(),  timestamp1.c_str()));
		      int i_point = 0;
		      for( int i_skim = TMath::Max(0, i_buf - NSB); i_skim < TMath::Min(buf_size, i_buf + NSA); i_skim++ )
			{
			  gr1->SetPoint(i_point, (dwel*i_skim)/microsec, record.record_data[i_skim] );
			  i_point = i_point + 1;
			}
		      gr1->Write(Form("gr_trip_%d_%d_%d", i, jentry, i_trip)); // The scaler channel, buffer number, and the trip number in the current buffer
		      gr1->Draw("AP");
		      c_trip->Print(Form("Beam_trips_%s.ps", file_init_part.c_str()));

		      i_trip = i_trip + 1;
		      i_buf = i_buf + NSA + 1;
		    }
		}
	      else if( counts > 5 )
		{
		  bool recover = check_beam_recover(record.record_data, i_buf);
		  
		  if( recover )
		    {	
		      string timestamp1 = rootTS.AsString("lc");
		      TGraph *gr1 = new TGraph();
		      gr1->SetMarkerStyle(24);
		      gr1->SetMarkerSize(0.15);
		      gr1->SetMarkerColor(2);
		      gr1->SetTitle(Form("channel: %s ,   %s; time #mu s ; counts",tree_names_[i].c_str(),  timestamp1.c_str()));
		      //gr1->SetTitle(Form("%s ; time #mu s ; counts", timestamp1.c_str()));
		      int i_point = 0;
		      for( int i_skim = TMath::Max(0, i_buf - NSA); i_skim < TMath::Min(buf_size, i_buf + NSB); i_skim++ )  // For recover NSA (NSB) actually means NSB (NSA)
			{
			  gr1->SetPoint(i_point, (sec + nanosec + dwel*i_skim)*microsec, record.record_data[i_skim] );
			  i_point = i_point + 1;
			}
		      gr1->Write(Form("gr_recover_%d_%d_%d", i, jentry, i_recover)); // The scaler channel, buffer number, and the recover number in the current buffer
		      gr1->Draw("AP");
		      c_recover->Print(Form("Beam_recovers_%s.ps", file_init_part.c_str()));
		      i_recover = i_recover + 1;
		      i_buf = i_buf + NSA + 1;
		    }
		}
	      
	    }
	}
      
    }

  c_trip->Print(Form("Beam_trips_%s.ps]", file_init_part.c_str()));
  c_recover->Print(Form("Beam_recovers_%s.ps]", file_init_part.c_str()));

}

bool check_beam_trip(Float_t *buffer, int index)
{
  bool trip = true;
  if( index > 30 && buffer[index - 29] > 1 && buffer[index - 28] > 1 && buffer[index - 27] > 1 && buffer[index - 26] > 1)
    {
      trip = true;
    }
  else
    {return false;}
  
  for( int i = 0; i < 25; i++ )
    {
      if( buffer[TMath::Max(index - i, 0)] != 0 )
	{
	  trip = false;
	}
    }
  return trip;
}

bool check_beam_recover(Float_t *buffer, int index)
{
  bool recover = true;

  for( int i = 0; i < 40; i++ )
    {
      if( buffer[TMath::Max(index - i - 1, 0)] > 1.5 )
	{
	  return false;
	}
    }

  return recover;
}


// 		      TGraph *gr1 = new TGraph();
// 		      gr1->SetMarkerStyle(24);
// 		      gr1->SetMarkerSize(0.15);
// 		      gr1->SetMarkerColor(4);
// 		      int i_point = 0;
// 		      for( int i_skim = TMath::Max(0, i_buf - NSB); i_skim < TMath::Min(buf_size, i_buf + NSA); i_skim++ )
// 			{
// 			  gr1->SetPoint(i_point, sec + nanosec + dwel*i_skim, record.record_data[i_skim] );
// 			  i_point = i_point + 1;
// 			}
// 		      gr1->Write(Form("gr_%d_%d_%d", i, jentry, i_trip)); // The scaler channel, buffer number, and the trip number in the current buffer
// 		      i_trip = i_trip + 1;
// 		      i_buf = i_buf + NSA + 1;
