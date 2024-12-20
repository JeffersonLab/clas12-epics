#!/usr/bin/env python3
import sys

# append all stdin to sys args:
if not sys.stdin.isatty():
    sys.argv.extend(sys.stdin.read().strip().split())

import argparse
cli = argparse.ArgumentParser(description='Generate BEAST XML for one level in the alarm tree.',epilog='Note, macros can be specified as a suffix on the OPI, e.g.:  -r \'/CLAS12_Share/test.opi &quot;NAME=VALUE&quot;\'')
cli.add_argument('-t', help='directory in tree, e.g., /HallB/Beamline/', required=True)
cli.add_argument('-d', help='description', required=True)
cli.add_argument('-g', help='guidance', required=True)
cli.add_argument('-r', help='related opi, e.g. /CLAS12_Share/test.opi', default=None)
cli.add_argument('-D', help='delay (seconds)', default=0, type=int)
cli.add_argument('-e', help='email address', default=None)
cli.add_argument('-n', help='person', default=None)
cli.add_argument('pv', nargs='*', help='PV names')
args = cli.parse_args()

args.t = args.t.strip(' /').split('/')

if (args.e and not args.n) or (args.n and not args.e):
    cli.error('Sending notifications requires both -n and -e.')

s=['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>']
s.append('<config name="{args[0]}">')
for c in args.t[1:]:
    s.append(f'    <component name="{c}">')
for pv in args.pv:
    s.append(f'''        <pv name="{pv}">
              <description>{args.d}</description>
              <latching>true</latching>
              <annunciating>true</annunciating>
              <delay>{args.D}</delay>
              <count>0</count>
              <guidance>
                  <title>Guidance</title>
                  <details>{args.g}</details>
              </guidance>''')
    if args.r is not None:
        s.append(f'''              <display>
                  <title>Open Related Display</title>
                  <details>{args.r}</details>
              </display>''')
    if args.e is not None:
        s.append(f'''              <automated_action>
                  <title>Email {args.n}</title>
                  <details>mailto:{args.e}</details>
              </automated_action>''')
    s.append('          </pv>')
for c in args.t[1:]:
    s.append('    </component>')
s.append('</config>')

print('\n'.join(s))

