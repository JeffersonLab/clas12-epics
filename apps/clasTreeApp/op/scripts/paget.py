#!/bin/python
from clas12NodesDict import *
import argparse
import epics

#This is a template for how to a run a command on the whole hierarchy of nodes from a starting point downwards.
#The doNode() function does the work
#It calls functions here as apropriate:

#The following 4 functions need to be defined.
#main():             to do any initialisation
#start_node():       called for every node before do_unto_elememt() is applied to all its elements    
#do_unto_element():  called for every element
#end_node():         called for every node after do_unto_elememt()  is applied to all its elements    

#Global variables here (and defined as global in any function that needs them)
pvname = ""
AsString = False

def main():
    global pvname
    global AsString
    
    parser = argparse.ArgumentParser()
    parser.add_argument("top", help="top node")
    parser.add_argument("pv", help="pv name")
    args   = parser.parse_args()
    pvname = args.pv
    topnode = args.top
    
    
    #This is the function that works recursively through the tree and calls do_unto_element start_node end_node
    doNode(topnode, 0, "")

    
def do_unto_element(element,depth,indent):
    global pvname
    print element+":"+pvname
    pv  = epics.PV(element+":"+pvname)
    return pv.get(as_string=AsString)

def start_node(node,depth,indent):
    global pvname
    return

def end_node(node,depth,indent):
    global pvname
    return


#########################################################################################
# Recursion begins here
# Do not edit below here unless you know are prepared to disappear up your own arse     #
# Kenneth
#########################################################################################

def doNode( node, depth, indent):
    subnodes = SubNodeNames[node].split()
    elements = ElementNames[node].split()
    #print indent+node
        
    for s in subnodes:
        #print indent+s
        doNode( node+"_"+s, depth+1,indent+"  " )
        
    for e in elements:
        #print indent+"  "+node+"_"+e
        do_unto_element(node+"_"+e,depth,indent)
        
    return
    
if __name__ == "__main__": main()

