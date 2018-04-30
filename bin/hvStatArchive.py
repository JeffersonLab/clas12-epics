#!/usr/bin/env python
import sys,datetime,subprocess

def getMyaTable(week,pv):
  cmd=['myget','-c',pv,'-b','-%dw'%(week),'-e','-%dw'%(week-1)]
  ret=[]
  try:
    ret=subprocess.check_output(cmd).split('\n')
  except:
    # myget returns error if no data (i.e. no PV updates in given time span)
    # but it's not really an error, so we have to catch and ignore:(
    pass
  return ret

def countBits(table):
  bitCounts=[0]*16
  for row in table:
    cols=row.split()
    if len(cols)!=3: continue
    val=int(cols[2])
    for ii in range(16):
      if val & (1<<ii): bitCounts[ii]+=1
  return bitCounts

def getPVs():
  pcal,ecal,ftof,ctof,htcc,ltcc=[],[],[],[],[],[]
  fmt='B_DET_PCAL_HV_SEC%d_%s_E%.2d:stat'
  for sector in range(1,7):
    for view in ['U','V','W']:
      for chan in range(1,{'U':68,'V':62,'W':62}[view]+1):
        pcal.append({'pv':fmt%(sector,view,chan)})
  fmt='B_DET_ECAL_HV_SEC%d_%s%s_E%.2d:stat'
  for sector in range(1,7):
    for layer in ['I','O']:
      for view in ['U','V','W']:
        for chan in range(1,37):
          ecal.append({'pv':fmt%(sector,view,layer,chan)})
  fmt='B_DET_FTOF_HV_SEC%d_PANEL%s_%s_E%.2d:stat'
  for sector in range(1,7):
    for panel in ['1A','1B','2']:
      for side in ['L','R']:
        for chan in range(1,{'1A':23,'1B':62,'2':5}[panel]+1):
          ftof.append({'pv':fmt%(sector,panel,side,chan)})
  fmt='B_DET_CTOF_HV_%s%.2d:stat'
  for side in ['U','D']:
    for chan in range(1,49):
      ctof.append({'pv':fmt%(side,chan)})
  fmt='B_DET_HTCC_HV_SEC%d_%s%d:stat'
  for sector in range(1,7):
    for side in ['L','R']:
      for chan in range(1,5):
        htcc.append({'pv':fmt%(sector,side,chan)})
  fmt='B_DET_LTCC_HV_SEC%d_%s_E%.2d:stat'
  for sector in range(1,7):
    for side in ['L','R']:
      for chan in range(1,19):
        ltcc.append({'pv':fmt%(sector,side,chan)})
  return {'PCAL':pcal,'ECAL':ecal,'FTOF':ftof,\
          'CTOF':ctof,'HTCC':htcc,'LTCC':ltcc}


if __name__ == '__main__':

  usage='hvStatArchive.py [-a] [weekOffset]'
  threshold=10 # counts per week of a bad bit
  weekOffset=1
  showAll=False
  badBits=[1,2,3,4,5,6,7,8,9,10,11]
  bitDefs='''
  0 ON
  1 RUP
  2 RDN
  3 OVC
  4 OVV
  5 UNV
  6 EXTRIP
  7 MAXV
  8 EXDIS
  9 TRIP
 10 CALIB
 11 UNPLUG
'''

  # interpret command line args:
  if len(sys.argv)>1:
    for arg in sys.argv[1:]:
      if arg == '-h': sys.exit(usage)
      if arg == '-a': showAll=True
    if len(sys.argv)>2 or showAll==False:
      try:    weekOffset = int(sys.argv[len(sys.argv)-1])
      except: sys.exit(usage+'\n+ERROR:  weekOffset must be a positive integer')

  DATA=getPVs()

  # retrieve and analyze archive info:
  for det,data in DATA.iteritems():
    print '\nQuerying Archive for ',det,' ',
    for ii in range(len(data)):
      data[ii]['bits'] = countBits(getMyaTable(weekOffset,data[ii]['pv']))
      if ii%20==0:
        sys.stdout.write('.')
        sys.stdout.flush()

  # print results:
  print '\n'
  for det,data in DATA.iteritems():
    for datum in data:
      if showAll==True: print datum['pv'],str(datum['bits'])
      else:
        for bb in badBits:
          if datum['bits'][bb]>threshold:
            print datum['pv'],str(datum['bits'])
            break
  print bitDefs+'\n'

