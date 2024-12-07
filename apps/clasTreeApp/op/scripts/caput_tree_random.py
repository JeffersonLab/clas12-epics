#!/bin/python
from NodesDict import *
import doNode
import argparse
from epics import caget, caput, cainfo
import random
import time
import sys

#This is a template for how to get all the elements and randomly write to them (really for tests)
#The doNode() function does the main work (see doNode.py)
#All arguments except the node are optional, and have defaults.
#To customize the behaviour, make a specialised version of do_node() see below.
#as alernatives to the default ones defined in doNode.py

#There should be several examples in the same directory.

elemNodes = []
nNodes = 0

pvname = ""
val    = 0
sigma  = 0.1

#Keep main() and add extra args and opts as required.
def main():
    parser = argparse.ArgumentParser()                            # parser for the inputs - must keep the 2 lines below.
    parser.add_argument("top",                 help="top node")   # must have a top node, -v VERBOSITY is an opion  
    parser.add_argument("-v", "--verbosity",   help="increase verbosity", nargs='?', const=0, default=0)
    #add extra args and opts here
    parser.add_argument("pv",                  help="pvname")   
    parser.add_argument('value',               help="value") 
    parser.add_argument('sigma',               help="sigma") 

    args = parser.parse_args()                      #get the input args from the parser
    
    global verbose
    verbose = args.verbosity

    global pvname
    global val
    global sigma
    

    pvname = args.pv
    val    = args.value
    sigma  = args.sigma
    
    #This calls the doNode() (bottom of this file) that works recursively through the tree and calls do_node()
    #which you may overwrite by calling your own function (eg my_node() shown here
    doNode.doNode(args.top,do_node=my_node, v=verbose)

    #get random all nodes with elements
    #This has now filled elemNodes[] with all the names of the nodes which contain detector elements.

    #go into a loop selecting nodes randomly, and fill pvname with random values 
    n=0
    while n < 1000000:
        time.sleep(0.001)
        rand_node = random.choice(elemNodes)
        randel = random.choice(ElementNames[NodeIndex[rand_node]].split(","))
        randval = random.gauss(float(val),float(sigma))
        fullpv=rand_node+"_"+randel+":"+str(pvname)
        caput(fullpv,randval)
        if verbose: 
            print n, "caput", fullpv, randval
        n += 1


        
def my_node(node,depth,mode='elem',result=None):
    #This must have the args defined here, and must have a section for each of the 3 modes:
    
    #mode='init': Do something before porcessing a node
    #mode='elem': Called for each element in the node. Can return a value which will be added to the result[] list.
    #mode='end':  Called at the end to process the result[] list for the node
    global nNodes
    global pvname
    global val
    global sigma
                
    if mode == 'init':                                        #if start of node
        index=NodeIndex[node]
        if len(ElementRecordNames[index]) > 1:
               elemNodes.append(node)
               nNodes += 1
               if verbose:                                                 #if verbose
                   print '  '*depth+"#Node:"+node, nNodes                         #print the indented node name
    return None

if __name__ == "__main__": main()
