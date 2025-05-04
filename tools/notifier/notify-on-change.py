#!/usr/bin/env python3

dryrun = False
title = 'Half-Wave plate changed'
pv = 'IGL1I00OD16_16'
log_books = ['CLAS12CALIB']
log_tags = ['Autolog','Moller']
email_sender = 'hallb-hwp@jlab.org'
email_recipients = ['baltzell@jlab.org']
urls = ['HWP in RCDB:\nhttps://clasweb.jlab.org/rcdb']
urls.append(f'HWP in Mya:\nhttps://epicsweb.jlab.org/wave/?myaDeployment=&myaLimit=100000&windowMinutes=30&title=&fullscreen=false&layoutMode=1&viewerMode=1&pv={pv}')

import threading
_lock = threading.Lock()
_changes = []
_disconnects = []

def report():
    _lock.acquire()
    if len(_disconnects) > 0:
        msg = 'HWP disconnects in the past 24 hours:\n'
        msg += '\n'.join([f'{i+1}.  {t}' for i,t in enumerate(_disconnects)])
        msg += '\n\n'+'\n\n'.join(urls)
        send_email(msg)
    # the first reading is just initialization, ignore it:
    if len(_changes) > 1:
        msg = 'HWP changes in the past 24 hours:\n'
        msg += '\n'.join([f'{i+1}.  {t} -- HWP --> {v}' for i,(t,v) in enumerate(_changes[1:])])
        msg += '\n\n'+'\n\n'.join(urls)
        send_email(msg)
        submit_log(msg)
    # keep the first, initialization reading for next time:
    for i in range(len(_changes)-1,0,-1):
        _changes.pop(i)
    _disconnects.clear()
    _lock.release()

def submit_log(msg):
    cmd = ['logentry','-t',title,'-b','-']
    for g in log_tags: cmd.extend(['-g',g])
    for l in log_books: cmd.extend(['-l',l])
    print(' '.join(cmd))
    if not dryrun:
       import subprocess
       print(subprocess.check_output(cmd, input=msg, universal_newlines=True))

def send_email(body):
    from email.mime.text import MIMEText
    t = MIMEText(body)
    t['Subject'] = title
    t['From'] = email_sender
    t['To'] = ', '.join(email_recipients)
    print(t)
    if not dryrun:
        import smtplib
        s = smtplib.SMTP('localhost')
        s.sendmail(email_sender, email_recipients, t.as_string())
        s.quit()

def changed(**kws):
    import datetime
    now = datetime.datetime.now()
    t = datetime.datetime.utcfromtimestamp(kws['timestamp']-4*60*60)
    v = kws['value']
    _lock.acquire()
    # the first is initialization, always keep it (and ignore it later):
    if len(_changes) == 0:
        _changes.append((t,v))
    # else check for a value change:
    elif v != _changes[len(_changes)-1][1]:
        _changes.append((t,v))
        print(f'Change #{len(_changes)-1}:  {t} --> {v}')
    # else it's a disconnect:
    else:
        _disconnects.append(now)
        print(f'Disconnect #{len(_disconnects)}:  {now}')
    _lock.release()

def launch():
    # monitor the EPICS PV:
    import epics
    epics.pv.PV(pv).add_callback(callback=changed)
    # schedule a daily report:
    import schedule
    #schedule.every(5).seconds.do(report)
    schedule.every().day.at("08:00").do(report)
    # keep alive:
    import time
    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == '__main__':
    launch()

