from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
import nodeLoader
from java.util import Arrays

#This is the code to update the list of items in combo widget to chose a node
#in the CLAS EPICS tree. 
#It is triggered by selection of a new node using the local PV loc://$(DID)_NODE
#It makes the item list of all the ancestors, the node, and the subnodes

nodeLoader.readTree()                        #make sure the node tree is made

topnode  = widget.getMacroValue("TOP")       #Name of the top node  Eg. B_SYS_HV
ntop     = len(topnode.split("_"))           #Work out the no of levels in the top node (eg. 3 here)

node     = topnode                           #Start off the node that this combo will display
       
index    =  int(nodeLoader.NodeIndex[node])     #get subnodes
subnodes = nodeLoader.SubNodeNames[index].rstrip("'").lstrip("'").split(",")
          
row = 0
rowlen = 6
col = 0
if len(subnodes[0]):                         #if there are subnodes
    for i in range(len(subnodes)):           #make a list, sort it and start it with this node
        # Fill the subnodes group container with relevant .opi files
        # header first
        index    =  int(nodeLoader.NodeIndex[node+"_"+subnodes[i]])
        erange = nodeLoader.ElementRange[index].strip("'")
        low  = erange.split(",")[0]
        high = erange.split(",")[1]
        
        linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
        linkingContainer.setPropertyValue("opi_file", "subnodeButton.opi" )
        linkingContainer.addMacro("SUBNODE", subnodes[i])
        linkingContainer.addMacro("RANGE_LOW", low)
        linkingContainer.addMacro("RANGE_HIGH", high)
        linkingContainer.setPropertyValue("resize_behaviour", 1)
        linkingContainer.setPropertyValue("border_style", 0)
        
        widget.addChild(linkingContainer)
        linkingContainer.setPropertyValue("x",str(col*40))
        linkingContainer.setPropertyValue("y",str(row*12))
        col+=1
        if col==10:
            row+=1
            col=0
            
        
