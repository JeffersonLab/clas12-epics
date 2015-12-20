#!/bin/python
from NodesDict import *
import doNode
import argparse
import random

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
    parser.add_argument("-v", "--verbosity",   help="increase verbosity 1,2 ..", nargs='?', const=0, default=0)
    #add extra args and opts here

    args = parser.parse_args()                      #get the input args from the parser
    
    global verbose
    verbose = args.verbosity
    
    #This calls the doNode() (bottom of this file) that works recursively through the tree and calls do_node()
    #which you may overwrite by calling your own function (eg my_node() shown here
    doNode.doNode(args.top,do_node=my_node, v=verbose)

    
def my_node(node,depth,mode='elem',result=None):
    #This must have the args defined here, and must have a section for each of the 3 modes:
    
    #mode='init': Do something before porcessing a node
    #mode='elem': Called for each element in the node. Can return a value which will be added to the result[] list.
    #mode='end':  Called at the end to process the result[] list for the node

    #In the example here, a random number around 10 is generated per element.
    #These are averaged for the node, and each node averages its subnodes - all the way up
    
    res=None
    
    if mode == 'init':                    #do nothing for starters
        return None               
    
    if mode == 'elem':
        res=random.gauss(10.0,1.0)        #random no as example
        if verbose:
            print '  '*depth+"  #Element: "+node+"  "+str(res)
    
    if mode == 'end':                     #return the mean of the results from the children
        res=0
        for n in range(len(result)):
            res += result[n]
        res = res/len(result)
        if verbose:
            print '  '*depth+"#NodeEnd: "+node+" N,Mean =", len(result), res
           
    return res

if __name__ == "__main__": main()
