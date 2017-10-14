#!/usr/bin/env python
import epics,subprocess

inputFileName='ESR_HALLS Cryogenics Overview Pages Rev 0_1 DK.csv'

nSkipFirstLines=5

missingPV=[]
unarchivedPV=[]

def isArchived(pvName):
  pp=subprocess.check_output(['archive',pvName])
  if 'not archived' in pp: return False
  else:                    return True

def isOnline(pvName):
  pv = pv.epics.pv.PV(name)
  if pv.get()==None: return False
  else:              return True

section=None

for line in open(inputFileName,'r').readlines()[nSkipFirstLines:]:

  cols=line.strip().replace('"','').split('#');

  while len(cols)>0 and cols[len(cols)-1]=='':
    cols.pop()

  if len(cols)==1:
    section=cols[0]
    print '#\n#',section
    continue

  name,units,desc,low,high=None,None,None,None,None

  if len(cols)>0:   name=cols[0]
  if len(cols)>1:   units=cols[1]
  if len(cols)>2:   desc=cols[2]
  if len(cols)>3:   low=cols[3]
  if len(cols)>4:   high=cols[4]

  if name:
    if not isOnline(name):   missingPV.append(name)
    if not isArchived(name): unarchivedPV.append(name)

  print name,units,low,high

print 'Offline PVs:'
for xx in missingPV: print xx

print 'Unarchived PVs:'
for xx in unarchivedPV: print xx

