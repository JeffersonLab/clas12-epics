#!/usr/bin/env python
import time,sys,os,argparse,atexit
from epics import pv
from ROOT import TH2D,TH2I,gStyle,gPad,TPaveText,TCanvas
from ROOT import TArrow,TBox,TLine,TDatime,TText,TGFrame
from ROOT import gClient,TGMainFrame,TGVerticalFrame
from ROOT import TGHorizontalFrame,TGLayoutHints
from ROOT import TRootEmbeddedCanvas,TApplication
import ROOT

class RichPmt:

  def __init__(self,keyval):
    self.vals={}
    if type(keyval) is dict:
      for kv in keyval.items():
        self.vals[kv[0]]=kv[1]
    else:
      sys.exit('Invalid Constructor.')

  def dump(self):
    for key in self.vals.keys():
      print '%15s'%(key+'='+str(self.vals[key])),
    print

class RichPmtCollection:

  def __init__(self,csvFileName=None):

    self.chans=[]
    self.keys=[]

    npmtPerRow=5
    ipmt=0
    for iy in range(23):
      npmtPerRow+=1
      for ix in range(npmtPerRow):

        vals={}

        vals['ipmt']=ipmt

        vals['ix']=ix
        vals['iy']=iy

        vals['X']=14-float(npmtPerRow)/2+float(ix)
        vals['Y']=float(iy)

        ipmt+=1

        print ipmt,ix,iy,vals['X'],vals['Y']

        vals['PVVAL']=0
        vals['PVNAME']='B_DET_RICH_SSP_PMT%.3d:scalers'%ipmt
        vals['PV']=pv.PV(vals['PVNAME'])

        self.chans.append(RichPmt(vals))

    nEcalChannels=len(self.chans)
    nNonEcalChannels = len(self.chans)-nEcalChannels

  def findChannelXY(self,x,y):
    for chan in self.chans:
      if chan.vals['X']==x and chan.vals['Y']==y:
        return chan
    return None


###########################################

ECAL=RichPmtCollection()

def calcRates(chans):
    total,maximum,top,bottom,left,right=0,0,0,0,0,0
    for ccc in chans:
       rate = ccc.vals['PVVAL']
       total += rate
       if rate>maximum: maximum=rate
       # X is upstream, swap it for downstream:
       if ccc.vals['X']<0: right  += rate
       else:               left   += rate
       if ccc.vals['Y']<0: bottom += rate
       else:               top    += rate
    return [total,maximum,top,bottom,left,right]

def setupHists(hhh):
    for hh in hhh:
        hh.SetStats(0)
        hh.GetXaxis().CenterLabels()
        hh.GetXaxis().SetNdivisions(28,0)
        hh.GetYaxis().CenterLabels()
        hh.GetYaxis().SetNdivisions(23,0)
        hh.GetYaxis().SetTickLength(0)
        hh.GetXaxis().SetTickLength(0)
        hh.GetYaxis().SetTitleOffset(1.0)
        hh.GetXaxis().SetLabelSize(0.02)
        hh.GetYaxis().SetLabelSize(0.02)
#        for ix in range(hh.GetNbinsX()):
#          if ix%8>0: hh.GetXaxis().SetBinLabel(ix,'')
#          else: hh.GetXaxis().SetBinLabel(ix,'%d'%ix)
#        for iy in range(hh.GetNbinsY()):
#          if iy%8>0: hh.GetYaxis().SetBinLabel(iy,'')
#          else: pass#hh.GetYaxis().SetBinLabel(iy,'%d'%iy)

def makeTime():
    datime=TDatime()
    return '%d/%d/%d %.2d:%.2d:%.2d'%(datime.GetDay(),
             datime.GetMonth(),
             datime.GetYear(),
             datime.GetHour(),
             datime.GetMinute(),
             datime.GetSecond())

def setupPaveTexts(pts):
    for pt in pts:
        pt.SetTextColor(1)
        pt.SetTextAngle(0)
        pt.SetFillColor(0)
        pt.SetBorderSize(0)
        pt.SetLineWidth(0)

def pix2xy(pad):
  px=gPad.GetEventX()
  py=gPad.GetEventY()
  # determined empirically (by clicking on canvas):
  tl=[71,79]
  tr=[709,44]
  br=[709,716]
  bl=[71,716]
  x=int(float(px-tl[0])/(tr[0]-tl[0])*22)-11
  y=int(float(py-tl[1])/(bl[1]-tl[1])*22)-11
  if x>=0: x+=1
  if y>=0: y+=1
  # swap y because pixel-coordinate inverted:
  y=-y
  # swap x to make it downstream view:
  x=-x
  return [x,y]

def printChannel(ee):
    return 'X/Y = %d/%d       FADC = %s/%s/%s       MB = %s      HV = %s      LED = %s'%(
            ee.vals['X'],
            ee.vals['Y'],
            ee.vals['Crate'],
            ee.vals['Slot'],
            ee.vals['Channel'],
            ee.vals['MoboSignal'],
            ee.vals['HV Group'],
            ee.vals['LED'])

def loadPV(chan):
  ch=chan.vals
  ch['PVVAL']=ch['PV'].get()
  #if not type(ch['PVVAL']) is float:
  #  ch['PVVAL']=ch['PVVAL'].tolist()
  #  if type(ch['PVVAL']) is list:
  #    ch['PVVAL']=ch['PVVAL'][0]
  #ch['PVVAL']/=1000


