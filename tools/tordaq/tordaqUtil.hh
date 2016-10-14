#ifndef __TORDAQUTIL_HH__
#define __TORDAQUTIL_HH__
class tordaqUtil
{
public:
static TH1* zoomHisto(TH1* hin,const char* name,const int firstBin,const int lastBin)
{
    if (gDirectory->Get(name)) gDirectory->Get(name)->Delete();
    if (firstBin>lastBin || firstBin<1 || lastBin>hin->GetNbinsX())
    {
        std::cerr<<"zoomHistogram Error:  invalid bins:  "<<std::endl;
        return NULL;
    }
    const int nBins=lastBin-firstBin+1;
    TH1* hout=new TH1F(
            name,
            Form(";%s;%s",hin->GetXaxis()->GetTitle(),hin->GetYaxis()->GetTitle()),
            nBins,
            hin->GetXaxis()->GetBinLowEdge(firstBin),
            hin->GetXaxis()->GetBinUpEdge(lastBin));
    for (int ii=firstBin; ii<=lastBin; ii++)
    {
        hout->SetBinContent(ii-firstBin+1, hin->GetBinContent(ii));
        hout->SetBinError(  ii-firstBin+1, hin->GetBinError(ii));
    }
    return hout;
}
static TH1* zoomHisto(TH1* hin,const char* name,const double x1,const double x2)
{
    int firstBin=hin->FindBin(x1);
    int lastBin=hin->FindBin(x2);
    if (firstBin<1) firstBin=1;
    if (lastBin>hin->GetNbinsX()) lastBin=hin->GetNbinsX();
    return zoomHisto(hin,name,firstBin,lastBin);
}


//
// Remove noise via transform to frequency domain and back.
// Copied from Hall-D (yqiang)
//
// needs ROOT built with FFT
//
static TH1 *deNoise(TH1 *h1)
{
    const double filter_range = 1.02;
    const double noise_sup = 30; //additional noise suppresion factor in db.
    const int index_max = 4;
    const double list_noise[6] = { 60, 120, 180, 205, 240, 300 };
    const double xrange = h1->GetXaxis()->GetXmax()-h1->GetXaxis()->GetXmin();
    const TString hname = TString(h1->GetName())+"_de";
    TH1 *h2 = (TH1*) gROOT->FindObject(hname);
    if (h2) delete h2;
    h2 = (TH1*) h1->Clone(hname);

    // FFT to frequency domain
    int nbin = h1->GetNbinsX();
    double *re_full = new double[nbin];
    double *im_full = new double[nbin];
    TVirtualFFT::SetTransform(0);
    TH1 *h1_mag = h1->FFT(0, "MAG");
    TVirtualFFT *fft = TVirtualFFT::GetCurrentTransform();
    fft->GetPointsComplex(re_full, im_full);

    // Uniform filter
    double * const filter = new double[nbin];
    for (int ii=0; ii<nbin; ii++) filter[ii]=1.;
    for (int index=0; index<index_max; index++)
    {
        int fmin = int(floor(list_noise[index] * xrange / filter_range))- 1;
        int fmax = int(ceil(list_noise[index] * xrange * filter_range)) + 1;
        if (fmin < 1) fmin = 1;
        if (fmax >= nbin / 2) fmax = nbin / 2 - 1;
        for (int ii=fmin; ii<fmax; ii++)
            filter[ii] = filter[nbin-ii-1] = pow(10,-noise_sup/10.);
    }

    // apply filter and transform back
    for (int ii=0; ii<nbin; ii++) {
        re_full[ii] *= filter[ii];
        im_full[ii] *= filter[ii];
    }
    TVirtualFFT *fft_back = TVirtualFFT::FFT(1, &nbin, "C2R M K");
    fft_back->SetPointsComplex(re_full, im_full);
    fft_back->Transform();
    TH1::TransformHisto(fft_back, (TH1*) h2, "Re");
    h2->Scale(1./nbin);

    delete h1_mag;
    //delete re_full;
    //delete im_full;
    //delete filter;
    return h2;
}

//
// Resample data to lower frequency than the base frequency (upto 10000 Hz)
// Copied from Hall-D (yqiang)
//
TH1 *Resample(
        TH1 * const h1,
        const double freq,
        const double offset, 
        const double delay,
        const double xmin=1,
        const double xmax=-1) 
{
    
    if (!h1) return 0;

    const int bin_xmin = xmax>xmin ? h1->FindBin(xmin) : 1;
    const int bin_xmax = xmax>xmin ? h1->FindBin(xmax) : h1->GetNbinsX();

    double base_frequency = h1->GetNbinsX()
        / (h1->GetXaxis()->GetBinUpEdge(h1->GetNbinsX())
        - h1->GetXaxis()->GetBinLowEdge(1));

    // round base frequency to 10 Hz
    base_frequency = floor(base_frequency / 10. + 0.5) * 10.;
    
    // number of bins to be combined for a new bin
    int nrebin = int(floor(base_frequency / freq + 0.5));
    if (nrebin<1) nrebin=1;
    const int bin_delay = int(floor(delay * base_frequency + 0.5));
    
    // number of new bins
    const int nbin_new = int(floor(double(bin_xmax - bin_xmin + 1) / double(nrebin)));
    const double xmin_new = h1->GetXaxis()->GetBinLowEdge(bin_xmin);
    const double xmax_new = h1->GetXaxis()->GetBinUpEdge(bin_xmin + nbin_new * nrebin - 1);

    const TString hname = TString(h1->GetName())+"_res";
    const TString htitle = TString(h1->GetName()) + ";" + TString(h1->GetXaxis()->GetTitle()) + ";";

    TH1F *h2 = (TH1F*) gROOT->FindObject(hname);
    if (h2) delete h2;
    h2 = new TH1F(hname, htitle, nbin_new, xmin_new, xmax_new);
    
    for (int ii=0; ii<nbin_new; ii++)
    {
        double tmpy=0;
        double tmpy2=0;
        for (int jj=0; jj<nrebin; jj++)
        {
            const int bin_old = bin_xmin + ii*nrebin + jj+1+bin_delay;
            if (bin_old > h1->GetNbinsX())
            {
                tmpy += h1->GetBinContent(h1->GetNbinsX());
                tmpy2 += pow(h1->GetBinContent(h1->GetNbinsX()), 2.);
            }
            else
            {
                tmpy += h1->GetBinContent(bin_xmin + ii*nrebin + jj+1+bin_delay);
                tmpy2 += pow(h1->GetBinContent(bin_xmin + ii*nrebin + jj+1+bin_delay), 2);
            }
        }
        tmpy = tmpy / double(nrebin);
        tmpy2 = sqrt(tmpy2 / double(nrebin) - tmpy * tmpy);
        h2->SetBinContent(ii+1, offset+tmpy);
        h2->SetBinError(ii+1, tmpy2/sqrt(double(nrebin)));
    }
    return h2;
}

};
#endif
