#!/usr/bin/env python
import time,sys,os,argparse,atexit
from epics import pv
from ROOT import TH2D,TH2I,gStyle,gPad,TPaveText,TCanvas
from ROOT import TArrow,TBox,TLine,TDatime,TText,TGFrame
from ROOT import gClient,TGMainFrame,TGVerticalFrame
from ROOT import TGHorizontalFrame,TGLayoutHints
from ROOT import TRootEmbeddedCanvas,TApplication
import ROOT

SECTORSPERREGION=[10,14,18]
STRIPSPERSECTOR=512

class SvtChannel:

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

class SvtChannelCollection:

  def __init__(self,csvFileName=None):

    self.chans=[]
    self.keys=[]

    for region in range(len(SECTORSPERREGION)):
      for sector in range(SECTORSPERREGION[region]):

        vals={}
        vals['REGION']=region+1
        vals['SECTOR']=sector+1
        vals['PVVAL']=0
        vals['PVNAME']='B_SVT_DAQ_R%dS%d:STRIPRATE'%(region+1,sector+1)
        vals['PV']=pv.PV(vals['PVNAME'])
        vals['PVTIME']=pv.PV(vals['PVNAME']+'-Time')

        self.chans.append(SvtChannel(vals))

    nEcalChannels=len(self.chans)

  def findChannelXY(self,x,y):
    for chan in self.chans:
      if chan.vals['X']==x and chan.vals['Y']==y:
        return chan
    return None


###########################################

SVT=SvtChannelCollection()

def calcRates(chans):
    r1,r2,r3=0,0,0
    for ccc in chans:
       rates = ccc.vals['PVVAL']
       for rate in rates:
         if ccc.vals['REGION']==1: r1+=rate
         elif ccc.vals['REGION']==2: r2+=rate
         elif ccc.vals['REGION']==3: r3+=rate
    return [r1,r2,r3]

def setupHists(hhh):
    for hh in hhh:
        hh.SetMinimum(1)
        #hh.SetMaximum(1e6)
        hh.SetStats(0)
        hh.GetYaxis().SetTickLength(0.01)
        hh.GetXaxis().SetTickLength(0.01)
        hh.GetXaxis().SetTitleOffset(1.4)
        for iy in range(hh.GetNbinsY()):
          if iy<10: hh.GetYaxis().SetBinLabel(iy+1,str(iy+1))
          elif iy<24: hh.GetYaxis().SetBinLabel(iy+1,str(iy+1-10))
          else: hh.GetYaxis().SetBinLabel(iy+1,str(iy+1-24))
        for ix in range(hh.GetNbinsX()):
          lab=ix
          if ix>=STRIPSPERSECTOR/2: lab=ix-STRIPSPERSECTOR/2
          if (ix%32==0): hh.GetXaxis().SetBinLabel(ix+1,str(lab))
          else:          hh.GetXaxis().SetBinLabel(ix+1,'')

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

def loadPV(chan):
  ch=chan.vals
  ch['PVVAL']=ch['PV'].get()
  ch['PVTIMEVAL']=ch['PVTIME'].get()


mf=TGMainFrame(gClient.GetRoot(),800,565)
gvf=TGVerticalFrame(mf,800,565)
rec=TRootEmbeddedCanvas("ccc",gvf,800,565)
gvf.AddFrame(rec,TGLayoutHints(ROOT.kLHintsExpandX|ROOT.kLHintsTop))
mf.AddFrame(gvf,TGLayoutHints(ROOT.kLHintsExpandX))
cc=rec.GetCanvas()
mf.SetEditable(0)
mf.SetWindowName('SVT Scalers')
mf.MapSubwindows()
mf.Resize(801,566)# resize to get proper frame placement
mf.MapWindow()
mf.SetCleanup(ROOT.kDeepCleanup)

def __atexit__():
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
    gStyle.SetGridStyle(0)
    gStyle.SetGridColor(18)

    nbinsX=0
    for ix in range(len(SECTORSPERREGION)):
      nbinsX+=SECTORSPERREGION[ix]
    hh=TH2D('hh',';Strip;Sector',STRIPSPERSECTOR,0,STRIPSPERSECTOR,nbinsX,0,nbinsX);
    setupHists([hh])
    hh.Draw('COLZ')

    gPad.SetLogz()
    gPad.SetLeftMargin(0.09)
    gPad.SetRightMargin(0.11)

    tt2=TPaveText(240,43,500,45)
    ttime=TPaveText(100,-5.5,412,-3)
    setupPaveTexts([tt2,ttime])
    tt2.SetTextSize(0.03)

    lll=TLine()
    lll.SetLineColor(15)
    y1=SECTORSPERREGION[0]
    y2=SECTORSPERREGION[0]+SECTORSPERREGION[1]
    lll.DrawLine(0,y1,STRIPSPERSECTOR,y1)
    lll.DrawLine(0,y2,STRIPSPERSECTOR,y2)

    tt=TText()
    tt.SetTextColor(1)
    tt.SetTextAngle(90)
    tt.SetTextSize(0.04)
    tt.DrawText(532,22,'Hz')
    tt.SetTextSize(0.06)
    tt.SetTextAngle(0)
    tt.SetTextColor(1)
    tt.DrawTextNDC(0.1,0.93,'SVT Scalers')

    tt.SetTextSize(0.03)
    tt.DrawText(-42,4,'R1')
    tt.DrawText(-42,16,'R2')
    tt.DrawText(-42,32,'R3')

    cc.cd()
    for xx in [ttime,tt2]: xx.Draw()
    cc.cd()

    gPad.SetEditable(0)

    while True:

            iy=0
            for ch in SVT.chans:
              loadPV(ch)
              ch=ch.vals
              data=ch['PVVAL']
              time2=ch['PVTIMEVAL']

              if time2>10:
                print 'More than 10 seconds since message:  '+ch['PVNAME']
                for ii in range(512):
                  data[ii]=0

              if iy<SECTORSPERREGION[0]:
                region=1
                sector=iy
              elif iy<SECTORSPERREGION[0]+SECTORSPERREGION[1]:
                region=2
                sector=iy-SECTORSPERREGION[0]
              else:
                region=3
                sector=iy-SECTORSPERREGION[0]-SECTORSPERREGION[1]

              if data==None or len(data)!=STRIPSPERSECTOR:
                print 'Error Reading '+ch['PVNAME']
                continue
              for ix in range(STRIPSPERSECTOR):
                  hh.SetBinContent(ix,iy+1,data[ix])
              iy += 1

            for xx in [ttime,tt2]: xx.Clear()

            [r1,r2,r3]=calcRates(SVT.chans)
            tt2.AddText('Sums:  R1 / R2 / R3 = %.2E / %.2E / %.2E Hz'%(r1,r2,r3))

            ttime.AddText(makeTime())

            if not gPad: sys.exit()

            cc.Modified()
            cc.Update()

            time.sleep(5)

if __name__ == '__main__': main()

