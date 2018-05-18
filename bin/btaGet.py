#!/usr/bin/env python
import sys,epics,datetime,subprocess

def getMyaTimestamp(tt):
  return '%4d-%.2d-%.2d %.2d:%.2d:%.2d' % \
    (tt.year,tt.month,tt.day,tt.hour,tt.minute,tt.second)

def getMyaAverage(start,end,pv):
  cmd=['myStats','-b',start,'-e',end,'-l',pv]
  return subprocess.check_output(cmd).split()[7]

def getMyaTable(start,nsamples,pvs):
  cmd=['mySampler','-b',start,'-n',str(nsamples),'-s','1s']
  cmd.extend(pvs)
  return subprocess.check_output(cmd).split('\n')

def getMyaBtaHour(start):
  print 'querying archive ...'
  table=getMyaTable(start,3600,['HLB:bta_daq_used','HLB:bta_bm_present'])
  abu,banu,bna=0,0,0
  for ii in range(1,len(table)):
    cols = table[ii].split()
    if len(cols)!=4: continue
    daqInUse,beamPresent = float(cols[2]),float(cols[3])
    abu += daqInUse*beamPresent
    if daqInUse==0 and beamPresent==1: banu += 1
    if beamPresent==0: bna += 1
  return [abu/60,banu/60,bna/60]


hourOffset = 1

# interpret command line arguments:
usage='btaGet.py [hour offset (default=1)]'
if len(sys.argv)>1:
  if sys.argv[len(sys.argv)-1]=='-h':  sys.exit(usage)
  try:
    hourOffset = int(sys.argv[len(sys.argv)-1])
    if hourOffset<=0: raise(ValueError)
  except:
    sys.exit(usage+'\n'+'Error:  hour offset must be a positive integer')

# figure out time range:
now        = datetime.datetime.now()
lastHour   = now.replace(minute=0,second=0,microsecond=0)
firstHour  = lastHour - datetime.timedelta(hours=hourOffset)
secondHour = firstHour + datetime.timedelta(hours=1)

# generate timestamp strings for mya:
start = getMyaTimestamp(firstHour)
end   = getMyaTimestamp(secondHour)

# get 1-hr BTA based on waveforms of previous 1-week of BTAs:
abuB  = epics.pv.PV('HLB:bta_sec_w_bm_w_daq_h').get().tolist().pop(hourOffset-1)/60
banuB = epics.pv.PV('HLB:bta_sec_w_bm_wo_daq_h').get().tolist().pop(hourOffset-1)/60
bnaB  = epics.pv.PV('HLB:bta_sec_wo_bm_h').get().tolist().pop(hourOffset-1)/60

# get 1-hr BTA based on Mya archive:
abuM,banuM,bnaM = getMyaBtaHour(start)

# if ABU/BANU/BNA don't add up to an hour, put the discrepancy on BNA:
if abuM+banuM+bnaM!=60:  bnaM=60-abuM-banuM

print
print '* FOR THE HOUR  '+str(firstHour)+' - '+str(secondHour)
print '*'
print '*'
print '* This is what should be populating the table automatically when clicking'
print '*  \'Load from EPICS\', although not currently guaranteed to be correct:'
print '*'
print '*    ABU: %.1f   BANU: %.1f   BNA: %.1f'%(abuB,banuB,bnaB)
print '*'
print '*'
print '* And this is the corresponding values from the Mya archive.'
print '*    IF THESE ARE SIGNIFICANTLY DIFFERENT THAN THE ABOVE NUMBERS,'
print '*    then you should manually adjust the table with these numbers'
print '*    * If we request NO BEAM, you must manually adjust BANU/ABU'
print '*'
print '*    ABU: %.1f   BANU: %.1f   BNA: %.1f'%(abuM,banuM,bnaM)
print



