#!/bin/python
#Create a dictionary of names, and lists to describe the nodes
#This is already generated as NodesDict.py - it's very big file.
#import NodesDict works fine in python, but in jython it hits a 64k limit for the size of the imported module
#Hence, a jython script (eg in CSS GUI) needs to load it like this - by parsing the lines from NodesDict.py and
#filling the dics and lists that way.
#Ken Livingston Nov 2015

import os
epics = os.environ['EPICS_SCRIPTS']

#If the structure of NodesDict.py changes, this needs to change too


#Dicts and lists 
NodeIndex              = {}
SubNodeNames           = []
ElementNames           = []
ElementRecordNames     = []
ElementRecordTypes     = []
ElementRecordFlags     = []
NodeRecordNames        = []
NodeRecordTypes        = []
ElementRange           = []

def readTree():
    #Fill the dictionaries.
    recList = {}                    #make a dict with names of the lists, and fill from lines
    recList['SubNodeNames']       = SubNodeNames
    recList['ElementNames']       = ElementNames
    recList['ElementRecordNames'] = ElementRecordNames
    recList['ElementRecordTypes'] = ElementRecordTypes
    recList['ElementRecordFlags'] = ElementRecordFlags
    recList['NodeRecordNames']    = NodeRecordNames
    recList['NodeRecordTypes']    = NodeRecordTypes
    recList['ElementRange']       = ElementRange
    
    
    if len(SubNodeNames) < 2:                  #if not already populated
        #f = open('/home/clasrun/CSS-Workspaces/.shared/HV2/NodesDict.py', 'rt')     #open the NodeDict.py file
        nodesdict=epics+"/NodesDict.py"   #ultimately should go here
        f = open(nodesdict, 'rt')     #open the NodeDict.py file
        for line in f:                             #go over all lines
            if "NodeIndex['" in line:                 #if this kind of line: "NodeIndex['BSIM'] = 666" 
                node = line.split("'")[1]             #get the string from beteen the ''
                ind = line.split()[2]                 #get the index
                #print node, ind
                NodeIndex[node] = ind                 #fill the dictionary
                
            elif "append" in line:                    #This kind of line: ElementNames.append('HVDC1,HV,HVDC2,.....')
                l = line.split(".")[0]                    #get the listname
                val = line.split('(', 1)[1].split(')')[0] #get the value from inside the ''
                recList[l].append(val)                    #append it to the relevant list
    return

def main():
    readTree()
if __name__ == "__main__": main()  # call main comes at the end: a quirk of python
