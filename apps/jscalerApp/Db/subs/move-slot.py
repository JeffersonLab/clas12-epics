#!/usr/bin/env python
import sys

old_slot = 12
new_slot = 17

crate_slot_column = 7
slot_column = 2

for line in open(sys.argv[1],'r').readlines():
  line=line.strip()
  if not line.startswith('{'):
    print(line)
  else:
    cols = line.strip('{}').replace('"','').split(',')
    crate_slot = int(cols[crate_slot_column],16)
    crate = crate_slot & 0xFF
    slot = crate_slot >> 8
    if slot == old_slot:
      crate_slot = crate + (new_slot<<8)
      cols[crate_slot_column] = '0x%x' % crate_slot
      cols[slot_column] = '%.0d' % new_slot
    print('{ %s }'%','.join(['"%s"'%x.strip() for x in cols]))

