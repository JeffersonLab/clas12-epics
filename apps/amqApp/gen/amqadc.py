#!/usr/bin/env python
import os

# converting jscaler to amq

def getChannels(fileName,detector):
  data=[]
  with open(fileName,'r') as file:
    for line in file.readlines():
      cols=line.split('"')
      if len(cols)<14: continue
      datum={}
      datum['detector'] = detector
      datum['element'] = cols[13]
      datum['crate'] = cols[3]
      slot = cols[5]
      chan = cols[7]
      while slot[0]=='0' and not slot=='0': slot=slot[1:]
      while chan[0]=='0' and not chan=='0': chan=chan[1:]
      datum['slot'] = int(slot)
      datum['chan'] = int(chan)
      data.append(datum)
  return data

def getChannelAliases(data):
  aliases=[]
  for dd in data:
    alias=dict(dd)
    alias['hw']='B_HW_%s_Sl%.2d_Ch%.2d:q'%(dd['crate'],dd['slot'],dd['chan'])
    alias['det']='B_DET_%s_FADC_%s:q'%(dd['detector'],dd['element'])
    aliases.append(alias)
  return aliases

def getAmqAliases(data):
  aliases=[]
  for dd in data:
    alias={}
    alias['amq']='%s_FADC250SLOT%d_Q'%(dd['crate'],dd['slot'])
    alias['epics']='B_HW_%s_Sl%.2d:q'%(dd['crate'],dd['slot'])
    new=True
    for xx in aliases:
      if xx['amq']==alias['amq'] and xx['epics']==alias['epics']:
        new=False
        break
    if new:
      alias.update(dd)
      aliases.append(alias)
  return aliases

def writeAliases(fileName,aliases):
  with open(fileName,'w+') as file:
    for alias in aliases:
      file.write('alias("%s","%s")\n'%(alias['hw'],alias['det']))

def writeAmqSubs(fileName,aliases):
  with open(fileName,'w+') as file:
    file.write('file "db/amqDoubleArray.db" {\n')
    file.write('pattern {P K N TH THH HSV HHSV}\n')
    for alias in aliases:
      file.write('{ %s %s 16 0 30 NO_ALARM NO_ALARM }\n'%(alias['epics'],alias['amq']))
    file.write('}\n')
    file.write('file "db/array-to-scalar-16.template" {\n')
    file.write('pattern {P R S INP FTVL SCALE PREC}\n')
    template='{ B_HW_%s_ Sl%.2d_Ch :q B_HW_%s_Sl%.2d:q DOUBLE 0.000019 2}\n'
    for alias in aliases:
      file.write(template%(alias['crate'],alias['slot'],alias['crate'],alias['slot']))
    file.write('}\n')

JDIR = os.getenv('EPICS')+'/apps/jscalerApp/Db/subs'

for detector in ['ECAL','PCAL','FTOF','HTCC','LTCC','CTOF','CND']:
  aliases,amqsubs = [],[]
  if detector in ['ECAL','PCAL','FTOF','LTCC']:
    for sector in range(1,7):
      data = getChannels('%s/jscalers_S%d_%s_FADC.substitutions'%(JDIR,sector,detector),detector)
      aliases.extend(getChannelAliases(data))
      amqsubs.extend(getAmqAliases(data))
  else:
    data = getChannels('%s/jscalers_%s_FADC.substitutions'%(JDIR,detector),detector)
    aliases.extend(getChannelAliases(data))
    amqsubs.extend(getAmqAliases(data))
  writeAliases('amq-adc-%s.alias'%detector,aliases)
  writeAmqSubs('amq-adc-%s.substitutions'%detector,amqsubs)

