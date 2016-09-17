
#include "tordaqGui.h"

ClassImp(MyMainFrame);

const char* dataDir="/usr/clas12/DATA/wf2root";
const char *filetypes[] = { "ROOT files", "*.root", 0, 0 };

MyMainFrame::MyMainFrame(const TGWindow *p, UInt_t w, UInt_t h) : TGMainFrame(p, w, h) {
    colors[0]=1;
    colors[1]=2;
    colors[2]=4;
    colors[3]=3;
    colors[4]=6;
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
    gStyle->SetPadTopMargin(0.06);
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

    legend1=new TLegend(0.8,0.8,1,1);
    legend1->SetNColumns(2);

    TGHorizontalFrame *frame_dir = new TGHorizontalFrame(this, 1000, 40);

    // button to open file
    TGTextButton *button_open = new TGTextButton(frame_dir, "&Open File");
    button_open->Connect("Clicked()", "MyMainFrame", this, "DoOpen()");
    frame_dir->AddFrame(button_open,
            new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 5, 5, 2, 2));

    label_dir = new TGLabel(frame_dir, "");
    label_dir->SetTextJustify(kTextLeft | kLHintsExpandX | kTextCenterY);
    label_dir->SetWrapLength(-1);
    frame_dir->AddFrame(label_dir,
            new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 5, 5, 2, 2));

    // button to exit
    TGTextButton *button_exit = new TGTextButton(frame_dir, "&Exit",
            "gApplication->Terminate(0)");
    frame_dir->AddFrame(button_exit,
            new TGLayoutHints(kLHintsRight | kLHintsCenterY, 10, 5, 2, 2));

    AddFrame(frame_dir, new TGLayoutHints(kLHintsExpandX, 2, 2, 2, 2));

    TGHorizontalFrame *dogframe = new TGHorizontalFrame(this, 1000, 250);

    TGVerticalFrame *catframe=new TGVerticalFrame(dogframe,100,250);

    for (int ii=0; ii<5; ii++)
    {
        combos1.push_back(new TGComboBox(catframe));
        combos1[combos1.size()-1]->AddEntry(" ",0);
        catframe->AddFrame(combos1[combos1.size()-1],new TGLayoutHints(kLHintsLeft | kLHintsCenterY,2,2,2,2));
        combos1[combos1.size()-1]->Resize(60,20);
        combos1[combos1.size()-1]->SetForegroundColor(colors[ii]);
    }
    
    button_redraw = new TGTextButton(catframe, "&Draw");
    button_redraw->Connect("Clicked()","MyMainFrame",this,"Update1()");
    button_redraw->Resize(60,20);
    catframe->AddFrame(button_redraw,new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 2, 2, 2, 2));
    
    button_zoomin = new TGTextButton(catframe, "&Zoom In");
    button_zoomin->Connect("Clicked()","MyMainFrame",this,"ZoomIn1()");
    button_zoomin->Resize(60,20);
    catframe->AddFrame(button_zoomin,new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 2, 2, 2, 2));
    button_zoomout = new TGTextButton(catframe, "&Zoom Out");
    button_zoomout->Connect("Clicked()","MyMainFrame",this,"ZoomOut1()");
    button_zoomout->Resize(60,20);
    catframe->AddFrame(button_zoomout,new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 2, 2, 2, 2));

    button_panleft = new TGTextButton(catframe, "&Pan Left");
    button_panleft->Connect("Clicked()","MyMainFrame",this,"PanLeft1()");
    button_panleft->Resize(60,20);
    catframe->AddFrame(button_panleft,new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 2, 2, 2, 2));
    button_panright = new TGTextButton(catframe, "&Pan Right");
    button_panright->Connect("Clicked()","MyMainFrame",this,"PanRight1()");
    button_panright->Resize(60,20);
    catframe->AddFrame(button_panright,new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 2, 2, 2, 2));
    
    dogframe->AddFrame(catframe,new TGLayoutHints(kLHintsLeft | kLHintsCenterY,2,2,2,2));

    // Canvas for history plot
    canvas1 = new TRootEmbeddedCanvas("canvas1", dogframe, 800, 250);
    dogframe->AddFrame(canvas1, new TGLayoutHints(kLHintsExpandX, 2, 2, 2, 2));

    AddFrame(dogframe,new TGLayoutHints(kLHintsExpandX,2,2,2,2));

