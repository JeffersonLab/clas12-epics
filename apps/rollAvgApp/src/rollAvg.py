#!/usr/bin/env python
import epics,subprocess,time,datetime,sys,threading,signal

# See $EPICS/apps/rollAvgApp/Db/rollingAverages.db for outputs

# time durations over which to average:
# - use myStats conventions
# - also the PV suffix
TIMES=['2h','8h','24h','1w']

# spans of time-derivatives:
# - PV suffix is dxdtDTTIMES
DTTIMES=['30m','2h','10h']

# corresponding "scan" periods (units=seconds):
SCANS=[ 2*60, 8*60, 24*60, 7*24*60 ]

DTSCANS=[ 2*60, 2*60, 2*60 ]

# name of file containing list of input PVs to be time-averaged:
PVFILE='./pvRollAvg.list'

# myStats command line for most recent DT time range:
CMD=['myStats','-b','-DT','-e','^DT','-l','PVNAME']

# the output PVs:
OPVS={}
OPVSDT={}

# status PVs:
HBEAT=epics.pv.PV('iocrollAvgGet:HEARTBEAT')
HBEATS,MYACOMMS,MESSAGES=[],[],[]
for tt in TIMES:
  HBEATS.append(epics.pv.PV('iocrollAvgGet:%s:HEARTBEAT'%tt))
  MYACOMMS.append(epics.pv.PV('iocrollAvgGet:%s:stat'%tt))
  pvPrev=epics.pv.PV('iocrollAvgGet:%s:prevUpdate'%tt)
  pvNext=epics.pv.PV('iocrollAvgGet:%s:nextUpdate'%tt)
  MESSAGES.append({'prev':pvPrev,'next':pvNext})

# logfile:
LOGFILENAME='/usr/clas12/DATA/logs/iocrollAvgGet.log'
LOGFILE=None

# setup the output PVs:
def initOutputs():
  global OPVS
  pvnames=[xx.strip() for xx in open(PVFILE,'r').readlines()]
#  pvnamesDT=[xx.strip() for xx in open(PVFILEDT,'r').readlines()]
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
#  for ii in range(len(DTTIMES)):
#    dt=DTTIMES[ii]
#    pvs=[]
#    for pvname in pvnamesDT:

# just run myStats and return output:
def myStats(pvNames,dt,t0=None):
  cmd=list(CMD)
  if t0==None:
    # averge over time range between -dt and now:
    cmd=[xx.replace('DT',dt) for xx in cmd]
  else:
    # average over time range between -t0 and -t0+dt:
    cmd=[xx.replace('-DT',t0) for xx in cmd]
    cmd=[xx.replace('^DT',dt) for xx in cmd]
  cmd=[xx.replace('PVNAME',','.join(pvNames)) for xx in cmd]
  out,err=None,None
  try:
    p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,err = p.communicate()
  except:
    # This happens.  Probably an nfs issue.
    myPrint( 'getMyaStats2:  exception running myStats!')
    # Prevent from trying again immediately:
    time.sleep(10)
  return out,err

# get myStats results:
def getMyaStats(pvNames,dt):
  stats=[]
  out,err=myStats(pvNames,dt)
  if not out or err:
    myPrint( 'getMyaStats:  error running myStats!')
    myPrint( err)
  else:
    lines=out.strip().split('\n')
    if len(lines) != 1+len(pvNames):
      myPrint( lines)
    else:
      headers = lines[0].split()
      for iline in range(1,len(lines)):
        line=lines[iline]
        data = line.split()
        if len(data) != len(headers):
          myPrint( data)
          myPrint( headers)
        else:
          stat={}
          for ii in range(len(data)):
            try:
              if headers[ii]=='Name': stat[headers[ii]]=data[ii]
              elif data[ii]=='N/A':
                myPrint( 'myStats N/A for '+pvNames[iline-1])
                stat[headers[ii]]=data[ii]
              else: stat[headers[ii]]=float(data[ii])
            except ValueError:
              myPrint( 'Bad value from myStats for %s : >%s<'%(pvNames[iline-1],data[ii]))
              break
          stats.append(stat)
  return stats

