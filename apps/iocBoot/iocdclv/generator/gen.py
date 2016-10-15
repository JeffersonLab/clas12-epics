#!/usr/bin/env python
import os

templateFile='./st-template.cmd'
mappingFile='./mapping.txt'

template=open(templateFile,'r').readlines()

mapping={}
for line in open(mappingFile,'r').readlines():
  [sr,host]=line.strip().split()
  mapping[sr]=host

for ss in range(1,7):
  for rr in range(1,4):
    sr='S%dR%d'%(ss,rr)
    host=mapping[sr]
    outDir='../../iocdclv_'+sr
    outFile=outDir+'/st.cmd'
    if not os.path.exists(outDir): os.makedirs(outDir)
    if os.path.exists(outFile):
      print 'File already exists:  '+outFile
      continue
    outFile=open(outFile,'w')
    for xx in template:
      xx=xx.replace('xxxGPIBHOSTxxx',host)
      xx=xx.replace('xxxSECTORxxx',str(ss))
      xx=xx.replace('xxxREGIONxxx',str(rr))
      outFile.write(xx)
    outFile.close()

