#include "tordaqGui.hh"
void tordaqGui::Update(
        TCanvas *canvas,std::vector<TH1*> *histos,
        const double xmin=0,const double xmax=-1,
        const double ymin=0,const double ymax=-1)
{
    if (histos->size()<1) return;
    if (!canvas) return;
    if (xmax>xmin)
    {
        for (unsigned int ii=0; ii<histos->size(); ii++) {
            histos->at(ii)->GetXaxis()->SetRangeUser(xmin,xmax);
            //histos->at(ii)=tordaqUtil::zoomHisto(histos->at(ii),
            //            Form("%s_zoom",histos->at(ii)->GetName()),
            //            xmin,
            //            xmax);
            //histos->at(ii)->Draw(ii==0?"":"SAME");
        }
        zoomSlider->SetPosition(xmin);
    }
    if (ymax>ymin) {
        for (unsigned int ii=0; ii<histos->size(); ii++) {
            histos->at(ii)->GetYaxis()->SetRangeUser(ymin,ymax);
            //histos->at(ii)=tordaqUtil::zoomHisto(histos->at(ii),
            //            Form("%s_zoom",histos->at(ii)->GetName()),
            //            xmin,
            //            xmax);
            //histos->at(ii)->Draw(ii==0?"":"SAME");
        }
    }
    canvas->Modified();
    canvas->Update();
}
void tordaqGui::Update(const double xmin=0,const double xmax=-1,
                       const double ymin=0,const double ymax=-1)
{
    if (canvas1 && canvas1->GetCanvas()) Update(canvas1->GetCanvas(),&histos1,xmin,xmax,ymin,ymax);
    if (canvas2 && canvas2->GetCanvas()) Update(canvas2->GetCanvas(),&histos2,xmin,xmax,ymin,ymax);
}
void tordaqGui::xZoomIn()
{
    if (histos1.size()<1) return;
    if (!canvas1 || !canvas1->GetCanvas()) return;
    static const double frac=0.45;
    double x1,x2,y1,y2;
    canvas1->GetCanvas()->GetRangeAxis(x1,y1,x2,y2);
    const double xlo=x1+(x2-x1)*frac;
    const double xhi=x2-(x2-x1)*frac;
    Update(xlo,xhi);
}
void tordaqGui::xZoomOut()
{
    if (histos1.size()<1) return;
    if (!canvas1 || !canvas1->GetCanvas()) return;
    static const double frac=1.0;
    double x1,x2,y1,y2;
    canvas1->GetCanvas()->GetRangeAxis(x1,y1,x2,y2);
    const double xlo=x1-(x2-x1)*frac;
    const double xhi=x2+(x2-x1)*frac;
    Update(xlo,xhi);
}
void tordaqGui::doZoomSlider()
{
    const int pos=zoomSlider->GetPosition();
    double x1,x2,y1,y2;
    TCanvas *ctmp=canvas1->GetCanvas();
    if (!ctmp || histos1.size()<1) {
        // invalid
        zoomSlider->SetPosition(zoomSlider->GetMinPosition());
    }
    else {
        ctmp->GetRangeAxis(x1,y1,x2,y2);
        if (pos>=histos1[0]->GetXaxis()->GetXmax()
                || pos<histos1[0]->GetXaxis()->GetXmin())
            zoomSlider->SetPosition(x1);
        else
            Update(pos,pos+(x2-x1));
    }
}
void tordaqGui::xSyncUp()
{
    if (histos1.size()<1 || histos2.size()<1) return;
    if (!canvas1 || !canvas1->GetCanvas()) return;
    if (!canvas2 || !canvas2->GetCanvas()) return;
    double x2a,x2b,y2a,y2b;
    canvas2->GetCanvas()->GetRangeAxis(x2a,y2a,x2b,y2b);
    Update(canvas1->GetCanvas(),&histos1,x2a,x2b);
}
void tordaqGui::xSyncDown()
{
    if (histos1.size()<1 || histos2.size()<1) return;
    if (!canvas1 || !canvas1->GetCanvas()) return;
    if (!canvas2 || !canvas2->GetCanvas()) return;
    double x1a,x1b,y1a,y1b;
    canvas1->GetCanvas()->GetRangeAxis(x1a,y1a,x1b,y1b);
    Update(canvas2->GetCanvas(),&histos2,x1a,x1b);
}
void tordaqGui::xPanLeft()
{
    if (histos1.size()<1) return;
    if (!canvas1 || !canvas1->GetCanvas()) return;
    static const double frac=0.3;
    double x1,x2,y1,y2;
    canvas1->GetCanvas()->GetRangeAxis(x1,y1,x2,y2);
    const double xlo=x1-(x2-x1)*frac;
    const double xhi=x2-(x2-x1)*frac;
    Update(xlo,xhi);
}
void tordaqGui::xPanRight()
{
    if (histos1.size()<1) return;
    if (!canvas1 || !canvas1->GetCanvas()) return;
    static const double frac=0.3;
    double x1,x2,y1,y2;
    canvas1->GetCanvas()->GetRangeAxis(x1,y1,x2,y2);
    const double xlo=x1+(x2-x1)*frac;
    const double xhi=x2+(x2-x1)*frac;
    Update(xlo,xhi);
}
void tordaqGui::yPanUp(TCanvas *canvas,std::vector<TH1*> *histos)
{
    if (histos->size()<1) return;
    if (!canvas1) return;
    static const double frac=0.2;
    double x1,x2,y1,y2;
    canvas->GetRangeAxis(x1,y1,x2,y2);
    const double ylo=y1+(y2-y1)*frac;
    const double yhi=y2+(y2-y1)*frac;
    Update(canvas,histos,x1,x2,ylo,yhi);
}
void tordaqGui::yPanDown(TCanvas *canvas,std::vector<TH1*> *histos)
{
    if (histos->size()<1) return;
    if (!canvas) return;
    static const double frac=0.2;
    double x1,x2,y1,y2;
    canvas->GetRangeAxis(x1,y1,x2,y2);
    const double ylo=y1-(y2-y1)*frac;
    const double yhi=y2-(y2-y1)*frac;
    Update(canvas,histos,x1,x2,ylo,yhi);
}
void tordaqGui::yZoomIn(TCanvas *canvas,std::vector<TH1*> *histos)
{
    if (histos->size()<1) return;
    if (!canvas) return;
    static const double frac=0.2;
    double x1,x2,y1,y2;
    canvas->GetRangeAxis(x1,y1,x2,y2);
    const double ylo=y1+(y2-y1)*frac;
    const double yhi=y2-(y2-y1)*frac;
    histos->at(0)->SetMinimum(ylo);
    histos->at(0)->SetMaximum(yhi);
    Update(canvas,histos);
}
void tordaqGui::yZoomOut(TCanvas *canvas,std::vector<TH1*> *histos)
{
    if (histos->size()<1) return;
    if (!canvas1) return;
    static const double frac=1.0;
    double x1,x2,y1,y2;
    canvas->GetRangeAxis(x1,y1,x2,y2);
    const double ylo=y1-(y2-y1)*frac;
    const double yhi=y2+(y2-y1)*frac;
    histos->at(0)->SetMinimum(ylo);
    histos->at(0)->SetMaximum(yhi);
    Update(canvas,histos);
}

void tordaqGui::yPanUp()
{
    if (canvas1) yPanUp(canvas1->GetCanvas(),&histos1);
    if (canvas2) yPanUp(canvas2->GetCanvas(),&histos2);
}
void tordaqGui::yPanDown()
{
    if (canvas1) yPanDown(canvas1->GetCanvas(),&histos1);
    if (canvas2) yPanDown(canvas2->GetCanvas(),&histos2);
}
void tordaqGui::yZoomIn()
{
    if (canvas1) yZoomIn(canvas1->GetCanvas(),&histos1);
    if (canvas2) yZoomIn(canvas2->GetCanvas(),&histos2);
}
void tordaqGui::yZoomOut()
{
    if (canvas1) yZoomOut(canvas1->GetCanvas(),&histos1);
    if (canvas2) yZoomOut(canvas2->GetCanvas(),&histos2);
}
