#!/usr/bin/env python3

suffixes = [
  'temp:fpga',
  'temp:reg0',
  'temp:reg1',
  'volt:pcb5',
  'volt:pcb3_3',
  'volt:int1',
  'volt:aux1_8',
  'volt:mgt1',
  'volt:mgt1_2'
]

with open('fiber.map','r') as f:

  pmts,tiles=set(),set()

  for line in f.readlines():

    slot,fiber,asic,pmt,tile = [int(x) for x in line.strip().split()]

    for scaler in ['scalers','scalersAvg','scalersAvgK']:
      pv = 'B_HW_SVT3_Sl%.2d_Fi%.2d_PMT%d:%s'%(slot,fiber,asic,scaler)
      alias = 'B_DET_RICH2_SSP_PMT%.3d:%s'%(pmt,scaler)
      print('alias("%s","%s")'%(pv,alias))

      #pv = 'B_DET_RICH2_SSP_PMT%.3d:%s.DESC'%(pmt,scaler)
      #desc = 'RICH2 - Sl%.2d, Fi%.2d, Ti%.3d, Pmt%.3d'%(slot,fiber,tile,pmt)
      #print('caput %s "%s"'%(pv,desc))

    continue

    if tile not in tiles:
      for suffix in suffixes:
        tiles.add(tile)
        pv = 'B_HW_SVT3_Sl%.2d_Fi%.2d:%s'%(slot,fiber,suffix)
        alias = 'B_DET_RICH2_SSP_TILE%.3d:%s'%(tile,suffix)
        print('alias("%s","%s")'%(pv,alias))

    for scaler in ['scalers','scalersAvg','scalersAvgK']:
      pv = 'B_HW_SVT3_Sl%.2d_Fi%.2d_PMT%d:%s'%(slot,fiber,asic,scaler)
      alias = 'B_DET_RICH2_SSP_PMT%.3d:%s'%(pmt,scaler)
      print('alias("%s","%s")'%(pv,alias))

