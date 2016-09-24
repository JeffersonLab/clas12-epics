#ifndef __TORDAQUTIL_HH__
#define __TORDAQUTIL_HH__
class tordaqUtil
{
public:
static TH1* zoomHisto(TH1* hin,const int firstBin,const int lastBin)
{
    if (firstBin<1 || lastBin>hin->GetNbinsX())
    {
        std::cerr<<"zoomHistogram Error:  invalid bins"<<std::endl;
        return NULL;
    }
    const int nBins=lastBin-firstBin+1;
    TH1* hout=new TH1F(
            Form("%s_zoom",hin->GetName()),
            Form(";%s;%s",hin->GetXaxis()->GetTitle,hin->GetYaxis()->GetTitle()),
            nBins,
            hin->GetXaxis()->GetBinLoEdge(firstBin),
            hin->GetXaxis()->GetBinUpEdge(lastBin));
    for (int ii=1,ii<nBins; ii++)
    {
        hout->SetBinContent(ii,hin->GetBinContent(firstBin+ii-1));
        hout->SetBinError(ii,hin->GetBinError(firstBin+ii-1));
    }
    return hout;
}

/*
 * Remove noise via transform to frequency domain and back.
 * copied from Hall-D (yqiang)
 */
static TH1 *deNoise(TH1 *h1)
{
    // copied from Hall-D (yqiang)

    const double filter_range = 1.02;
    const double noise_sup = 30; //additional noise suppresion factor in db.
    const int index_max = 4;
    const double list_noise[6] = { 60, 120, 180, 205, 240, 300 };

    const double xrange = h1->GetXaxis()->GetXmax() - h1->GetXaxis()->GetXmin();
    const int nbin = h1->GetNbinsX();
    const TString hname = TString(h1->GetName())+"_de";
    TH1 *h2 = (TH1*) gROOT->FindObject(hname);
    if (h2) delete h2;
    h2 = (TH1*) h1->Clone(hname);

    // FFT to frequency domain
    double *re_full = new double[nbin];
    double *im_full = new double[nbin];
    TVirtualFFT::SetTransform(0);
    TH1 *h1_mag = h1->FFT(0, "MAG");
    TVirtualFFT *fft = TVirtualFFT::GetCurrentTransform();
    fft->GetPointsComplex(re_full, im_full);

    // Uniform filter
    double *filter = new double[nbin];
    for (int i = 0; i < nbin; i++)
        filter[i] = 1.;
    for (int index = 0; index < index_max; index++) {
        int fmin = int(floor(list_noise[index] * xrange / filter_range))
            - 1;
        int fmax = int(ceil(list_noise[index] * xrange * filter_range)) + 1;
        if (fmin < 1)
            fmin = 1;
        if (fmax >= nbin / 2)
            fmax = nbin / 2 - 1;
        for (int i = fmin; i < fmax; i++) {
            filter[i] = filter[nbin - i - 1] = pow(10, -noise_sup / 10.);
        }
    }

    // apply filter and transform back
    for (int i = 0; i < nbin; i++) {
        re_full[i] *= filter[i];
        im_full[i] *= filter[i];
    }
    TVirtualFFT *fft_back = TVirtualFFT::FFT(1, &nbin, "C2R M K");
    fft_back->SetPointsComplex(re_full, im_full);
    fft_back->Transform();
    TH1::TransformHisto(fft_back, (TH1*) h2, "Re");
    h2->Scale(1. / nbin);

    delete h1_mag;
    //delete re_full;
    //delete im_full;
    //delete filter;
    return h2;
}

/*
 * Resample data to lower frequency than the base frequency (upto 10000 Hz)
 * copied from Hall-D (yqiang)
 */
TH1F *Resample(
        TH1 *h1,
        const double freq,
        const double offset, 
        const double delay,
        const Bool_t denoise,
        const Bool_t cut,
        const double xmin,
        const double xmax,
        const struct Scale scale) {
    
    if (!h1) return 0;

    const int nbin = h1->GetNbinsX();
    int bin_xmin, bin_xmax;
    if (cut) {
        bin_xmin = h1->FindBin(xmin);
        bin_xmax = h1->FindBin(xmax);
    } else {
        bin_xmin = 1;
        bin_xmax = nbin;
    }

    double base_frequency = nbin
        / (h1->GetXaxis()->GetBinUpEdge(nbin)
        - h1->GetXaxis()->GetBinLowEdge(1));
    // round base frequency to 10 Hz
    base_frequency = floor(base_frequency / 10. + 0.5) * 10.;
    // number of bins to be combined for a new bin
    int nrebin = int(floor(base_frequency / freq + 0.5));
    if (nrebin < 1) nrebin = 1;
    const int bin_delay = int(floor(delay * base_frequency + 0.5));
    // number of new bins
    const int nbin_new = int(
            floor(double(bin_xmax - bin_xmin + 1) / double(nrebin)));
    const double xmin_new = h1->GetXaxis()->GetBinLowEdge(bin_xmin);
    const double xmax_new = h1->GetXaxis()->GetBinUpEdge(
            bin_xmin + nbin_new * nrebin - 1);

    const TString hname = TString(h1->GetName())+"_res";
    const TString htitle = TString(h1->GetName()) + TString(';')
        + TString(h1->GetXaxis()->GetTitle()) + TString(';') + scale.unit;

    TH1F *h2 = (TH1F*) gROOT->FindObject(hname);
    if (h2) delete h2;

    h2 = new TH1F(hname, htitle, nbin_new, xmin_new, xmax_new);
    for (int i = 0; i < nbin_new; i++) {
        double tmpy = 0;
        double tmpy2 = 0;
        for (int j = 0; j < nrebin; j++) {
            const int bin_old = bin_xmin + i * nrebin + j + 1 + bin_delay;
            if (bin_old > nbin) {
                tmpy += h1->GetBinContent(nbin);
                tmpy2 += pow(h1->GetBinContent(nbin), 2.);
            } else {
                tmpy += h1->GetBinContent(
                        bin_xmin + i * nrebin + j + 1 + bin_delay);
                tmpy2 += pow(
                        h1->GetBinContent(
                        bin_xmin + i * nrebin + j + 1 + bin_delay), 2);
            }
        }
        tmpy = tmpy / double(nrebin);
        tmpy2 = sqrt(tmpy2 / double(nrebin) - tmpy * tmpy);
        h2->SetBinContent(i + 1, offset + tmpy);
        h2->SetBinError(i + 1, tmpy2 / sqrt(double(nrebin)));
    }
    h2->Scale(scale.coeff);
    if (!denoise) return h2;
    else {
        TH1F* h3 = DeNoise(h2);
        return h3;
    }
}
};
#endif
