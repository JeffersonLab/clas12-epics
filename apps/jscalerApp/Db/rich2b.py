#!/usr/bin/env python3

pmts = {}

with open('jscaler_RICH2_Maps.db','r') as f:

  for line in f.readlines():

    if line.find('B_DET_RICH2_SSP_PMT') < 0:
      continue

    cols = line.split('"')
    x,y = cols[1],cols[3]

    slot,fiber = x.split('_')[3:4+1]
    slot = int(slot[2:])
    fiber = int(fiber.split(':').pop(0)[2:])
    pmt = int(y.split('_').pop().split(':').pop(0)[3:])

    if pmt not in pmts:
      pmts[pmt] = {}

    pmts[pmt]['slot'] = slot
    pmts[pmt]['fiber'] = fiber

with open('jscaler_RICH2_Maps.db','r') as f:

  for line in f.readlines():

    if line.find('B_DET_RICH2_SSP_TILE') < 0:
      continue

    cols = line.split('"')
    x,y = cols[1],cols[3]

    slot,fiber = x.split('_')[3:4+1]
    slot = int(slot[2:])
    fiber = int(fiber.split(':').pop(0)[2:])
    tile = int(y.split('_').pop(4).split(':').pop(0)[4:])

    for pmt,x in pmts.items():
      if x['slot'] == slot:
        if x['fiber'] == fiber:
          x['tile'] = tile

with open('lv-tile.txt','r') as f:

  for line in f.readlines():
    cols = line.strip().split()
    lv = int(cols.pop(0))
    tiles = [int(x) for x in cols]
    for pmt,x in pmts.items():
      if x['tile'] in tiles:
        x['lv'] = lv

for pmt,x in pmts.items():
  pv = 'B_DET_RICH2_SSP_PMT%.3d:scalers.DESC' % pmt
  val = 'RICH2 - Sl%d, Fi%d, Ti%d, Pmt%d, Lv%d' % (x['slot'],x['fiber'],x['tile'],pmt,x['lv'])
  print('caput %s \'%s\' '%(pv,val))

