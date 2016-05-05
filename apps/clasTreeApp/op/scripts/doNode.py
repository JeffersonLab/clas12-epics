#!/bin/python
from NodesDict import *
import argparse

#This is to allow operations on the hierarchy of nodes defined in NodesDict
#An action can be carried at every level down from the entry point in the tree,
#and the result passed up the the parent

#To use this, 
#import doNode into a python script and provide a custom replacement for 
#default_node(node,depth,mode='elem',result=None)

#For example see caput_tree.py and caget_tree.py addUpExample.py
#

#doNode.py can also be run standalone in verbose mode to print out the hierarchy
#This can be piped to othe scripts to do things.

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("top",                 help="top node")           #Add args and opts
    parser.add_argument("-v", "--verbosity",   help="increase verbosity 1,2 ..", nargs='?', const=0, default=0)
    args = parser.parse_args()                                            #parse them

    #Calls the doNode() (see below) that works recursively through the tree and calls do_element start_node end_node
    doNode(args.top,v=int(args.verbosity))


def default_node(node,depth,mode='elem',result=None):
    #mode can be
    #init: to initialise before processing elemenst and subnodes, return a val to start result[]
    #sum:  to do something with result[] from subnodes and return a single value
    #end:  to do something with result[] from elements/subnodes and return value for parent
    

    if mode == 'init':                                       #if start of node
        index=NodeIndex[node]                                #Get index from dict
        if verbose:                                                 #if verbose
            if ElementRange[index] != "":
                erange=ElementRange[index].split(",")
                print '  '*depth+"#Node:"+node+"      Erange:  "+erange[0]+" - "+erange[1]      #print the indented node name
            else:
                print '  '*depth+"#Node:"+node
        if verbose > 1:                                             #if very verbose mode, print record details if any.
            nrnames=NodeRecordNames[index].split(",")
            nrtypes=NodeRecordTypes[index].split(",")
            for i in range(len(nrtypes)):
                if nrtypes[i] != "":
                    print '  '*depth+"  #NodeRecordName: "+repr(nrnames[i]).ljust(20)+ "#NodeRecordType: "+repr(nrtypes[i])
            ernames=ElementRecordNames[index].split(",")
            ertypes=ElementRecordTypes[index].split(",")
            erflags=ElementRecordFlags[index].split(",")
            for i in range(len(ertypes)):
                if ertypes[i] != "":
                    print '  '*depth+"  #ElementRecordName: "+repr(ernames[i]).ljust(10)+ "#ElementRecordType: "+repr(ertypes[i])+ "  #ElementRecordFlag: "+repr(erflags[i])

    elif mode == 'elem':
        if verbose:
            print '  '*depth+"  #Element: "+node #print the indented elment name
            return None
                    
    elif mode == 'end':
        if verbose:
            print '  '*depth+"#NodeEnd: "+node
        
    else:
        return None


def default_sum(node,depth,result=None):
    return None




##########################################################################################
# Recursion here. It gets called for every node in the tree
# Do not edit below here unless you know are prepared to disappear up your own arse      #
# Kenneth
##########################################################################################

#      ----<-----<-----<-----<-----<-----<-----<-----<-----<-----<-----<-----<-----<-----<---
#    /                                                                                        \
#   |                                                                                          \
def doNode(node, do_node=default_node, depth=0, v=0): #                                         \
    #                                                                                            |
    result= [];                                    # init a list for results                     ^
    total = None                                   #                                             ^
                                                   #                                             |
    global verbose                                 #                                             |
    verbose  = v                                   #                                             ^
    #                                                                                            ^
    res = do_node(node, depth, 'init')             # init node (can init result list if reqd)    |
    if res != None:                                # if result, append to list                   |
        result.append(res)                         #                                             ^
    #                                                                                            ^
    if not node in NodeIndex:                      # check node defined, or print error and ret  |
        print "Error: There is no Key for \""+node+"\" in NodeIndex[]" #                         |
        return None                                #                                             |
    #                                                                                            ^
    index=NodeIndex[node]                          #find the index of the node for the lists     |
    #                                                                                            |
    #-----------------------------------------Do subnodes----------------------------------      |
    if SubNodeNames[index] != "":                     #If valid subnode list              |      ^
        subnodes = SubNodeNames[index].split(",")        #split into list                 |      ^
        for s in subnodes:                                  #go over list                 |      |
            if s != "":                                        #if valid subnode          |      |
                res = doNode(node+"_"+s, do_node, depth+1,v)      # doNode() recursivly --|--->--
                if res != None:                                   #if result, add to list |     
                    result.append(res)                            #                       |                   
    #--------------------------------------------------------------------------------------

    
    #Elements should really be at the end of the line. ie
    #the subnode containing the elements should have no further subnodes defined in tree
    #-----------------------------------------Do elements----------------------------------
    if ElementNames[index] != "":                     #if valid element list              |
        elements = ElementNames[index].split(",")        #split into list                 |              
        for e in elements:                                  #go over list                 |
            if e != "":                                         #if valid element         |
                res = do_node(node+"_"+e, depth,'elem')         #do the element           |
                if res != None:                                 #if result, add to list   |
                    result.append(res)                          #                         |
    #--------------------------------------------------------------------------------------
    
    total=do_node(node, depth, 'end', result)    
    return total   


###########################################################################################
# Recursion ends here
#
###########################################################################################

if __name__ == "__main__": main()  # call main comes at the end: a quirk of python
