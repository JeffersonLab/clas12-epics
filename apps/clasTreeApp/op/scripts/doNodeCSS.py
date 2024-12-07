import nodeLoader
from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
from java.util import Arrays
import os

def default_node(node,depth,mode='elem',result=None):

    global doElems
    
    if mode == 'init':                                        #if start of node
        index=int(nodeLoader.NodeIndex[node])                   #Get index from dict
        if verbose > 0:                                                 #if verbose
            erange=nodeLoader.ElementRange[index].replace("\'","").split(",")
            if len(erange)>1:
                ConsoleUtil.writeInfo( '  '*depth+"#Node:"+node+"      Erange:  "+erange[0]+" - "+erange[1])      #print the indented node name
        
        if verbose > 1:                                             #if very verbose mode, print record details if any.
            nrnames=nodeLoader.NodeRecordNames[index].split(",")
            nrtypes=nodeLoader.NodeRecordTypes[index].split(",")
            for i in range(len(nrtypes)):
                if nrtypes[i] != "":
                    ConsoleUtil.writeInfo( '  '*depth+"  #NodeRecordName: "+repr(nrnames[i]).ljust(20)+ "#NodeRecordType: "+repr(nrtypes[i]))
            ernames=nodeLoader.ElementRecordNames[index].replace("\'","").split(",")
            ertypes=nodeLoader.ElementRecordTypes[index].replace("\'","").split(",")
            erflags=nodeLoader.ElementRecordFlags[index].replace("\'","").split(",")
            for i in range(len(ertypes)):
                if ertypes[i] != "":
                    ConsoleUtil.writeInfo( '  '*depth+"  #ElementRecordName: "+repr(ernames[i]).ljust(10)+ "#ElementRecordType: "+repr(ertypes[i])+ "  #ElementRecordFlag: "+repr(erflags[i]))

        if len(nodeLoader.ElementNames[index]) >2:
            linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
            linkingContainer.setPropertyValue("opi_file", opi_node_info)
            linkingContainer.addMacro("P", node)
            linkingContainer.setPropertyValue("resize_behaviour", 1)
            linkingContainer.setPropertyValue("border_style", 0)
            linkingContainer.setPropertyValue("background_color", "OPI_Background")
            widget.addChildToBottom(linkingContainer)

                    
    #elif mode == 'elem':
        #if verbose>0:
        #    ConsoleUtil.writeInfo( '  '*depth+"  #Element: "+node) #print the indented elment name
        #    #return None
        #esel=node.split("_")[len(node.split("_"))-1]
        #linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
        #linkingContainer.setPropertyValue("opi_file", opi_element)
        #linkingContainer.addMacro("P", node)
        #linkingContainer.addMacro("S", esel)
        #linkingContainer.addMacro("C", str(eCount))
        #linkingContainer.setPropertyValue("resize_behaviour", 1)
        #linkingContainer.setPropertyValue("border_style", 0)
        #widget.addChildToBottom(linkingContainer)
        #ConsoleUtil.writeInfo( '  '*depth+"  #Element: "+node+"   sel: "+esel) #print the indented elment name
            
        
    elif mode == 'end':
        if verbose:
            ConsoleUtil.writeInfo( '  '*depth+"#NodeEnd: "+node)
        
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
    if not node in nodeLoader.NodeIndex:           # check node defined, or print error and ret  |
        ConsoleUtil.writeInfo( "Error: There is no Key for \""+node+"\" in NodeIndex[]") #       |
        return None                                #                                             |
    #                                                                                            ^
    index=int(nodeLoader.NodeIndex[node])          #find the index of the node for the lists     |
    #                                                                                            |
    #-----------------------------------------Do subnodes----------------------------------      |
    if nodeLoader.SubNodeNames[index] != "":                     #If valid subnode list   |      ^
        subnodes = nodeLoader.SubNodeNames[index].replace("\'","").split(",") #split into |      ^
        for s in subnodes:                                  #go over list                 |      |
            if s != "":                                        #if valid subnode          |      |
                res = doNode(node+"_"+s, do_node, depth+1,v)      # doNode() recursivly --|--->--
                if res != None:                                   #if result, add to list |     
                    result.append(res)                            #                       |                   
    #--------------------------------------------------------------------------------------

    
    #Elements should really be at the end of the line. ie
    #the subnode containing the elements should have no further subnodes defined in tree
    #-----------------------------------------Do elements----------------------------------
    if nodeLoader.ElementNames[index] != "":                     #if valid element list   |
        elements = nodeLoader.ElementNames[index].replace("\'","").split(",") #split      |              
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

#def main():
#    #Read in the node tree
nodeLoader.readTree()
#
#    #Calls the doNode() (see below) that works recursively through the tree and calls do_element start_node end_node
topnode=widget.getMacroValue("TOP")
node = PVUtil.getString(pvArray[0])

if not node in nodeLoader.NodeIndex:             # check node defined, or try parent, or force to top node
	if node.find("_"):
		parent = node.split("_"+node.split("_")[len(node.split("_"))-1])[0]
		ConsoleUtil.writeInfo("Update: parent="+parent)
		if parent in nodeLoader.NodeIndex:
			esel=node.split("_")[len(node.split("_"))-1]
			node=parent
		else:
		        node=topnode
	else:
		node=topnode

dir = os.environ["CSS_SHARE_DIR"]

#Now do the same for ..._element.opi. This will make a widget for every element
opi_element=dir+"/apps/clasTreeApp/"+topnode+"_element.opi"          #Default to top

opi_node=node                                                     #default to node
while not opi_node == topnode:                          #if not at top node yet
	if  not "_" in opi_node:                                  
		break
	filename=dir+"/apps/clasTreeApp/"+opi_node+"_element.opi" #make a filename
	#ConsoleUtil.writeInfo("looking for "+filename) 
	if os.path.isfile(filename):                              #test to see if it exists
		opi_element=filename
		break                                             #if so, keep it and break
	else:                                                     #otherwise, try the parent 
		opi_node=opi_node[:-1]

#opi_node_info=dir+"/apps/clasTreeApp/nodeInfoButton.opi"
opi_node_info=dir+"/apps/clasTreeApp/nodeInfo.opi"
                
widget.removeAllChildren()


#before plunging into the tree, draw the parents
tempnode=node
tempnode=tempnode.replace(topnode+"_","")
nlist=tempnode.split("_") 
tempnode=topnode
for i in range(len(nlist)):
    linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
    linkingContainer.setPropertyValue("opi_file", opi_node_info)
    linkingContainer.addMacro("P", tempnode)
    linkingContainer.addMacro("N", str(i))
    linkingContainer.setPropertyValue("resize_behaviour", 1)
    linkingContainer.setPropertyValue("border_style", 0)
    linkingContainer.setPropertyValue("background_color", "OPI_Background")
    widget.addChildToBottom(linkingContainer)
    tempnode=tempnode+"_"+nlist[i]
   
doNode(node,v=1)
