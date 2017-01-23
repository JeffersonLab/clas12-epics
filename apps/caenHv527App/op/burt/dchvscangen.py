#!/usr/bin/env python

PREFIX='B_DET_DC_HV'
SFWIRES=['01-08','09-16','17-24','25-32','33-48','49-64','65-80','81-112']
GWIRES= ['01-32','33-112']
WIRES={'S':SFWIRES,'F':SFWIRES,'G':GWIRES}
BURTHEADER='''--- Start BURT header
Time:
Login ID:
Eff  UID:
Group ID:
Keywords:
Comments:
Type:
Directory
Req File:
--- End BURT header
'''

SETTINGS=[]

# load table from Mac:
for line in open('dchvscan2.txt','r').readlines():
  if line.find('Region')>=0: continue
  region,setno,total,sense,field,guard=line.strip().split()
  thisset,newset={},True
  for ss in SETTINGS:
    if ss['setno']==setno:
      thisset=ss;
      newset=False
      break
  if newset:
    thisset['S']={}
    thisset['F']={}
    thisset['G']={}
    thisset['setno']=setno
  thisset['S'][region]=sense
  thisset['F'][region]=field
  thisset['G'][region]=guard
  if newset: SETTINGS.append(thisset)

# generate burt snapshots:
for ss in SETTINGS:
  print ss
  ofile=open('HVDC-VSCAN-%.2d.snp'%(int(ss['setno'])),'w')
  ofile.write(BURTHEADER)
  for sec in [1,2,3,4,5,6]:
    for reg in [1,2,3]:
      for lay in range(2*(reg-1)+1,2*(reg-1)+3):
        for sfg in ['S','F','G']:
          for wir in WIRES[sfg]:
            pv=PREFIX+'_SEC%d_R%d_SL%d_%s%s:vset'%(sec,reg,lay,sfg,wir)
            ofile.write(pv+' 1 %.4e\n'%(float(ss[sfg][str(reg)])))


