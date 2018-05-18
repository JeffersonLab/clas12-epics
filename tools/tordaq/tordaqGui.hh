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
        static const int NCOLORS=5;
        int colors[NCOLORS];
        TRootEmbeddedCanvas *canvas1=NULL;
        TRootEmbeddedCanvas *canvas2=NULL;
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
        TGTextButton *yPanUpBtn;
        TGTextButton *yPanDownBtn;
        TGTextButton *xSyncUpBtn;
        TGTextButton *xSyncDownBtn;
        TGTextButton *panrightBtn;
        TGCheckButton *denoiseCheck;
        TGHSlider *zoomSlider;
        TGHProgressBar *progressBar;
        TGLabel *zoomSliderLabelMin;
        TGLabel *zoomSliderLabelMid;
        TGLabel *zoomSliderLabelMax;
        TGCheckButton* showAllCheck=NULL;
        std::vector <TGComboBox*> combos1;
        std::vector <TGComboBox*> combos2;
        std::vector <TH1*> histos1;
        std::vector <TH1*> histos2;
        TLegend *legend1;
        TLegend *legend2;
        TFile *datafile;
        TTree *datatree;
        TTimeStamp starttime;
        std::vector <TH1*> dataHistos1;
        std::vector <TH1*> dataHistos2;
        tordaqReader tdReader;
        //tordaqData tdData;

    public:
        tordaqGui(const TGWindow *p, UInt_t w, UInt_t h);
        virtual ~tordaqGui();
        ClassDef(tordaqGui,0);
        void *DoOpen1(void *ptr);
        void DoOpen(TString filename);
        inline void DoOpen() { DoOpen(""); }
        void Draw();
        void Update(const double,const double,const double,const double);
        void Update(TCanvas *,std::vector<TH1*>*,const double,const double,const double,const double);
        void xZoomIn();
        void xZoomOut();
        void yZoomIn();
        void yZoomOut();
        void xPanLeft();
        void xPanRight();
        void xSyncUp();
        void xSyncDown();
        void yPanUp();
        void yPanDown();
        void yPanUp(TCanvas *,std::vector<TH1*>*);
        void yPanDown(TCanvas *,std::vector<TH1*>*);
        void yZoomIn(TCanvas *,std::vector<TH1*>*);
        void yZoomOut(TCanvas *,std::vector<TH1*>*);
        void doZoomSlider();
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
