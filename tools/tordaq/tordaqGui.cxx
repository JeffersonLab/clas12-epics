#include "tordaqGui.hh"
#include "tordaqUtil.hh"

#include "TThread.h"

ClassImp(tordaqGui);

TString filename="";
//const char* dataDir="/usr/clas12/DATA/wf2root";
const char* dataDir="/logs/torus";
const char *filetypes[] = { "ROOT files", "*.root", 0, 0 };
bool doSynchroAna=false;
bool forceSynchro=false;

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

    // modern c++ should let me set this with a const one-liner in the class def,
    // but looks like ROOT (maybe need ROOT6) dictionary generator donot like it.  
    colors[0]=1;
    colors[1]=2;
    colors[2]=4;
    colors[3]=3;
    colors[4]=6;

    legend1=new TLegend(0.1,0.9,0.9,1);
    legend1->SetNColumns(5);
    legend1->SetBorderSize(0);


    // TOP FRAME -----------------------------------------------------------------

    topFrame = new TGHorizontalFrame(this, 2000, 40);

    TGTextButton *openBtn = new TGTextButton(topFrame, "&Open File");
    openBtn->Connect("Released()", "tordaqGui", this, "DoOpen()");
    topFrame->AddFrame(openBtn,new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 10, 1, 5, 5));

    fileLabel = new TGLabel(topFrame, "");
    fileLabel->SetTextJustify(kTextLeft | kLHintsExpandX | kTextCenterY);
    fileLabel->SetWrapLength(-1);
    topFrame->AddFrame(fileLabel,new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 10, 1, 5, 5));
    
    //progressBar = new TGHProgressBar(topFrame,50,20);
    //topFrame->AddFrame(progressBar,new TGLayoutHints(kLHintsExpandX | kLHintsCenterY,5,1,1,1));

    TGTextButton *exitBtn = new TGTextButton(topFrame, "&Exit","gApplication->Terminate(0)");
    topFrame->AddFrame(exitBtn,new TGLayoutHints(kLHintsRight | kLHintsCenterY, 1, 10, 5, 5));
   
    //TGTextButton *rootBtn = new TGTextButton(topFrame, "Save ROOT File");
    ////rootBtn->Connect("Released()", "tordaqGui", this, "SaveRoot()");
    //topFrame->AddFrame(rootBtn,new TGLayoutHints(kLHintsRight | kLHintsCenterY, 1, 10, 5, 5));

    AddFrame(topFrame, new TGLayoutHints(kLHintsExpandX, 1, 1, 1, 1));


    // MIDDLE FRAME ---------------------------------------------------------------

    TGHorizontalFrame *middleFrame = new TGHorizontalFrame(this, 1600, 600);

    
    // LEFT FRAME -----------------------------------------------------------------
    
    TGVerticalFrame *leftFrame=new TGVerticalFrame(middleFrame,100,600);
   
    TGVerticalFrame *selectFrame=new TGVerticalFrame(leftFrame,100,600);

    for (int ii=0; ii<10; ii++)
    {
        combos1.push_back(new TGComboBox(selectFrame));
        combos1[combos1.size()-1]->AddEntry(" ",0);
        selectFrame->AddFrame(combos1[combos1.size()-1],new TGLayoutHints(kLHintsCenterX | kLHintsExpandX | kLHintsTop,2,2,2,2));
        combos1[combos1.size()-1]->Resize(60,20);
        combos1[combos1.size()-1]->SetForegroundColor(colors[ii]);
    }
    
    showAllCheck=new TGCheckButton(selectFrame,"Show All");
    
    selectFrame->AddFrame(showAllCheck,new TGLayoutHints(kLHintsExpandX | kLHintsTop,1,1,1,1));
    redrawBtn = new TGTextButton(selectFrame, "&Draw");
    redrawBtn->Connect("Released()","tordaqGui",this,"Draw1()");
    redrawBtn->Resize(60,20);
    
    selectFrame->AddFrame(redrawBtn,new TGLayoutHints(kLHintsCenterY | kLHintsExpandX, 1, 1, 1, 1));
    
    leftFrame->AddFrame(selectFrame,new TGLayoutHints(kLHintsExpandX | kLHintsTop,1,1,5,1));
    
    TGLabel *yZoomLabel = new TGLabel(leftFrame, "Y-Zoom");
    yZoomLabel->SetTextJustify(kTextCenterX | kTextCenterY);
    yZoomLabel->SetWrapLength(-1);
    TGHorizontalFrame *yZoomFrame = new TGHorizontalFrame(leftFrame, 100, 60);
    yZoominBtn = new TGTextButton(yZoomFrame, "In");
    yZoominBtn->Connect("Released()","tordaqGui",this,"yZoomIn1()");
    yZoominBtn->Resize(60,20);
    yZoomFrame->AddFrame(yZoominBtn,new TGLayoutHints(kLHintsExpandX | kLHintsBottom, 1, 1, 1, 1));
    yZoomoutBtn = new TGTextButton(yZoomFrame, "Out");
    yZoomoutBtn->Connect("Released()","tordaqGui",this,"yZoomOut1()");
    yZoomoutBtn->Resize(60,20);
    yZoomFrame->AddFrame(yZoomoutBtn,new TGLayoutHints(kLHintsExpandX | kLHintsBottom, 1, 1, 1, 1));

    TGLabel *xZoomLabel = new TGLabel(leftFrame, "X-Zoom");
    xZoomLabel->SetTextJustify(kTextCenterX | kTextCenterY);
    xZoomLabel->SetWrapLength(-1);
    TGHorizontalFrame *xZoomFrame = new TGHorizontalFrame(leftFrame, 100, 60);
    xZoominBtn = new TGTextButton(xZoomFrame, "In");
    xZoominBtn->Connect("Released()","tordaqGui",this,"ZoomIn1()");
    xZoominBtn->Resize(60,20);
    xZoomFrame->AddFrame(xZoominBtn,new TGLayoutHints(kLHintsExpandX | kLHintsBottom, 1, 1, 1, 1));
    xZoomoutBtn = new TGTextButton(xZoomFrame, "Out");
    xZoomoutBtn->Connect("Released()","tordaqGui",this,"ZoomOut1()");
    xZoomoutBtn->Resize(60,20);
    xZoomFrame->AddFrame(xZoomoutBtn,new TGLayoutHints(kLHintsExpandX | kLHintsBottom, 1, 1, 1, 1));

    TGLabel *panLabel = new TGLabel(leftFrame, "X-Pan");
    panLabel->SetTextJustify(kTextCenterX | kLHintsExpandX | kTextCenterY);
    panLabel->SetWrapLength(-1);
    TGHorizontalFrame *panFrame = new TGHorizontalFrame(leftFrame, 100, 60);
    panleftBtn = new TGTextButton(panFrame, "Left");
    panleftBtn->Connect("Released()","tordaqGui",this,"PanLeft1()");
    panleftBtn->Resize(60,20);
    panFrame->AddFrame(panleftBtn,new TGLayoutHints(kLHintsExpandX | kLHintsBottom, 1, 1, 1, 1));
    panrightBtn = new TGTextButton(panFrame, "Right");
    panrightBtn->Connect("Released()","tordaqGui",this,"PanRight1()");
    panrightBtn->Resize(60,20);
    panFrame->AddFrame(panrightBtn,new TGLayoutHints(kLHintsExpandX | kLHintsBottom, 1, 1, 1, 1));
   
    // stacking from the bottom upwards:
    leftFrame->AddFrame(panFrame,new TGLayoutHints(kLHintsExpandX | kLHintsBottom,1,1,1,1));
    leftFrame->AddFrame(panLabel,new TGLayoutHints(kLHintsCenterX | kLHintsBottom, 1, 1, 1, 1));
    leftFrame->AddFrame(xZoomFrame,new TGLayoutHints(kLHintsExpandX | kLHintsBottom,1,1,1,8));
    leftFrame->AddFrame(xZoomLabel,new TGLayoutHints(kLHintsCenterX | kLHintsBottom, 1, 1, 1, 1));
    leftFrame->AddFrame(yZoomFrame,new TGLayoutHints(kLHintsExpandX | kLHintsBottom,1,1,1,8));
    leftFrame->AddFrame(yZoomLabel,new TGLayoutHints(kLHintsCenterX | kLHintsBottom, 1, 1, 1, 1));

    //denoiseCheck=new TGCheckButton(leftFrame,"Denoise");
    //leftFrame->AddFrame(denoiseCheck,new TGLayoutHints(kLHintsCenterX | kLHintsBottom, 1,1,1,1));

    middleFrame->AddFrame(leftFrame,new TGLayoutHints(kLHintsLeft | kLHintsExpandY,5,5,1,1));

    // RIGHT FRAME -------------------------------------------------------------------
    
    TGVerticalFrame *rightFrame = new TGVerticalFrame(middleFrame, 900, 400);
    
    
    canvas1 = new TRootEmbeddedCanvas("canvas1", rightFrame, 900, 500);
    rightFrame->AddFrame(canvas1, new TGLayoutHints(kLHintsExpandX|kLHintsExpandY, 1, 1, 1, 1));

    TGVerticalFrame *sliderFrame = new TGVerticalFrame(rightFrame, 1600, 40);
    
    zoomSlider = new TGHSlider(sliderFrame);
    zoomSlider->Connect("Released()", "tordaqGui", this, "doZoomSlider1()");
    //zoomSlider->Connect("PositionChanged(Int_t)", "tordaqGui", this, "doZoomSlider1()");
    zoomSlider->SetPosition(0);
    sliderFrame->AddFrame(zoomSlider,new TGLayoutHints(kLHintsLeft | kLHintsBottom |kLHintsExpandX, 20,20,0,0));

    TGHorizontalFrame *sliderLabelFrame = new TGHorizontalFrame(sliderFrame,1000,20);
    zoomSliderLabelMin = new TGLabel(sliderLabelFrame, "");
    zoomSliderLabelMin->SetTextJustify(kTextLeft | kLHintsExpandX | kTextCenterY);
    zoomSliderLabelMin->SetWrapLength(-1);
    sliderLabelFrame->AddFrame(zoomSliderLabelMin,new TGLayoutHints(kLHintsLeft | kLHintsBottom, 0, 0, 0, 0));
    zoomSliderLabelMid = new TGLabel(sliderLabelFrame, "");
    zoomSliderLabelMid->SetTextJustify(kTextCenterX | kLHintsExpandX | kTextCenterY);
    zoomSliderLabelMid->SetWrapLength(-1);
    sliderLabelFrame->AddFrame(zoomSliderLabelMid,new TGLayoutHints(kLHintsCenterX | kLHintsBottom, 0, 0, 0, 0));
    zoomSliderLabelMax = new TGLabel(sliderLabelFrame, "");
    zoomSliderLabelMax->SetTextJustify(kTextLeft | kLHintsExpandX | kTextCenterY);
    zoomSliderLabelMax->SetWrapLength(-1);
    sliderLabelFrame->AddFrame(zoomSliderLabelMax,new TGLayoutHints(kLHintsRight | kLHintsBottom, 0, 0, 0, 0));
    sliderFrame->AddFrame(sliderLabelFrame,new TGLayoutHints(kLHintsExpandX | kLHintsBottom, 0,0,0,0));

    rightFrame->AddFrame(sliderFrame,new TGLayoutHints(kLHintsLeft | kLHintsBottom | kLHintsExpandX, 2,2,2,2));

    middleFrame->AddFrame(rightFrame,new TGLayoutHints(kLHintsExpandX | kLHintsExpandY,1,1,1,1));

    AddFrame(middleFrame,new TGLayoutHints(kLHintsExpandX | kLHintsExpandY,1,1,1,1));


    // status bar, how to update it?  (answer:  threads ...)
    Int_t parts[] = {20, 15, 10, 55};
    fStatusBar = new TGStatusBar(this, 50, 10, kVerticalFrame);
    fStatusBar->SetParts(parts, 4);
    fStatusBar->Draw3DCorner(kFALSE);
    AddFrame(fStatusBar, new TGLayoutHints(kLHintsExpandX, 0, 0, 10, 0));

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

