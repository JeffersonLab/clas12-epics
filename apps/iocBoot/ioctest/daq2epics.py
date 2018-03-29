#!/usr/bin/env python
import epics,time,subprocess,os,re

os.putenv('MYSQL_HOST','clondb1')
os.putenv('EXPID','clasrun')
os.putenv('SESSION','clasprod')

CFG={
'B_DAQ:livetime':     {'ini':-1,   'cmd':['tcpClient','trig1','tsBusy']},
'B_DAQ:run_number':   {'ini':-1,   'cmd':['run_number']},
'B_DAQ:run_nfiles':   {'ini':-1,   'cmd':['run_nfiles']},
'B_DAQ:run_status':   {'ini':'UDF','cmd':['run_status']},
'B_DAQ:run_config':   {'ini':'UDF','cmd':['run_config']},
'B_DAQ:run_time':     {'ini':-1,   'cmd':['run_time']},
'B_DAQ:run_ndata':    {'ini':-1,   'cmd':['run_ndata']},
'B_DAQ:run_nevents':  {'ini':-1,   'cmd':['run_nevents']}
}

HBEAT=epics.pv.PV('B_DAQ:livetime_heartbeat')

nonNumber=re.compile(r'[^\d.]+')

for pvName in CFG.keys():
  CFG[pvName]['pv']=epics.pv.PV(pvName)
  CFG[pvName]['pv'].put(CFG[pvName]['ini'])

ii=0
while True:

  success=True
  for pvName in CFG.keys():
    try:
      xx=subprocess.check_output(CFG[pvName]['cmd']).strip()
      yy=xx
      if type(CFG[pvName]['ini']) is not str:
        yy=re.sub(nonNumber,'',xx)
      if pvName=='B_DAQ:livetime':
        if xx.find('Livetime')==0:
          jj=HBEAT.get()
          HBEAT.put(jj+1)
          CFG[pvName]['pv'].put(yy)
      else:
        CFG[pvName]['pv'].put(yy)
    except:
      success=False
      print 'Error on '+pvName
  if success:
    ii+=1

  time.sleep(2)

