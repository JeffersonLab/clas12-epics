#include "tordaqGui.hh"

ClassImp(tordaqGui);

TString filename="";
const char* dataDir="/usr/clas12/DATA/wf2root";
const char *filetypes[] = { "ROOT files", "*.root", 0, 0 };

TString getTimeString(const Double_t time)
{
    char stime[26];
    const time_t timet=(int)time;
    const struct tm* stm=localtime(&timet);
    strftime(stime,26,"%H:%M:%S",stm);
    return TString(stime);
}

tordaqGui::tordaqGui(const TGWindow *p, UInt_t w, UInt_t h) : TGMainFrame(p, w, h) {
    
    SetStyle();

    // modern c++ should let me set this with a one-liner in the class def:
    colors[0]=1;
    colors[1]=2;
    colors[2]=4;
    colors[3]=3;
    colors[4]=6;

    legend1=new TLegend(0.1,0.9,0.9,1);
    legend1->SetNColumns(5);
    legend1->SetBorderSize(0);


    // TOP FRAME -----------------------------------------------------------------

    topFrame = new TGHorizontalFrame(this, 1000, 40);

    TGTextButton *openBtn = new TGTextButton(topFrame, "&Open File");
    openBtn->Connect("Clicked()", "tordaqGui", this, "DoOpen()");
    topFrame->AddFrame(openBtn,new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 10, 1, 5, 5));

    fileLabel = new TGLabel(topFrame, "");
    fileLabel->SetTextJustify(kTextLeft | kLHintsExpandX | kTextCenterY);
    fileLabel->SetWrapLength(-1);
    topFrame->AddFrame(fileLabel,new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 10, 1, 5, 5));

    TGTextButton *exitBtn = new TGTextButton(topFrame, "&Exit","gApplication->Terminate(0)");
    topFrame->AddFrame(exitBtn,new TGLayoutHints(kLHintsRight | kLHintsCenterY, 1, 10, 5, 5));
    
    TGTextButton *rootBtn = new TGTextButton(topFrame, "Save ROOT File");
    //rootBtn->Connect("Clicked()", "tordaqGui", this, "SaveRoot()");
    topFrame->AddFrame(rootBtn,new TGLayoutHints(kLHintsRight | kLHintsCenterY, 1, 10, 5, 5));

    AddFrame(topFrame, new TGLayoutHints(kLHintsExpandX, 1, 1, 1, 1));



    // MIDDLE FRAME ---------------------------------------------------------------

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
    redrawBtn->Connect("Clicked()","tordaqGui",this,"Draw1()");
    redrawBtn->Resize(60,20);
    leftFrame->AddFrame(redrawBtn,new TGLayoutHints(kLHintsLeft | kLHintsCenterY | kLHintsExpandX, 1, 1, 1, 1));
    
    TGLabel *zoomLabel = new TGLabel(leftFrame, "X-Zoom");
    zoomLabel->SetTextJustify(kTextLeft | kLHintsExpandX | kTextCenterY);
    zoomLabel->SetWrapLength(-1);
    leftFrame->AddFrame(zoomLabel,new TGLayoutHints(kLHintsCenterY | kLHintsCenterX, 1, 1, 20, 1));
    
    TGHorizontalFrame *zoomFrame = new TGHorizontalFrame(leftFrame, 100, 60);
    zoominBtn = new TGTextButton(zoomFrame, "In");
    zoominBtn->Connect("Clicked()","tordaqGui",this,"ZoomIn1()");
    zoominBtn->Resize(60,20);
    zoomFrame->AddFrame(zoominBtn,new TGLayoutHints(kLHintsExpandX | kLHintsCenterY, 1, 1, 1, 1));
    zoomoutBtn = new TGTextButton(zoomFrame, "Out");
    zoomoutBtn->Connect("Clicked()","tordaqGui",this,"ZoomOut1()");
    zoomoutBtn->Resize(60,20);
    zoomFrame->AddFrame(zoomoutBtn,new TGLayoutHints(kLHintsExpandX | kLHintsCenterY, 1, 1, 1, 1));
    leftFrame->AddFrame(zoomFrame,new TGLayoutHints(kLHintsExpandX|kLHintsCenterY,1,1,1,1));

    TGLabel *panLabel = new TGLabel(leftFrame, "X-Pan");
    panLabel->SetTextJustify(kTextLeft | kLHintsExpandX | kTextCenterY);
    panLabel->SetWrapLength(-1);
    leftFrame->AddFrame(panLabel,new TGLayoutHints(kLHintsCenterY | kLHintsCenterX, 1, 1, 20, 1));
    
    TGHorizontalFrame *panFrame = new TGHorizontalFrame(leftFrame, 100, 60);
    panleftBtn = new TGTextButton(panFrame, "Left");
    panleftBtn->Connect("Clicked()","tordaqGui",this,"PanLeft1()");
    panleftBtn->Resize(60,20);
    panFrame->AddFrame(panleftBtn,new TGLayoutHints(kLHintsExpandX | kLHintsCenterY, 1, 1, 1, 1));
    panrightBtn = new TGTextButton(panFrame, "Right");
    panrightBtn->Connect("Clicked()","tordaqGui",this,"PanRight1()");
    panrightBtn->Resize(60,20);
    panFrame->AddFrame(panrightBtn,new TGLayoutHints(kLHintsExpandX | kLHintsCenterY, 1, 1, 1, 1));
    leftFrame->AddFrame(panFrame,new TGLayoutHints(kLHintsExpandX|kLHintsCenterY,1,1,1,1));

    middleFrame->AddFrame(leftFrame,new TGLayoutHints(kLHintsLeft | kLHintsCenterY,5,5,1,1));

    canvas1 = new TRootEmbeddedCanvas("canvas1", middleFrame, 800, 250);
    middleFrame->AddFrame(canvas1, new TGLayoutHints(kLHintsExpandX|kLHintsExpandY, 1, 1, 1, 1));

    AddFrame(middleFrame,new TGLayoutHints(kLHintsExpandX|kLHintsExpandY,1,1,1,1));


    // BOTTOM FRAME -----------------------------------------------------------------
    
    TGHorizontalFrame *bottomFrame = new TGHorizontalFrame(this, 1000, 40);

    resampleField = new TGNumberEntryField(bottomFrame, -1, 100,
            TGNumberFormat::kNESInteger, TGNumberFormat::kNEANonNegative,
            TGNumberFormat::kNELLimitMinMax, 1, 10000);
    resampleField->SetWidth(40);
    bottomFrame->AddFrame(new TGLabel(bottomFrame, "Resample Freq."),new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 5, 2, 2, 2));
    bottomFrame->AddFrame(resampleField,new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 2, 5, 2, 2));
    denoiseCheck = new TGCheckButton(bottomFrame, "DeNoise");
    bottomFrame->AddFrame(denoiseCheck,new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 5, 20, 2, 2));

    TGVerticalFrame *sliderFrame = new TGVerticalFrame(bottomFrame, 1000, 40);
    
    zoomSlider = new TGHSlider(sliderFrame);
    zoomSlider->Connect("PositionChanged(Int_t)", "tordaqGui", this, "doZoomSlider1()");
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

