#!/usr/bin/env python

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
    outFile=open('st-'+sr+'z.cmd','w')
    for xx in template:
      xx=xx.replace('xxxGPIBHOSTxxx',host)
      xx=xx.replace('xxxSECTORxxx',str(ss))
      xx=xx.replace('xxxREGIONxxx',str(rr))
      outFile.write(xx)
    outFile.close()

#for ss in range(1,7):
#  for rr in range(1,4):
#    fout=open('stS%dR%da.cmd'%(ss,rr),'w')
#    for line in open(template,'r').readlines():
#      if line.find('S%dR%d'%(ss,rr))>=0:
#        #if line.find('db/A6551.db')<0:
#        #  line=line.lstrip('#')
#        if line.find('db/prologix.db')<0:
#          line=line.lstrip('#')
#      fout.write(line)
#    fout.close()

