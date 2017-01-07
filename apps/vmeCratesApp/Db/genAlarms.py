#!/usr/bin/env python
crates=open('../../iocBoot/iocvmeCrates/vmeCrates.list','r').readlines()
template=open('vmeCrateAlarms.template','r').readlines()

alarm=template.pop().strip()
header=template

opidir='/CLAS12_Share/apps/vmeCratesApp/'

for hh in header: print hh.strip()
for cc in crates:
  if cc.find('dc')==0: opi='vmeCrates_write-DC.opi'
  else:                opi='vmeCrates_write.opi'
  aa=alarm.replace('$(HOST)',cc.strip())
  aa=aa.replace('$(OPI)',opidir+opi)
  print aa

