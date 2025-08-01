#!/usr/bin/env python
#
# hack to get stuff from DAQ into EPICS
#

import math,epics,time,datetime,subprocess,os,re

os.environ['MYSQL_HOST']='clondb1'
os.environ['EXPID']='clasrun'
os.environ['SESSION']='clasprod'

# kludge for CODA's new GCC not in .setup (only in clasrun's ~/.cshrc!), which will surely break again:
os.environ['LD_LIBRARY_PATH']='/apps/gcc/8.3.0/lib:/apps/gcc/8.3.0/lib64:/usr/lib:/usr/local/lib'
os.environ['PATH']='/usr/clas12/release/1.4.0/coda/Linux_x86_64/bin/:'+os.environ['PATH']

def get_fcup_prescale():
    t = epics.pv.PV('B_DAQ:trigger_file').get()
    with open('/usr/clas12/release/1.4.0/parms/trigger/%s.trg'%t) as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            line = line.strip().split()
            if len(line) == 3 and line[0] == 'TS_FP_PRESCALE':
                if line[1] == '8' and int(line[2]) != 0:
                    return '%.8f'% (1.0 / (math.pow(2,int(line[2])-1) + 1))
    return str(1)

CFG={
'B_DAQ:run_status':   {'ini':'UDF','cmd':['run_status']},
'B_DAQ:run_config':   {'ini':'UDF','cmd':['run_config']},
'B_DAQ:run_number':   {'ini':0,    'cmd':['run_number'],'max':1e9},
'B_DAQ:trigger_file': {'ini':'UDF','cmd':['daq_config']},
'B_DAQ:disk_free:clondaq7': {'ini':0, 'skip':60, 'scale':1e-9, 'cmd':['ssh','clondaq7','df','/data','|','grep','-v','Filesystem','|','awk','\'{print$4}\'']},
'B_DAQ:disk_free:clondaq6': {'ini':0, 'skip':60, 'scale':1e-9, 'cmd':['ssh','clondaq6','df','/data','|','grep','-v','Filesystem','|','awk','\'{print$4}\'']},
'B_DAQ:disk_free:clondaq5': {'ini':0, 'skip':60, 'scale':1e-9, 'cmd':['ssh','clondaq5','df','/data','|','grep','-v','Filesystem','|','awk','\'{print$4}\'']},
'B_DAQ:fcup:prescale': {'ini':0, 'skip':10, 'cmd':get_fcup_prescale}
}

#'B_DAQ:disk_free:logs    ': {'ini':0, 'skip':60, 'scale':1e-9, 'cmd':['df','/data','|','grep','-v','Filesystem','|','awk','\'{print$4}\'']}
#'B_DAQ:livetime':     {'ini':-1,   'cmd':['tcpClient','trig1','tsBusy']},

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
      if callable(CFG[pvName]['cmd']):
          xx = CFG[pvName]['cmd']()
      else:
          try:
            xx=subprocess.check_output(CFG[pvName]['cmd'],env=os.environ).strip()
          except TimeoutExpired:
            print(now+' : Timeout on '+pvName)
            continue
      yy=xx

      #print(pvName,CFG[pvName]['cmd'],yy)

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

      # strip trigger file name:
      elif pvName=='B_DAQ:trigger_file':
        yy=yy.split('/').pop()
        if yy.endswith('.cnf'):
          yy=yy[:-4]
        CFG[pvName]['pv'].put(yy)

      # treat everything else uniformly:
      else:
        if 'scale' in CFG[pvName]:
          yy = float(yy)
          yy *= CFG[pvName]['scale']
        if 'max' in CFG[pvName]:
          try:
            yy = float(yy)
            if yy<CFG[pvName]['max']:
              CFG[pvName]['pv'].put(yy)
          except:
            print(now + ' : Conversion failure on'+pvName)
        else:
          CFG[pvName]['pv'].put(yy)

    except:
      success=False
      print(now+' :  Error on '+pvName)

  if success:
    NPOLLS+=1
    NCONSECERR=0
  else:
    NCONSECERR+=1

  # avoid overflow arbitrarily:
  if NPOLLS>1e8: NPOLLS=0

  if NCONSECERR>20:
    print(now+' : # Consecutive Errors: '+str(NCONSECERR))
    time.sleep(5)

  time.sleep(2)

