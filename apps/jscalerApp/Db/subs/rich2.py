#!/usr/bin/env python3
with open('jscalers_RICH_SSP.substitutions','r') as f:
  for l in f.readlines():
    l = l.strip()
    cols = l.split(',')
    if l.find('pattern') >=0 or len(cols) != 19:
      print(l)
    else:

      new_crate = 1

      # add 10 to the slot number:
      #slot = cols[2].strip().strip('"')
      #slot = int(slot) + 10
      #cols[2] = '"%.2d"' % slot

      # add 10 to the slot number and change crate number:
      cscode = cols[7].strip().strip('"')
      slot = int(cscode, 16) >> 8
      #slot += 10
      cscode = (slot << 8) + new_crate
      cols[7] = '"0x%X"' % cscode

      # change crate number:
      cols[0] = '"%.2d"' % new_crate

      print(','.join(cols))