/*
    // status bar, wothless how to update it?
    Int_t parts[] = {20, 15, 10, 55};
    fStatusBar = new TGStatusBar(this, 50, 10, kVerticalFrame);
    fStatusBar->SetParts(parts, 4);
    fStatusBar->Draw3DCorner(kFALSE);
    AddFrame(fStatusBar, new TGLayoutHints(kLHintsExpandX, 0, 0, 10, 0));
*/

    SetWindowName("Hall-B Torus Analysis");
    MapSubwindows();
    Resize(GetDefaultSize());
    MapWindow();

    if (filename!="") DoOpen(filename);
}
tordaqGui::~tordaqGui() {
    Cleanup();
    gApplication->Terminate(0);
}

void tordaqGui::DoOpen(TString filename="") {

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

    if (gSystem->AccessPathName(filename))
    {
        std::cerr<<"FILE NOT FOUND:  "+filename<<std::endl;
        fileLabel->ChangeText("FILE NOT FOUND:  "+filename);
        this->Layout();
        return;
    }

    std::cout<<"Reading "+filename+" ....."<<std::endl;

    // how to get it to update immeditately?
    fileLabel->ChangeText("Reading "+filename+" ....");
    //fileLabel->SetText("Reading "+filename+" ....");
    //fileLabel->Draw();
    //topFrame->Layout();
    //gClient->NeedRedraw(fileLabel);
    //gClient->ForceRedraw();
    //this->Layout();

    datafile=new TFile(filename,"READ");
    int ivt=1;
    
    // zero the combos boxes:
    std::vector <TGComboBox*>::iterator cbit;
    for (cbit=combos1.begin(); cbit!=combos1.end(); ++cbit)
    {
        (*cbit)->RemoveAll();
        (*cbit)->AddEntry(" ",0);
    }

    // generate the hitsos if not already there:
    if (!gDirectory->Get("h1"))
    {
        tdReader.makeHistos=true;
        if (!tdReader.process())
        {
            std::cerr<<"NO WF2ROOT TREES FOUND IN   "+filename<<std::endl;
            fileLabel->ChangeText("NO WF2ROOT TREES FOUND IN   "+filename);
            this->Layout();
            return;
        }
    }

    while (1)
    {
        tordaqReader::ProgressMeter(tordaqData::NVT,ivt);

        TObject* xx=gDirectory->Get(Form("h%d",ivt));
        if (!xx) break;

        // copy into memory (if on disk):
        // TH1* hh=(TH1*)xx->Clone("hvt%d");

        TH1* hh=(TH1*)xx;

        hh->GetXaxis()->SetTimeFormat("#splitline{}{#splitline{%b %d}{%H:%M:%S}}");
        hh->GetXaxis()->SetTimeDisplay(1);
        hh->GetXaxis()->SetNdivisions(5);
        hh->GetYaxis()->SetTitleOffset(0.5);
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
        ivt++;
        // if (ivt>5) break;
    }
    
    fileLabel->ChangeText(filename);
    this->Layout();
}
void tordaqGui::Draw1()
{
    if (datahistos.size()<1)
    {
        fileLabel->ChangeText("!! OPEN A FILE FIRST !!");
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
void tordaqGui::Update1()
{
    canvas1->GetCanvas()->Modified();
    canvas1->GetCanvas()->Update();
}
void tordaqGui::ZoomIn1()
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
void tordaqGui::ZoomOut1()
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
void tordaqGui::doZoomSlider1()
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
void tordaqGui::PanLeft1()
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
void tordaqGui::PanRight1()
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
int main(int argc, char **argv) {

    if (argc>1) filename=argv[1];
    TApplication theApp("App", &argc, argv);
    tordaqGui * mmf=new tordaqGui(gClient->GetRoot(), 1000, 600);
    theApp.Run();
    return 0;
}

