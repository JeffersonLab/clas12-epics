from clas12NodesDict import SubNodeNames,  ElementNames, ElementRecordNames, ElementRecordTypes, NodeRecordNames, NodeRecordTypes

def doNode( node, depth, indent):
    subnodes = SubNodeNames[node].split()
    elements = ElementNames[node].split()
    
    print indent+node
        
    for s in subnodes:
        do_unto_element(node,depth,indent)
 #       print indent+s
        getNodeInfo( node+"_"+s, depth+1,indent+"  " )
        
    for e in elements:
        print indent+"  "+node+":"+e
        
    return;


#getNodeInfo('BSIM_HV',0,"")
   

