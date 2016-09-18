void draw2(const int ivt1,const int ivt2=0,const int ivt3=0)
{
  TH1 *hh=(TH1*)gDirectory->Get(Form("h%d",ivt1));
  TAxis *xax=hh->GetXaxis();
  xax->SetTimeDisplay(1);
  xax->SetTimeFormat("#splitline{}{#splitline{%b %d}{%H:%M:%S}}");
  xax->SetNdivisions(3);
  xax->SetTitleOffset(0.5);
  xax->SetTitle("");
  hh->Draw();
  gPad->Update();
}

void draw2(const char* filename,const int ivt1)
{
    TFile *f=new TFile(filename,"READ");
    draw2(ivt1);
}

