#!/usr/bin/env python

# convert Brian's xlsx file to csv with tab-separator

MAXSTRING=39

def printRecord(name,units,desc):
  desc=desc[0:MAXSTRING]
  if units=='boolean': print 'record(bi,"'+name+'") {'
  else:                print 'record(ai,"'+name+'") {'
  print '\tfield(DESC,"'+desc+'")'
  if units=='boolean':
    print '\tinfo(autosaveFields_pass0,"ZSV OSV")'
  else:
    print '\tfield(EGU,"'+units+'")'
    print '\tinfo(autosaveFields_pass0,"HIHI HIGH LOW LOLO HHSV HSV LSV LLSV")'
  print '}'

for line in open('MVT Gas PVs.csv','r').readlines():
  cols=line.strip().split('\t')
  if len(cols)!=4: continue
  [name,units,deadband,desc]=cols
  desc=desc.replace('"','')
  if len(desc)>MAXSTRING: desc=desc.replace('Calculated','')
  if len(desc)>MAXSTRING: desc=desc.replace('B_DET_MVT_GAS_MIX','')
  if len(desc)>MAXSTRING: desc=desc.replace(' ','')
  if not name.find('B_')==0: continue
  printRecord(name,units,desc)