/*
    TGHorizontalFrame *frame_cut2 = new TGHorizontalFrame(this, 1000, 40);
    for (int ii=1; ii<=22; ii++)
    {
        selectors1.push_back(new TGCheckButton(frame_cut2,Form("%d",ii)));
        frame_cut2->AddFrame(selectors1[selectors1.size()-1],
                new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 5, 5, 2, 2));
    }
    AddFrame(frame_cut2, new TGLayoutHints(kLHintsExpandX, 2, 2, 2, 2));
*/

    /*
       TGHorizontalFrame *frame_cut3 = new TGHorizontalFrame(this, 1000, 40);
       for (int ii=1; ii<=22; ii++)
       {
       selectors2.push_back(new TGCheckButton(frame_cut3,Form("%d",ii)));
       frame_cut3->AddFrame(selectors2[selectors2.size()-1],
       new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 5, 5, 2, 2));
       }
       AddFrame(frame_cut3, new TGLayoutHints(kLHintsExpandX, 2, 2, 2, 2));
       */

    /*
     * Horizontal frame for plot parameters
     */
    TGHorizontalFrame *frame_cut = new TGHorizontalFrame(this, 1000, 40);

    // Data resample, 1-10000 Hz
    field_resample = new TGNumberEntryField(frame_cut, -1, 100,
            TGNumberFormat::kNESInteger, TGNumberFormat::kNEANonNegative,
            TGNumberFormat::kNELLimitMinMax, 1, 10000);
    field_resample->SetWidth(40);
    frame_cut->AddFrame(new TGLabel(frame_cut, "Resample Freq."),
            new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 5, 2, 2, 2));
    frame_cut->AddFrame(field_resample,
            new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 2, 5, 2, 2));

    // check box for legend
    check_legend = new TGCheckButton(frame_cut, "Legend");
    frame_cut->AddFrame(check_legend,
            new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 10, 5, 2, 2));

    // check box for error bars
    check_error = new TGCheckButton(frame_cut, "Error");
    frame_cut->AddFrame(check_error,
            new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 5, 5, 2, 2));

    // check box for mean value
    check_mean = new TGCheckButton(frame_cut, "Mean");
    frame_cut->AddFrame(check_mean,
            new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 5, 5, 2, 2));

    // check box to do pol2 fit
    check_fit = new TGCheckButton(frame_cut, "Fit");
    frame_cut->AddFrame(check_fit,
            new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 5, 5, 2, 2));

    // check box for denoise
    check_denoise = new TGCheckButton(frame_cut, "DeNoise");
    frame_cut->AddFrame(check_denoise,
            new TGLayoutHints(kLHintsLeft | kLHintsCenterY, 5, 20, 2, 2));

    // button to create root file
    TGTextButton *button_root = new TGTextButton(frame_cut, "Save ROOT File");
    button_root->Connect("Clicked()", "MyMainFrame", this, "DoRoot()");
    frame_cut->AddFrame(button_root,
            new TGLayoutHints(kLHintsRight | kLHintsCenterY, 20, 5, 2, 2));

    AddFrame(frame_cut, new TGLayoutHints(kLHintsExpandX));



    /*
     * Frame to generate plots
     */
    //TGHorizontalFrame *frame_plota = new TGHorizontalFrame(this, 1000, 40);









    /*
     * Canvas for misc plots: zero and ratio
     */
    canvas2 = new TRootEmbeddedCanvas("canvas2", this, 800, 800);
    AddFrame(canvas2,
            new TGLayoutHints(kLHintsExpandX | kLHintsExpandY, 2, 2, 2, 2));

    canvas2->GetCanvas()->Connect("ProcessedEvent(Int_t,Int_t,Int_t,TObject*)","MyMainFrame",this, 
            "EventInfo(Int_t,Int_t,Int_t,TObject*)");

    // status bar
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

void MyMainFrame::DoOpen() {

    std::cout << std::endl;
    // get list of files from GUI
    TList myli;
    TGFileInfo fi;
    TObjString str1;
    fi.fFileTypes = filetypes;
    fi.fIniDir = StrDup(dataDir);
    fi.fMultipleSelection = true;
    TList *filelist;
    new TGFileDialog(gClient->GetRoot(), this, kFDOpen, &fi);
    if (!fi.fFileNamesList) {
        std::cout << "No file selected!" << std::endl;
        return;
    }
    filelist = fi.fFileNamesList;
    TObjLink *lnk=filelist->FirstLink();
    label_dir->ChangeText(lnk->GetObject()->GetName());

    fStatusBar->SetText("Reading Data File ...",0);
    this->Layout();


    datafile=new TFile(lnk->GetObject()->GetName(),"READ");
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
            hh->SetTitle(Form("VT%d",ivt));
            datahistos.push_back(hh);
            for (cbit=combos1.begin(); cbit!=combos1.end(); ++cbit)
                (*cbit)->AddEntry(Form("VT%d",ivt),ivt);
        }
        else break;
        ivt++;
        //if (ivt>3) break;
    }
    
    fStatusBar->SetText("Done Reading Data File.",0);
}
void MyMainFrame::Update1()
{
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
void MyMainFrame::ZoomIn1()
{
    double frac=0.45;
    double x1,x2,y1,y2;
    TCanvas *ctmp=canvas1->GetCanvas();
    ctmp->GetRangeAxis(x1,y1,x2,y2);
    histos1[0]->GetXaxis()->SetRangeUser(x1+(x2-x1)*frac,x2-(x2-x1)*frac);
    //ctmp->Update();
    Update1();
}
void MyMainFrame::ZoomOut1()
{
    double frac=0.45;
    double x1,x2,y1,y2;
    TCanvas *ctmp=canvas1->GetCanvas();
    ctmp->GetRangeAxis(x1,y1,x2,y2);
    histos1[0]->GetXaxis()->SetRangeUser(x1-(x2-x1)*frac,x2+(x2-x1)*frac);
    //ctmp->Update();
    Update1();
}
void MyMainFrame::PanLeft1()
{
    double frac=0.5;
    double x1,x2,y1,y2;
    TCanvas *ctmp=canvas1->GetCanvas();
    ctmp->GetRangeAxis(x1,y1,x2,y2);
    histos1[0]->GetXaxis()->SetRangeUser(x1-(x2-x1)*frac,x2-(x2-x1)*frac);
    Update1();
}
void MyMainFrame::PanRight1()
{
    double frac=0.5;
    double x1,x2,y1,y2;
    TCanvas *ctmp=canvas1->GetCanvas();
    ctmp->GetRangeAxis(x1,y1,x2,y2);
    histos1[0]->GetXaxis()->SetRangeUser(x1+(x2-x1)*frac,x2+(x2-x1)*frac);
    Update1();
}
int main(int argc, char **argv) {

    TApplication theApp("App", &argc, argv);
    new MyMainFrame(gClient->GetRoot(), 1000, 800);
    theApp.Run();
    return 0;

}

