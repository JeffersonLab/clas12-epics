#!/usr/bin/env python3

dryrun = False
verbose = False
pv = 'IGL1I00OD16_16'
title = 'Half-Wave plate changed'
log_book = 'CLAS12CALIB'
log_author = 'baltzell'
email_sender = 'hallb-hwp@jlab.org'
email_recipients = ['baltzell@jlab.org']
url = f'\n\nHWP in Mya:\nhttps://epicsweb.jlab.org/wave/?myaDeployment=&myaLimit=100000&windowMinutes=30&title=&fullscreen=false&layoutMode=1&viewerMode=1&pv={pv}'
url += '\n\nHWP in RCDB:\nhttps://clasweb.jlab.org/rcdb'

import threading
lock = threading.Lock()
changes = []

def report():
    lock.acquire()
    if len(changes) > 0:
        msg = 'HWP changes in the past 24 hours:\n'
        msg += '\n'.join([f'{i}.  {t} -- HWP --> {v}' for i,(t,v) in enumerate(changes)])
        msg += f'{url}\n'
        send_email(msg)
        submit_log(msg)
    changes.clear()
    lock.release()

def submit_log(msg):
    cmd = ['logentry','-g','Autolog','-g','Moller','-l',log_book,'-t',title,'-b','-','-e',log_author]
    if verbose:
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
    if verbose:
        print(t)
    if not dryrun:
        import smtplib
        s = smtplib.SMTP('localhost')
        s.sendmail(email_sender, email_recipients, t.as_string())
        s.quit()

def changed(**kws):
    import datetime
    t = datetime.datetime.utcfromtimestamp(kws['timestamp']-4*60*60)
    lock.acquire()
    if changed.n > 0:
        changes.append((t,kws['value']))
    lock.release()
    changed.n += 1

changed.n = 0

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

