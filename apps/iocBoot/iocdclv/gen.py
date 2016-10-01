#!/usr/bin/env python
for ss in range(1,7):
  for rr in range(1,4):
    fout=open('stS%dR%da.cmd'%(ss,rr),'w')
    for line in open('st.cmd-template','r').readlines():
      if line.find('S%dR%d'%(ss,rr))>=0:
        #if line.find('db/A6551.db')<0:
        #  line=line.lstrip('#')
        if line.find('db/prologix.db')<0:
          line=line.lstrip('#')
      fout.write(line)
    fout.close()