void *tordaqGui::DoOpen1(void *ptr)
{
//    TThread *th1=new TThread("th1",DoOpen,(void*) 1);
}

void tordaqGui::DoOpen(TString filename="")
{

    if (filename=="")
    {
        TList myli;
        TGFileInfo fi;
        TObjString str1;
        fi.fFileTypes = filetypes;
        fi.fIniDir = StrDup(dataDir);
        fi.fMultipleSelection = true;
        TList *filelist;
        TGFileDialog *tgfd=new TGFileDialog(gClient->GetRoot(), this, kFDOpen, &fi);
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

    // how to get it to update immeditately?  (answer:  threads)
    fileLabel->ChangeText("Reading "+filename+" ....");
    //fileLabel->SetText("Reading "+filename+" ....");
    //fileLabel->Draw();
    //topFrame->Layout();
    //gClient->NeedRedraw(fileLabel);
    //gClient->ForceRedraw();
    //this->Layout();

    datafile=new TFile(filename,"READ");
    
    // zero the combos boxes:
    std::vector <TGComboBox*>::iterator cbit;
    for (cbit=combos1.begin(); cbit!=combos1.end(); ++cbit)
    {
        (*cbit)->RemoveAll();
        (*cbit)->AddEntry(" ",0);
    }

    // generate the hitsos if not already there:
    if (!gDirectory->Get(("h"+tdReader.tdData.VARNAMES[0]).c_str()))
    {
        tdReader.makeHistos=true;
        //tdReader.progressMeter=progressBar;
        tdReader.doSynchroAna=doSynchroAna;
        if (!tdReader.process())
        {
            std::cerr<<"Error Reading WF2ROOT Trees in   "+filename<<std::endl;
            fileLabel->ChangeText("Error Reading WF2ROOT Trees in   "+filename);
            this->Layout();
            return;
        }
    }

    histos1.clear();
    dataHistos1.clear();
    for (unsigned int iv=0; iv<tdReader.tdData.VARNAMES.size(); iv++)
    {
        const TString vn=tdReader.tdData.VARNAMES[iv];

        //tdReader.ProgressMeter(tdReader.tdData.VARNAMES.size(),iv);

        TObject* xx=gDirectory->Get("h"+vn);
        if (!xx) 
        {
            std::cerr<<"tordaqGui:  Error Reading Histogram:  "<<vn<<std::endl;
            continue;
        }

        // copy into memory (if on disk):
        // TH1* hh=(TH1*)xx->Clone("hvt%d");

        TH1* hh=(TH1*)xx;

        hh->GetXaxis()->SetTimeFormat("#splitline{}{#splitline{%b %d}{%H:%M:%S}}");
        hh->GetXaxis()->SetTimeDisplay(1);
        hh->GetXaxis()->SetNdivisions(5);
        hh->GetYaxis()->SetTitleOffset(0.5);
        hh->GetXaxis()->SetTitle("");
        hh->GetYaxis()->SetTitle("");
        hh->SetTitle(vn);
        dataHistos1.push_back(hh);
        for (cbit=combos1.begin(); cbit!=combos1.end(); ++cbit)
            // must offset by 1, because 0 is reserved for no selection
            (*cbit)->AddEntry(vn,iv+1);
        if (iv==0)
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
    
    if (dataHistos1.size() != tdReader.tdData.VARNAMES.size())
         fileLabel->ChangeText(filename + " --   ERROR READING HISTOS.");
    else fileLabel->ChangeText(filename);
    this->Layout();
}
void tordaqGui::Draw1()
{
    if (dataHistos1.size()<1)
    {
        fileLabel->ChangeText("!! OPEN A FILE FIRST !!");
        this->Layout();
        return;
    }

    TCanvas *ctmp=canvas1->GetCanvas();
    double xmin,xmax;
    if (histos1.size()>0) {
        double ymin,ymax;
        ctmp->GetRangeAxis(xmin,ymin,xmax,ymax);
    }
    ctmp->cd();
    ctmp->Clear();
   
    // determine minimum and maximum for y-range:
    float min=999999,max=-9999999;
    for (unsigned int ii=0; ii<dataHistos1.size(); ii++)
    {
        TH1* hh=dataHistos1[ii];

        bool selected=false;
        for (unsigned jj=0; jj<combos1.size(); jj++)
        {
            // must offset by 1, because 0 is reserved for no selection
            if (combos1[jj]->GetSelected()==ii+1) selected=true;
        }
        if (selected || showAllCheck->IsOn())
        {
            if (hh->GetMaximum()>max) max=hh->GetMaximum();
            if (hh->GetMinimum()<min) min=hh->GetMinimum();
        }
    }

    legend1->Clear();
    histos1.clear();
    for (unsigned int ii=0; ii<dataHistos1.size(); ii++)
    {
        bool selected=false;
        for (unsigned jj=0; jj<combos1.size(); jj++)
        {
            // must offset by 1, because 0 is reserved for no selection
            if (combos1[jj]->GetSelected()==ii+1) selected=true;
        }
        if (selected || showAllCheck->IsOn())
        {
            TH1* hh=dataHistos1[ii];
            //TH1* hh;
            //if (denoiseCheck->IsOn()) hh=tordaqUtil::deNoise(dataHistos1[ii]);
            //else hh=dataHistos1[ii];
            
            hh->SetMaximum(max);
            hh->SetMinimum(min);
            hh->GetXaxis()->SetRangeUser(xmin,xmax);

            // This should give a huge speed up when overlaying many plots.
            // But will need some reworking in the tordaqGui's zoom functions.
            //histos1.push_back(tordaqUtil::zoomHisto(
            //            hh,
            //            Form("%s_zoom",histos1[ii]->GetName()),
            //            xmin,
            //            xmax));

            histos1.push_back(hh);
           
            hh->SetLineWidth(2);
            hh->SetLineColor(colors[(histos1.size()-1)%5]);
            hh->SetLineStyle((histos1.size()-1)/5+1);
            legend1->AddEntry(hh,hh->GetTitle(),"L");
            hh->Draw(histos1.size()==1?"":"SAME");
        }
    }
    
    legend1->Draw();
    ctmp->Update();
}
void tordaqGui::Update1(const double xmin=0,const double xmax=-1)
{
    if (xmax>xmin)
    {
        for (unsigned int ii=0; ii<histos1.size(); ii++)
        {
            histos1[ii]->GetXaxis()->SetRangeUser(xmin,xmax);
            //histos1[ii]=tordaqUtil::zoomHisto(histos1[ii],
            //            Form("%s_zoom",histos1[ii]->GetName()),
            //            xmin,
            //            xmax);
            //histos1[ii]->Draw(ii==0?"":"SAME");
        }
        zoomSlider->SetPosition(xmin);
    }
    canvas1->GetCanvas()->Modified();
    canvas1->GetCanvas()->Update();
}
void tordaqGui::ZoomIn1()
{
    static const double frac=0.45;
    double x1,x2,y1,y2;
    TCanvas *ctmp=canvas1->GetCanvas();
    ctmp->GetRangeAxis(x1,y1,x2,y2);
    const double xlo=x1+(x2-x1)*frac;
    const double xhi=x2-(x2-x1)*frac;
    Update1(xlo,xhi);
}
void tordaqGui::ZoomOut1()
{
    static const double frac=1.0;
    double x1,x2,y1,y2;
    TCanvas *ctmp=canvas1->GetCanvas();
    ctmp->GetRangeAxis(x1,y1,x2,y2);
    const double xlo=x1-(x2-x1)*frac;
    const double xhi=x2+(x2-x1)*frac;
    Update1(xlo,xhi);
}
void tordaqGui::yZoomIn1()
{
    static const double frac=0.2;
    double x1,x2,y1,y2;
    TCanvas *ctmp=canvas1->GetCanvas();
    ctmp->GetRangeAxis(x1,y1,x2,y2);
    const double ylo=y1+(y2-y1)*frac;
    const double yhi=y2-(y2-y1)*frac;
    histos1[0]->SetMinimum(ylo);
    histos1[0]->SetMaximum(yhi);
    Update1();
}
void tordaqGui::yZoomOut1()
{
    static const double frac=1.0;
    double x1,x2,y1,y2;
    TCanvas *ctmp=canvas1->GetCanvas();
    ctmp->GetRangeAxis(x1,y1,x2,y2);
    const double ylo=y1-(y2-y1)*frac;
    const double yhi=y2+(y2-y1)*frac;
    histos1[0]->SetMinimum(ylo);
    histos1[0]->SetMaximum(yhi);
    Update1();
}
void tordaqGui::doZoomSlider1()
{
    const int pos=zoomSlider->GetPosition();
    double x1,x2,y1,y2;
    TCanvas *ctmp=canvas1->GetCanvas();
    if (!ctmp || histos1.size()<1)
    {
        // invalid
        zoomSlider->SetPosition(zoomSlider->GetMinPosition());
    }
    else
    {
        ctmp->GetRangeAxis(x1,y1,x2,y2);
        if (pos>=histos1[0]->GetXaxis()->GetXmax()
                || pos<histos1[0]->GetXaxis()->GetXmin())
            zoomSlider->SetPosition(x1);
        else
            Update1(pos,pos+(x2-x1));
    }
}
void tordaqGui::PanLeft1()
{
    if (histos1.size()<1) return;
    static const double frac=0.5;
    double x1,x2,y1,y2;
    TCanvas *ctmp=canvas1->GetCanvas();
    ctmp->GetRangeAxis(x1,y1,x2,y2);
    const double xlo=x1-(x2-x1)*frac;
    const double xhi=x2-(x2-x1)*frac;
    Update1(xlo,xhi);
}
void tordaqGui::PanRight1()
{
    if (histos1.size()<1) return;
    static const double frac=0.5;
    double x1,x2,y1,y2;
    TCanvas *ctmp=canvas1->GetCanvas();
    ctmp->GetRangeAxis(x1,y1,x2,y2);
    const double xlo=x1+(x2-x1)*frac;
    const double xhi=x2+(x2-x1)*frac;
    Update1(xlo,xhi);
}
int main(int argc, char **argv)
{    
    int itmp;
    const char* usage="\ntordaqGui [options] [filename]\n"
        "\t -A (do synchronization analysis - memory intensive)\n"
        "\t -S (force synchronization)\n"
        "\t -h (print usage)\n";
    while ( (itmp=getopt(argc,argv,"ASh")) != -1 )
    {
        switch (itmp)
        {
            case 'A':
                doSynchroAna=true;
                std::cout<<"Performing synchronization analysis (memory intensive)."<<std::endl;
                break;
            case 'S':
                forceSynchro=true;
                std::cout<<"Forcing synchronization."<<std::endl;
                break;
            case 'h':
                std::cout<<usage<<std::endl;
                exit(0);
            default:
                std::cout<<"Invalid Argument:  -"<<itmp<<std::endl;
                std::cout<<usage<<std::endl;
                exit(0);
        }
    }

    if (argc>1 && strcmp(argv[argc-1],"-A") && 
                  strcmp(argv[argc-1],"-S") &&
                  strcmp(argv[argc-1],"-h"))
        filename=argv[argc-1];
    
    TApplication theApp("App", &argc, argv);
    tordaqGui * mmf=new tordaqGui(gClient->GetRoot(), 2000, 600);
    theApp.Run();
    return 0;
}

