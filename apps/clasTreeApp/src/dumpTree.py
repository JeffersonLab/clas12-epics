#!/bin/python
from clas12NodesDict import *
import argparse

#This is a template for how to a run a command on the whole hierarchy of nodes from a starting point downwards.
#The doNode() function does the work
#It calls functions here as apropriate:

#The following 4 functions need to be defined.
#main():             to do any initialisation
#start_node():       called for every node before do_unto_elememt() is applied to all its elements    
#do_unto_element():  called for every element
#end_node():         called for every node after do_unto_elememt()  is applied to all its elements    

#This is the very simplest template - just dumps the node  and element names

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("top", help="top node")
    args   = parser.parse_args()
    topnode = args.top

    #This is the function that works recursively through the tree and calls do_unto_element start_node end_node
    doNode(topnode, 0, "")
    
def do_unto_element(element,depth,indent):
    print indent+"#Elem: "+element #print the indented elment name 
    return

def start_node(node,depth,indent):
    print indent+"#Node:"+node     #print the indented node name 
    return

def end_node(node,depth,indent):
    return


#########################################################################################
# Recursion begins here
# Do not edit below here unless you know are prepared to disappear up your own arse     #
# Kenneth
#########################################################################################

def doNode( node, depth, indent):
    subnodes = SubNodeNames[node].split()
    elements = ElementNames[node].split()
        
    start_node( node, depth, indent)
    for s in subnodes:
        doNode( node+"_"+s, depth+1,indent+"  " )        
    end_node ( node, depth, indent )
               
    for e in elements:
        do_unto_element(node+"_"+e,depth,indent+"  ")
        
    return
    
if __name__ == "__main__": main()

