#!/usr/bin/env python
import re

mappingFile='./SspRich_cabling.txt'

#headers=[]
tiles=[]
pmts=[]

# load Matteo's mapping:
for line in open(mappingFile,'r').readlines():

  line=line.strip()

  #if len(headers)==0:
  #  headers=line.split()
  #  continue

  if line.find('[')<0: continue
  if line.find(']')<0: continue

  a,b=line.find('['),line.find(']')

  slot,fiber,cable,maroc=line[0:a].split()
  slot=int(slot)
  fiber=int(fiber)

  tile=int(line[b+1:])

  tilePmts=line[a+1:b].split(',')
  for ii in range(len(tilePmts)):
    tilePmts[ii]=int(tilePmts[ii].strip())

  tiles.append({'slot':slot,'fiber':fiber,'tile':tile,
    'pmt1':tilePmts[0],
    'pmt2':tilePmts[1],
    'pmt3':tilePmts[2]})

  for ii in range(len(tilePmts)):
    if tilePmts[ii]==0: continue #empty asic
    pmts.append({'slot':slot,'fiber':fiber,'asic':ii,'tile':tile,'pmt':tilePmts[ii]})

#  for pmt in tilePmts:
#    if pmt==0: continue
#    pmts.append({'slot':slot,'fiber':fiber,'tile':tile,'pmt':pmt})

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

if False:
  # generate TILE aliases:
  for xx in tiles:
    hwpv='B_HW_FEVME1_Sl%.2d_Fi%.2d'%(xx['slot'],xx['fiber'])
    depv='B_DET_RICH_SSP_TILE%.3d'%(xx['tile'])
    for suff in tileSuffixes:
      print 'alias("%s%s","%s%s")'%(hwpv,suff,depv,suff)

if True:
  # generate DESC fields:
  for xx in pmts:
    for yy in pmtSuffixes:
      pv='B_DET_RICH_SSP_PMT%.3d%s.DESC'%(xx['pmt'],yy)
      print 'dbpf("%s","RICH Scalers - Sl%.2d, Fi%.2d.%d, Tile#%.3d, Pmt#%.3d")' % \
        (pv,xx['slot'],xx['fiber'],xx['asic'],xx['tile'],xx['pmt'])
  for xx in tiles:
    for yy in tileSuffixes:
      pv='B_DET_RICH_SSP_TILE%.3d%s.DESC'%(xx['tile'],yy)
      print 'dbpf("%s","RICH FPGA - Sl%.2d, Fi%.2d, Tile#%.3d")' % \
        (pv,xx['slot'],xx['fiber'],xx['tile'])


