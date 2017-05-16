#!/usr/bin/env python
import sys

ICOLS={'desc':0,
      'access':1,
      'type':2,
      'pvoldname':3,
      'units':4,
      'pvname':7}

for line in open('ftintlk.csv','r').readlines():
  cols=line.strip().split(',')
  if len(cols)!=8: continue
  vals={}
  for key in ICOLS.keys():
    vals[key]=cols[ICOLS[key]]

  vals['desc'].replace('FTCalorimeter','FTC')
  vals['desc'].replace('FTHodoscope','FTH')

  pvtype=None
  if   vals['type']=='Double': pvtype='a'
  elif vals['type']=='Boolean': pvtype='b'
  else: sys.exit('Unknown type:\n'+line.strip())
  if   vals['access']=='Read Only':  pvtype+='i'
  elif vals['access']=='Read/Write': pvtype+='o'
  else: sys.exit('Unknown access:\n'+line.strip())

  prec,units,asfields=None,None,None
  if pvtype=='ai' or pvtype=='ao':
    if vals['units'].find('%')>=0: units='%'
    elif vals['units'].find('C')>=0: units='C'
    elif vals['units'].find('N/A')>=0: units=''
    else: units=vals['units']
    asfields='HIHI HIGH LOW LOLO HHSV HSV LSV LLSV'
  elif pvtype=='bi' or pvtype=='bo':
    asfields='ZSV OSV'

#  print vals
  print 'record(%s,"%s") {'%(pvtype,vals['pvname'])
  print '  field("DESC","%s")'%(vals['desc'])
  if units: print '  field("EGU","%s")'%(units)
  if prec:  print '  field("PREC","%s")'%(prec)
  print '  info(autosaveFields_pass0,"%s")'%(asfields)
  print '}'

