#ifndef __GUI_H__
#define __GUI_H__

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
#include <TROOT.h>
#include <TFile.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <math.h>
#include <vector>


class MyMainFrame: public TGMainFrame {
    private:
        int colors[5];
        TRootEmbeddedCanvas *canvas1;
        TRootEmbeddedCanvas *canvas2;
        TGStatusBar          *fStatusBar;
        TGLabel *fileLabel;
        TGNumberEntryField *field_delay;
        TGNumberEntryField *field_resample;
        TGNumberEntryField *field_window;
        TGTextButton *redrawBtn;
        TGTextButton *zoomoutBtn;
        TGTextButton *zoominBtn;
        TGTextButton *panleftBtn;
        TGTextButton *panrightBtn;
        TGCheckButton *check_denoise;
        TGDoubleHSlider *zoomSlider;
        TGLabel *zoomSliderLabel1;
        TGLabel *zoomSliderLabel2;
        TGLabel *zoomSliderLabelU1;
        TGLabel *zoomSliderLabelU2;
        std::vector <TGCheckButton*> selectors1;
        std::vector <TGCheckButton*> selectors2;
        std::vector <TGComboBox*> combos1;
        std::vector <TH1*> histos1;
        TLegend *legend1;
        TGComboBox *combo2;
        TFile *datafile;
        TTree *datatree;
        TTimeStamp starttime;
        std::vector <TH1*> datahistos;
    public:
        MyMainFrame(const TGWindow *p, UInt_t w, UInt_t h);
        virtual ~MyMainFrame();
        ClassDef(MyMainFrame,0);
        void DoOpen();
        void Update1();
        void ZoomIn1();
        void ZoomOut1();
        void PanLeft1();
        void PanRight1();
        void SetStyle();
        void UpdateZoomLabels();
};
#endif
