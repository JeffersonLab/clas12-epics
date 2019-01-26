#! /usr/bin/env python3

# Brian Eng, April 2018
# scrapes facilities webserver, pushes to EPICS pvs

import urllib.request
import epics
import time,datetime
from socket import timeout

URL = "https://www.jlab.org/fm/wx/VWS/data/data2.csv"

CFG = {
'B_SYS_WEATHER_OUT_Temp': {'col': 13},
'B_SYS_WEATHER_OUT_Humid': {'col': 11},
'B_SYS_WEATHER_OUT_Press': {'col': 14},
'B_SYS_WEATHER_OUT_Dewpoint': {'col': 31},
'B_SYS_WEATHER_OUT_Wind': {'col': 7},
'B_SYS_WEATHER_OUT_WindGust': {'col': 8},
'B_SYS_WEATHER_OUT_WindChill': {'col': 28}
}

CONSECERR=0
LASTUPDATE='Never'

# Initalize PVs
for pvName in CFG.keys():
  CFG[pvName]['pv'] = epics.pv.PV(pvName)

while True:

  error=False
  now=str(datetime.datetime.now())

  try:
    resp = urllib.request.urlopen(URL, timeout=5)
  except Exception as e:
    print(now+" Failed to get FM WX Webpage: "+str(e))
    error=True

  # Only parse response if it was OK 
  if resp.getcode() != 200:
    print(now+" Error from server")
    error=True

  else:
    data = resp.read().decode('utf-8').split(',')

    for pvName in CFG.keys():
      # Make sure conversion to float is okay
      try:
        val = float(data[CFG[pvName]['col']])
        CFG[pvName]['pv'].put(val)
      except ValueError as e:
        print(now+' ValueError on ',pvName)
        error=True
        pass
      except IndexError as e:
        print(now+' IndexError on ',pvName)
        error=True
        pass

  if error:
    CONSECERR += 1
  else:
    CONSECERR = 0
    LASTUPDATE = now

  if CONSECERR>30:
    print ('ERROR:  Last Update: '+LASTUPDATE)
    time.sleep(20)


  time.sleep(10)

