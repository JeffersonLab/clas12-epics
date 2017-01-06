#!/usr/bin/env python

hosts={
'dc11-crate' : '129.57.68.184',
'dc12-crate' : '129.57.68.179',
'dc13-crate' : '129.57.68.181',
'dc21-crate' : '129.57.68.183',
'dc22-crate' : '129.57.68.178',
'dc23-crate' : '129.57.68.168',
'dc31-crate' : '129.57.68.169',
'dc32-crate' : '129.57.68.175',
'dc33-crate' : '129.57.68.172',
'dc41-crate' : '129.57.68.170',
'dc42-crate' : '129.57.68.176',
'dc43-crate' : '129.57.68.173',
'dc51-crate' : '129.57.68.171',
'dc52-crate' : '129.57.68.177',
'dc53-crate' : '129.57.68.174',
'dc61-crate' : '129.57.68.185',
'dc62-crate' : '129.57.68.180',
'dc63-crate' : '129.57.68.182'
}

dbload='''
dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=${host},IP=${ip}")
dbLoadRecords("db/wienerW.db","HOST=${host},IP=${ip}")
dbLoadRecords("db/vmePedestals.db","HOST=${host},IP=${ip},VXS_FLAG=1")
'''

for host in sorted(hosts.keys()):
  yy=dbload
  yy=yy.replace('${host}',host.replace('-crate',''))
  yy=yy.replace('${ip}',hosts[host])
  print yy

