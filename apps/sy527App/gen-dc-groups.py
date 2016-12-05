#!/usr/bin/env python

#class group:
#   self.crate=0
#   self.board=0
#   self.sector=0
#   self.region=0
#   self.superlayers=[]
#   self.wiretype=0

groups=[]

for crate in [1]:#,2,3,4]:

  macroDefs={}
  sub='../db/HVDC%d_DC.substitutions'%(crate)

  for row in open(sub,'r').readlines():

    row=row.strip()
    row=row.replace('{','')
    row=row.replace('}','')
    row=row.replace(',','')
    row=row.replace('"','')

    if len(row)<=0: continue
    if row.find('#')==0: continue
    if row.find('file')==0: continue

    if row.find('pattern')==0:
      cols=row.replace('pattern','').split()
      for ii in range(len(cols)):
        macroDefs[ii] = cols[ii]
        macroDefs[cols[ii]] = ii

    else:
      macros={}
      cols = row.split()
      for ii in range(len(cols)):
        macros[macroDefs[ii]] = cols[ii]

      ii = macros['Element'].find('_SEC')
      sector = macros['Element'][ii+4]

      ii = macros['Element'].find('_SL')
      superlayer = macros['Element'][ii+3]

      ii = macros['Element'].find('_R')
      region = macros['Element'][ii+2]

      newGroup = True
      for gg in groups:
        if gg['crate']==crate and gg['Sl']==macros['Sl']:
          newGroup = False
      if newGroup:
        groups.append({'crate':crate,'Sl':macros['Sl']})
        groups[len(groups)-1]['sector']=sector
        groups[len(groups)-1]['region']=region
        groups[len(groups)-1]['superlayers']=superlayer
#        groups[len(groups)-1]['wiretype']=wiretype


  #print crate,macroNames

for gg in groups:
  print gg

