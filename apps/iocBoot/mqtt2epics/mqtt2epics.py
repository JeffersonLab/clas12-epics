#!/usr/bin/env python3
import sys
import subprocess
import json
import epics
import argparse

#
# Requires a configuration file following the expected message format,
# but with strings for PV names instead of number values, e.g.:
#    { KEY : PV, KEY2 : [ PV1, PV2 ] }
#

if len(sys.argv) != 2:
    print('USAGE:  mqtt2epics.py configfile')
    sys.exit(1)

# load configuration and initialize PVs:
with open(sys.argv[1], encoding='utf-8') as f:
    config = json.load(f)
    print(json.dumps(config, indent=2, separators=(',',': ')))
    for key,vals in config.items():
        if type(vals) is list:
            for i,val in enumerate(vals):
                config[key][i] = epics.pv.PV(val)
        else:
            config[key] = epics.pv.PV(vals)

# subscribe to mqtt messages with mosquitto:
cmd = ['mosquitto_sub','-t','clasrun/clasprod/controls','-h','clon00']
process = subprocess.Popen(cmd, stdout=subprocess.PIPE)

# parse the messages, write to config:
message_body = ''
for c in iter(lambda: process.stdout.read(1), b''):
    if c == b'\n':
        for key,vals in json.loads(message_body).items():
            if key in config:
                if type(vals) is list:
                    for pv,val in zip(config[key],vals):
                        pv.put(float(val))
                else:
                    config[key].put(float(vals))
        message_body = ''
    else:
        message_body += c.decode('utf-8')

