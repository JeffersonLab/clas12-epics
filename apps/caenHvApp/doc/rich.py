#!/usr/bin/env python

keys=['Cr','CrName','CrType','Sl','Ch','Sys','Det','Element','CScode']

lvkeys=list(keys)
lvkeys.extend(['pwonoff','v0set','i0set','rampup','rampdn','unvt','ovvt'])

hvkeys=list(keys)
hvkeys.extend(['pwonoff','v0set','i0set','trip','rampup','rampdn','svmax','enable'])

base={'Cr':16,'CrName':'"HVRICH1"','CrType':'"4527"'}

hvs=[]
for line in open('rich_HV_Naming.txt','r').readlines():
  line=line.strip()
  if line.find('RICH1')!=0: continue
  crate,slot,chan,name=line.split()
  chan=int(chan)
  slot=int(slot)
  name=name.replace('HVTILE_','')
  hv=dict(base)
  hv['CScode']='"#C0x%X"'%(hv['Cr']+(slot<<8));
  hv['Sl']='"%.2d"'%(slot)
  hv['Ch']='"%.2d"'%(chan)
  hv['Sys']='"HV"'
  hv['Det']='"RICH"'
  hv['Element']='"TILE'+name+'"'
  hv['enable']= '"S0x%X"'%(0x100+chan)
  hv['v0set']=  '"S0x%X"'%(0x200+chan)
  hv['rampdn']= '"S0x%X"'%(0x300+chan)
  hv['rampup']= '"S0x%X"'%(0x400+chan)
  hv['i0set']=  '"S0x%X"'%(0x500+chan)
  hv['trip']=   '"S0x%X"'%(0xA00+chan)
  hv['pwonoff']='"S0x%X"'%(0xB00+chan)
  hv['svmax']=  '"S0x%X"'%(0xD00+chan)
  hvs.append(hv)

lvs=[]
for line in open('rich_LV_Naming.txt','r').readlines():
  line=line.strip()
  if line.find('RICH1')!=0: continue
  crate,slot,chan,name=line.split()
  chan=int(chan)
  slot=int(slot)
  name=name.replace('LVGRP_','')
  lv=dict(base)
  lv['CScode']='"#C0x%X"'%(hv['Cr']+(slot<<8));
  lv['Sl']='"%.2d"'%(slot)
  lv['Ch']='"%.2d"'%(chan)
  lv['Sys']='"LV"'
  lv['Det']='"RICH"'
  lv['Element']='"GRP'+name+'"'
  lv['enable']= '"S0x%X"'%(0x100+chan)
  lv['v0set']=  '"S0x%X"'%(0x200+chan)
  lv['rampdn']= '"S0x%X"'%(0x300+chan)
  lv['rampup']= '"S0x%X"'%(0x400+chan)
  lv['i0set']=  '"S0x%X"'%(0x500+chan)
  lv['pwonoff']='"S0x%X"'%(0xB00+chan)
  lv['unvt']=   '"S0x%X"'%(0x1000+chan)
  lv['ovvt']=   '"S0x%X"'%(0x1100+chan)
  lvs.append(lv)

print 'file "db/caenlv.db" {'
print 'pattern {',
comma=''
for key in lvkeys:
    if key=='Cr' or key=='Sl' or key=='Ch' or key=='Sys':
      print '%s%4s'%(comma,key),
    else:
      print '%s%8s'%(comma,key),
    comma=','
print '}'
for lv in lvs:
  print '        {',
  comma=''
  for key in lvkeys:
    if key=='Cr' or key=='Sl' or key=='Ch' or key=='Sys':
      print '%s%4s'%(comma,lv[key]),
    else:
      print '%s%8s'%(comma,lv[key]),
    comma=','
  print '}'
print '}'

print 'file "db/caenhv.db" {'
print 'pattern {',
comma=''
for key in hvkeys:
    if key=='Cr' or key=='Sl' or key=='Ch' or key=='Sys':
      print '%s%4s'%(comma,key),
    else:
      print '%s%8s'%(comma,key),
    comma=','
print '}'
for hv in hvs:
  print '        {',
  comma=''
  for key in hvkeys:
    if key=='Cr' or key=='Sl' or key=='Ch' or key=='Sys':
      print '%s%4s'%(comma,hv[key]),
    else:
      print '%s%8s'%(comma,hv[key]),
    comma=','
  print '}'
print '}'


