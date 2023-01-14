#!/usr/bin/env python3

import re

n = 66

sa = '''record(subArray,"$(P)$(R)%.2d$(S):sa") {
    field(DESC,"$(DESC=)")
    field(INP,"$(INP) CPP")
    field(FTVL,"$(FTVL=DOUBLE)")
    field(MALM,%d)
    field(NELM,1)
    field(INDX,%d)
    alias("$(P)$(R)%d$(S):sa")
    field(FLNK,"$(P)$(R)%.2d$(S):sa.PROC")
}'''

ai = '''record(ai,"$(P)$(R)%.2d$(S)") {
    field(DTYP,"Raw Soft Channel")
    field(ASLO,"$(SCALE=1)")
    field(PREC,"$(PREC=1)")
    field(EGU,"$(EGU=)")
    field(INP,"$(P)$(R)%.2d$(S):sa")
    alias("$(P)$(R)%d$(S)")
    field(FLNK,"$(P)$(R)%.2d$(S).PROC")
}'''

def reflnk(record, flnk):
  m = re.search('(.*)(field\(FLNK,")(.*)("\)\n)(.*)', record, flags=re.DOTALL)
  x = ''.join(m.groups()[0:1])
  if flnk is not None:
    x += 'field(FLNK,"%s")\n' % flnk
  x += m.groups()[4]
  return x

def unalias(record):
  lines = record.split('\n')
  for i,line in enumerate(lines):
    if line.find('alias') >= 0:
      lines.pop(i)
  return '\n'.join(lines)

for i in range(n):
  x = sa % (i,n,i,i,i+1)
  if i == n-1:
    x = reflnk(x, '$(P)$(R)00$(S).PROC')
  if i >= 10:
    x = unalias(x)
  if i > 0:
    x = x.replace(' CPP','')
  print(x)

for i in range(n):
  x = ai % (i,i,i,i+1)
  if i == n-1:
    x = reflnk(x, None)
  if i >= 10:
    x = unalias(x)
  print(x)

