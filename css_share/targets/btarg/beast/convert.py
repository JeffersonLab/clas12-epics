#!/usr/bin/env python3

with open('BTARG_PVs.csv','r') as f:
  for line in f.readlines():
    x = line.strip().split(',')
    pv,guidance,display_details,email = x[0],x[3],x[4],x[5]
    description,latching,annunciating='','true','true'
    display_title='Open Related Display'
    if len(guidance) == 0:
      continue
    print(','.join([pv,description,latching,annunciating,display_title,display_details,guidance,email]))

