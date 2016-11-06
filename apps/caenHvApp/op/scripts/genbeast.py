#!/usr/bin/python
import os,glob

indir=os.getenv('EPICS')+'/apps/db'
subs=glob.glob(indir+'/HV*.substitutions')

pvs=[]
for sub in subs:
  if sub.find('SPARES')>=0: continue
  for line in open(sub,'r').readlines():
    cols=line.rstrip().split()
    if not len(cols)==17: continue
    sys=cols[5].replace('"','').replace(',','')
    det=cols[6].replace('"','').replace(',','')
    cha=cols[7].replace('"','').replace(',','')
    pv='B_DET_'+det+'_'+sys+'_'+cha
    if pv.find('SPARE')>=0: continue
    pvs.append(pv)

dets=['CTOF']
#,'FTOF','ECAL','PCAL','HTCC','LTCC','DC']

for det in dets:
  # need to open new file here
  print 'HallB, '+det+', HV'
  print 'pv, description, latching, annunciating, display title, display details, display macros'
  for pv in pvs:
    if pv.find(det)<=0: continue
    print pv+', hv channel, true, true, Open Controls, /CLAS12_Share/apps/caenhv_channel_novice.opi, P='+pv

