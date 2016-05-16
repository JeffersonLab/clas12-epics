#!/usr/bin/env python
#
# Convert CSV to XML for BEAST configuration
#
# Usage:
#   ./csv2beast.py <directory path>
#
# Input format:
#   Line 1: <config name>, <component 0>, <component 1>, <component N>, ...
#   Line 2: column headers (Must start with pv)
#   Line 3: data (Must start with pv name)
#
# Input example:
#   HallB, Torus, Vacuum
#   pv, description, latching, annunciating
#   B_TORUS:FOR:CCM_A:LC817A1, Torus Load Cell, true, true
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
if len(sys.argv) != 2:
    path="./"
else:
    path = sys.argv[1]  # folder
    os.chdir(path)

csvFiles = [f for f in os.listdir('.') if f.endswith('.csv') or f.endswith('.CSV')]
print "Processing files:"
for csvFile in csvFiles:
    print "  " + csvFile
    xmlFile = csvFile[:-4] + '.xml'
    csvData = csv.reader(open(csvFile))
    xmlData = open(xmlFile, 'w')
    xmlData.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
    rowNum = 0
    for row in csvData:
        row = filter(None, row)
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
        if rowNum == 1:
            tags = row

        # fill pv's
        if rowNum > 1:
            vals = row
            for i in range(len(tags)):
                if i == 0:  # pv
                    xmlData.write('\t\t<' + tags[i] + ' name="' + vals[i] + '">\n')
                else:       # elements
                    xmlData.write('\t\t\t<' + tags[i] + '>' + vals[i] + '</' + tags[i] + '>\n')
            xmlData.write('\t\t</' + tags[0] + '>\n')
        rowNum += 1

    # close components and config
    levels.reverse()
    for i in range(len(levels)-1):
        if levels[i] != "":
            xmlData.write('\t</component>\t<!-- ' + levels[i] + ' -->\n')

    xmlData.write('</config>\t<!-- ' + levels[-1] + ' -->\n')
    xmlData.close()
