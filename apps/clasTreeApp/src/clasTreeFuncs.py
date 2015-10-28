from clas12NodesDict import SubNodeNames,  ElementNames, ElementRecordNames, ElementRecordTypes, NodeRecordNames, NodeRecordTypes
import epics



#pvname = 'BSIM_HV_PCAL_SEC6_W:ElementNames.VAL'
#pv  = epics.PV(pvname)
##print pv.info
#plain_val = pv.get()
#char_val = pv.get(as_string=True)
#print char_val


def getNodeInfo( node, depth, indent, function, *args, **kwargs):
    subnodes = SubNodeNames[node].split()
    elements = ElementNames[node].split()
    
    print indent+node
        
    for s in subnodes:
 #       print indent+s
        getNodeInfo( node+"_"+s, depth+1,indent+"  " )
        
    for e in elements:
        print indent+"  "+node+":"+e
        
    return;


#getNodeInfo('BSIM_HV',0,"")
   

