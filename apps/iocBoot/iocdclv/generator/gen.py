#!/usr/bin/env python
import os

iocBootDir='../../'

outDirStub='./output/iocdclv_'
#outDirStub=iocBootDir+'iocdclv_'

templateFile='./st-template.cmd'
templateFileS='../st-generic.cmd'
mappingFile='./mapping.txt'

template=open(templateFile,'r').readlines()
templateS=open(templateFileS,'r').readlines()

mapping={}
for line in open(mappingFile,'r').readlines():
  [sr,host]=line.strip().split()
  mapping[sr]=host

for ss in range(1,7):

  outDir=outDirStub+'S'+str(ss)
  if not os.path.exists(outDir): os.makedirs(outDir)
  outFileS=open(outDir+'/st.cmd','w')

  addr=1
  dogs=list(templateS)
  while True:
    if dogs[0].find('drvAsynIPPortConfigure')==0: break
    xx=dogs.pop(0)
    outFileS.write(xx)

  for rr in range(1,4):

    sr='S%dR%d'%(ss,rr)
    host=mapping[sr]

    outDir=outDirStub+sr
    outFile=outDir+'/st.cmd'
    if not os.path.exists(outDir): os.makedirs(outDir)

    outFileSR=open(outFile,'w')

    for xx in template:
      xx=xx.replace('xxxGPIBHOSTxxx',host)
      xx=xx.replace('xxxSECTORxxx',str(ss))
      xx=xx.replace('xxxREGIONxxx',str(rr))
      xx=xx.replace('xxxADDRxxx','1')
      outFileSR.write(xx)

    for xx in dogs:
      if xx.find('drvAsynIPPortConfigure')==0 or \
         xx.find('dbLoadRecords("db/A6551.db')==0:
        xx=xx.replace('${PORT}',sr)
        xx=xx.replace('${GPIB}',host)
        xx=xx.replace('${SCAN}','2 seconds')
        xx=xx.replace('${SECREG}','SEC%d_R%d'%(ss,rr))
        xx=xx.replace('${ADDR}',str(addr))
        outFileS.write(xx)

        print host,addr

    #addr+=1

    outFileSR.close()

  for xx in dogs: outFileS.write(xx)
  outFileS.close()


