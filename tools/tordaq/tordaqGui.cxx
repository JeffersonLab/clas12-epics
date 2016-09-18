
#include "tordaqGui.h"

ClassImp(MyMainFrame);

const char* dataDir="/usr/clas12/DATA/wf2root";
const char *filetypes[] = { "ROOT files", "*.root", 0, 0 };

TString getTimeString(const Double_t time)
{
    char stime[26];
    const time_t timet=(int)time;
    const struct tm* stm=localtime(&timet);
    strftime(stime,26,"%H:%M:%S",stm);
    return TString(stime);

// I wanted this to give more precision, but it does't work:
//    const double fracsec=time-floor(time);
//    return TString(Form("%s.%d",stime,1000*fracsec));
}

MyMainFrame::MyMainFrame(const TGWindow *p, UInt_t w, UInt_t h) : TGMainFrame(p, w, h) {

    // modern c++ should let me set this with a one-liner in the class def:
    colors[0]=1;
    colors[1]=2;
    colors[2]=4;
    colors[3]=3;
    colors[4]=6;

    // bunch of global settings:
    SetStyle();

    legend1=new TLegend(0.1,0.9,0.9,1);
    legend1->SetNColumns(5);
    legend1->SetBorderSize(0);

    TGHorizontalFrame *topFrame = new TGHorizontalFrame(this, 1000, 40);

    TGTextButton *openBtn = new TGTextButton(topFrame, "&Open File");
    openBtn->Connect("Clicked()", "MyMainFrame", this, "DoOpen()");
    topFrame->AddFrame(openBtn,new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 10, 1, 5, 5));

    fileLabel = new TGLabel(topFrame, "");
    fileLabel->SetTextJustify(kTextLeft | kLHintsExpandX | kTextCenterY);
    fileLabel->SetWrapLength(-1);
    topFrame->AddFrame(fileLabel,new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 10, 1, 5, 5));

    TGTextButton *exitBtn = new TGTextButton(topFrame, "&Exit","gApplication->Terminate(0)");
    topFrame->AddFrame(exitBtn,new TGLayoutHints(kLHintsRight | kLHintsCenterY, 1, 10, 5, 5));
    
    TGTextButton *rootBtn = new TGTextButton(topFrame, "Save ROOT File");
    //rootBtn->Connect("Clicked()", "MyMainFrame", this, "DoRoot()");
    topFrame->AddFrame(rootBtn,new TGLayoutHints(kLHintsRight | kLHintsCenterY, 1, 10, 5, 5));
    

    AddFrame(topFrame, new TGLayoutHints(kLHintsExpandX, 1, 1, 1, 1));

    TGHorizontalFrame *middleFrame = new TGHorizontalFrame(this, 1000, 250);

    TGVerticalFrame *leftFrame=new TGVerticalFrame(middleFrame,100,250);
    for (int ii=0; ii<5; ii++)
    {
        combos1.push_back(new TGComboBox(leftFrame));
        combos1[combos1.size()-1]->AddEntry(" ",0);
        leftFrame->AddFrame(combos1[combos1.size()-1],new TGLayoutHints(kLHintsCenterX | kLHintsExpandX | kLHintsCenterY,2,2,2,2));
        combos1[combos1.size()-1]->Resize(60,20);
        combos1[combos1.size()-1]->SetForegroundColor(colors[ii]);
    }
    redrawBtn = new TGTextButton(leftFrame, "&Draw");
    redrawBtn->Connect("Clicked()","MyMainFrame",this,"Draw1()");
    redrawBtn->Resize(60,20);
    leftFrame->AddFrame(redrawBtn,new TGLayoutHints(kLHintsLeft | kLHintsCenterY | kLHintsExpandX, 1, 1, 1, 1));
    
    TGLabel *zoomLabel = new TGLabel(leftFrame, "X-Zoom");
    zoomLabel->SetTextJustify(kTextLeft | kLHintsExpandX | kTextCenterY);
    zoomLabel->SetWrapLength(-1);
    leftFrame->AddFrame(zoomLabel,new TGLayoutHints(kLHintsCenterY | kLHintsCenterX, 1, 1, 20, 1));
    
    TGHorizontalFrame *zoomFrame = new TGHorizontalFrame(leftFrame, 100, 60);
    zoominBtn = new TGTextButton(zoomFrame, "In");
    zoominBtn->Connect("Clicked()","MyMainFrame",this,"ZoomIn1()");
    zoominBtn->Resize(60,20);
    zoomFrame->AddFrame(zoominBtn,new TGLayoutHints(kLHintsExpandX | kLHintsCenterY, 1, 1, 1, 1));
    zoomoutBtn = new TGTextButton(zoomFrame, "Out");
    zoomoutBtn->Connect("Clicked()","MyMainFrame",this,"ZoomOut1()");
    zoomoutBtn->Resize(60,20);
    zoomFrame->AddFrame(zoomoutBtn,new TGLayoutHints(kLHintsExpandX | kLHintsCenterY, 1, 1, 1, 1));
    leftFrame->AddFrame(zoomFrame,new TGLayoutHints(kLHintsExpandX|kLHintsCenterY,1,1,1,1));

    TGLabel *panLabel = new TGLabel(leftFrame, "X-Pan");
    panLabel->SetTextJustify(kTextLeft | kLHintsExpandX | kTextCenterY);
    panLabel->SetWrapLength(-1);
    leftFrame->AddFrame(panLabel,new TGLayoutHints(kLHintsCenterY | kLHintsCenterX, 1, 1, 20, 1));
    
    TGHorizontalFrame *panFrame = new TGHorizontalFrame(leftFrame, 100, 60);
    panleftBtn = new TGTextButton(panFrame, "Left");
    panleftBtn->Connect("Clicked()","MyMainFrame",this,"PanLeft1()");
    panleftBtn->Resize(60,20);
    panFrame->AddFrame(panleftBtn,new TGLayoutHints(kLHintsExpandX | kLHintsCenterY, 1, 1, 1, 1));
    panrightBtn = new TGTextButton(panFrame, "Right");
    panrightBtn->Connect("Clicked()","MyMainFrame",this,"PanRight1()");
    panrightBtn->Resize(60,20);
    panFrame->AddFrame(panrightBtn,new TGLayoutHints(kLHintsExpandX | kLHintsCenterY, 1, 1, 1, 1));
    leftFrame->AddFrame(panFrame,new TGLayoutHints(kLHintsExpandX|kLHintsCenterY,1,1,1,1));

    middleFrame->AddFrame(leftFrame,new TGLayoutHints(kLHintsLeft | kLHintsCenterY,5,5,1,1));

    canvas1 = new TRootEmbeddedCanvas("canvas1", middleFrame, 800, 250);
    middleFrame->AddFrame(canvas1, new TGLayoutHints(kLHintsExpandX|kLHintsExpandY, 1, 1, 1, 1));

    AddFrame(middleFrame,new TGLayoutHints(kLHintsExpandX|kLHintsExpandY,1,1,1,1));

    
    TGHorizontalFrame *bottomFrame = new TGHorizontalFrame(this, 1000, 40);

    field_resample = new TGNumberEntryField(bottomFrame, -1, 100,
            TGNumberFormat::kNESInteger, TGNumberFormat::kNEANonNegative,
            TGNumberFormat::kNELLimitMinMax, 1, 10000);
    field_resample->SetWidth(40);
    bottomFrame->AddFrame(new TGLabel(bottomFrame, "Resample Freq."),new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 5, 2, 2, 2));
    bottomFrame->AddFrame(field_resample,new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 2, 5, 2, 2));
    check_denoise = new TGCheckButton(bottomFrame, "DeNoise");
    bottomFrame->AddFrame(check_denoise,new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 5, 20, 2, 2));


    TGVerticalFrame *sliderFrame = new TGVerticalFrame(bottomFrame, 1000, 40);
    
    zoomSlider = new TGHSlider(sliderFrame);
    zoomSlider->Connect("PositionChanged(Int_t)", "MyMainFrame", this, "doZoomSlider1()");
    zoomSlider->SetPosition(0);
    sliderFrame->AddFrame(zoomSlider,new TGLayoutHints(kLHintsLeft | kLHintsCenterY |kLHintsExpandX, 20,20,0,0));

    TGHorizontalFrame *sliderLabelFrame = new TGHorizontalFrame(sliderFrame,1000,20);
    zoomSliderLabelMin = new TGLabel(sliderLabelFrame, "");
    zoomSliderLabelMin->SetTextJustify(kTextLeft | kLHintsExpandX | kTextCenterY);
    zoomSliderLabelMin->SetWrapLength(-1);
    sliderLabelFrame->AddFrame(zoomSliderLabelMin,new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 0, 0, 0, 0));
    zoomSliderLabelMid = new TGLabel(sliderLabelFrame, "");
    zoomSliderLabelMid->SetTextJustify(kTextCenterX | kLHintsExpandX | kTextCenterY);
    zoomSliderLabelMid->SetWrapLength(-1);
    sliderLabelFrame->AddFrame(zoomSliderLabelMid,new TGLayoutHints(kLHintsCenterX | kLHintsCenterY, 0, 0, 0, 0));
    zoomSliderLabelMax = new TGLabel(sliderLabelFrame, "");
    zoomSliderLabelMax->SetTextJustify(kTextLeft | kLHintsExpandX | kTextCenterY);
    zoomSliderLabelMax->SetWrapLength(-1);
    sliderLabelFrame->AddFrame(zoomSliderLabelMax,new TGLayoutHints(kLHintsRight | kLHintsCenterY, 0, 0, 0, 0));
    sliderFrame->AddFrame(sliderLabelFrame,new TGLayoutHints(kLHintsExpandX | kLHintsCenterY, 0,0,0,0));

    bottomFrame->AddFrame(sliderFrame,new TGLayoutHints(kLHintsLeft | kLHintsCenterY | kLHintsExpandX, 2,2,2,2));
    
    AddFrame(bottomFrame, new TGLayoutHints(kLHintsExpandX));

    // status bar, wothless how to update it?
    Int_t parts[] = {20, 15, 10, 55};
    fStatusBar = new TGStatusBar(this, 50, 10, kVerticalFrame);
    fStatusBar->SetParts(parts, 4);
    fStatusBar->Draw3DCorner(kFALSE);
    AddFrame(fStatusBar, new TGLayoutHints(kLHintsExpandX, 0, 0, 10, 0));

    SetWindowName("Hall-B Torus Analysis");
    MapSubwindows();
    Resize(GetDefaultSize());
    MapWindow();
}
MyMainFrame::~MyMainFrame() {
    Cleanup();
    gApplication->Terminate(0);
}

