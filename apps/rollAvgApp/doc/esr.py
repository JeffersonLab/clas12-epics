#!/usr/bin/env python
import epics,subprocess,sys

# False: print substitutions file
# True:  print online/archiving status
PRINTSTATS=False
if len(sys.argv)>1:
  if sys.argv[1]=='-p': PRINTSTATS=True
  else:                 sys.exit('Usage:  esr.py [-p]')

# Kashy's spreadsheet, exported to ascii:
INPUTFILE='ESR_HALLS Cryogenics Overview Pages Rev 1_2.csv'
FIELDSEPERATOR='#'

# Ignore lines containing:
IGNORE=['Sub System','High Power Target Power']

SKIPFIRSTLINES=5

VERBOSE=False

def parseSpreadsheet():

  recs,section=[],None

  for line in open(INPUTFILE,'r').readlines()[SKIPFIRSTLINES:]:

    line=line.strip().replace('"','')

    ignore=False
    for ign in IGNORE:
      if line.find(ign)>=0:
        ignore=True
        break
    if ignore: continue

    cols=line.split(FIELDSEPERATOR);
    for ii in range(len(cols)):
      cols[ii]=cols[ii].strip()

    while len(cols)>0 and cols[len(cols)-1]=='': cols.pop()

    if len(cols)<1: continue

    if len(cols)==1:
      section=cols[0]
      if VERBOSE: print '#\n#',section
      continue

    name=cols[0].replace('.VAL','')

    rec={'name':name,'section':section,\
        'units':None,'desc':None,'low':None,'high':None,\
        'online':False,'archived':False,'malformed':False}

    if rec['name'].find('.')>=0: rec['malformed']=True

    if len(cols)>1: rec['units']=cols[1]
    if len(cols)>2: rec['desc']=cols[2]
    if len(cols)>3: rec['low']=cols[3]
    if len(cols)>4: rec['high']=cols[4]

    if VERBOSE:
      print '%s %s %s %s <>%s<>'%(name,units,low,high,desc)

    recs.append(rec)

  return recs

def clean(ss):
  if ss==None: ss=''
  elif ss=='None': ss=''
  elif ss=='N/A': ss=''
  elif ss=='microAmps': ss='uA'
  elif ss=='Atm': ss='atm'
  elif ss=='SLM': ss='slm'
  elif ss=='Watts': ss='W'
  elif ss=='Amps': ss='A'
  else: ss=ss.replace('?','')
  return ss

def isArchived(pvName):
  pp=subprocess.check_output(['archive',pvName])
  if 'not archived' in pp: return False
  else:                    return True

def isOnline(pvName):
  pv = epics.pv.PV(pvName)
  if pv.get()==None: return False
  else:              return True

def getStats(records):
  for rec in records:
    if isOnline(rec['name']):   rec['online']=True
    if isArchived(rec['name']): rec['archived']=True

# generate the substitutions file:
def printSubs (records):
  print 'file "db/rollingAverages.db" {'
  print 'pattern {P EGU LOW HIGH DESC}'
  for rec in records:
    desc=rec['desc'][0:39]
    if rec['malformed']: continue
    print '{"%s" "%s" "%s" "%s" "%s"}' %\
        (rec['name'],
         clean(rec['units']),
         clean(rec['low']),
         clean(rec['high']),
         desc)
  print '}'

# generate the format used by opi/js (with sections):
def printPvList(records):
  section=None
  for rec in records:
    if rec['section']!=section:
      section=rec['section']
      print '#'+section
    # ignore records with errors:
    if not rec['online']: continue
    if not rec['archived']: continue
    if rec['malformed']: continue
    print rec['name']

######################################################

records=parseSpreadsheet()

if PRINTSTATS:
  getStats(records)
  print '\n\n##### Offline PVs:'
  for rec in records:
    if not rec['online']: print rec['name']
  print '\n\n##### Unarchived PVs:'
  for rec in records:
    if not rec['archived']: print rec['name']
  print '\n\n##### Malformed PVs:'
  for rec in records:
    if rec['malformed']: print rec['name']
  print '\n\n##### Good PVs:'
  printPvList(records)

else:
  printSubs(records)


