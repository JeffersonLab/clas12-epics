#!/usr/bin/env python
import subprocess
import argparse
import datetime
import epics
import time
import sys
import os

IGNORE_TILES = { 'RICH':[], 'RICH2':[21] }
RECOVERY_PERIOD_SECONDS = 24*60*60
MIN_TILES = 275
MAX_ATTEMPTS = 4
MAPPING = {}

PV_CLOCK = epics.pv.PV('B_RICH:recovery:clock:go')
PV_GO = epics.pv.PV('B_RICH:recovery:go')
PV_STATUS = epics.pv.PV('B_RICH:recovery:stat')
PV_MSG = epics.pv.PV('B_RICH:recovery:msg')
PV_DURATION = epics.pv.PV('B_RICH:recovery:duration')

with open('/usr/clas12/release/pro/epics/apps/jscalerApp/Db/rich-lv-tile.txt') as f:
    for line in f.readlines():
      columns = line.strip().split()
      lv = columns.pop(0)
      for tile in columns:
          if tile in MAPPING:
              print('Duplicate tile:  '+tile)
              sys.exit(111)
          else:
              MAPPING[int(tile)] = int(lv)

def get_lv_channels(tiles):
    for tile in tiles:
        yield MAPPING.get(tile)

def check_scaler_max():
    c1 = epics.caget('B_DET_RICH_SCALERS_PMTS:max',timeout=2)
    c2 = epics.caget('B_DET_RICH2_SCALERS_PMTS:max',timeout=2)
    return c1 is not None and c2 is not None and c1>0 and c2>0

def get_bad_tiles(rich):
    for tile in range(1,134):
        if tile in IGNORE_TILES.get(rich):
            print('%s Ignoring %s tile %d'%(date(),rich,tile))
            continue
        t = epics.caget('B_DET_%s_SSP_TILE%.3d:temp:fpga'%(rich,tile),timeout=2)
        if t is None or t < 1.0:
            yield tile

def cycle(pvonoff, pvstat, timeout=10):
    n_attempts = 0
    max_attempts = 10
    if epics.caput(pvonoff, 0, timeout=2) is None:
        return False
    for i in range(timeout):
        stat = epics.caget(pvstat, timeout=2)
        if stat is None or stat != 0:
            time.sleep(1)
            continue
        if epics.caput(pvonoff, 1, timeout=2) is None:
            while i in range(timeout):
                stat = epics.caget(pvstat, timeout=2)
                if stat is None or stat != 0:
                    time.sleep(1)
                    continue
                else:
                    break
        n_attempts += 1
    return True

def lv_cycle(rich, channels):
  for c in channels:
      pvonoff = 'B_DET_%s_LV_GRP%.2d:pwonoff'%(rich,c)
      pvstat = 'B_DET_%s_LV_GRP%.2d:stat'%(rich,c)
      if not cycle(pvonoff, pvstat):
          return False
  return True

def caen_ioc_reboot():
    comms = epics.caget('B_DET_RICH_ALL_LV:isComm',timeout=2)
    if comms != 1:
        set_status(1,'Reestablishing CAEN comms ...')
        stdout = subprocess.check_output(['softioc_console','-R','ioccaenhv_HVRICH'],stderr=subprocess.STDOUT)
        print(stdout)
        time.sleep(10)
        if epics.caget('ioccaenhv_HVRICH:SysReset',timeout=10) is None:
            return False
    return True

def lv_all_off(timeout=20):
    off = 'B_DET_RICH_ALL_LV:stagger:OFF'
    isoff = 'B_DET_RICH_ALL_LV:isOff'
    if epics.caput(off, 1, timeout=2) is None:
        return False
    if not clear_alarms():
        if not caen_ioc_reboot():
            return False
    for i in range(timeout):
        time.sleep(2)
        stat = epics.caget(isoff, timeout=2)
        if stat == 1:
            return True
    return False

