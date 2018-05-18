#!/usr/bin/env python
import sys

# INPUTS:
# for full RICH:
mappingFile='./SspRich_cabling_ILA.txt'
# for cosmic RICH:
#mappingFile='./SspRich_cabling_cosmic_ILA.txt'
tileToLvFile='../../caenHvApp/doc/rich_TILE2LV.txt'

# OUTPUTS:
# jscalerApp/Db/jscaler_RICH_Maps.db
# iocjscalersRICH/richPmt-setDesc.cmd
# iocjscalersRICH/richTile-setDesc.cmd

ALIASES=False
DESCES=False
CAPUT=True
if len(sys.argv)>1:
  if sys.argv[1]=='-a':
    ALIASES=True
  elif sys.argv[1]=='-d':
    DESCES=True
    CAPUT=False
  elif sys.argv[1]=='-c':
    DESCES=True
    CAPUT=True

tiles=[]
pmts=[]

tileToLv=[]
for xx in open(tileToLvFile,'r').readlines():
  tileToLv.append(int(xx.strip()))


###################################################################
###################################################################
# load Matteo's mapping:
for line in open(mappingFile,'r').readlines():

  line=line.strip()

  if line.find('#')==0: continue

  # ignore the extra columns introduced in later versions of Matteo's file:
  if line.find('A')>=0:
    line=line[0:line.find('A')]

  # PMT### uses a different seperator than everything else,
  # if we don't find it then move on:
  if line.find('[')<0: continue
  if line.find(']')<0: continue

  # use the [] characters to designate PMTs:
  a,b=line.find('['),line.find(']')
  if a<0 or b<0: sys.exit('NOPE, MISSING []')

  # look at lefter columns to get slot/fiber/cable/maroc: 
  slot,fiber,cable,maroc=line[0:a].split()
  slot=int(slot)
  fiber=int(fiber)

  # look at righter columns to get tile:
  tile=int(line[b+1:])

  # fill 3-long array of pmts per tile:
  tilePmts=line[a+1:b].split(',')
  for ii in range(len(tilePmts)):
    tilePmts[ii]=int(tilePmts[ii].strip())

  # fill map per tile:
  tiles.append({'slot':slot,'fiber':fiber,'tile':tile,
    'pmt1':tilePmts[0],
    'pmt2':tilePmts[1],
    'pmt3':tilePmts[2]})

  # fill map per pmt:
  for ii in range(len(tilePmts)):
    if tilePmts[ii]==0: continue #empty asic
    pmts.append({'slot':slot,'fiber':fiber,'asic':ii,'tile':tile,'pmt':tilePmts[ii]})


###################################################################
###################################################################
# now that maps are loaded, printout the maps to EPICS syntax:

tileSuffixes=[
    ':temp:fpga',
    ':temp:reg0',':temp:reg1',
    ':volt:pcb5',':volt:pcb3_3',
    ':volt:int1',':volt:aux1_8',
    ':volt:mgt1',':volt:mgt1_2']
pmtSuffixes=[
    ":scalers",
    ":scalersAvg",
    ":scalersAvgK"]

if ALIASES:
  # generate TILE/PMT aliases:
  # NOTE, aliases have to be loaded in the IOC
  for xx in tiles:
    hwpv='B_HW_FEVME1_Sl%.2d_Fi%.2d'%(xx['slot'],xx['fiber'])
    depv='B_DET_RICH_SSP_TILE%.3d'%(xx['tile'])
    for suff in tileSuffixes:
      print 'alias("%s%s","%s%s")'%(hwpv,suff,depv,suff)
  for xx in pmts:
    hwpv='B_HW_FEVME1_Sl%.2d_Fi%.2d_PMT%d'%(xx['slot'],xx['fiber'],xx['asic'])
    depv='B_DET_RICH_SSP_PMT%.3d'%(xx['pmt'])
    for suff in pmtSuffixes:
      print 'alias("%s%s","%s%s")'%(hwpv,suff,depv,suff)

if DESCES:
  # generate DESC fields:
  # NOTE:  can be be loaded after IOC init, as .DESC fields are autosaved
  for xx in pmts:
    for yy in pmtSuffixes:
      pv='B_DET_RICH_SSP_PMT%.3d%s.DESC'%(xx['pmt'],yy)
      if CAPUT: fmt='caput %s \'RICH - Sl%.2d, Fi%.2d, Ti%.3d, Pmt%.3d, Lv%.2d\''
      else:     fmt='dbpf("%s","RICH - Sl%.2d, Fi%.2d, Ti%.3d, Pmt%.3d, Lv%.2d")'
      print fmt % (pv,xx['slot'],xx['fiber'],xx['tile'],xx['pmt'],tileToLv[int(xx['tile'])-1])
  for xx in tiles:
    for yy in tileSuffixes:
      pv='B_DET_RICH_SSP_TILE%.3d%s.DESC'%(xx['tile'],yy)
      if CAPUT: fmt='caput %s \'RICH - Sl%.2d, Fi%.2d, Ti%.3d, Lv%.2d\''
      else:     fmt='dbpf("%s","RICH - Sl%.2d, Fi%.2d, Ti%.3d, Lv%.2d")'
      print fmt % (pv,xx['slot'],xx['fiber'],xx['tile'],tileToLv[int(xx['tile'])-1])


