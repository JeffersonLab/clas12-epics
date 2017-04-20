#!/usr/bin/env python
import re,sys

nchan,region,sector,slot=1,None,None,None

for xx in open('lv-channels.opi','r').readlines():
  xx=xx.strip()
  if xx.find('<L>')>=0:
    mm = re.search('.*R(\d+)S(\d+)(.)',xx)
    if mm==None: sys.exit('WHAT?')

    if region == int(mm.group(1)):
      nchan += 1
    else:
      region = int(mm.group(1))
      nchan = 0

    sector = int(mm.group(2))
    topbot = mm.group(3)

    slot = nchan/4+1

    if region==4 and sector>12:
      slot -= 6

    print '%s  R%dS%d%s_Slot%d'%(xx,region,sector,topbot,slot)

  if xx.find('<SL>')>=0:
    print '<SL>'+str(slot)+'</SL>'

  else:
    print xx

