#!/usr/bin/env python

nTiles=138

prefix='B_DET_RICH_SSP'

lnks=['1','2','3','4','5','6','7','8','9','A']

nLinks=0
nRecords=0

print 'record(ai,"%s:$(R):$(L)") {'%(prefix)
print '\tfield(FLNK,"%s:$(R):$(L)seq0.PROC")'%(prefix)
print '}'

for iTile in range(1,nTiles+1):

  if nLinks==0:
    print 'record(seq,"%s:$(R):$(L)seq%d") {'%(prefix,nRecords)

  print '\tfield(LNK%s,"%s_TILE%.3d:$(R).$(L) CPP")'%(lnks[nLinks],prefix,iTile)
  print '\tfield(DOL%s,"%s:$(R):$(L)")'%(lnks[nLinks],prefix)

  nLinks+=1

  if nLinks==10:
    nRecords+=1
    nLinks=0
    print '\tfield(FLNK,"%s:$(R):$(L)seq%d.PROC")'%(prefix,nRecords)
    print '}'


