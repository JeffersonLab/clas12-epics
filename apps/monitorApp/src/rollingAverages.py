#!/usr/bin/env python
import epics,subprocess,time,sys,threading

# See $EPICS/apps/monitorApp/Db/rollingAverages.db for outputs

# time durations over which to average:
# - use myStats conventions
# - also the PV suffix
TIMES=['2h','8h','24h','1w']

# corresponding "scan" periods (units=seconds):
SCANS=[ 2*60, 8*60, 24*60, 7*24*60 ]

# name of file containing list of input PVs to be time-averaged:
PVFILE='./pv.list'

# myStats command line for most recent DT time range:
CMD=['myStats','-b','-DT','-e','^DT','-l','PVNAME']

# the output PVs:
OPVS={}

HBEAT=epics.pv.PV('iocRollingAverages:HEARTBEAT')

# setup the output PVs:
def initOutputs():
  global OPVS
  pvnames=[xx.strip() for xx in open(PVFILE,'r').readlines()]
  for ii in range(len(TIMES)):
    dt=TIMES[ii]
    pvs=[]
    for pvname in pvnames:
      if not pvname or pvname=='': continue
      if pvname.find('#')==0: continue
      pv={}
      pv['name']=pvname
      pv['dt']=dt
      pv['scan']=SCANS[ii]
      # output PV naming convention:
      pv['pv']=epics.pv.PV(pvname+':'+dt)
      pvs.append(pv)
    OPVS[dt]=pvs

# get myStats results:
def getMyaStats(pvNames,dt):
  cmd=list(CMD)
  cmd=[xx.replace('DT',dt) for xx in cmd]
  cmd=[xx.replace('PVNAME',','.join(pvNames)) for xx in cmd]
  p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  out,err = p.communicate()
  if not out or err:
    if err and err != '': print err
    return None
  lines=out.strip().split('\n')
  if len(lines) != 1+len(pvNames):
    print lines
    return None
  headers = lines[0].split()
  stats=[]
  for line in lines[1:]:
    data = line.split()
    if len(data) != len(headers):
      print data
      print headers
      return None
    stat={}
    for ii in range(len(data)):
      try:
        if headers[ii]=='Name': stat[headers[ii]]=data[ii]
        else:                   stat[headers[ii]]=float(data[ii])
      except ValueError:
        print 'getMyaStats: ERROR on '+pvName
        return None
    stats.append(stat)
  return stats

# one thread per scan period (units=seconds):
def scanThread(period,pvs):
  pvNames=[]
  for pv in pvs: pvNames.append(pv['name'])
  while True:
    stats=getMyaStats(pvNames,pv['dt'])
    if stats and len(stats)==len(pvs):
      for ii in range(len(pvs)):
        pvs[ii]['pv'].put(float(stats[ii]['Mean']))
    else:
      print 'rollAverages.py:  ERROR'
    time.sleep(pv['scan'])

def heartbeatThread():
  while True:
    if HBEAT.get()==0: new=1
    else:              new=0
    HBEAT.put(new)
    time.sleep(1)

######################################

initOutputs()

threads=[]

t=threading.Thread(target=heartbeatThread)
t.start()
threads.append(t)

for ii in range(len(TIMES)):
  t=threading.Thread(target=scanThread,args=(SCANS[ii],OPVS[TIMES[ii]]))
  t.start()
  threads.append(t)

print 'rollingAverages.py:  # of threads:  '+str(len(threads))

# TODO: listen for signal (e.g. SIGTERM) and kill all threads