def updateHeartbeat(heartbeat):
  if heartbeat.get()==0: heartbeat.put(1)
  else:                  heartbeat.put(0)

def getPrettyTime(dateTime):
  return '%d/%d %.2d:%.2d'%\
      (dateTime.month,dateTime.day,dateTime.hour,dateTime.minute)


class ScanThread(threading.Thread):
  def __init__(self,period,pvs):
    threading.Thread.__init__(self)
    self.shutdownFlag = threading.Event()
    self.lastScan=-99999
    self.period=period
    self.pvs=pvs
    self.pvNames=[]
    self.dt=pvs[0]['dt']
    for pv in pvs: self.pvNames.append(pv['name'])
  def run(self):
    global MYACOMMS
    myPrint( 'Scan Thread Started: Scan=%.0fs dt=%s'%(self.period,self.dt))
    #myPrint( ' '.join(self.pvNames))
    nConsecBad=0
    while not self.shutdownFlag.is_set():
      # if Mya comms problem, reset lastScan to force an update:
      m1=MESSAGES[TIMES.index(self.dt)]['prev'].get()
      m2=MESSAGES[TIMES.index(self.dt)]['next'].get()
      if m1=='Uninitialized' or m2=='Uninitialized' or \
          MYACOMMS[TIMES.index(self.dt)].get()==1:
        nConsecBad += 1
        if nConsecBad>1: self.lastScan=-99999
        time.sleep(2)
      else:
        nConsecBad = 0
      time.sleep(1)
      updateHeartbeat(HBEATS[TIMES.index(self.dt)])
      now=time.time()
      #myPrint( '\nScan=%.0fs dt=%s -- Now=%.2f Last=%.2f Delta=%.2f'%\)
      #(self.period,self.dt,now,self.lastScan,(now-self.lastScan))
      if now-self.lastScan < self.period: continue
      pretty=str(datetime.datetime.now())
      myPrint( '%s - Calling myStats - Scan=%.0fs DeltaT=%s'%(pretty,self.period,self.dt))
      success=True
      stats=getMyaStats(self.pvNames,self.dt)
      if stats and len(stats)==len(self.pvs):
        for ii in range(len(self.pvs)):
          if not stats[ii].has_key('Mean'):
            myPrint( stats[ii])
            myPrint( 'ERROR:  Missing Key: '+self.pvNames[ii])
            success=False
            continue
          if stats[ii]['Mean']=='N/A':
            myPrint( 'ERROR:  N/A: '+self.pvNames[ii])
            success=False
            continue
          try:
            self.pvs[ii]['pv'].put(float(stats[ii]['Mean']))
          except:
            myPrint( 'ERROR CAPUT %s %.2f'%(self.pvNames[ii],stats[ii]['Mean']))
            success=False
      else:
        myPrint( 'THREAD ERROR: myStats: Scan=%.0fs dt=%s'%(self.period,self.dt))
        success=False
      # if full success, update last scan time
      # otherwise sleep a little and scan again on next cycle
      if success:
        self.lastScan=now
        dt=datetime.timedelta(seconds=SCANS[TIMES.index(self.dt)])
        t1=datetime.datetime.now()
        t2=t1+dt
        MESSAGES[TIMES.index(self.dt)]['prev'].put(getPrettyTime(t1))
        MESSAGES[TIMES.index(self.dt)]['next'].put(getPrettyTime(t2))
        MYACOMMS[TIMES.index(self.dt)].put(0)
      else:
        MYACOMMS[TIMES.index(self.dt)].put(1)
        time.sleep(120)
    myPrint( 'Scan Thread Stopped: Scan=%.0fs dt=%s'%(self.period,self.dt))

class HeartbeatThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.shutdownFlag = threading.Event()
  def run(self):
    myPrint( 'Heartbeat Thread started.')
    while not self.shutdownFlag.is_set():
      time.sleep(1)
      updateHeartbeat(HBEAT)
    myPrint( 'Heartbeat Thread stopped.')

class ServiceExit(Exception):
  pass
def serviceShutdown(signum,frame):
  myPrint( '\nCaught signal %d'%signum)
  raise ServiceExit


######################################

