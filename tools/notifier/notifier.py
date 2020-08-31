#!/usr/bin/env python
import epics,time,smtplib,sys,argparse,os
from email.mime.text import MIMEText

print sys.argv

cli=argparse.ArgumentParser(description='Simple Alarm Notifier.')
cli.add_argument('-n',help='group name', type=str, required=True)
cli.add_argument('-e',help='email address (otherwise from first line in file)', type=str, default=[], action='append', required=False)
cli.add_argument('-f',help='path to file containing list of PVs', type=str, required=True)
args,unknown=cli.parse_known_args(sys.argv[1:])

pvs=[]
if not os.path.isfile(args.f):
  cli.error('Missing file: '+args.f)
for line in open(args.f,'r').readlines():
  if len(args.e)==0:
    args.e.extend(line.strip().split(','))
  elif line.strip().find('#')!=0:
    pvs.append(line.strip().split().pop(0))

minTimeDelta=60*30#seconds

notifiers={}
svt={}
svt['name']=args.n
svt['emails']=args.e
svt['pvnames']=pvs
notifiers['svt']=svt

print notifiers

def sendEmail(pvname,group):
  print 'Sending email ...',pvname,group['emails']
  msg=MIMEText(pvname+' entered MAJOR alarm state\n\nEmails disabled for this PV for the next '+str(minTimeDelta)+' seconds')
  msg['Subject']=group['name']+' Alarm: '+pvname
  msg['From']='hallb-alarm-notifier@jlab.org'
  msg['To']=', '.join(group['emails'])
  s=smtplib.SMTP('localhost')
  s.sendmail('hallb@jlab.org',group['emails'],msg.as_string())
  s.quit()

def onAlarm(pvname=None,severity=None,timestamp=None,group=None,**kws):
  if severity<2:
    return
  if 'tprev' not in group:
    group['tprev']={}
  if not pvname in group['tprev']:
    sendEmail(pvname,group)
  elif timestamp-group['tprev'][pvname]>minTimeDelta:
    sendEmail(pvname,group)
  else:
    print 'Not sending email on '+pvname+', since last one was less than '+str(minTimeDelta)+'s ago.'
  group['tprev'][pvname]=timestamp

for group in notifiers.keys():
  for pvname in notifiers[group]['pvnames']:
    if not pvname in notifiers[group]:
      notifiers[group][pvname]=epics.pv.PV(pvname,auto_monitor=epics.dbr.DBE_ALARM)
      notifiers[group][pvname].add_callback(callback=onAlarm,index=0,group=notifiers[group])

while True:
  time.sleep(100)

