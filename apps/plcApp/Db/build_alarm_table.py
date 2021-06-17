#!/usr/bin/env python

from argparse import ArgumentParser
import sys
import glob
import os
import csv
from epics import PV

csvFiles = []

if len(sys.argv) < 2:
    csvFiles = glob.glob("./*.[cC][sS][vV]")
else:
    for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            csvFiles.append(arg)
        elif os.path.isdir(arg):
            if not arg.endswith('/'):
                arg += '/'
            arg += "*.[cC][sS][vV]"
            csvFiles = glob.glob(arg)
        else:
            print "Warning: " + arg + " not found"

if len(csvFiles) == 0:
    print "No files to be processed"
    exit(0)

csvFiles.sort(key=str.lower)

csvOut = csv.writer(open("zzz.csv",'w'))
csvOut.writerow([ 'PV Name', 'Description', 'LLSV', 'LOLO', 'LSV', 'LOW', 'HSV', 'HIGH', 'HHSV', 'HIHI', 'ZSV', 'OSV' ])

for csvFile in csvFiles:
    if os.stat(csvFile).st_size == 0:
        print "Warning: empty file, skipping " + csvFile
        continue

    csvData = csv.reader(open(csvFile))

    rowNum = 0
    for row in csvData:
        vals = map(str.strip, row)
        if vals[0].startswith("B_"):
            name = vals[0]
            desc = vals[1]
            pv = PV(name)
            pv.get()
            print name, pv.type, pv.value
            levels = [ 'NO_ALARM', 'MINOR', 'MAJOR', 'INVALID' ]
            if pv.type == 'time_double':
                llsv = levels[PV(name + ".LLSV").get()]
                lolo = PV(name + ".LOLO").get()
                lsv  = levels[PV(name + ".LSV").get()]
                low  = PV(name + ".LOW").get()
                hsv  = levels[PV(name + ".HSV").get()]
                high = PV(name + ".HIGH").get()
                hhsv = levels[PV(name + ".HHSV").get()]
                hihi = PV(name + ".HIHI").get()
                zsv  = ''
                osv  = ''
            elif pv.type == 'time_enum':
                llsv = ''
                lolo = ''
                lsv  = ''
                low  = ''
                hsv  = ''
                high = ''
                hhsv = ''
                hihi = ''
                zsv  = levels[PV(name + ".ZSV").get()]
                osv  = levels[PV(name + ".OSV").get()]
            else:
                print name + ": failed to get PV type"
                exit(1)
            csvOut.writerow([ name, desc, llsv, lolo, lsv, low, hsv, high, hhsv, hihi, zsv, osv ])
        rowNum += 1

