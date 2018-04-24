#! /usr/bin/env python3

# Brian Eng, April 2018
# scrapes facilities webserver, pushes to EPICS pvs

import urllib.request
import epics
import time

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

# Initalize PVs
for pvName in CFG.keys():
  CFG[pvName]['pv'] = epics.pv.PV(pvName)

while True:

  try:
    resp = urllib.request.urlopen(URL)
  except Exception as e:
    print("Failed to get FM WX Webpage")

  # Only parse response if it was OK 
  if resp.getcode() == 200:

    data = resp.read().decode('utf-8').split(',')

    for pvName in CFG.keys():
      # Make sure conversion to float is okay
      try:
        val = float(data[CFG[pvName]['col']])
        CFG[pvName]['pv'].put(val)
      except ValueError as e:
        print('ValueError on ',pvName)
        pass
      except IndexError as e:
        print('IndexError on ',pvName)
        pass

  time.sleep(5)

