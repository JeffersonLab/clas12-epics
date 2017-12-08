#!/usr/bin/env python
import sys

if len(sys.argv)<2:
  sys.exit('Usage:  richIntlk.py csvFileName')

ICOLS={
      'access':4,
      'type':5,
      'units':7,
      'pvname':6}

for line in open(sys.argv[1],'r').readlines():
  if line.find('PV')==0: continue
  if line.find('Hall B RICH')==0: continue
  cols=line.strip().split(',')
  if len(cols)!=9 and len(cols)!=8: continue
  vals={}
  for key in ICOLS.keys():
    vals[key]=cols[ICOLS[key]]

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
    asfields='HIHI HIGH LOW LOLO HHSV HSV LSV LLSV MDEL'
  elif pvtype=='bi' or pvtype=='bo':
    asfields='ZSV OSV'

#  print vals
  print 'record(%s,"%s") {'%(pvtype,vals['pvname'])
  #print '  field("DESC","%s")'%(vals['desc'])
  if units: print '  field("EGU","%s")'%(units)
  if prec:  print '  field("PREC","%s")'%(prec)
  print '  info(autosaveFields_pass0,"%s")'%(asfields)
  print '}'

