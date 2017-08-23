#!/usr/bin/env python
import re,sys

matteoFile='sspRich_mapFIBER2PMT_sortbyPMT.txt'

oldFile='../Db/jscaler_RICH_ChannelMap.db'

suffixes=['scalers','scalersAvg','scalersAvgK']

pmtsNew=[]
slotFiber=[]
for line in open(matteoFile,'r').readlines():
  line=line.strip()
  slot,fiber,asic,pmt=line.split()
  pv='B_HW_FEVME1_Sl%.2d_Fi%.2d_PMT%d'%(int(slot),int(fiber),int(asic))
  alias='B_DET_RICH_SSP_PMT%.3d'%(int(pmt))
  slot='%.2d'%(int(slot))
  fiber='%.2d'%(int(fiber))
  pmt='%.3d'%(int(pmt))
  pmtsNew.append({'slot':slot,'fiber':fiber,'asic':asic,'pmt':pmt,'pv':pv,'alias':alias})

  if not {'slot':slot,'fiber':fiber} in slotFiber:
    slotFiber.append({'slot':slot,'fiber':fiber})

#  for suffix in suffixes:
#    print 'alias("%s:%s","%s:%s")'%(pv,suffix,alias,suffix)

for line in open('../../iocBoot/iocjscalersRICH/richPmt-setDesc.cmd','r').readlines():
  if line.find('dbpf')!=0: continue
  cols=line.strip().split('"')
  pv,oldDesc=cols[1],cols[3]
  mm=re.match('B_DET_RICH_SSP_PMT(\d\d\d)',pv)
  pmt=mm.group(1)
  found=False
  for xx in pmtsNew:
    if pmt==xx['pmt']:
      found=True
      pmt=xx
      break
  if not found:
    sys.exit('asdf:  '+str(pmt))

  newDesc='RICH Scalers - Sl%s, Fi%s.%s, Pmt#%s'%(xx['slot'],xx['fiber'],xx['asic'],xx['pmt'])

  print 'dbpf("'+pv+'","'+newDesc+'")'


sys.exit()

for sf in slotFiber:
  pv='B_HW_FEVME1_Sl%s_Fi%s'%(sf['slot'],sf['fiber'])
  print pv+':temp:fpga 0.2'
  print pv+':volt:pcb5 0.05'

pmtsOld=[]
for line in open(oldFile,'r').readlines():
  line=line.strip()
  if line.find('alias')!=0: continue

  pv,alias=line.split(',')
  pv=pv.split('"')[1]
  alias=alias.split('"')[1]
  mm=re.match('B_DET_RICH_SSP_PMT(\d\d\d)',alias)
  pmt=mm.group(1)
  mm=re.match('B_HW_FEVME1_Sl(\d\d)_Fi(\d\d)_PMT(\d)',pv)
  slot,fiber,asic=mm.group(1),mm.group(2),mm.group(3)
  pmtsOld.append({'slot':slot,'fiber':fiber,'asic':asic,'pmt':pmt})

for pmtOld in pmtsOld:
  pmtNew=None
  for new in pmtsNew:
    if new['slot']!=pmtOld['slot']: continue
    if new['fiber']!=pmtOld['fiber']: continue
    if new['asic']!=pmtOld['asic']: continue
    pmtNew=new
    break

#  if not pmtNew:
#    print pmtOld

