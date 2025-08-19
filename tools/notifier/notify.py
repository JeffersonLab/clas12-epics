#!/usr/bin/env python3

mya_url = 'https://epicsweb.jlab.org/wave/?myaDeployment=&myaLimit=100000&windowMinutes=30&title=&fullscreen=false&layoutMode=1&viewerMode=1&pv={pv}'

def _daemon():
    import time
    import schedule
    while True:
        schedule.run_pending()
        time.sleep(10)

from typing import NamedTuple

class Config(NamedTuple):
    title: str
    pv: str
    log_books: list = []
    log_tags: list = []
    log_users: list = []
    email_sender: str = "hallb-notify@jlab.org"
    email_recipients: list = None
    urls: map = {}
    debug: bool = False
    dryrun: bool = False

class Notify():

    import threading
    keepalive = threading.Thread(target=_daemon)

    def __init__(self, config):
        import threading
        if config.debug: print(config)
        self.cfg = config
        self.lock = threading.Lock()
        self.changes = []
        self.disconnects = []
        self.urls = dict(self.cfg.urls)
        self.urls[f'{self.cfg.pv} in MYA'] = mya_url.format(pv=self.cfg.pv)
        import epics
        epics.pv.PV(self.cfg.pv).add_callback(callback=self.changed, connection_callback=self.changed)
        import schedule
        if self.cfg.debug:
            schedule.every(5).seconds.do(self.report)
        else:
            schedule.every().day.at("08:00").do(self.report)
        if not Notify.keepalive.is_alive():
            Notify.keepalive.start()

    def report(self):
        if self.cfg.debug: print(self.changes)
        self.lock.acquire()
        if len(self.disconnects) > 0:
            msg = f'{self.cfg.pv} disconnects in the past 24 hours:\n'
            msg += '\n'.join([f'{i+1}.  {t}' for i,t in enumerate(self.disconnects)])
            msg += '\n\n'+'\n\n'.join([f'{k}:  {v}' for k,v in self.urls.items()])
            self.send_email(msg)
        # the first reading is just initialization, ignore it:
        if len(self.changes) > 1:
            msg = f'{self.cfg.pv} changes in the past 24 hours:\n'
            msg += '\n'.join([f'{i+1}.  {t}->{v}' for i,(t,v) in enumerate(self.changes[1:])])
            msg += '\n\n'+'\n\n'.join([f'{k}:  {v}' for k,v in self.urls.items()])
            self.submit_log(msg)
            self.send_email(msg)
        # keep only the last reading, as initialization for next time:
        while len(self.changes) > 1:
            self.changes.pop(0)
        self.disconnects.clear()
        self.lock.release()

    def changed(self,**kws):
        import datetime
        now = datetime.datetime.now()
        t = datetime.datetime.utcfromtimestamp(kws['timestamp']-4*60*60)
        v = kws['value']
        self.lock.acquire()
        # the first "change" is always initialization, keep it and ignore it later:
        if len(self.changes) == 0:
            self.changes.append((t,v))
        # else check for a value change:
        elif v != self.changes[-1][1]:
            self.changes.append((t,v))
            print(f'Change #{len(self.changes)-1}:  {t} --> {v}')
        # else it's a disconnect:
        else:
            self.disconnects.append(now)
            print(f'Disconnect #{len(self.disconnects)}:  {now}')
        self.lock.release()

    def submit_log(self):
        if len(self.cfg.log_books) > 0:
            cmd = ['logentry','-t',self.title,'-b','-']
            for u in self.log_users: cmd.extend(['-e',u])
            for g in self.log_tags: cmd.extend(['-g',g])
            for l in self.log_books: cmd.extend(['-l',l])
            print(' '.join(cmd))
            if not self.cfg.dryrun:
               import subprocess
               print(subprocess.check_output(cmd, input=msg, universal_newlines=True))

    def send_email(self,body):
        if len(self.cfg.email_recipients) > 0:
            from email.mime.text import MIMEText
            t = MIMEText(body)
            t['Subject'] = self.cfg.title
            t['From'] = self.cfg.email_sender
            t['To'] = ', '.join(self.cfg.email_recipients)
            print(t)
            if not self.cfg.dryrun:
                import smtplib
                s = smtplib.SMTP('localhost')
                s.sendmail(self.cfg.email_sender, self.cfg.email_recipients, t.as_string())
                s.quit()

########################################################################
########################################################################

_hwp  = Config(title='test', pv='IGL1I00OD16_16', email_recipients=['baltzell@jlab.org'], debug=False)
_ebeam = Config(title='test', pv='MBSY2C_energy', email_recipients=['baltzell@jlab.org'], debug=False)

def test():
    print(_hwp)
    print(_ebeam)
    Notify(_hwp)
    Notify(_ebeam)

