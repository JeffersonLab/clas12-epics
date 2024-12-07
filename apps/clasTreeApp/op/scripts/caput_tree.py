#!/bin/python
from NodesDict import *
import doNode
import argparse
from epics import caget, caput, cainfo

#This is a template for how to a run a command on the whole hierarchy of nodes from a starting point downwards.
#The doNode() function does the main work (see doNode.py)
#All arguments except the node are optional, and have defaults.
#To customize the behaviour, make a specialised version of do_node() see below.
#as alernatives to the default ones defined in doNode.py

#There should be several examples in the same directory.


#Keep main() and add extra args and opts as required.
def main():
    parser = argparse.ArgumentParser()                            # parser for the inputs - must keep the 2 lines below.
    parser.add_argument("top",                 help="top node")   # must have a top node, -v VERBOSITY is an opion  
    parser.add_argument("-v", "--verbosity",   help="increase verbosity", nargs='?', const=0, default=0)
    #add extra args and opts here
    parser.add_argument("pv",                  help="pvname")   
    parser.add_argument('value',               help="value") 

    args = parser.parse_args()                      #get the input args from the parser
    
    global verbose
    verbose = args.verbosity

    global pvname
    global val
    
    pvname = args.pv
    val    = args.value
    
    #This calls the doNode() (bottom of this file) that works recursively through the tree and calls do_node()
    #which you may overwrite by calling your own function (eg my_node() shown here
    doNode.doNode(args.top,do_node=my_node, v=verbose)

    
def my_node(node,depth,mode='elem',result=None):
    #This must have the args defined here, and must have a section for each of the 3 modes:
    
    #mode='init': Do something before porcessing a node
    #mode='elem': Called for each element in the node. Can return a value which will be added to the result[] list.
    #mode='end':  Called at the end to process the result[] list for the node
            
    if mode == 'elem':                                       # if element
        fullpv=node+":"+str(pvname)                          # make pvname
        if verbose:                                          #if verbose print details
            print '  '*depth+"  #caput(\""+fullpv+"\","+val+")" 
        caput(fullpv,val)                                    #do the caput to the element
    
    if mode == 'init':                                        #if start of node
        if verbose:                                                 #if verbose
            print '  '*depth+"#Node:"+node                          #print the indented node name
            return None

    if mode == 'end':                                        #if end of node
        if verbose:                                                 #if verbose
            print '  '*depth+"#NodeEnd:"+node                       #print the indented node name
            return None

if __name__ == "__main__": main()
