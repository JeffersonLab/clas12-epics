#!/usr/bin/env python
import os,sys,epics,subprocess,datetime

PVNAMES='''
scaler_calc1;BeamCurrent
B_DET_FTC_FADC:avg;FTC:AvgCounts
B_DET_ECAL_TDC_SEC2_UI_E01-E12:avg;ECAL:UI:SEC2:1-12:avg
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
  for row in PVNAMES.split():
    cols=row.strip().split(';')
    name=cols.pop(0)
    desc=' '.join(cols)
    PVS.append({'name':name,'pv':epics.pv.PV(name),'desc':desc})

def printTable(file=None):
  if not file: file=sys.stdout
  print >> file, '%19s'%'Time',
  for pv in PVS:
    fmt='%%%ds'%(len(pv['desc'])+1)
    print >> file, fmt%pv['desc'],
  print >> file
  for row in TABLE:
    print >> file, '%19s'%row[0],
    for icol in range(1,len(row)):
      fmt='%%%d.3e'%(len(PVS[icol-1]['desc'])+1)
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
  cmd=[LOGENTRY,'-l',LOGBOOK,'-t','\'CLAS12 Luminosity Scan\'','-a',oo.name,'-b',oo.name]
  pp=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  out,err = pp.communicate()
  if out: print out
  if err: print err

#############################################

loadPVs()

first=True

while True:
  if not first:
    takeSnapshot()
    printTable()
  print 'Press Return to take next snapshot and append table.'
  if not first:
    print 'Press L and then Return to send to logbook and quit.'
  if raw_input()=='L' and not first:
    makeLogEntry()
    sys.exit()
  first=False


