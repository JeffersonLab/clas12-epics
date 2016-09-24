#include "tordaqData.hh"
class tordaqWriter {
public:
    const char* separator=",";
    tordaqWriter(){};
    ~tordaqWriter(){};
    TNtupleD* ntuple=NULL;;
    std::vector <TH1*> histos;
    bool writeAsciiFileFromNtuple()
    {
        return true;
    }
    bool writeAsciiFileFromHistos()
    {
        return true;
    }
    bool writeAsciiFile(const char* filename)
    {
        ntuple=NULL;
        histos.clear();
        TObject *xx=gDirectory->Get("tordaq");
        if (xx)
        {
            ntuple=(TNtupleD*)xx;
            return writeAsciiFileFromNtuple();
        }
        else {
            int ivt=0;
            while (1)
            {
                TObject *xx=gDirectory->Get(Form("h%d",ivt+1));
                if (!xx) break;
                histos.push_back((TH1*)xx);
                ivt++;
            }
            if (ivt!=tordaqData::NVT)
            {
                std::cerr<<"tordaqWriter:  Wrong number of histograms."<<std::endl;
                return false;
            }
            return writeAsciiFileFromHistos();
        }
    }
};

