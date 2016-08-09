#!/usr/bin/env python
import sys,os,stat,re

# N.Baltzell
#
# TODO: mkChannels* --> read from ccdb (?)
#

DBFILE='db/jscaler_channel.db'
KEYS=['CrNo','CrName','Sl','Ch','Det','Sys','Element','CScode','Thresh','Mode','Counts']



FTOF_SLOT_F2D={
    3:2,
    4:4,
    5:5,
    6:7,
    7:8,
    8:10,
    9:12,
    10:14,
    13:15,
    14:17,
    15:18,
    16:20
}
ECAL_SLOT_F2D={
    3:3,
    4:4,
    5:5,
    6:7,
    7:8,
    8:9,
    9:10,
    10:12,
    13:13,
    14:14,
    15:15,
    16:17,
    17:18,
    18:20,
    19:21,
    20:22
}
PCAL_SLOT_F2D={
    3:2,
    4:3,
    5:4,
    6:5,
    7:7,
    8:8,
    9:9,
    10:10,
    13:12,
    14:13,
    15:14,
    16:15
}
SLOT_F2D={'FTOF':FTOF_SLOT_F2D,
          'PCAL':PCAL_SLOT_F2D,
          'ECAL':ECAL_SLOT_F2D,
          'LTCC':ECAL_SLOT_F2D}

STARTUP='''#!../../bin/linux-x86_64/iocscalers
< envPaths
cd ${TOP}

Init_SCALERS()

STARTCRATE

## Register all support components
dbLoadDatabase("dbd/iocscalers.dbd")
iocscalers_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")

LOADRECORDS

cd ${TOP}/iocBoot/${IOC}

iocInit
'''


def printSubstitutions(channels,fileName=None):
  if fileName!=None: file=open(fileName,'w')
  else:              file=sys.stdout
  print >>file, 'file "'+DBFILE+'" {'
  print >>file, 'pattern {',','.join(KEYS),'}'
  for cc in channels:
    row=','.join(KEYS)
    for kk in KEYS: row=row.replace(kk,'"%s"'%(cc[kk]))
    print >>file, '{',row,'}'
  print >>file, '}'

