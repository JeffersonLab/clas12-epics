#!/usr/bin/env python

prefix='B_DET_CND_FADC_'

for seg in range(1,25):
  for imo in ['Inner','Middle','Outer']:
    for ee in [1,2]:
      pv=(prefix+imo+'_Seg%.2d_E%d')%(seg,ee)
      print pv


