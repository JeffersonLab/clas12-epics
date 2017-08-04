#!/usr/bin/env python
#
# Lists PVs that are NOT currently being archived.
#
# Usage:
#  check_archive.py [-r] [-d] [file]...
#
#  The -r option instead prints PVs that ARE archived.
#  The -d option instead prints PVs that are disconnected.
#
#  If no files are specified, searches current directory for
#  .txt and .list files.
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
is_archived = []
is_disconnected = []

printMissing = True
printDisconnected = False

clipvs=[]

# Nathan's arguments:
if len(sys.argv)>1:
    if sys.argv[1]=='-r':
        printMissing = False
        sys.argv.pop(1)
    elif sys.argv[1]=='-d':
        printDisconnected = True
        sys.argv.pop(1)


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
            print "Warning: " + arg + " not found, assuming it's a pv"
            clipvs.append(arg)

if len(files) == 0:
    print "No files to be processed"

else:
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

                if printDisconnected:
                    try:
                      fnull=open(os.devnull,'w')
                      subprocess.check_output(['caget','-w','0.2',pv],stderr=fnull)
                    except subprocess.CalledProcessError:
                      is_disconnected.append(pv)

                else:
                    p = subprocess.check_output(["archive", pv])
                    if "not archived" in p:
                        not_archived.append(pv)
                    else:
                        is_archived.append(pv)

for pv in clipvs:
    p = subprocess.check_output(["archive", pv])
    if "not archived" in p:
        not_archived.append(pv)
    else:
        is_archived.append(pv)

if printDisconnected:
    if len(is_disconnected) == 0:
        print "All PVs are connected"
        exit(0)
    else:
        print "PVs are disconnected:"
        print '\n'.join(is_disconnected)
        exit(1)

elif printMissing:
    if len(not_archived) == 0:
        print "All PVs are archived"
        exit(0)
    else:
        print "PVs not archived:"
        not_archived.sort()
        print '\n'.join(not_archived)
        exit(1)
else:
    if len(is_archived) == 0:
        print "No PVs are archived"
        exit(0)
    else:
        print "PVs are archived:"
        is_archived.sort()
        print '\n'.join(is_archived)
        exit(1)