def lv_all_on(timeout=20):
    on = 'B_DET_RICH_ALL_LV:stagger:ON'
    ison = 'B_DET_RICH_ALL_LV:isOn'
    if epics.caput(on, 1, timeout=2) is None:
        return False
    for i in range(timeout):
        time.sleep(2)
        stat = epics.caget(ison, timeout=2)
        if stat == 1:
            return True
    return False

def lv_cycle_all_tiles(max_attempts=3):
    for i in range(max_attempts):
        set_status(1,'Turning LV off')
        if lv_all_off():
            set_status(1,'Turning LV on')
            if lv_all_on():
                return True
    return False

def lv_cycle_bad_tiles(max_attempts=3):
    n_attempts = 0
    while True:
        clear_alarms()
        success = True
        for r in ['RICH','RICH2']:
            for l in set(list(get_lv_channels(get_bad_tiles(r)))):
                set_status(1,'Cycling %s LV group #%d'%(r,l))
                if not lv_cycle(r,[l]):
                    success = False
        if success:
            return True
        elif n_attempts >= max_attempts:
            return False
        n_attempts += 1

def clear_alarms():
    if epics.caput('B_HW_HVRICH1:ClearAlarm', 1, timeout=2) is None:
        if epics.caput('B_HW_HVRICH1:ClearAlarm', 1, timeout=2) is None:
            return False
    if epics.caput('B_HW_HVRICH2:ClearAlarm', 1, timeout=2) is None:
        if epics.caput('B_HW_HVRICH2:ClearAlarm', 1, timeout=2) is None:
            return False
    return True

def wait_for_ssh(hostname='rich4'):
    n_attempts = 0
    max_attempts = 60
    while True:
        n_attempts += 1
        if 0 == os.system('ssh -q %s exit'%hostname):
            return True
        if n_attempts > max_attempts:
            return False
        time.sleep(1)

def roc_reboot_and_wait_for_ssh(hostname='rich4'):
    max_attempts = 60
    delay_seconds = 70
    stdout = subprocess.check_output(['roc_reboot',hostname],stderr=subprocess.STDOUT)
    print(stdout)
    set_status(1,'Waiting for ssh rich4 ...')
    for i in range(delay_seconds):
        print(i),
        time.sleep(1)
    for i in range(max_attempts):
        if 0 == os.system('ssh -q %s exit'%hostname):
            return True
        if i > max_attempts:
            return False
        time.sleep(1)

def rich_init(hostname='rich4'):
    stdout = subprocess.check_output(['ssh',hostname,'rich_init'],stderr=subprocess.STDOUT)
    print(stdout)
    for line in stdout.strip().split('\n')[-100:]:
        if line.find('Total Tiles connected') >= 0:
            return line.split()[3]
    return None

def date():
    return datetime.datetime.strftime(datetime.datetime.now(),
        '%m/%d/%y %H:%M:%S')

def set_status(state, message):
    print('%s %s'%(date(),message))
    PV_STATUS.put(state)
    PV_MSG.put(message)

