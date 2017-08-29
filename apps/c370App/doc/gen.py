#!/usr/bin/env python
import re,sys

csvFile='Saclaytgt_modbus_registers.csv'

variableGroup=None
baseAddress=None
maxOffset=0

prtPattern='drvModbusAsynConfigure("C370x%x","ETH1",1, 1, 0x%x, %3d, 0, 2000, "C370")'

subPattern='{%10s, %12s, %12s, %5s, %10s, %10s, %7s, %7s, %s }'

print 'file "db/c370bi.template" { pattern'
print subPattern%('P','R','PORT','OFFSET','ZSV','OSV','ZNAM','ONAM','DESC')

portStartups=[]

for line in open(csvFile,'r').readlines():

  line=line.strip()
  cols=line.split(',')

  if line.find('Logic Input Card')>=0 or \
     line.find('Logic Input Card')>=0 or \
     line.find('Bit for regulated valves')>=0 or \
     line.find('Bit for valves')>=0 or \
     line.find('Internal Variable')>=0:
    variableGroup=line.replace(',','')
    print '##################################################################################################'
    print '#### '+variableGroup
    continue
  elif line.find('Libre')>=0: continue
  elif line.find(',,,,')>=0:
    if variableGroup and baseAddress:
      portStartups.append(prtPattern%(baseAddress,baseAddress,maxOffset+1))
    variableGroup,baseAddress=None,None
    maxOffset=0

  if not variableGroup: continue

  if not baseAddress: baseAddress=int(cols[10])

  name=cols[1]
  address=int(cols[10])
  offset=address-baseAddress
  if offset>maxOffset: maxOffset=offset
  port='C370x%x'%(baseAddress)
  prefix='B_SACLAYTGT:'
  zsv,osv='NO_ALARM','NO_ALARM'
  znam,onam='0','1'
  desc='DESC'

  if variableGroup.find('valve')>=0: znam,onam='OPEN','CLOSED'
  if name.find('FV')==0: znam,onam='OPEN','CLOSED'
  if name.find('AL')==0: osv='MAJOR'

  print subPattern%(prefix,name,port,str(offset),zsv,osv,znam,onam,desc)

print '}\n'

for xx in portStartups: print xx

