#!/usr/bin/env python
#
# hack to get stuff from DAQ into EPICS
#

import epics,time,datetime,subprocess,os,re

os.putenv('MYSQL_HOST','clondb1')
os.putenv('EXPID','clasrun')
os.putenv('SESSION','clasprod')

CFG={
'B_DAQ:livetime':     {'ini':-1,   'cmd':['tcpClient','trig1','tsBusy']},
'B_DAQ:run_status':   {'ini':'UDF','cmd':['run_status']},
'B_DAQ:run_config':   {'ini':'UDF','cmd':['run_config']},
'B_DAQ:run_number':   {'ini':-1,   'cmd':['run_number']},
'B_DAQ:disk_free:clondaq6': {'ini':0, 'skip':60, 'scale':1e-9, 'cmd':['ssh','clondaq6','df','/data','|','grep','-v','Filesystem','|','awk','\'{print$4}\'']},
'B_DAQ:disk_free:clondaq5': {'ini':0, 'skip':60, 'scale':1e-9, 'cmd':['ssh','clondaq5','df','/data','|','grep','-v','Filesystem','|','awk','\'{print$4}\'']}
}

# These are proven unreliable, so useless:
#'B_DAQ:run_nfiles':   {'ini':-1,   'cmd':['run_nfiles']},
#'B_DAQ:run_time':     {'ini':-1,   'cmd':['run_time']},
#'B_DAQ:run_ndata':    {'ini':-1,   'cmd':['run_ndata']},
#'B_DAQ:run_nevents':  {'ini':-1,   'cmd':['run_nevents']},

HBEAT=epics.pv.PV('B_DAQ:livetime_heartbeat')

NONNUMBER=re.compile(r'[^\d.]+')

# initialize PVs:
for pvName in CFG.keys():
  CFG[pvName]['pv']=epics.pv.PV(pvName)
  CFG[pvName]['pv'].put(CFG[pvName]['ini'])
#  CFG[pvName+':comms']['pv']=epics.pv.PV(pvName)
#  CFG[pvName+':comms']['pv'].put(0)

NPOLLS=0
NCONSECERR=0

while True:

  now=str(datetime.datetime.now())
  success=True

  for pvName in CFG.keys():

    try:

      # skip slow-rate pvs:
      if 'skip' in CFG[pvName] and NPOLLS%CFG[pvName]['skip']!=0:
        continue

      # run the command, collect its output:
      xx=subprocess.check_output(CFG[pvName]['cmd']).strip()
      yy=xx

      # if it's a number, strip all non-numbers:
      if type(CFG[pvName]['ini']) is not str:
        yy=re.sub(NONNUMBER,'',xx)

      # treat livetime specially:
      if pvName=='B_DAQ:livetime':
        if xx.find('Livetime')==0:
          jj=HBEAT.get()
          HBEAT.put(jj+1)
          CFG[pvName]['pv'].put(yy)
        else:
          CFG[pvName]['pv'].put(CFG[pvName]['ini'])

      # treat everything else uniformly:
      else:
        if 'scale' in CFG[pvName]:
          yy = float(yy)
          yy *= CFG[pvName]['scale']
        CFG[pvName]['pv'].put(yy)

    except:
      success=False
      print now+' :  Error on '+pvName

  if success:
    NPOLLS+=1
    NCONSECERR=0
  else:
    NCONSECERR+=1

  # avoid overflow arbitrarily:
  if NPOLLS>1e8: NPOLLS=0

  if NCONSECERR>20:
    print now+' : # Consecutive Errors: '+str(NCONSECERR)
    time.sleep(5)

  time.sleep(2)

