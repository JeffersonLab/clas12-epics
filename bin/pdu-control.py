#!/usr/bin/env python
import os
import sys
import time
import argparse
import subprocess

os.environ['MIBDIRS'] += ':'+os.path.dirname(os.path.realpath(__file__))+'/../tools/tripplite'

devices = {
    'ecal-chiller' : { 'host':'hallb-pdu-1', 'outlet':1 },
    'svt-camera'   : { 'host':'hallb-pdu-1', 'outlet':2 },
    'test'         : { 'host':'hallb-pdu-1', 'outlet':3 },
}

cli=argparse.ArgumentParser(description='Control outlets on a Tripp-Lite power distribution unit')
cli.add_argument('-host', default=None, type=str, help='set hostname of PDU')
cli.add_argument('-outlet', default=None, type=int, help='set outlet number on the PDU')
cli.add_argument('-device', default=None, type=str, help='set device name (overrides host/outlet)')
subclis = cli.add_subparsers(dest='command')
subclis.add_parser('off')
subclis.add_parser('on')
subclis.add_parser('cycle')
subclis.add_parser('list')

args = cli.parse_args(sys.argv[1:])

if args.command == 'list':
  print('Valid devices:\n'+'\n'.join(devices.keys()))
  sys.exit(0)

if args.device is not None:
  if args.device in devices:
    args.host = devices[args.device]['host']
    args.outlet = devices[args.device]['outlet']
  else:
    cli.error('Invalid device: %s\nValid devices: %s'%(args.device,devices.keys()))
if args.host is None or args.outlet is None:
  cli.error('Must define either -device or -host and -outlet.')

oid = 'TRIPPLITE-PRODUCTS::tlpPduOutletCommand.1.'+str(args.outlet)
cmd = ['snmpset','-v','2c','-c','tripplite',args.host,oid,'i']

if args.command == 'off' or args.command == 'cycle':
  print(subprocess.check_output(cmd+['1'],env=os.environ))

if args.command == 'on' or args.command == 'cycle':
  if args.command == 'cycle':
    print('Waiting 30 seconds to repower ...')
    time.sleep(30)
  print(subprocess.check_output(cmd+['2'],env=os.environ))


