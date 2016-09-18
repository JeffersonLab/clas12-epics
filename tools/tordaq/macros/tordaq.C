void format()
{
  TH2* hh=(TH2*)gPad->GetPrimitive("htemp");
  TAxis *xax=hh->GetXaxis();
  TAxis *yax=hh->GetYaxis();
  xax->SetTimeDisplay(1);
  xax->SetTimeFormat("#splitline{}{#splitline{%b %d}{%H:%M:%S}}");
  xax->SetNdivisions(3);
  xax->SetTitleOffset(0.5);
  xax->SetTitle("");
  gPad->Update();
}

void draw(const int ivt1,const int ivt2=0,const int ivt3=0)
{
  // Looks like ROOT works from 1995/01/01 00:00:00
  // This is the offset from the normal unix epoch:
  const int toff=788918400;

  gStyle->SetMarkerStyle(20);
  gStyle->SetMarkerSize(1);
  gEnv->SetValue("Hist.Binning.2D.x",100000);
  gEnv->SetValue("Hist.Binning.2D.y",100);
  TNtupleD* tt=(TNtupleD*)gDirectory->Get("tordaq");
  tordaq->Draw(Form("x%d:t%d-%d",ivt1,ivt1,toff),Form("t%d>0",ivt1),"LINE");
  if (ivt2>0) tordaq->Draw(Form("x%d:t%d-%d",ivt2,ivt2,toff),"","LINESAME");
  if (ivt3>0) tordaq->Draw(Form("x%d:t%d-%d",ivt3,ivt3,toff),"","LINESAME");
  format();
}

void draw(const char* filename,const int ivt1)
{
    TFile *f=new TFile(filename,"READ");
    draw(ivt1);
}