def checkLogFile():
  global LOGFILE
  if not LOGFILE or LOGFILE.closed:
    while not LOGFILE:
      LOGFILE=open(LOGFILENAME,'a+')
      time.sleep(5)

def myPrint(text):
  global LOGFILE
  print text
  try :
    LOGFILE.write(text)
  except TypeError:
    print 'Invalid Text'

def main():

  signal.signal(signal.SIGTERM, serviceShutdown)
  signal.signal(signal.SIGINT, serviceShutdown)

  initOutputs()

  threads=[]

  try:

    checkLogFile()

    t=HeartbeatThread()
    threads.append(t)
    for ii in range(len(TIMES)):
      t=ScanThread(SCANS[ii],OPVS[TIMES[ii]])
      threads.append(t)
    myPrint( '\nrollAvg.py:  # of threads: %d\n '%len(threads))
    for tt in threads:
      tt.start()
      time.sleep(1)

    # keep alive in order to handle signals and close threads:
    while True: time.sleep(1)

  except ServiceExit:
    myPrint( '\nrollAvg.py:  shutting down ...')
    for tt in threads: tt.shutdownFlag.set()
    for tt in threads: tt.join()

if __name__ == '__main__': main()






#class MyThread(threading.Thread):
#  def __Init__(self,name):
#    threading.Thread.__init__(self)
#    self.shutdownFlag = threading.Event()
#    self.name = name
#  def run(self):
#    myPrint( 'Thread started:   %s'%self.name)
#    while not self.shutdownFlag.is_set():
#      self.process()
#      time.sleep(1)
#    myPrint( 'Thread stopped:  %s'%self.name)
#  def process(self):
#    pass
#
#class HeartbeatThread(MyThread):
#  def __init__(self,name):
#    MyThread.__init__(self,name)
#  def process(self):
#    if HBEAT.get()==0: HBEAT.put(1)
#    else:              HBEAT.put(0)
#
#class ScanThread(MyThread):
#  def __init__(self,name,period,pvs):
#    MyThread.__init__(self,name)
#    self.lastScan=-99999
#    self.period=period
#    self.pvs=pvs
#    self.pvNames=[]
#    self.dt=pvs[0]['dt']
#    for pv in pvs: self.pvNames.append(pv['name'])
#  def process(self):
#    now=time.time()
#    #myPrint( '\nScan=%.0fs dt=%s -- Now=%.2f Last=%.2f Delta=%.2f'%\)
#    #(self.period,self.dt,now,self.lastScan,(now-self.lastScan))
#    if now-self.lastScan < self.period: continue
#    pretty=str(datetime.datetime.now())
#    myPrint( '%s - Calling myStats - Scan=%.0fs DeltaT=%s'%(pretty,self.period,self.dt))
#    success=True
#    stats=getMyaStats(self.pvNames,self.dt)
#    if stats and len(stats)==len(self.pvs):
#      for ii in range(len(self.pvs)):
#        if not stats[ii].has_key('Mean'):
#          myPrint( stats[ii])
#          myPrint( 'ERROR:  Missing Key: '+self.pvNames[ii])
#          success=False
#          continue
#        if stats[ii]['Mean']=='N/A':
#          myPrint( 'ERROR:  N/A: '+self.pvNames[ii])
#          success=False
#          continue
#        try:
#          self.pvs[ii]['pv'].put(float(stats[ii]['Mean']))
#        except:
#          myPrint( 'Error caputting '+self.pvNames[ii])
#          success=False
#    else:
#      myPrint( 'THREAD ERROR: myStats: Scan=%.0fs dt=%s'%(self.period,self.dt))
#      success=False
#    # if not full success, don't update last scan time:
#    if success:
#      self.lastScan=now

# if there's a maximum on #pvs to pass to myStats:
#def getMyaStats63(pvNames,dt):
#  stats=[]
#  aa=list(pvNames)
#  while len(aa)>0:
#    bb=[]
#    while len(aa)>0 and len(bb)<63:
#      bb.append(aa.pop(0))
#    stat=getMyaStats(bb,dt)
#    if stat and len(stat)==len(bb):
#      stats.extend(stat)
#  return stats

