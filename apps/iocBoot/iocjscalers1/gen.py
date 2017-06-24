#!/usr/bin/env python
import sys

detect=sys.argv[1]
sector=sys.argv[2]
scaler=sys.argv[3]
suffix=sys.argv[4]

pvs=[]

if detect=='ECAL':
  for uvw in ['U','V','W']:
    for io in ['I','O']:
      for ch in range(36):
        pvs.append('%s_SEC%s_%s%s_E%.2d'%(scaler,sector,uvw,io,ch+1))

elif detect=='PCAL':
  for uvw in ['U','V','W']:
    for ch in range({'U':68,'V':62,'W':62}[uvw]):
        pvs.append('%s_SEC%s_%s_E%.2d'%(scaler,sector,uvw,ch+1))

elif detect=='FTOF':
  for panel in ['1A','1B','2']:
    for ch in range({'1A':23,'1B':62,'2':5}[panel]):
      for lr in ['L','R']:
        pvs.append('%s_SEC%s_PANEL%s_%s_E%.2d'%(scaler,sector,panel,lr,ch+1))

elif detect=='LTCC':
  for ch in range(18):
    for side in ['L','R']:
      pvs.append('%s_SEC%s_%s_E%.2d'%(scaler,sector,side,ch+1))

elif detect=='CTOF':
  for side in ['U','D']:
    for ch in range(48):
      pvs.append('%s_%s_%s%.2d'%(scaler,side,ch+1))

elif detect=='HTCC':
  for ch in range(4):
    for side in ['L','R']:
      pvs.append('%s_SEC%s_%s%d'%(scaler,sector,side,ch+1))


for pv in pvs:
  print 'B_DET_%s_%s:%s'%(detect,pv,suffix)

