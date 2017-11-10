#!/usr/bin/env python
import os,sys,epics,subprocess,datetime

PVNAMES='''
scaler_calc1
B_DET_FTC_FADC:avg
'''

LOGBOOK='TLOG'
LOGENTRY='/cs/certified/apps/logentrycli/PRO/bin/logentry'
OUTSTUB=os.getenv('HOME')+'/lumiscan/lumiscan'

PVS,TABLE=[],[]

def getPrettyTime():
  pt=str(datetime.datetime.now())
  pt=pt.split('.')[0].replace(' ','_')
  return pt

def loadPVs():
  for name in PVNAMES.split():
    PVS.append({'name':name,'pv':epics.pv.PV(name)})

def printTable(file=None):
  if not file: file=sys.stdout
  print >> file, '%19s'%'Time',
  for pv in PVS:
    fmt='%%%ds'%(len(pv['name'])+1)
    print >> file, fmt%pv['name'],
  print >> file
  for row in TABLE:
    print >> file, '%19s'%row[0],
    for icol in range(1,len(row)):
      fmt='%%%d.3e'%(len(PVS[icol-1]['name'])+1)
      print >> file, fmt%row[icol],
    print >> file
  print >> file

def takeSnapshot():
  vals=[getPrettyTime()]
  for pv in PVS: vals.append(pv['pv'].get())
  TABLE.append(vals)
  if len(TABLE)>1e3:
    print 'Exiting.  Table is too big.'
    printTable()
    sys.exit()

def makeLogEntry():
  oo=open(OUTSTUB+'_'+getPrettyTime()+'.txt','w+')
  printTable(oo)
  oo.close()
  print 'Data table is here: '+oo.name
  cmd=[LOGENTRY,'-l',LOGBOOK,'-t','test','-a',oo.name,'-b',oo.name]
  pp=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  out,err = pp.communicate()
  if out: print out
  if err: print err

#############################################

loadPVs()

while True:
  takeSnapshot()
  printTable()
  print 'Press Return to take next snapshot and append table.'
  print 'Press L and then Return to sent to logbook and quit.'
  a=raw_input()
  if a=='L':
    makeLogEntry()
    sys.exit()

