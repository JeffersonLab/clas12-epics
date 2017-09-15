#include "tordaqGui.hh"
void tordaqGui::Update1(const double xmin=0,const double xmax=-1,
                        const double ymin=0,const double ymax=-1)
{
    if (histos1.size()<1) return;
    if (!canvas1 || !canvas1->GetCanvas()) return;
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
    if (ymax>ymin) {
        for (unsigned int ii=0; ii<histos1.size(); ii++)
        {
            histos1[ii]->GetYaxis()->SetRangeUser(ymin,ymax);
            //histos1[ii]=tordaqUtil::zoomHisto(histos1[ii],
            //            Form("%s_zoom",histos1[ii]->GetName()),
            //            xmin,
            //            xmax);
            //histos1[ii]->Draw(ii==0?"":"SAME");
        }
    }
    canvas1->GetCanvas()->Modified();
    canvas1->GetCanvas()->Update();

    if (histos2.size()<1) return;
    if (!canvas2 || !canvas2->GetCanvas()) return;
    if (xmax>xmin)
    {
        for (unsigned int ii=0; ii<histos2.size(); ii++)
            histos2[ii]->GetXaxis()->SetRangeUser(xmin,xmax);
        zoomSlider->SetPosition(xmin);
    }
    if (ymax>ymin) {
        for (unsigned int ii=0; ii<histos2.size(); ii++)
        {
            histos2[ii]->GetYaxis()->SetRangeUser(ymin,ymax);
        }
    }
    canvas2->GetCanvas()->Modified();
    canvas2->GetCanvas()->Update();
}
void tordaqGui::xZoomIn1()
{
    if (histos1.size()<1) return;
    if (!canvas1 || !canvas1->GetCanvas()) return;
    static const double frac=0.45;
    double x1,x2,y1,y2;
    canvas1->GetCanvas()->GetRangeAxis(x1,y1,x2,y2);
    const double xlo=x1+(x2-x1)*frac;
    const double xhi=x2-(x2-x1)*frac;
    Update1(xlo,xhi);
}
void tordaqGui::xZoomOut1()
{
    if (histos1.size()<1) return;
    if (!canvas1 || !canvas1->GetCanvas()) return;
    static const double frac=1.0;
    double x1,x2,y1,y2;
    canvas1->GetCanvas()->GetRangeAxis(x1,y1,x2,y2);
    const double xlo=x1-(x2-x1)*frac;
    const double xhi=x2+(x2-x1)*frac;
    Update1(xlo,xhi);
}
void tordaqGui::yZoomIn1()
{
    if (histos1.size()<1) return;
    if (!canvas1 || !canvas1->GetCanvas()) return;
    static const double frac=0.2;
    double x1,x2,y1,y2;
    canvas1->GetCanvas()->GetRangeAxis(x1,y1,x2,y2);
    const double ylo=y1+(y2-y1)*frac;
    const double yhi=y2-(y2-y1)*frac;
    histos1[0]->SetMinimum(ylo);
    histos1[0]->SetMaximum(yhi);
    Update1();
}
void tordaqGui::yZoomOut1()
{
    if (histos1.size()<1) return;
    if (!canvas1 || !canvas1->GetCanvas()) return;
    static const double frac=1.0;
    double x1,x2,y1,y2;
    canvas1->GetCanvas()->GetRangeAxis(x1,y1,x2,y2);
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
            Update1(pos,pos+(x2-x1));
    }
}
void tordaqGui::xSyncUp()
{
    if (histos1.size()<1 || histos2.size()<1) return;
    if (!canvas1 || !canvas1->GetCanvas()) return;
    if (!canvas2 || !canvas2->GetCanvas()) return;
    double x1,x2,y1,y2;
    canvas2->GetCanvas()->GetRangeAxis(x1,y1,x2,y2);
    Update1(x1,x2,y1,y2);
}
void tordaqGui::xSyncDown()
{
    if (histos1.size()<1 || histos2.size()<1) return;
    if (!canvas1 || !canvas1->GetCanvas()) return;
    if (!canvas2 || !canvas2->GetCanvas()) return;
    double x1,x2,y1,y2;
    canvas1->GetCanvas()->GetRangeAxis(x1,y1,x2,y2);
    Update1(x1,x2,y1,y2);
}
void tordaqGui::yPanUp()
{
    if (histos1.size()<1) return;
    if (!canvas1 || !canvas1->GetCanvas()) return;
    static const double frac=0.2;
    double x1,x2,y1,y2;
    canvas1->GetCanvas()->GetRangeAxis(x1,y1,x2,y2);
    const double ylo=y1+(y2-y1)*frac;
    const double yhi=y2+(y2-y1)*frac;
    Update1(x1,x2,ylo,yhi);
}
void tordaqGui::yPanDown()
{
    if (histos1.size()<1) return;
    if (!canvas1 || !canvas1->GetCanvas()) return;
    static const double frac=0.2;
    double x1,x2,y1,y2;
    canvas1->GetCanvas()->GetRangeAxis(x1,y1,x2,y2);
    const double ylo=y1-(y2-y1)*frac;
    const double yhi=y2-(y2-y1)*frac;
    Update1(x1,x2,ylo,yhi);
}
void tordaqGui::xPanLeft1()
{
    if (histos1.size()<1) return;
    if (!canvas1 || !canvas1->GetCanvas()) return;
    static const double frac=0.5;
    double x1,x2,y1,y2;
    canvas1->GetCanvas()->GetRangeAxis(x1,y1,x2,y2);
    const double xlo=x1-(x2-x1)*frac;
    const double xhi=x2-(x2-x1)*frac;
    Update1(xlo,xhi);
}
void tordaqGui::xPanRight1()
{
    if (histos1.size()<1) return;
    if (!canvas1 || !canvas1->GetCanvas()) return;
    static const double frac=0.5;
    double x1,x2,y1,y2;
    canvas1->GetCanvas()->GetRangeAxis(x1,y1,x2,y2);
    const double xlo=x1+(x2-x1)*frac;
    const double xhi=x2+(x2-x1)*frac;
    Update1(xlo,xhi);
}
