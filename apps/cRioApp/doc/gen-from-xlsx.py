#!/usr/bin/env python
import openpyxl

wb = openpyxl.load_workbook('LTCC Purifier PVs.xlsx')
ws = wb['New PVs']

def getBi(name,ZNAM=None,ONAM=None,ZSV=None,OSV=None,DESC=None):
  bi = 'record(bi,"'+name+'") {\n'
  if ZNAM is not None: bi += '    field(ZNAM,"'+ZNAM+'")\n'
  if ONAM is not None: bi += '    field(ONAM,"'+ONAM+'")\n'
  if ZSV  is not None: bi += '    field(ZSV,"'+ZSV+'")\n'
  if OSV  is not None: bi += '    field(OSV,"'+OSV+'")\n'
  if DESC is not None: bi += '    field(DESC,"'+DESC+'")\n'
  bi += '    info(autosaveFields_pass0,"OSV ZSV")\n'
  bi += '}\n\n'
  return bi

def getMbbi(name,ZRST=None,ONST=None,TWST=None,THST=None,FRST=None,FVST=None,DESC=None):
  mbbi = 'record(mbbi,"'+name+'") {\n'
  if ZRST is not None: mbbi += '    field(ZRST,"'+ZRST+'")\n'
  if ONST is not None: mbbi += '    field(ONST,"'+ONST+'")\n'
  if TWST is not None: mbbi += '    field(TWST,"'+TWST+'")\n'
  if THST is not None: mbbi += '    field(THST,"'+THST+'")\n'
  if FRST is not None: mbbi += '    field(FRST,"'+FRST+'")\n'
  if FVST is not None: mbbi += '    field(FVST,"'+FVST+'")\n'
  if DESC is not None: mbbi += '    field(DESC,"'+DESC+'")\n'
  mbbi += '    info(autosaveFields_pass0,"ZRSV ONSV TWSV THSV FRSV FVSV")\n'
  mbbi += '}\n\n'
  return mbbi

def getAi(name,EGU=None,DESC=None):
  ai = 'record(ai,"'+name+'") {\n'
  if EGU is not None: ai += '    field(EGU,"'+EGU+'")\n'
  ai += '    info(autosaveFields_pass0,"HIGH HIHI LOW LOLO HSV HHSV LSV LLSV")\n'
  ai += '}\n\n'
  return ai

def getAo(name,EGU=None,DESC=None):
  return getAi(name,EGU).replace('record(ai','record(ao')

pvs=[]

for row in ws.iter_rows():

  name,dataType,deadband,egu,notes = [name.value for name in row[0:5]]
  if name is None: continue
  if name == 'Name': continue

  pv={'name':name,'deadband':deadband}

  if dataType.lower() == 'boolean':
    ZNAM,ONAM,OSV = None,None,None
    if notes.find('1 = valve open')>=0:
      ZNAM,ONAM = 'Closed','Open'
    elif notes.find('1 = pump on')>=0:
      ZNAM,ONAM = 'Off','On'
    elif notes.find('1 = fault')>=0:
      ZNAM,ONAM,OSV = 'No Fault','Fault','MAJOR'
    elif notes.find('1 = manual override enabled')>=0:
      ZNAM,ONAM = 'Disabled','Enabled'
    pv['record'] = getBi(name,ZNAM=ZNAM,ONAM=ONAM,OSV=OSV)

  elif dataType.lower() == 'enum':
    ZRST,TWST,THST,FRST,FVST=None,None,None,None,None
    if notes.find(', 2 = ')>0:
      states = notes.strip().split(',')
      for state in states:
        val,desc = state.strip().split('=')
        desc = desc.strip().capitalize()
        desc = ' '.join([x.strip().capitalize() for x in desc.split(' ')])
        desc = '/'.join([x.strip().capitalize() for x in desc.split('/')])
        if int(val)==0:
          ZRST=desc
        elif int(val)==1:
          ONST=desc
        elif int(val)==2:
          TWST=desc
        elif int(val)==3:
          THST=desc
        elif int(val)==4:
          FRST=desc
        elif int(val)==5:
          FVST=desc
    pv['record'] = getMbbi(name,ZRST=ZRST,ONST=ONST,TWST=TWST,THST=THST,FRST=FRST,FVST=FVST)

  elif dataType.lower() == 'double':
    EGU,DESC=egu,None
    if name.endswith('_SET'):
      pv['record'] = getAo(name,EGU=EGU,DESC=DESC)
    else:
      pv['record'] = getAi(name,EGU=EGU,DESC=DESC)

  pvs.append(pv)

#for pv in pvs: print pv

  print deadband
  if deadband is None:
    pv['deadband'] = 0
  else:
    pv['deadband'] = float(deadband)

with open('mya.txt','w') as f:
  for pv in pvs:
    if pv['deadband'] is None or float(pv['deadband'])==0:
      f.write('%s 0\n'%(pv['name']))
    else:
      f.write('%s %.5f\n'%(pv['name'],float(pv['deadband'])))

with open('pvs.db','w') as f:
  for pv in pvs:
    f.write(pv['record'])


