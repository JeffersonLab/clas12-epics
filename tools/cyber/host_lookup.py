#!/usr/bin/env python
#
# Read inventory files and lookup hostnames
#

import sys
import glob
import os
import socket

def lookup(addr):
    try:
        return socket.gethostbyaddr(addr)
    except:
        return None, None, None


filelist = []

if len(sys.argv) < 2:
    print "No input file(s) or directories defined."
else:
    for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            filelist.append(arg)
        elif os.path.isdir(arg):
            if not arg.endswith('/'):
                arg += '/'
            arg += "*.[tT][xX][tT]"
            filelist = glob.glob(arg)
        else:
            print "Warning: " + arg + " not found"

if len(filelist) == 0:
    print "No files to be processed"
    exit(0)

for hostfile in filelist:
    if os.stat(hostfile).st_size == 0:
        #print "Warning: empty file, skipping " + hostfile
        continue

    hosts = open(hostfile, 'r')
    for line in hosts:
        ip = line.strip()
        if not ip.startswith('#') and ip!='' :
            if '/' not in ip:
                print ip, lookup(ip)[0]
            else:
                print ip, "<<< IP RANGE >>>"
                ip_range = ip.split('/')[1]
                if ip_range == 24:
                    for i in 255:
                        print ip, lookup(ip + i)[0]

exit(0)
