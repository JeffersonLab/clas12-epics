#!/usr/bin/env python
#
# Check if PV(s) are currently being archived
#
# Author: Wesley Moore (wmoore@jlab.org)
# Date:   June 2016
#

import sys
import glob
import os
import subprocess

files = []
not_archived = []

if len(sys.argv) < 2:
    files = glob.glob("./*.txt")
    files += glob.glob("./*.list")
else:
    for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            files.append(arg)
        elif os.path.isdir(arg):
            if not arg.endswith('/'):
                arg += '/'
            arg += "*.txt"
            files = glob.glob(arg)
        else:
            print "Warning: " + arg + " not found"

if len(files) == 0:
    print "No files to be processed"
    exit(0)

print "Processing files:"
files.sort(key=str.lower)

for file in files:
    if os.stat(file).st_size == 0:
        print "Warning: empty file, skipping " + file
        continue

    print "  " + file
    pvlist = open(file, 'r')
    for pv in pvlist:
        pv = pv.split(' ', 1)[0]
        pv = pv.split('\n',1)[0]
        if pv != "":
            p = subprocess.check_output(["archive", pv])
            if "not archived" in p:
                not_archived.append(pv)

if len(not_archived) == 0:
    print "All PVs are archived"
    exit(0)
else:
    print "PVs not archived:"
    not_archived.sort()
    print '\n'.join(not_archived)
    exit(1)

