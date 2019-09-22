#include <TH1D.h>
#include <TH2D.h>
#include <TFile.h>
#include <TTree.h>
#include <TGraph.h>
#include <iostream>
#include <TCanvas.h>
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

int main(int argc, char** argv)
{

  string file_name;
  string file_init_part;
  if( argc == 2 )
    {
      file_name = argv[1];
      file_init_part = file_name.substr(0, 17);
    }
  else
    {
      cout<<"Please specify file_name"<<endl;
      cout<<"The program is exiting"<<endl;
      exit(1);
    }
  
  cout<<"Filename initial part = "<<file_init_part<<endl;

  const int n_trees = 5;  // number of trees in the file
  const int n_max_graphi_points = 200000; 
  const int buf_size = 60000;
  const int n_train_groups = n_max_graphi_points/60000;

  //  const int buf_size = 2048;

  TCanvas *c1 = new TCanvas("c1", "", 2000, 1000);

  TTimeStamp t_stamp;

  //  string tree_names_[n_trees] = {"sixtyHz_0", "sixtyHz_1", "sixtyHz_2", "sixtyHz_3", "sixtyHz_6", "sixtyHz_7", "sixtyHz_8", "sixtyHz_9", "sixtyHz_10", "sixtyHz_11", "sixtyHz_12", "sixtyHz_13", "sixtyHz_14", "sixtyHz_15"};

  string tree_names_[n_trees] = {"struckDaq_copy_0", "struckDaq_copy_1", "struckDaq_copy_2", "struckDaq_copy_3", "struckDaq_copy_4"};
  //string tree_names_[n_trees] = {"sixtyHz_15"};


  TFile *file_in = new TFile(Form("/usr/clas12/hps/DATA/waveforms/%s", file_name.c_str()), "Read");
  TFile *file_out = new TFile(Form("out_%s",file_name.c_str() ), "Recreate");

  // Define tree variables
  TBranch *br_record;
  Long64_t tsec, tnsec;
  double data[buf_size];

  scaler_record record;

  TTree *tr1_[n_trees];

  TGraph *gr_60Hz_[n_trees];

  // Initialize trees

  //ofstream out_dat("test_log.dat"); // just test log file, will be removed, when code is defined working
  for(int i = 0; i < n_trees; i++)
    {
      cout<<"Preocessing Tree "<<i<<endl;
      tr1_[i] = (TTree*)file_in->Get(Form("%s", tree_names_[i].c_str()));
      tr1_[i]->SetBranchAddress("record", &record.record_tsec,  &br_record);
      gr_60Hz_[i] = new TGraph();

      int nev = tr1_[i]->GetEntries();   // NUmber of entries for that particular Scaler channel
      
      int n_of_graphs = nev/n_train_groups + 1;
      
      TGraph *gr_Struk_chan_[n_of_graphs];

      for( int jj = 0; jj < n_of_graphs; jj++ )
	{
	  gr_Struk_chan_[jj] = new TGraph();
	}

      cout<<"nev = "<<nev<<endl;

      //Long64_t t0 = 0;
      Double_t t0 = 0;
      //for( int jentry = 0; jentry < 300; jentry++ )
      for( int jentry = 0; jentry < nev; jentry++ )
	{
	  tr1_[i]->GetEntry(jentry);
	  
	  TTimeStamp rootTS( (time_t)record.record_tsec,  (Int_t)record.record_nsec );
	  
	  int gr_index = jentry/n_train_groups;
	  
	  Double_t sec = rootTS.GetSec();
	  Double_t nanosec = rootTS.GetNanoSec();
	  
	  Double_t cur_t = sec + nanosec/1.e9;
	  
// 	  cout<<cur_t<<endl;
// 	  cout <<" at " << rootTS.AsString("lc") << endl;
// 	  cout<<"nanosec "<<rootTS.GetNanoSec()<<endl;
// 	  cout<<"sec = "<<rootTS.GetSec()<<endl;
// 	  cout<<"jentry = "<<jentry<<endl;

	  if( jentry == 0 )
	    {
	      t0 = sec + nanosec/1.e9;
	    }
	  int gr_sub_index = jentry%n_train_groups; // This will show the train number in the graph e.g. can be 0, 1, 2, 3, ... n_train_groups

	  for( int jj = 0; jj < buf_size; jj++ )
	    {
	      if( i == 0 &&  record.record_data[jj] < 300 )
		{
		  cout<<"============================================ counts = "<<record.record_data[jj]<<endl;
		}
	      //gr_60Hz_[i]->SetPoint(jentry*buf_size + jj, cur_t - t0 + 15000.*Double_t(jj)/1.e9, record.record_data[jj] );
	      gr_Struk_chan_[gr_index]->SetPoint(gr_sub_index*buf_size + jj, cur_t - t0 + 15000.*Double_t(jj)/1.e9, record.record_data[jj]);
	      //if( i == 13 )
	      {
		//out_dat<<record.record_data[jj]<<"   time is "<<t_stamp.AsString()<<endl;
	      }
	    }
	  gr_sub_index = gr_sub_index + 1;
	  
	}
      
      for( int jj = 0; jj < n_of_graphs; jj++ )
	{
	  gr_Struk_chan_[jj]->SetMarkerStyle(24);
	  gr_Struk_chan_[jj]->SetMarkerColor(4);
	  gr_Struk_chan_[jj]->SetMarkerSize(0.45);
	  gr_Struk_chan_[jj]->SetTitle(Form("%s; t - t0 (sec); counts", tree_names_[i].c_str()));
	  gr_Struk_chan_[jj]->Write(Form("gr_Struk_chan_%d_%d", i, jj));
	  delete gr_Struk_chan_[jj];
	}
      
    }

//   gr_60Hz_[12]->SetMarkerStyle(24);
//   gr_60Hz_[12]->SetMarkerColor(4);
//   gr_60Hz_[12]->SetMarkerSize(0.1);
//   gr_60Hz_[12]->SetTitle("sixtyHz_raw_14; t - t0 (sec); counts");
//   gr_60Hz_[12]->Draw("AP");
//   c1->Print("sixtyHz_raw_14_vs_time.eps");
//   c1->Print("sixtyHz_raw_14_vs_time.pdf");
//   c1->Print("sixtyHz_raw_14_vs_time.gif");

//   for( int i = 0; i < 1; i++ )
//     {
//       gr_60Hz_[i]->SetMarkerStyle(24);
//       gr_60Hz_[i]->SetMarkerColor(4);
//       gr_60Hz_[i]->SetMarkerSize(0.45);
//       gr_60Hz_[i]->SetTitle(Form("%s; t - t0 (sec); counts", tree_names_[i].c_str()));
//       gr_60Hz_[i]->Draw("AP");
//       gr_60Hz_[i]->Write(Form("gr_%s", tree_names_[i].c_str()));
//       c1->Print(Form("%s_vs_time.eps",tree_names_[i].c_str() ));
//       c1->Print(Form("%s_vs_time.pdf",tree_names_[i].c_str() ));
//       c1->Print(Form("%s_vs_time.gif",tree_names_[i].c_str() ));
//     }

  file_out->Close();
  return 0;
}
