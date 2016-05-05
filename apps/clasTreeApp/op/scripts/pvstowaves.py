#!/bin/python
from NodesDict import *
import doNode
import argparse
from epics import ca, PV
import time
import sys
import numpy
from threading import Thread
from enum import IntEnum


pvdata    = []     #list with all pv info for monitored pvs, with the following 
#                  #each list element contains the following (enumerated) entities: 
pvf       = IntEnum('pvf','TOP NAME PERIOD WF EN ID ARRAY') #Careful - they start at 1,2 ...
mon_line  = 0      #global counter to say which line is current 

pvfull    = []     #full names of pvs for single monitor temporarily

def main():

    parser = argparse.ArgumentParser()        # parser for the inputs - must keep the 2 lines below.
    parser.add_argument("-f", "--setupfile",  help="setup file (default = monitor.dat)",nargs='?', const=0, default="monitor.dat")   
    parser.add_argument("-v", "--verbosity",  help="increase verbosity", nargs='?', const=0, default=0)

    args = parser.parse_args()                 #get the input args from the parser
    
    global verbose
    verbose = args.verbosity
    setup_file = args.setupfile
    
    global pvdata
    global mon_line
    global pvf

    global pvfull

    #read the setup file, which has the form 
    #index    TOP        PVname  Period(s)

    for line in file(setup_file):                             #read the lines in the setup file to pvdata monitor list
        if not (line.startswith("#") or len(line.split())<3): #skip comments and require 3 fields
            s=line.split()                                    #split input into fields
            wf=PV(s[pvf.TOP]+":"+s[pvf.NAME]+"_wf")            #wf, en are PVs for waveform and enable
            en=PV(s[pvf.TOP]+":"+s[pvf.NAME]+"_en")  
            pvdata.append([s[0],s[pvf.TOP],s[pvf.NAME],s[pvf.PERIOD],wf,en,[]]) #add to list, with list for IDS
            
            #Call doNode() which works recursively through the tree and calls do_node()
            #which you may overwrite by calling your own function (eg my_node() shown here)
            #In this case, it calls my_node() for every element - see below.
            doNode.doNode(pvdata[mon_line][pvf.TOP],do_node=my_node, v=verbose)
            
            #now the pvf.ID array has been filled, try to connect to all the elements
            for n,chid in enumerate(pvdata[mon_line][pvf.ID]):
                if not ca.connect_channel(chid,timeout=0.001):
                    if verbose:
                        print pvfull[n], "... Not connected, chid = 0"
                    pvdata[mon_line][pvf.ID][n]=0
                else:
                    if verbose:
                        print pvfull[n], "... Connected, chid = ",chid
            pvdata[mon_line].append(numpy.zeros(len(pvdata[mon_line][pvf.ID]))) #create a zero numpy array for the data
            
            pvfull = [] #reset the list of names
            mon_line+=1 #increment the current line number 
      
    #start a monitor thread for each
    for l in range(mon_line):
        t = Thread(target=monitor, args=(l,))
        t.start()
      
    #do the poll loop here, to cover all monitor threads 
    while mon_line > 0:
        ca.poll()
        time.sleep(1.0)
        print "poll"



def monitor(mon_line):                               #this is run as a thread to monitor a specific pv for many elements
    global pvdata
    global pvf

    while mon_line > -1:                                 #ie infinite loop
        if not pvdata[mon_line][pvf.EN].get():               #if not enabled just wait 1s
            print "Not enabled: ",pvdata[mon_line][pvf.TOP]+":"+pvdata[mon_line][pvf.NAME]+"_wf"
            time.sleep(1.0)
        else:                                                #if enabled
            for chid in pvdata[mon_line][pvf.ID]:                #for all the chids
                if chid > 0:                                        #if the channel is connected
                    ca.get(chid, wait=False)                           #Tell them all to start getting but don't wait
            for n,chid in enumerate(pvdata[mon_line][pvf.ID]):   #for all the chids
                if chid > 0:                                        #if the channel is connected
                    pvdata[mon_line][pvf.ARRAY][n]=ca.get_complete(chid)#get the value to the array
            pvdata[mon_line][pvf.WF].put(pvdata[mon_line][pvf.ARRAY])#put to the waveform      
            print "mon_line",mon_line,pvdata[mon_line][pvf.PERIOD]
            time.sleep(float(pvdata[mon_line][pvf.PERIOD]))          #wait for the refresh period
                


def my_node(node,depth,mode='elem',result=None):
    #This must have the args defined here, and may have a section for each of the 3 modes:
    
    #mode='init': Do something before porcessing a node
    #mode='elem': Called for each element in the node. Can return a value which will be added to the result[] list.
    #mode='end':  Called at the end to process the result[] list for the node


    global pvdata
    global pvf
    global mon_line
    
    global pvfull

    if mode == 'elem':
        fullpv=node+":"+pvdata[mon_line][pvf.NAME]                      #create full pvname
        chid = ca.create_channel(fullpv, connect=False, auto_cb=False) #create channel
        pvdata[mon_line][pvf.ID].append(chid)                           #save the chid
        pvfull.append(fullpv)                                          #save the name temporarily
        

if __name__ == "__main__": main()  # call main comes at the end: a quirk of python
