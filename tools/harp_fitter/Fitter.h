#include <TQObject.h> 
#include <RQ_OBJECT.h>
#include <TGFileDialog.h>

class TF1;
class TH1D;
class TGWindow; 
class TTimeStamp;
class TGMainFrame; 
class TRootEmbeddedCanvas;
class TGTextEntry;
class TGTextEdit;
class TGMsgBox;
class TGComboBox;
class TGraph;
class TGNumberEntry;
class TGCheckButton;
class TGLabel;

class Fitter { 
  RQ_OBJECT("Fitter")
  private: 
    TGMainFrame         *fMain;
    const TGWindow *p_wind;
    TRootEmbeddedCanvas *fEcanvas;
    TGTextEntry *par0;
    TGFileInfo file_info;
    static const int n_counters = 15;
    static const std::string all_harps_dir;
    static const double sqrt2 = 1.41421356237309515;
    void InitData( std::string );
    TGraph *gr_[n_counters];
    std::string counter_names_[n_counters];
    std::string file_name;
    std::string harp_name;
    TGLabel *status_label;
    TGComboBox *counters_box;
    TGTextEdit *comments;
    TGCheckButton *but_to_MYA;
    TGCheckButton *but_to_HBLOG;
    TGCheckButton *but_to_ELOG;
    TGCheckButton *but_to_TLOG;
    //TGMainFrame *fMain_log;
    TGTransientFrame *fMain_log;
    TGTransientFrame *f_Main_FitPars;
    bool fit_2c21;
    bool fit_tagger;
    bool fit_2H02A;
    bool fit_2H00A;
    bool fit_2H01;
    bool preview_mode;
    TGNumberEntry *First_peak_bgr, *First_peak_bgr_min, *First_peak_bgr_max;
    TGNumberEntry *First_peak_A, *First_peak_A_min, *First_peak_A_max;
    TGNumberEntry *First_peak_mean, *First_peak_mean_min, *First_peak_mean_max;
    TGNumberEntry *First_peak_sigm, *First_peak_sigm_min, *First_peak_sigm_max;
    TGNumberEntry *First_peak_range_min, *First_peak_range_max;
    TGNumberEntry *Second_peak_bgr, *Second_peak_bgr_min, *Second_peak_bgr_max;
    TGNumberEntry *Second_peak_A, *Second_peak_A_min, *Second_peak_A_max;
    TGNumberEntry *Second_peak_mean, *Second_peak_mean_min, *Second_peak_mean_max;
    TGNumberEntry *Second_peak_sigm, *Second_peak_sigm_min, *Second_peak_sigm_max;
    TGNumberEntry *Second_peak_range_min, *Second_peak_range_max;
    TGNumberEntry *Third_peak_bgr, *Third_peak_bgr_min, *Third_peak_bgr_max;
    TGNumberEntry *Third_peak_A, *Third_peak_A_min, *Third_peak_A_max;
    TGNumberEntry *Third_peak_mean, *Third_peak_mean_min, *Third_peak_mean_max;
    TGNumberEntry *Third_peak_sigm, *Third_peak_sigm_min, *Third_peak_sigm_max;
    TGNumberEntry *Third_peak_range_min, *Third_peak_range_max;

    TF1 *f_1st_peak, *f_2nd_peak, *f_3rd_peak;
    TH1D *h_1st_peak, *h_2nd_peak, *h_3rd_peak;

    TTimeStamp *tstmp_scan_time;
    long int scan_time_in_sec;

    double aa, bb, alpha;

    TH1D *h_gr_tmp; // This will be used in the Graph2Hist method, 
    // When a hist will be created it will be assigned to h_gr_tmp;

    double *pars_bgr_1st_peak, *pars_A_1st_peak, *pars_mean_1st_peak, *pars_sigm_1st_peak, *range_1st_peak;
    double *pars_bgr_2nd_peak, *pars_A_2nd_peak, *pars_mean_2nd_peak, *pars_sigm_2nd_peak, *range_2nd_peak;
    double *pars_bgr_3rd_peak, *pars_A_3rd_peak, *pars_mean_3rd_peak, *pars_sigm_3rd_peak, *range_3rd_peak;

    //========= Default parameters for "Set Fit Ranges" window =================
    double min_1st_hist, max_1st_hist;
    double min_2nd_hist, max_2nd_hist;
    double min_3rd_hist, max_3rd_hist;

    double scale_Xaxis;

  public:
    Fitter(const TGWindow *p,UInt_t w,UInt_t h, std::string );
    virtual ~Fitter();
    //void DoDraw();
    void OpenFile();
    void Draw_All_Counters();
    void FitData( bool, bool );
    void GetComments();
    void popupMSG(std::string);
    void CloseUtilFrame();
    void CloseFitRanges();
    void CloseApp();
    void SubmitToLogbook();
    bool Fit_2c21(TGraph *, std::string );
    bool Fit_tagger(TGraph *, std::string );
    bool Fit_2H02A(TGraph *, std::string );
    //  bool Fit_2H00A(TGraph *, std::string );
    bool Search_2c21_peaks(TGraph *);
    bool Search_three_peaks(TGraph *);
    void Set_Fit_Pars();
    TH1D *Graph2Hist(TGraph *, double );
    void Load_Fit_Pars();
    void CAPUT();

};