def printStartup(crates,fileName=None):
  if fileName!=None: file=open(fileName,'w')
  else:              file=sys.stdout
  startCrates,loadRecords='',''
  for crate in crates:

    if startCrates.find(crate['CrName'])<0:
      startCrates += 'Start_SCALERS_CRATE("%d","%s")\n'%(int(crate['CrNo']),crate['CrName'])

    for subFileName in crate['subFileName']:
      subFileName=re.sub('.*/','',subFileName)
      loadRecords += 'dbLoadTemplate("db/%s")\n'%(subFileName)

    #subFileName=re.sub('.*/','',crate['subFileName'])
    #loadRecords += 'dbLoadTemplate("db/%s")\n'%(subFileName)

  contents= STARTUP.replace('STARTCRATE',startCrates)
  contents=contents.replace('LOADRECORDS',loadRecords)
  print >>file,contents
  if fileName!=None:
    file.close()
    # add execute permissions to startups:
    st=os.stat(fileName)
    os.chmod(fileName,st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

def setCodes(crateNumber,channel):
  channel['CrNo']='%.2d'%(crateNumber)
  channel['CScode']=int(channel['CrNo'])+(int(channel['Sl'])<<8)
  channel['Thresh']=int(channel['Ch'])+(0<<8)
  channel['Counts']=int(channel['Ch'])+(0<<8)
  channel['Mode']  =int(channel['Ch'])+(1<<8)

def mkChannelsECAL(crateNumber,sector,system):
  if system=='FADC': crate='ADCECAL'+str(sector)
  else:              crate='TDCECAL'+str(sector)
  layers=['UI','VI','WI','UO','VO','WO']
  nPerLayer,iChan,channels=36,0,[]
  for slot in [3,4,5,6,7,8,9,10,13,14,15,16,17,18]:
    if system!='FADC': slot=SLOT_F2D['ECAL'][slot]
    for chan in range(16):
      if slot==9 and chan>11: break
      if iChan%nPerLayer==0:
        if len(layers)==0: break
        else:              layer=layers.pop(0)
      channel={'Sl':'%.2d'%(slot),'Ch':'%.2d'%(chan),'Layer':layer,'CrName':crate,'Det':'ECAL','Sys':system}
      channel['Element']='SEC%d_%s_E%.2d'%(sector,layer,iChan%nPerLayer+1)
      setCodes(crateNumber,channel)
      channels.append(channel)
      iChan += 1
  return channels

def mkChannelsPCAL(crateNumber,sector,system):
  if system=='FADC': crate='ADCPCAL'+str(sector)
  else:              crate='TDCPCAL'+str(sector)
  layers=['U','V','W']
  nPerLayers={'U':68,'V':62,'W':62}
  iChan,channels=0,[]
  for slot in [3,4,5,6,7,8,9,10,13,14,15,16]:
    if system!='FADC': slot=SLOT_F2D['PCAL'][slot]
    for chan in range(16):
      if iChan==0 or iChan%nPerLayers[layer]==0:
        iChan=0
        if len(layers)==0: break
        else:              layer=layers.pop(0)
      channel={'Sl':'%.2d'%(slot),'Ch':'%.2d'%(chan),'Layer':layer,'CrName':crate,'Det':'PCAL','Sys':system}
      channel['Element']='SEC%d_%s_E%.2d'%(sector,layer,iChan%nPerLayers[layer]+1)
      setCodes(crateNumber,channel)
      channels.append(channel)
      iChan += 1
  return channels

def mkChannelsLTCC(crateNumber,sector,system):
  if system=='FADC': crate='ADCECAL'+str(sector)
  else:              crate='TDCECAL'+str(sector)
  sides=['L','R']
  nChanPerSide=18
  # LTCC FADC starts in slot 18, channel 12 (after last ECAL channel)
  fadcSlot,hwChan=18,12
  channels=[]
  for side in sides:
    for detChan in range(1,nChanPerSide+1):
        if hwChan>=16:
          hwChan=0
          fadcSlot+=1
        hwSlot=fadcSlot
        if system!='FADC': hwSlot=SLOT_F2D['ECAL'][hwSlot]
        channel={'Sl':'%.2d'%(hwSlot),'Ch':'%.2d'%(hwChan),'Side':side,'CrName':crate,'Det':'LTCC','Sys':system}
        channel['Element']='SEC%d_%s%.2d'%(sector,side,detChan)
        setCodes(crateNumber,channel)
        channels.append(channel)
        hwChan+=1
  return channels

def mkChannelsFTOF(crateNumber,sector,system):
  if system=='FADC': crate='ADCFTOF'+str(sector)
  else:              crate='TDCFTOF'+str(sector)
  _layers={2:'1A',1:'1B',3:'2'}
  _lrs={1:'L',2:'R'}
  layers=[
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
  2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
  2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 0, 3, 0,
  2, 2, 2, 2, 2, 0, 2, 0, 3, 3, 3, 3, 0, 0, 0, 0,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
  ]
  slabs=[
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  1, 3, 1, 3, 5, 7, 5, 7, 9,11, 9,11,13,15,13,15,
  2, 4, 2, 4, 6, 8, 6, 8,10,12,10,12,14,16,14,16,
 17,19,17,19,21,23,21,23, 1, 3, 1, 3, 5, 0, 5, 0,
 18,20,18,20,22, 0,22, 0, 2, 4, 2, 4, 0, 0, 0, 0,
  1, 3, 1, 3, 5, 7, 5, 7, 9,11, 9,11,13,15,13,15,
  2, 4, 2, 4, 6, 8, 6, 8,10,12,10,12,14,16,14,16,
 17,19,17,19,21,23,21,23,25,27,25,27,29,31,29,31,
 18,20,18,20,22,24,22,24,26,28,26,28,30,32,30,32,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 33,35,33,35,37,39,37,39,41,43,41,43,45,47,45,47,
 34,36,34,36,38,40,38,40,42,44,42,44,46,48,46,48,
 49,51,49,51,53,55,53,55,57,59,57,59,61, 0,61, 0,
 50,52,50,52,54,56,54,56,58,60,58,60,62, 0,62, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
  ]
  lrs=[
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2,
  1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2,
  1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 0, 2, 0,
  1, 1, 2, 2, 1, 0, 2, 0, 1, 1, 2, 2, 0, 0, 0, 0,
  1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2,
  1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2,
  1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2,
  1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2,
  1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2,
  1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 0, 2, 0,
  1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 0, 2, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
  ]
  channels=[]
  for ii in range(17*16):
    if layers[ii]==0: continue
    slot=ii/16
    if system!='FADC': slot=SLOT_F2D['FTOF'][slot]
    channel={'Sl':'%.2d'%(slot),'Ch':'%.2d'%(ii%16),'CrName':crate,'Det':'FTOF','Sys':system}
    channel['Element']='SEC%d_PANEL%s_%s_E%.2d'%(
        sector,_layers[layers[ii]],_lrs[lrs[ii]],slabs[ii])
    setCodes(crateNumber,channel)
    channels.append(channel)
  return channels

def mkCrates(channels,subfileName):
  crates=[]
  for channel in channels:
    oldCrate=None
    for crate in crates:
      if crate['CrName']==channel['CrName']:
        oldCrate=crate
        break
    if oldCrate==None:
      crate={}
      crate['Det']=channel['Det']
      crate['CrNo']=channel['CrNo']
      crate['CrName']=channel['CrName']
      crate['subFileName']=[subfileName]
      crates.append(crate)
    else:
      if subfileName not in oldCrate['subFileName']:
        oldCrate['subFileName'].append(subfileName)
  return crates

def mkChannels(detector,crateNumber,sector,system):
  if   detector=='ECAL': return mkChannelsECAL(crateNumber,sector,system)
  elif detector=='PCAL': return mkChannelsPCAL(crateNumber,sector,system)
  elif detector=='FTOF': return mkChannelsFTOF(crateNumber,sector,system)
  elif detector=='LTCC': return mkChannelsLTCC(crateNumber,sector,system)
  else: sys.exit('Invalid detector:  ',detector)

def printTriggerSubs(sector,CrNo,CrName):
  if CrName.find('FTOF')<0 and CrName.find('PCAL')<0: return
  channels=[]
  if CrName.find('FTOF')>=0:
    cc={'Sl':'20','Ch':'15','Det':'TRIG','Sys':'DISC','CrName':CrName,'CrNo':CrNo}
    cc['Element']='SEC%d_F%.2d'%(sector,15)
    setCodes(CrNo,cc)
    channels.append(cc)
  elif CrName.find('PCAL')>=0:
    for ch in range(16):
      cc={'Sl':'18','Ch':'%.2d'%(ch),'Det':'TRIG','Sys':'DISC','CrName':CrName,'CrNo':CrNo}
      cc['Element']='SEC%d_P%.2d'%(sector,ch)
      setCodes(CrNo,cc)
      channels.append(cc)
  subFileName='../Db/jscalers_%s_TRIG.sub'%(CrName)
  printSubstitutions(channels,subFileName)

# make substution files and one startup per sector:
def mkSector(sector):
  iCrate,crates=0,[]
  for system in ['FADC','DISC']:
    for detector in ['ECAL','LTCC','PCAL','FTOF']:
      if detector=='LTCC': iCrate-=1 # <--- HACK
      channels=mkChannels(detector,iCrate,sector,system)
      subFileName='../Db/jscalers_S%d_%s_%s.sub'%(sector,detector,system)
      printSubstitutions(channels,subFileName)
      if system=='DISC' and (detector=='PCAL' or detector=='FTOF'):
        printTriggerSubs(sector,iCrate,'TDC'+detector+str(sector))
      crates.extend(mkCrates(channels,subFileName))
      iCrate += 1

  printStartup(crates,'jscalers_S%d.cmd'%(sector))


for sector in range(6): mkSector(sector+1)


