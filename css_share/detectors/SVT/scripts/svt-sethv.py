#!/usr/bin/env python
import os,sys,epics

USAGE='''Usage:  svt-sethv.py [options]
\t\t-h(elp)
\t\t-v(erbose)
\t\t-d(ryrun)'''

KEYS=['v','vLOLO','vLOW','vHIGH','vHIHI','iLOLO','iLOW','iHIGH','iHIHI']
for kk in KEYS: USAGE+='\n\t\t'+kk+'=#'

DRYRUN=False
VERBOSE=False

VMON=':outputMeasSenseV'
IMON=':outputMeasCurrent'
VSET=':outputVoltage'
PREFIX='B_SVT_HV_'

VALS={}

def getArguments():
  global VALS,DRYRUN,VERBOSE
  for arg in sys.argv[1:]:
    if arg=='-h': sys.exit(USAGE)
    elif arg=='-d': DRYRUN=True
    elif arg=='-v': VERBOSE=True
    elif arg.find('=')>=0:
      (key,val)=arg.split('=',1)
      if key not in KEYS:
        print('Invalid argument: '+arg)
        sys.exit(USAGE)
      VALS[key]=float(val)
    else:
      print('Invalid argument: '+arg)
      sys.exit(USAGE)

def getPvList(hvs):
  pvs=[]
  for hv in hvs.split('\n'):
    if len(hv)<1: continue
    rr,ss,sl=hv.strip().split()
    for tb in ['T','B']:
      stub='R'+rr+'S'+ss+tb+'_Slot'+sl
      imon=PREFIX+stub+IMON
      vmon=PREFIX+stub+VMON
      vset=PREFIX+stub+VSET
      if VALS.has_key('v'):
        pvs.append({'name':vset,'val':VALS['v']})
      for field in ['LOLO','LOW','HIGH','HIHI']:
        if VALS.has_key('v'+field):
          pvs.append({'name':vmon+'.'+field,'val':VALS['v'+field]})
        if VALS.has_key('i'+field):
          pvs.append({'name':imon+'.'+field,'val':VALS['i'+field]})
  return pvs

def getPvValues(pvs,tag):
  for pv in pvs:
    # for outputs records, use the corresponding input:
    if pv['name'].endswith(':outputVoltage'):
      epv=epics.pv.PV(pv['name']+'R')
    else:
      epv=epics.pv.PV(pv['name'])
    pv[tag]=float(epv.get())

def setPvValues(pvs,tag):
  for pv in pvs:
    epv=epics.pv.PV(pv['name'])
    epv.put(pv[tag])

def checkPvValues(pvs,requested,readback):
  bad=[]
  for pv in pvs:
    if pv[requested] != pv[readback]:
      bad.append(pv)
  return bad

HV='''
1 1 7
1 2 7
1 3 7
1 4 7
1 5 7
1 6 7
1 7 7
1 8 7
1 9 8
1 10 8
2 1 9
2 2 9
2 3 9
2 4 9
2 5 9
2 6 9
2 7 9
2 8 9
2 9 10
2 10 10
2 11 10
2 12 10
2 13 10
2 14 10
3 1 8
3 2 8
3 3 8
3 4 8
3 5 8
3 6 8
3 7 8
3 8 8
3 9 9
3 10 9
3 11 9
3 12 9
3 13 9
3 14 9
3 15 9
3 16 9
3 17 10
3 18 10
'''

#################################

getArguments()

pvs=getPvList(HV)

getPvValues(pvs,'old')

if DRYRUN:
  for pv in pvs:
    print '%-50s current=%.2f request=%.2f'%(pv['name'],pv['old'],pv['val'])

else:
  setPvValues(pvs,'val')
  getPvValues(pvs,'new')
  bad=checkPvValues(pvs,'val','new')
  if VERBOSE:
    for pv in pvs:
      print '%-50s previous=%.2f request=%.2f current=%2f'%(pv['name'],pv['old'],pv['val'],pv['new'])
  for pv in bad:
    print 'ERROR: %-50s previous=%.2f request=%.2f current=%2f'%(pv['name'],pv['old'],pv['val'],pv['new'])