void MyMainFrame::DoOpen(TString filename="") {

    if (filename=="")
    {
        TList myli;
        TGFileInfo fi;
        TObjString str1;
        fi.fFileTypes = filetypes;
        fi.fIniDir = StrDup(dataDir);
        fi.fMultipleSelection = true;
        TList *filelist;
        new TGFileDialog(gClient->GetRoot(), this, kFDOpen, &fi);
        if (!fi.fFileNamesList) return;
        filelist = fi.fFileNamesList;
        TObjLink *lnk=filelist->FirstLink();
        filename=lnk->GetObject()->GetName();
    }

    fileLabel->ChangeText("Reading "+filename+" ....");
   
    // how to get it to update immeditately?
    //fStatusBar->SetText("Reading Data File ...",0);
    gClient->NeedRedraw(fileLabel);
    this->Layout();

    datafile=new TFile(filename,"READ");
    int ivt=1;
    std::vector <TGComboBox*>::iterator cbit;
    for (cbit=combos1.begin(); cbit!=combos1.end(); ++cbit)
    {
        (*cbit)->RemoveAll();
        (*cbit)->AddEntry(" ",0);
    }
    while (1)
    {
        TObject* xx=datafile->Get(Form("h%d",ivt));
        if (xx) {
            TH1* hh=(TH1*)xx;
            hh->GetXaxis()->SetTimeFormat("#splitline{}{#splitline{%b %d}{%H:%M:%S}}");
            hh->GetXaxis()->SetTimeDisplay(1);
            hh->GetXaxis()->SetNdivisions(5);
            hh->GetYaxis()->SetTitleOffset(0.7);
            hh->GetXaxis()->SetTitle("");
            hh->GetYaxis()->SetTitle("");
            hh->SetTitle(Form("VT%d",ivt));
            datahistos.push_back(hh);
            for (cbit=combos1.begin(); cbit!=combos1.end(); ++cbit)
                (*cbit)->AddEntry(Form("VT%d",ivt),ivt);
            if (ivt==1)
            {
              const double t0=hh->GetXaxis()->GetXmin();
              const double t1=hh->GetXaxis()->GetXmax();
              zoomSlider->SetRange(t0,t1);
              zoomSlider->SetPosition(t0);
              zoomSliderLabelMin->SetText(getTimeString(t0));
              zoomSliderLabelMid->SetText(getTimeString(t0+(t1-t0)*0.50));
              zoomSliderLabelMax->SetText(getTimeString(t1));
            }
        }
        else break;
        ivt++;
        if (ivt>10) break;
    }
    
    fileLabel->ChangeText(filename);
    //fStatusBar->SetText("Done Reading Data File.",0);
    this->Layout();
}
void MyMainFrame::Draw1()
{

    if (datahistos.size()<1)
    {
        fileLabel->ChangeText("OPEN A FILE FIRST!");
        this->Layout();
        return;
    }

    TCanvas *ctmp=canvas1->GetCanvas();
    ctmp->cd();
    ctmp->Clear();
    float min=999999,max=-9999999;
    for (unsigned int ii=0; ii<combos1.size(); ii++)
    {
        const int jj=combos1[ii]->GetSelected();
        if (jj>0 && jj<=datahistos.size()) {
            if (datahistos[jj-1]->GetMaximum()>max) max=datahistos[jj-1]->GetMaximum();
            if (datahistos[jj-1]->GetMinimum()<min) min=datahistos[jj-1]->GetMinimum();
        }
    }
    bool first=true;
    legend1->Clear();
    histos1.clear();
    for (unsigned int ii=0; ii<combos1.size(); ii++)
    {
        const int jj=combos1[ii]->GetSelected();
        if (jj>0 && jj<=datahistos.size()) {
            if (first)
            {
                datahistos[jj-1]->SetMaximum(max);
                datahistos[jj-1]->SetMinimum(min);
            }
            histos1.push_back(datahistos[jj-1]);
            datahistos[jj-1]->SetLineColor(colors[ii]);
            legend1->AddEntry(datahistos[jj-1],datahistos[jj-1]->GetTitle(),"L");
            datahistos[jj-1]->Draw(first?"":"SAME");
            first=false;
        }
    }
    legend1->Draw();
    ctmp->Update();
}
void MyMainFrame::Update1()
{
    TCanvas *ctmp=canvas1->GetCanvas();
    ctmp->Modified();
    ctmp->Update();
//    ctmp->cd();
//    ctmp->ForceUpdate();
}
void MyMainFrame::ZoomIn1()
{
    double frac=0.45;
    double x1,x2,y1,y2;
    TCanvas *ctmp=canvas1->GetCanvas();
    ctmp->GetRangeAxis(x1,y1,x2,y2);
    const double xlo=x1+(x2-x1)*frac;
    const double xhi=x2-(x2-x1)*frac;
    histos1[0]->GetXaxis()->SetRangeUser(xlo,xhi);
    zoomSlider->SetPosition(xlo);
    Update1();
}
void MyMainFrame::ZoomOut1()
{
    double frac=1.0;
    double x1,x2,y1,y2;
    TCanvas *ctmp=canvas1->GetCanvas();
    ctmp->GetRangeAxis(x1,y1,x2,y2);
    const double xlo=x1-(x2-x1)*frac;
    const double xhi=x2+(x2-x1)*frac;
    histos1[0]->GetXaxis()->SetRangeUser(xlo,xhi);
    zoomSlider->SetPosition(xlo);
    Update1();
}
void MyMainFrame::doZoomSlider1()
{
    const int pos=zoomSlider->GetPosition();
    double x1,x2,y1,y2;
    TCanvas *ctmp=canvas1->GetCanvas();
    ctmp->GetRangeAxis(x1,y1,x2,y2);
    if (pos>=histos1[0]->GetXaxis()->GetXmax()
            || pos<histos1[0]->GetXaxis()->GetXmin())
        zoomSlider->SetPosition(x1);
    else
    {
        histos1[0]->GetXaxis()->SetRangeUser(pos,pos+(x2-x1));
        Update1();
    }
}
void MyMainFrame::PanLeft1()
{
    double frac=0.5;
    double x1,x2,y1,y2;
    TCanvas *ctmp=canvas1->GetCanvas();
    ctmp->GetRangeAxis(x1,y1,x2,y2);
    const double xlo=x1-(x2-x1)*frac;
    const double xhi=x2-(x2-x1)*frac;
    histos1[0]->GetXaxis()->SetRangeUser(xlo,xhi);
    zoomSlider->SetPosition(xlo);
    Draw1();
}
void MyMainFrame::PanRight1()
{
    double frac=0.5;
    double x1,x2,y1,y2;
    TCanvas *ctmp=canvas1->GetCanvas();
    ctmp->GetRangeAxis(x1,y1,x2,y2);
    const double xlo=x1+(x2-x1)*frac;
    const double xhi=x2+(x2-x1)*frac;
    histos1[0]->GetXaxis()->SetRangeUser(xlo,xhi);
    zoomSlider->SetPosition(xlo);
    Update1();
}
void MyMainFrame::SetStyle()
{
    // Fill color
    gStyle->SetStatColor(0);
    gStyle->SetTitleFillColor(0);
    gStyle->SetCanvasColor(0);
    gStyle->SetPadColor(0);
    gStyle->SetFrameFillColor(0);
    // Border mode
    gStyle->SetCanvasBorderMode(0);
    gStyle->SetPadBorderMode(0);
    gStyle->SetFrameBorderMode(0);
    // Margin
    gStyle->SetPadLeftMargin(0.06);
    gStyle->SetPadRightMargin(0.04);
    gStyle->SetPadTopMargin(0.1);
    gStyle->SetPadBottomMargin(0.12);
    // Font
    gStyle->SetTextFont(132);
    gStyle->SetLabelFont(132, "XYZ");
    gStyle->SetTitleFont(132, "XYZ");
    gStyle->SetStatFont(132);
    gStyle->SetLegendFont(132);
    // Fontsize
    gStyle->SetLabelSize(0.05, "XYZ");
    gStyle->SetTitleSize(0.06, "XYZ");
    gStyle->SetTitleOffset(0.9, "X");
    gStyle->SetTitleOffset(0.2, "Y");
    // Opt
    gStyle->SetOptTitle(0);
    gStyle->SetOptFit(1);
    gStyle->SetOptStat(0);
    gStyle->SetStatX(0.97);
    gStyle->SetStatY(0.98);
    // Axis
    //TGaxis::SetMaxDigits(3);
    //TGaxis::SetExponentOffset(-0.06, -0.04,"y");
    // Grid
    gStyle->SetPadGridX(kTRUE);
    gStyle->SetPadGridY(kTRUE);
}
int main(int argc, char **argv) {

    TApplication theApp("App", &argc, argv);
    MyMainFrame * mmf=new MyMainFrame(gClient->GetRoot(), 1000, 400);
    if (argc>1)
    {
        mmf->SetFilename(argv[1]);
    }
    theApp.Run();
    return 0;
}

