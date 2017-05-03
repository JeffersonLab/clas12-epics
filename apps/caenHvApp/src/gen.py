#!/usr/bin/env python
import sys

G={
'NSLOT':16,
'NCHAN':24,
'CRNUMB':0,
'CRTYPE':'1527',
'CRNAME':'MVTHV',
'SYS':'HV',
'DET':'MVT',
'ELSTUB':'SPARE',
'enable':1,
'pwonoff':11,
'v0set':2,
'i0set':5,
'trip':10,
'rampup':4,
'rampdn':3,
'svmax':13
}

for arg in sys.argv[1:]:
  arg=arg.strip()
  if len(arg.split('='))!=2:
    sys.exit('Usage:  gen.py [key=val [key=val [...]]]')
  key,val=arg.split('=')
  G[key]=val

print 'file "db/caenhv.db" {'
print 'pattern {Cr,CrName,CrType,Sl,Ch,Sys,Det,Elecment,CScode,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax,enable}'

for slot in range(G['NSLOT']):
  for chan in range(G['NCHAN']):
    cscode = G['CRNUMB'] + 256*slot
    print '{',
    print '"%.2d"'%(G['CRNUMB']),
    print '"%s",'%(G['CRNAME']),
    print '"%s",'%(G['CRTYPE']),
    print '"%.2d"'%(slot),
    print '"%.2d"'%(chan),
    print '"%s"'%(G['SYS']),
    print '"%s"'%(G['DET']),
    print '"%s_Sl%.2d_Ch%.2d"'%(G['ELSTUB'],slot,chan),
    print '"#C%d"'%(cscode),
    print '"S%d"'%(G['pwonoff']*256+slot),
    print '"S%d"'%(G['v0set']*256+slot),
    print '"S%d"'%(G['i0set']*256+slot),
    print '"S%d"'%(G['trip']*256+slot),
    print '"S%d"'%(G['rampup']*256+slot),
    print '"S%d"'%(G['rampdn']*256+slot),
    print '"S%d"'%(G['svmax']*256+slot),
    print '"S%d"'%(G['enable']*256+slot),
    print '}'

