#!/usr/bin/env python3

import collections

crate_name = 'CNAME'
crate_type = '1527'
detector_name = 'X'
system_name = 'HV'

crate = 12
n_slots = 20
n_channels_per_slot = 24

header = collections.OrderedDict()
header['Cr'] = 2
header['CrName'] = 8
header['CrType'] = 6
header['Sl'] = 2
header['Ch'] = 2
header['Sys'] = 5
header['Det'] = 5
header['Element'] = 7
header['CScode'] = 7
header['pwonoff'] = 7
header['v0set'] = 7
header['i0set'] = 7
header['trip'] = 7
header['rampup'] = 7
header['rampdn'] = 7
header['svmax'] = 7
header['enable'] = 7

channel_data = collections.OrderedDict()
channel_data['Cr'] = crate
channel_data['CrName'] = crate_name
channel_data['CrType'] = crate_type
channel_data['Sl'] = None
channel_data['Ch'] = None
channel_data['Sys'] = system_name
channel_data['Det'] = detector_name
channel_data['Element'] = None

commands = collections.OrderedDict()
commands['pwonoff'] = 0x0B
commands['v0set'] = 0x02
commands['i0set'] = 0x05
commands['trip'] = 0x0A
commands['rampup'] = 0x04
commands['rampdn'] = 0x03
commands['svmax'] = 0x0D
commands['enable'] = 0x01

def format_row(values,quotes):
  if quotes:
    values = [ '"%s"' % x for x in values ]
  else:
    values = [ '%s' % x for x in values ]
  fmt = [ '%%%ds' % (x+2) for x in header.values() ]
  fmt = ', '.join(fmt)
  return '{ ' + fmt % tuple(values) + ' }'

print('file "db/caenhv.db" {')
print('pattern ' + format_row(tuple(header.keys()),False))

element = 0

for slot in range(n_slots):

  for channel in range(n_channels_per_slot):

    cdata = channel_data.copy()

    cdata['Sl'] = '%0.2d'%slot
    cdata['Ch'] = '%0.2d'%channel
    cdata['Element'] = 'E%d' % (element)
    cdata['CScode'] = '#C%d' % (crate + (slot<<8))

    for command in commands.keys():
      cdata[command] = 'S%d' % (channel + 256*commands[command])

    print('        ' +format_row(tuple(cdata.values()),True))

    element += 1

print('}')

