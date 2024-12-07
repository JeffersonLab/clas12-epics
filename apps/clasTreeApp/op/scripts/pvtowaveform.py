#!/bin/python
from NodesDict import *
import doNode
import argparse
from epics import ca, PV
import time
import sys
import numpy

#The doNode() function does the main work (see doNode.py)
#All arguments except the node are optional, and have defaults.
#To customize the behaviour of doNode(), make a specialised version of do_node() see below.
#as alernatives to the default ones defined in doNode.py

#There should be several examples in the same directory.

#This 
pvname = ""    #The pvname to be read for each element

allnames = []  #list of all the full names for all the elements
allids = []    #list of all the chid of all the channels
nChid = 0      #counter for all the elements

#This uses some of the fast access techniques described here:
#http://cars9.uchicago.edu/software/python/pyepics3/advanced.html


#Keep main() and add extra args and opts as required.
def main():
    parser = argparse.ArgumentParser()                            # parser for the inputs - must keep the 2 lines below.
    parser.add_argument("top",                 help="top node")   # must have a top node, -v VERBOSITY is an opion  
    parser.add_argument("-v", "--verbosity",   help="increase verbosity", nargs='?', const=0, default=0)
    #add extra args and opts here
    parser.add_argument("pv",                  help="pvname")   

    args = parser.parse_args()                 #get the input args from the parser
    
    global verbose
    verbose = args.verbosity

    global pvname
    global nChid

    
    pvname = args.pv
    
    #This calls the doNode() (bottom of this file) that works recursively through the tree and calls do_node()
    #which you may overwrite by calling your own function (eg my_node() shown here
    #In this case, it calls my_node() for every element - see below.
    doNode.doNode(args.top,do_node=my_node, v=verbose)

    
    wave=numpy.zeros(nChid)             #create an array for all the values

    pvname_wf = args.top+":"+pvname+"_wf"    #make the names of the PVs for waveform and enable switch
    pvname_en = args.top+":"+pvname+"_en"

    print pvname_wf,pvname_en
    
    pvwf = PV(pvname_wf)          #set the PV
    pven = PV(pvname_en)          #set the PV

    pven.put(1)

    for i in range(len(allids)):        #connect call the channels
        if not ca.connect_channel(allids[i],timeout=0.001):
            allids[i]=0
            print "Warning didn't connect to PV =", allnames[i], "ignoring this one"
            
    ca.poll()                           #Not sure exactly what this does!
    n=0
    while n < 100000:
        for i in range(len(allids)):
            #print i, allids[i]
            if allids[i] > 0:
                ca.get(allids[i], wait=False) #Tell them all to start getting but don't wait
        ca.poll() 
        
        for i in range(len(allids)):           #now finish getting
            if allids[i] > 0:
                val = ca.get_complete(allids[i])
                wave[i]=val
                if verbose:
                    #print allnames[i],val
        pvwf.put(wave)
        time.sleep(0.5)

        if not pven.get():
            exit()
        #print n,pven.get()
        n+=1
                
        
def my_node(node,depth,mode='elem',result=None):
    #This must have the args defined here, and may have a section for each of the 3 modes:
    
    #mode='init': Do something before porcessing a node
    #mode='elem': Called for each element in the node. Can return a value which will be added to the result[] list.
    #mode='end':  Called at the end to process the result[] list for the node

    global pvname
    global nChid
    
    if mode == 'elem':
        fullpv=node+":"+pvname                                         #create full pvname
        chid = ca.create_channel(fullpv, connect=False, auto_cb=False) #create channel
        print fullpv,chid
        allnames.append(fullpv)                                        #store name and channel
        allids.append(chid)
        nChid += 1
        
if __name__ == "__main__": main()



