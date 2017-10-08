#!/usr/bin/env python
import epics,subprocess,time,datetime,sys,threading,signal

# See $EPICS/apps/monitorApp/Db/rollingAverages.db for outputs

# time durations over which to average:
# - use myStats conventions
# - also the PV suffix
TIMES=['2h','8h','24h','1w']

# corresponding "scan" periods (units=seconds):
SCANS=[ 2*60, 8*60, 24*60, 7*24*60 ]

# name of file containing list of input PVs to be time-averaged:
PVFILE='./pvRollAvg.list'

# myStats command line for most recent DT time range:
CMD=['myStats','-b','-DT','-e','^DT','-l','PVNAME']

# the output PVs:
OPVS={}

# heartbeat PV:
HBEAT=epics.pv.PV('rollAvg:HEARTBEAT')

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

# just run myStats and return output:
def myStats(pvNames,dt):
  cmd=list(CMD)
  cmd=[xx.replace('DT',dt) for xx in cmd]
  cmd=[xx.replace('PVNAME',','.join(pvNames)) for xx in cmd]
  out,err=None,None
  try:
    p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,err = p.communicate()
  except:
    # This happens.  Probably an nfs issue.
    print 'getMyaStats2:  exception running myStats!'
    # Prevent from trying again immediately:
    time.sleep(10)
  return out,err

# get myStats results:
def getMyaStats(pvNames,dt):
  stats=[]
  out,err=myStats(pvNames,dt)
  if not out or err:
    print 'getMyaStats:  error running myStats!'
    print err
  else:
    lines=out.strip().split('\n')
    if len(lines) != 1+len(pvNames):
      print lines
    else:
      headers = lines[0].split()
      for iline in range(1,len(lines)):
        line=lines[iline]
        data = line.split()
        if len(data) != len(headers):
          print data
          print headers
        else:
          stat={}
          for ii in range(len(data)):
            try:
              if headers[ii]=='Name': stat[headers[ii]]=data[ii]
              elif data[ii]=='N/A':
                print 'myStats N/A for '+pvNames[iline-1]
                stat[headers[ii]]=data[ii]
              else: stat[headers[ii]]=float(data[ii])
            except ValueError:
              print 'Bad value from myStats for %s : >%s<'%(pvNames[iline-1],data[ii])
              break
          stats.append(stat)
  return stats

# if there's a maximum on #pvs to pass to myStats:
def getMyaStats63(pvNames,dt):
  stats=[]
  aa=list(pvNames)
  while len(aa)>0:
    bb=[]
    while len(aa)>0 and len(bb)<63:
      bb.append(aa.pop(0))
    stat=getMyaStats(bb,dt)
    if stat and len(stat)==len(bb):
      stats.extend(stat)
  return stats

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
    print 'Scan Thread Started: Scan=%.0fs dt=%s'%(self.period,self.dt)
    #print ' '.join(self.pvNames)
    while not self.shutdownFlag.is_set():
      time.sleep(1)
      now=time.time()
      #print '\nScan=%.0fs dt=%s -- Now=%.2f Last=%.2f Delta=%.2f'%\
      #(self.period,self.dt,now,self.lastScan,(now-self.lastScan))
      if now-self.lastScan < self.period: continue
      pretty=str(datetime.datetime.now())
      print '%s - Calling myStats - Scan=%.0fs DeltaT=%s'%(pretty,self.period,self.dt)
      success=True
      stats=getMyaStats(self.pvNames,self.dt)
      if stats and len(stats)==len(self.pvs):
        for ii in range(len(self.pvs)):
          if not stats[ii].has_key('Mean'):
            print stats[ii]
            print 'ERROR:  Missing Key: '+self.pvNames[ii]
            success=False
            continue
          if stats[ii]['Mean']=='N/A':
            print 'ERROR:  N/A: '+self.pvNames[ii]
            success=False
            continue
          try:
            self.pvs[ii]['pv'].put(float(stats[ii]['Mean']))
          except:
            print 'Error caputting '+self.pvNames[ii]
            success=False
      else:
        print 'THREAD ERROR: myStats: Scan=%.0fs dt=%s'%(self.period,self.dt)
        success=False
      # if full success, update last scan time
      # otherwise sleep a little and scan again on next cycle
      if success:
        self.lastScan=now
      else:
        time.sleep(5)
    print 'Scan Thread Stopped: Scan=%.0fs dt=%s'%(self.period,self.dt)

class HeartbeatThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.shutdownFlag = threading.Event()
  def run(self):
    print 'Heartbeat Thread started.'
    while not self.shutdownFlag.is_set():
      time.sleep(1)
      if HBEAT.get()==0: HBEAT.put(1)
      else:              HBEAT.put(0)
    print 'Heartbeat Thread stopped.'

class ServiceExit(Exception):
  pass
def serviceShutdown(signum,frame):
  print '\nCaught signal %d'%signum
  raise ServiceExit


######################################


def main():

  signal.signal(signal.SIGTERM, serviceShutdown)
  signal.signal(signal.SIGINT, serviceShutdown)

  initOutputs()

  threads=[]

  try:
    t=HeartbeatThread()
    threads.append(t)
    for ii in range(len(TIMES)):
      t=ScanThread(SCANS[ii],OPVS[TIMES[ii]])
      threads.append(t)
    print '\nrollAvg.py:  # of threads: %d\n '%len(threads)
    for tt in threads:  tt.start()

    # keep alive in order to handle signals and close threads:
    while True: time.sleep(1)

  except ServiceExit:
    print '\nrollAvg.py:  shutting down ...'
    for tt in threads: tt.shutdownFlag.set()
    for tt in threads: tt.join()

if __name__ == '__main__': main()




#class MyThread(threading.Thread):
#  def __Init__(self,name):
#    threading.Thread.__init__(self)
#    self.shutdownFlag = threading.Event()
#    self.name = name
#  def run(self):
#    print 'Thread started:   %s'%self.name
#    while not self.shutdownFlag.is_set():
#      self.process()
#      time.sleep(1)
#    print 'Thread stopped:  %s'%self.name
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
#    #print '\nScan=%.0fs dt=%s -- Now=%.2f Last=%.2f Delta=%.2f'%\
#    #(self.period,self.dt,now,self.lastScan,(now-self.lastScan))
#    if now-self.lastScan < self.period: continue
#    pretty=str(datetime.datetime.now())
#    print '%s - Calling myStats - Scan=%.0fs DeltaT=%s'%(pretty,self.period,self.dt)
#    success=True
#    stats=getMyaStats(self.pvNames,self.dt)
#    if stats and len(stats)==len(self.pvs):
#      for ii in range(len(self.pvs)):
#        if not stats[ii].has_key('Mean'):
#          print stats[ii]
#          print 'ERROR:  Missing Key: '+self.pvNames[ii]
#          success=False
#          continue
#        if stats[ii]['Mean']=='N/A':
#          print 'ERROR:  N/A: '+self.pvNames[ii]
#          success=False
#          continue
#        try:
#          self.pvs[ii]['pv'].put(float(stats[ii]['Mean']))
#        except:
#          print 'Error caputting '+self.pvNames[ii]
#          success=False
#    else:
#      print 'THREAD ERROR: myStats: Scan=%.0fs dt=%s'%(self.period,self.dt)
#      success=False
#    # if not full success, don't update last scan time:
#    if success:
#      self.lastScan=now

