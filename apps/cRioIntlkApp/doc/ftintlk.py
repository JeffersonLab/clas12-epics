#!/usr/bin/env python
import sys

SPREADSHEET='ftintlk.csv'
SPREADSHEET='svtHardIntlk.csv'

ICOLS={'desc':0,
      'access':1,
      'type':2,
      'pvoldname':3,
      'units':4,
      'pvname':7}

if SPREADSHEET.find('svt')>=0:
  ICOLS['desc']=1
  ICOLS['access']=2
  ICOLS['type']=3
  ICOLS['pvname']=4
  ICOLS['units']=5

for line in open(SPREADSHEET,'r').readlines():

  if line.find('LabVIEW')>=0: continue

  cols=line.strip().split(',')

  if cols[ICOLS['pvname']] == '': continue

  if len(cols)!=8: continue
  vals={}
  for key in ICOLS.keys():
    vals[key]=cols[ICOLS[key]]

  if vals['desc'].find('SVT EPICS')>=0:
    vals['desc']=vals['desc'].replace('SVT EPICS','SVT')
  if vals['desc'].find('SVT Detector')>=0:
    vals['desc']=vals['desc'].replace('SVT Detector','SVT')

  vals['pvname']=vals['pvname'].strip()

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

