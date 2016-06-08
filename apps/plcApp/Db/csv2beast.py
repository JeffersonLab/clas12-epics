#!/usr/bin/env python
#
# Convert CSV to XML for BEAST configuration
#
# Usage:
#   csv2beast.py [FILE...] [DIR...]
#
#   Excepts combinations of files and directories.  Output file(s) will be the same as the input, only
#   with xml extension.
#
# Input format:
#   Line 1: <config name>, <component 0>, <component 1>, <component N>, ...
#   Line 2: column headers (Must start with pv)
#   Line 3: data (Must start with pv name)
#
# Input example:
#   HallB, Torus, Vacuum
#   pv, description, latching, annunciating, display title, display details
#   B_TORUS:FOR:CCM_A:LC817A1, Torus Load Cell, true, true, Open Force GUI, /CLAS12_Share/blah-blah
#
# Output example:
#   <?xml version="1.0"?>
#   <config name="HallB">
#	    <component name=" Torus">
#	    <component name=" Vacuum">
#   		<pv name="B_TORUS:FOR:CCM_A:LC817A1">
#   			<description>Torus Load Cell</description>
#   			<latching>true</latching>
#   			<annunciating>true</annunciating>
#               <display>
#                   <title>Open Force GUI</title>
#                   <details</CLAS12_Share/blah-blah</details>
#               </display>
#   		</pv>
#       </component>
#       </component>
#   </config>
#
# Author: Wesley Moore (wmoore@jlab.org)
# Date:   May 2016
#

import sys
import os
import csv

csvFiles = []

if len(sys.argv) < 2:
    csvFiles = [f for f in os.listdir("./") if f.endswith('.csv') or f.endswith('.CSV')]
else:
    for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            csvFiles.append(arg)
        elif os.path.isdir(arg):
            csvFiles = [f for f in os.listdir(arg) if f.endswith('.csv') or f.endswith('.CSV')]
        else:
            print "Warning: " + arg + " not found"

if len(csvFiles) == 0:
    print "No files to be processed"
    exit(0)

print "Processing files:"
for csvFile in csvFiles:
    print "  " + csvFile
    xmlFile = csvFile[:-4] + '.xml'
    csvData = csv.reader(open(csvFile))
    try:
        xmlData = open(xmlFile, 'w')
        xmlData.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
    except IOError:
        print "Write permission denied: " + xmlFile
        exit(1)
    rowNum = 0
    for row in csvData:
        row = map(str.strip, row)
        #print row
        if len(row) == 0:
            break

        # set config and component levels
        if rowNum == 0:
            levels = row

            for i in range(len(levels)):
                if i == 0:
                    xmlData.write('<config name="' + levels[i] + '">\n')
                elif levels[i] != "":
                    xmlData.write('\t<component name="' + levels[i] + '">\n')

        # set tags
        elif rowNum == 1:
            tags = row

        # fill pv's
        elif rowNum > 1:
            vals = row
            i = 0
            while i < len(tags):
                if tags[i] == "pv":
                    xmlData.write('\t\t<' + tags[i] + ' name="' + vals[i] + '">\n')
                elif (' ' in tags[i]):
                    # nested element
                    elem = tags[i].split()
                    top  = elem[0]
                    xmlData.write('\t\t\t<' + elem[0] + '>\n')
                    xmlData.write('\t\t\t\t<' + elem[1] + '>' + vals[i] + '</' + elem[1] + '>\n')
                    j = i+1
                    while j < len(tags):
                        # search until not a sub-element
                        elem = tags[j].split()
                        if elem[0] == top:
                            xmlData.write('\t\t\t\t<' + elem[1] + '>' + vals[j] + '</' + elem[1] + '>\n')
                            j+=1
                        else:
                            break
                    xmlData.write('\t\t\t</' + top + '>\n')
                    i = j-1 # skip to this column
                else:       # pv elements
                    xmlData.write('\t\t\t<' + tags[i] + '>' + vals[i] + '</' + tags[i] + '>\n')
                i+=1
            xmlData.write('\t\t</' + tags[0] + '>\n')
        rowNum += 1

    # close components and config
    levels.reverse()
    for i in range(len(levels)-1):
        if levels[i] != "":
            xmlData.write('\t</component>\t<!-- ' + levels[i] + ' -->\n')

    xmlData.write('</config>\t<!-- ' + levels[-1] + ' -->\n')
    xmlData.close()