mf=TGMainFrame(gClient.GetRoot(),800,665)
gvf=TGVerticalFrame(mf,800,665)
rec=TRootEmbeddedCanvas("ccc",gvf,800,640)
rec2=TRootEmbeddedCanvas("ccc2",gvf,800,25)
gvf.AddFrame(rec,TGLayoutHints(ROOT.kLHintsExpandX|ROOT.kLHintsTop))
gvf.AddFrame(rec2,TGLayoutHints(ROOT.kLHintsExpandX|ROOT.kLHintsBottom))
mf.AddFrame(gvf,TGLayoutHints(ROOT.kLHintsExpandX))
cc=rec.GetCanvas()
cc2=rec2.GetCanvas()
mf.SetEditable(0)
mf.SetWindowName('RICH SSP Scalers')
mf.MapSubwindows()
mf.Resize(801,666)# resize to get proper frame placement
mf.MapWindow()
mf.SetCleanup(ROOT.kDeepCleanup)

def __atexit__():
    del cc2
    del cc
    del rec
    del rec2
    del gvf
    del mf

def main():

    cc.cd()
    cc.SetBorderMode(0)
    cc.SetFixedAspectRatio(1)
    cc.FeedbackMode(1)

    gStyle.SetOptStat(0)
    gStyle.SetGridStyle(1)
    gStyle.SetGridColor(18)

    hh=TH2D('hh',';X;Y',8*28,0,28,8*23,0,23);
    hi=TH2I('hi',';X;Y',8*28,0,28,8*23,0,23);
    setupHists([hh,hi])
    xax,yax=hh.GetXaxis(),hh.GetYaxis()
    hh.Draw('COLZ')
    hh.SetMinimum(1)
    hh.SetMaximum(1.5e3)
    #hi.Draw('TEXTSAME')

    gPad.SetLogz()
    gPad.SetGrid(1,1)
    gPad.SetLeftMargin(0.09)
    gPad.SetRightMargin(0.11)

    #tt2=TPaveText(0.7,0.96,0.9,0.99,'NDC')
    ttM=TPaveText(-3+0.05, 7-4.45, 4.0, 8-4.51)
    tt2=TPaveText(-3+0.05, 7-5.45, 4.0, 8-5.51)

    ttX=TPaveText(-2, 7-8.00, 3, 8-8.00)
    ttY=TPaveText(-2, 7-9.00, 3, 8-9.00)

    ttime=TPaveText(8,-2,20,-1)
    tchan=TPaveText(0,0,0.9,1)
    setupPaveTexts([tt2,ttM,ttime,tchan,ttX,ttY])
    ttM.SetTextColor(2)
    ttM.SetFillStyle(0)
    tt2.SetFillStyle(0)

    tt=TText()
    tt.SetTextColor(1)
    tt.SetTextAngle(90)
    tt.SetTextSize(0.04)
    tt.DrawText(29.5,10,'kHz')
    tt.SetTextAngle(0)
    tt.SetTextColor(1)
    tt.DrawTextNDC(0.3,0.92,'RICH SSP Scalers')

#    bb=TBox()
#    bb.SetFillStyle(1001)
#    bb.SetFillColor(0)
#    bb.SetLineWidth(1)
#    bb.SetLineColor(1)
#    bb.DrawBox(-3.47,-1.47,4.47,2.46)
#    bb.DrawBox(-1.47,-3.47,2.49,4.47)
#    bb.DrawBox(-2.47,-2.47,3.49,3.47)

    cc.cd()
    for xx in [ttime]: xx.Draw()#ttM,tt2,ttime,ttX,ttY]: xx.Draw()
    cc2.cd()
    tchan.Draw('NDC')
    cc.cd()

    gPad.SetEditable(0)

    while True:

            for ch in ECAL.chans:
              loadPV(ch)
              ch=ch.vals
              xx,yy=ch['X'],ch['Y']
              data=ch['PVVAL']

              for ix in range(8):
                for iy in range(8):
                  ii=ix*8+iy
                  #print ch['PVNAME'],data[ii]
                  xoff=float(ix)/8
                  yoff=float(iy)/8

                  hh.SetBinContent(xax.FindBin(xx+xoff),yax.FindBin(yy+yoff),data[ii])
#                  hi.SetBinContent(xax.FindBin(xx+xoff),yax.FindBin(yy+yoff),data[ii])
#
            for xx in [ttime]: ttime.Clear()# xx.,tt2,ttM,ttX,ttY]: xx.Clear()
#            [total,maximum,top,bottom,left,right]=calcRates(ECAL.chans)

#            tt2.AddText('Total:  %.1f MHz'%(total/1000))
#            ttM.AddText('Max:  %.0f kHz'%(maximum))

#            if total>1e2:
#              xasy = (right-left)/total
#              yasy = (top-bottom)/total
#              ttX.AddText('X-Asy:  %+.1f%%'%(100*xasy))
#              ttY.AddText('Y-Asy:  %+.1f%%'%(100*yasy))
#            else:
#              ttX.AddText('X-Asy:  N/A')
#              ttY.AddText('Y-Asy:  N/A')

            ttime.AddText(makeTime())

            if not gPad: sys.exit()

#            if gPad.GetEvent()==11:
#                xy=pix2xy(gPad)
#                ee=ECAL.findChannelXY(xy[0],xy[1])
#                if ee:
#                    tchan.Clear()
#                    tchan.AddText(printChannel(ee))
#                    cc2.Modified()
#                    cc2.Update()
#            elif gPad.GetEvent()==12:
#                tchan.Clear()
#                cc2.Modified()
#                cc2.Update()


            cc.Modified()
            cc.Update()

            time.sleep(1)

if __name__ == '__main__': main()