def recover(alllv=False):
    start = datetime.datetime.now()
    PV_STATUS.put(1)
    if alllv:
        set_status(1,'Starting Full Recovery ...')
    else:
        set_status(1,'Starting Fast Recovery ...')
    time.sleep(1)
    status = False
    n_attempts = 0
    max_attempts = MAX_ATTEMPTS
    # decide whether to roc_reboot on the first attempt:
    roc_reboot = False
    set_status(1,'Checking Scalers ...')
    if not check_scaler_max():
        set_status(1,'Bad Scalers')
        roc_reboot = True
    # reboot the CAEN HV/LV IOC once (why?):
    if not caen_ioc_reboot():
        set_status(2,'Bad IOC Reboot')
    else:
        # try power cycling and reinitialization:
        while n_attempts < max_attempts:
            set_status(1,'Attempt #%d, checking LV ...'%(n_attempts+1))
            # cycle bad tiles:
            if alllv:
                lvstat = lv_cycle_all_tiles()
            else:
                lvstat = lv_cycle_bad_tiles()
            if not lvstat:
                set_status(3,'Bad Cycle')
                time.sleep(1)
            else:
                # reboot ROC every other attempt:
                if roc_reboot or alllv:
                    set_status(1,'Running roc_reboot rich4 ...')
                    if not roc_reboot_and_wait_for_ssh():
                        set_status(4,'Failure on roc_reboot rich4')
                        break
                # initialize FPGAs and check the tile/fiber count:
                time.sleep(10)
                set_status(1,'Running rich_init ...')
                r = rich_init()
                if r is not None and int(r) >= MIN_TILES:
                    status = True
                    set_status(1,'Last Recovery Successful on Attempt #%d'%(n_attempts+1))
                    if alllv:
                        PV_CLOCK.put(0)
                    break
            n_attempts += 1
            time.sleep(1)
    if not status:
        set_status(1,'Last RICH Recovery Failed')
    duration = datetime.datetime.now() - start
    PV_STATUS.put(0)
    PV_GO.put(0)
    PV_DURATION.put(str(duration))
    print('%s %s'%(date(),'Recovery Duration:  %s'%duration))
    return status

def listen():
    print(date()+' Running in Server Mode')
    set_status(0, 'Idle')
    PV_GO.put(0)
    while True:
        if not PV_GO.wait_for_connection(timeout=1):
            print('ERROR1')
            continue
        if not PV_STATUS.wait_for_connection(timeout=1):
            print('ERROR2')
            continue
        if PV_GO.get() == 1:
            recover()
        elif PV_GO.get() == 2:
            recover(alllv=True)
        time.sleep(1)

if __name__ == '__main__':

    cli = argparse.ArgumentParser(description='RICH Tile Recovery and Interrogation Tool',epilog='If no arguments are specified, run in server mode.')
    cli.add_argument('-r',help='run recovery once',action='store_true',default=False)
    cli.add_argument('-L',help='power cycle all LV channels during recovery',action='store_true',default=False)
    cli.add_argument('-rr',help='reboot rich4',action='store_true',default=False)
    cli.add_argument('-ri',help='rich_init',action='store_true',default=False)
    cli.add_argument('-b',help='print bad tiles',action='store_true',default=False)
    cli.add_argument('-bb',help='cycle bad tiles',action='store_true',default=False)
    cli.add_argument('-s',metavar='HOSTNAME',help='test an ssh connection',type=str,default=False)
    cli.add_argument('-l1',metavar='#',help='cycle the specified LV channel in RICH1',action='append',type=int,default=[])
    cli.add_argument('-l2',metavar='#',help='cycle the specified LV channel in RICH2',action='append',type=int,default=[])
    cli.add_argument('-t1',metavar='#',help='cycle the LV channel corresponding to the specified tile in RICH1',action='append',type=int,default=[])
    cli.add_argument('-t2',metavar='#',help='cycle the LV channel corresponding to the specified tile in RICH2',action='append',type=int,default=[])
    args = cli.parse_args(sys.argv[1:])

    if args.b:
        for r in ['RICH','RICH2']:
            print(r+': '+str(list(get_bad_tiles(r))))
    elif args.bb:
        lv_cycle_bad_tiles()
    elif args.r:
        if PV_GO.get() == 0 and PV_STATUS.get() == 0:
            recover(alllv=args.L)
        else:
            print('ERROR:  another recover is currently running')
    elif args.s:
        print(wait_for_ssh(hostname=args.s))
    elif args.rr:
        print(roc_reboot_and_wait_for_ssh())
    elif args.ri:
        print(rich_init())
    elif len(args.l1) > 0:
        print(lv_cycle('RICH',args.l1))
    elif len(args.l2) > 0:
        print(lv_cycle('RICH2',args.l2))
    elif len(args.t1) > 0:
        print(lv_cycle('RICH',get_lv_channels(args.t1)))
    elif len(args.t2) > 0:
        print(lv_cycle('RICH2',get_lv_channels(args.t2)))
    else:
        listen()

