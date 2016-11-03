#ifndef __TORDAQGUI_H__
#define __TORDAQGUI_H__

#include <TApplication.h>
#include <TStyle.h>
#include <TGaxis.h>
#include <TCanvas.h>
#include <TGFrame.h>
#include <TGButton.h>
#include <TGLabel.h>
#include <TGFileDialog.h>
#include <TText.h>
#include <TLegend.h>
#include <TSystem.h>
#include <Rtypes.h>
#include <TH1.h>
#include <TF1.h>
#include <TTree.h>
#include <TProfile.h>
#include <TObject.h>
#include <TVirtualFFT.h>
#include <TMath.h>
#include <TList.h>
#include <TGenericClassInfo.h>
#include <TGNumberEntry.h>
#include <TRootEmbeddedCanvas.h>
#include <TGStatusBar.h>
#include <TTimeStamp.h>
#include <TString.h>
#include <TGComboBox.h>
#include <TGSlider.h>
#include <TGDoubleSlider.h>
#include <TGProgressBar.h>
#include <TROOT.h>
#include <TFile.h>
#include <TGaxis.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <math.h>
#include <vector>

#include "tordaqReader.hh"

class tordaqGui: public TGMainFrame {
    private:
        int colors[5];
        TRootEmbeddedCanvas *canvas1;
        TRootEmbeddedCanvas *canvas2;
        TGStatusBar          *fStatusBar;
        TGLabel *fileLabel;
        TGNumberEntryField *delayField;
        TGNumberEntryField *resampleField;
        TGHorizontalFrame *topFrame;
        TGTextButton *redrawBtn;
        TGTextButton *xZoomoutBtn;
        TGTextButton *xZoominBtn;
        TGTextButton *yZoomoutBtn;
        TGTextButton *yZoominBtn;
        TGTextButton *panleftBtn;
        TGTextButton *panrightBtn;
        TGCheckButton *denoiseCheck;
        TGHSlider *zoomSlider;
        TGHProgressBar *progressBar;
        TGLabel *zoomSliderLabelMin;
        TGLabel *zoomSliderLabelMid;
        TGLabel *zoomSliderLabelMax;
        TGCheckButton* showAllCheck;
        std::vector <TGCheckButton*> selectors1;
        std::vector <TGCheckButton*> selectors2;
        std::vector <TGComboBox*> combos1;
        std::vector <TH1*> histos1;
        TLegend *legend1;
        TGComboBox *combo2;
        TFile *datafile;
        TTree *datatree;
        TTimeStamp starttime;
        std::vector <TH1*> dataHistos1;
        std::vector <TH1*> dataHistos1N;
        std::vector <TH1*> dataHistos1S;
        tordaqReader tdReader;
        //tordaqData tdData;

    public:
        tordaqGui(const TGWindow *p, UInt_t w, UInt_t h);
        virtual ~tordaqGui();
        ClassDef(tordaqGui,0);
        void *DoOpen1(void *ptr);
        void DoOpen(TString filename);
        inline void DoOpen() { DoOpen(""); }
        void Draw1();
        void Update1(const double,const double);
        void ZoomIn1();
        void ZoomOut1();
        void yZoomIn1();
        void yZoomOut1();
        void PanLeft1();
        void PanRight1();
        void doZoomSlider1();
        void SetStyle()
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
            gStyle->SetPadBottomMargin(0.15);
            // Font
            gStyle->SetTextFont(132);
            gStyle->SetLabelFont(132, "XYZ");
            gStyle->SetTitleFont(132, "XYZ");
            gStyle->SetStatFont(132);
            gStyle->SetLegendFont(132);
            // Fontsize
            gStyle->SetLabelSize(0.05, "XYZ");
            gStyle->SetTitleSize(0.06, "XYZ");
            gStyle->SetTitleOffset(0.6, "X");
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

            gROOT->ForceStyle();
        }
};
#endif
