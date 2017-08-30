#!/usr/bin/env python
import re,sys

#
# Read Denis's spreasheet, produce EPICS records
# and modbus ports for c370 PLC, for booleans ONLY.
#
# N. Baltzell
#

# input table, converted from Denis's spreadsheet:
csvFile='Saclaytgt_modbus_registers.csv'

# known descriptions:
descriptions={
    'LS_TB':     '"Low Level in Target Alarm"',
    'LS_TH':     '"High Level in Target Alarm"',
    'AL_NIV_C_L':'"Target Level Sensor Alarm"',
    'AL_VIDE':   '"Vacuum Chamber Alarm"',
    'ALARMEH2D2':'"H2/D2 Detection Alarm"',
    'AL_NIV_C_P':'"Target Pressure Alarm"',
    'CI_VIDEHE4':'"Target Empty He4"',
    'CI_VIDE_HD':'"Target Empty H2/D2"',
    'BET1909':   '"Target Empty He3"',
    'AL_STOCK':  '"H2/D2 Storage Alarm"',
    'AL_SALLE':  '"Control Room Alarm"',
    'H2':'"H2 Target"',
    'D2':'"D2 Target"',
    'HE3':'"HE3 Target"',
    'HE4':' "HE4 Target"',

}

# printing patterns for uniform output:
prtPattern='drvModbusAsynConfigure("C370x%x","ETH1",1, 1, 0x%x, %3d, 0, 2000, "C370")'
subPattern='{%10s, %12s, %12s, %5s, %10s, %10s, %7s, %7s, %s }'

# keep track of per-port stuff:
offsets=[]
variableGroup=None
baseAddress=None
maxOffset=0

# count internals:
nInternal=0

# accumulate list of all port startups: 
portStartups=[]

# print template header:
print 'file "db/c370bi.template" { pattern'
print subPattern%('P','R','PORT','OFFSET','ZSV','OSV','ZNAM','ONAM','DESC')

# loop over all lines in Denis's spreadsheet:
for line in open(csvFile,'r').readlines():

  line=line.strip()
  cols=line.split(',')

  # ignore the first group of internals (they're analogs):
  if line.find('Internal Variable')>=0: nInternal+=1

  # check for relevant setion headers:
  if line.find('Logic Input Card')>=0 or \
     line.find('Logic Output Card')>=0 or \
     line.find('Bit for regulated valves')>=0 or \
     line.find('Bit for valves')>=0 or \
     (line.find('Internal Variable')>=0 and nInternal>1):
    # we found a good group   
    # set group name:
    variableGroup=line.replace(',','')
    # print seperator, just comments:
    print
    for ii in range(50): print '#',
    print '\n#### '+variableGroup
    continue

  # "libre" means free, i.e. unused, ignore:
  elif line.find('Libre')>=0: continue

  # previous group is done:
  elif line.find(',,,,')>=0:
    # close this port:
    if variableGroup and baseAddress:
      portStartups.append(prtPattern%(baseAddress,baseAddress,maxOffset+1))
    # prepare for a new port:
    variableGroup,baseAddress=None,None
    offsets=[]
    maxOffset=0

  # no relevant section header found yet, ignore this line:
  if not variableGroup: continue

  # update base address:
  if not baseAddress: baseAddress=int(cols[10])

  # get the column values:
  name=cols[1]
  address=int(cols[10])
  offset=address-baseAddress

  # switch ports:
  if True and offset>63:
    # close old port:
    portStartups.append(prtPattern%(baseAddress,baseAddress,maxOffset+1))
    # make new port:
    baseAddress=baseAddress+offset
    offset=0
    maxOffset=offset
    offsets=[0]

  # keep track of offsets:
  if offset>maxOffset: maxOffset=offset
  offsets.append(offset)

  # set defults on new record:
  port='C370x%x'%(baseAddress)
  prefix='B_SACLAYTGT:'
  zsv,osv='NO_ALARM','NO_ALARM'
  znam,onam='ZERO','ONE'
  desc='"DESC"'

  # override defaults on new record: 
  if variableGroup.find('valve')>=0: znam,onam='CLOSED','OPEN'
  if name.find('FV')==0: znam,onam='OPEN','CLOSED'
  if name.find('AL')==0: osv='MAJOR'
  if name=='LS_TB': osv='MAJOR'
  if name=='LS_TH': osv='MAJOR'
  if name in descriptions.keys(): desc=descriptions[name]

  # print record
  print subPattern%(prefix,name,port,str(offset),zsv,osv,znam,onam,desc)

# close remaining port:
if variableGroup and baseAddress:
  portStartups.append(prtPattern%(baseAddress,baseAddress,maxOffset+1))

# print template footer:
print '}\n'

# print port startups:
for xx in portStartups: print xx

