#!/usr/bin/env python3

import re
import sys
import atexit
import socket
import logging
import argparse
import datetime
import epics

# 
# There appears to be a bug in ASYN, even the latest, 4-42,
# where I/O Intr records cause deadlock.  Here we workaround
# that by parsing the periodic, unsolicited data from the
# Dynapower and just write to PVs.
#

class Dynapower():
  pvs = {}
  pvs['volt'] = epics.PV('DYNAB:v:rbk')
  pvs['amps'] = epics.PV('DYNAB:i:rbk')
  pvs['temp'] = epics.PV('DYNAB:temp')
  pvs['flow'] = epics.PV('DYNAB:flow')
  pvs['stat'] = epics.PV('DYNAB:stat:rbk')
  pvs['flt1'] = epics.PV('DYNAB:fault:1')
  pvs['flt2'] = epics.PV('DYNAB:fault:2')
  def __init__(self, match):
    self.data = {}
    self.data['raw'] = match.group(0)
    self.data['volt'] = float(match.group(1))/10
    self.data['amps'] = float(match.group(2))/10
    self.data['temp'] = float(match.group(3))/10
    self.data['flow'] = float(match.group(4))/10
    self.data['stat'] = int(match.group(5),16)
    self.data['flt1'] = int(match.group(6),16)
    self.data['flt2'] = int(match.group(7),16)
  def update(self):
    for k,v in Dynapower.pvs.items():
      v.put(self.data[k])
  def __str__(self):
    return str(self.data['raw'])

cli=argparse.ArgumentParser(description='asdf')
cli.add_argument('-debug', help='enable debugging verbosity', default=False, action='store_true')
cli.add_argument('host',  help='host name', type=str)
cli.add_argument('port',  help='port number', type=int)
args = cli.parse_args(sys.argv[1:])

if args.debug:
  logging.basicConfig(level=logging.DEBUG, format='%(levelname)-9s %(message)s')
else:
  logging.basicConfig(level=logging.INFO, format='%(levelname)-9s %(message)s')

logger = logging.getLogger(__name__)

regex = b'^ \r\n (\d+) \r\n (\d+) \r\n (\d+) \r\n (\d+) \r\n (\d\d\d\d) \r\n (\d\d\d\d) \r\n (\d\d\d\d)\r\n'
terminator = r'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
re.compile(regex)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((args.host,args.port))
logger.info('Connected to %s:%d'%(args.host,args.port))

last_update = None
n = 0
data = b''

while True:

    data += sock.recv(1)
    logger.debug('%d >%s<'%(n,str(data)))

    if str(data).find(terminator) >= 0:
        m = re.match(regex, data)
        if m is not None:
            x = Dynapower(m)
            logger.info(str(x))
            last_update = datetime.datetime.now()
            logger.info(str(last_update))
            x.update()
        data = b''

    n += 1

