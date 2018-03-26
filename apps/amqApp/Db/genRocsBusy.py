#!/usr/bin/env python
import os,sys

crates=[]
for xx in open(os.getenv('CLON_PARMS')+'/portnames.txt','r').readlines():
  columns=xx.split()
  crates.append(columns[2])


subArray='''
record(subArray,"B_DAQ:ROCS_BUSY:sa%d") {
    field(INP,"B_DAQ:ROCS_BUSY CPP")
    field(FTVL,"DOUBLE")
    field(MALM,"72")
    field(NELM,"1")
    field(INDX,"%d")
    field(EGU,"%%")
    field(FLNK,"B_DAQ:ROCS_BUSY:sa%d.PROC")
}'''

aiRecord='''
record(ai,"B_DAQ:ROCS_BUSY:%d") {
    field(INP,"B_DAQ:ROCS_BUSY:sa%d")
    field(FLNK,"B_DAQ:ROCS_BUSY:%d.PROC")
    field(DESC,"%s")
    alias("%s")
}'''

for ii in range(72):
  print subArray%(ii,ii,ii+1)

for ii in range(72):
  alias='B_DAQ:ROCS_BUSY:'+crates[ii]
  print aiRecord%(ii,ii,ii+1,crates[ii],alias)

