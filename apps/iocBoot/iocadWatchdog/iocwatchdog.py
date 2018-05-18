#!/usr/bin/env python
import sys,epics,time,subprocess

# watch a pv and reboot ioc if not updating

iocName='iocareaDetector'
pvName='cctv6:image1:ArrayData'

logfileDir='/usr/clas12/DATA/logs'

maxStaleCount=2
staleTolerance=10    # seconds
checkPeriod=6        # seconds
delayBeforeReboot=10 # seconds
delayAfterReboot=30  # seconds

maxConsecutiveReboots=3

debug=True
dryRun=False
singleKill=False

staleCount=None
lastCallback=None
PV=None

#logfile=open(logfileDir+'/'+iocName+'Watchdog.log','w+')
#def myprint(ss):
#  print ss
#  logfile.write(ss)

def reboot():
  print 'Rebooting ...'
  cc=subprocess.check_output(['softioc_console','-R',iocName])
  print cc

def callbackfcn(**kws):
  global lastCallback
  if debug:
    print 'callback: '+time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime())
  lastCallback=time.time()

def reset():
  global lastCallback,staleCount
  lastCallback=time.time()
  staleCount=0

def disconnect():
  print 'Disconnecting ...'
  PV.disconnect()

def reconnect():
  print 'Reconnecting ...'
  PV.reconnect()
  PV.wait_for_connection()

def isAlive():
  global staleCount
  dt=time.time()-lastCallback
  if debug: print 'check: %0.2f seconds'%dt
  alive=False
  if dt<staleTolerance:
    alive=True
    staleCount=0
  else:
    staleCount+=1
  return alive

def loadpvs():
  global PV
  PV=epics.pv.PV(pvName,auto_monitor=True)
  PV.add_callback(callbackfcn)
  reset()


def main():
  loadpvs()
  nKills,consecutiveReboots=0,0
  while True:

    time.sleep(checkPeriod)

    if isAlive():

      consecutiveKills=0

    else:

      if staleCount>maxStaleCount:

        if consecutiveKills>maxConsecutiveReboots:
          time.sleep(20)

        if singleKill and nKills>0:
          sys.exit('Single Kill Only')
        else:
          print 'Kill #'+str(nKills+1)

        disconnect()
        time.sleep(delayBeforeReboot)
        reboot()
        time.sleep(delayAfterReboot)
        loadpvs()
        nKills+=1
        consecutiveKills+=1

if __name__ == "__main__":
  while len(sys.argv)>1:
    if sys.argv[ii]=='--single-kill':
      singleKill=True
    elif sys.argv[ii]=='--debug':
      debug=True
    elif sys.argv[ii]=='--dry-run':
      dryRun=True
    elif sys.argv[ii]=='--ioc':
      ii+=1
      iocName=sys.argv[ii]
    elif sys.argv[ii]=='--pv':
      ii+=1
      pvName=sys.argv[ii]
    ii+=1
  main()

