#import the nodes dictionary describing the Hall-B tree
#from NodesDict import SubNodeNames
import nodeLoader
from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
from java.util import Arrays
import os.path

#This scripts is associated with choice buttons used to select nodes and browser the EPICS hierarchy.
#Each, choice button (menu.

#Read in the node tree
nodeLoader.readTree()


#The macro P is like this:      B_SYS_HV_ECAL_SEC1_.....
#split into list with elements  0 1   2  3    4    5
#                                             *

#This script relates to choice button with number n (taken from macro N) - let's say 4 in this case (* above).
#If the macro has 5 (n+1) or more elements we want to draw the button, make the choices the siblings of element n,
#and mark the correct one as selected.



#Get the macro(s) associated with the widget
#The standard EPICS marco P=prefix is always passed. It is the name of the node or element.
node = widget.getMacroValue("P")     #main node for the GUI
n = int(widget.getMacroValue("N"))   #index of this menu

widget.setPropertyValue("visible","false")
drawing=0

if not node in nodeLoader.NodeIndex:                      # check node defined, or print error and ret  
        #ConsoleUtil.write("Error: There is no Key for \""+str(node)+"\" in NodeIndex[]") 
        node="B"

if not node.find("_"):
        if n==1:
                drawing=1
                parent=node
                shortnode=node
else:        
        if n < len(node.split("_")):
                drawing=1
                shortnode = node.split("_")[n]
                parent = node.split("_"+node.split("_")[n])[0]

if drawing==1:
 
        widget.setPropertyValue("visible","true")
        pindex =  int(nodeLoader.NodeIndex[parent])  
        siblings = nodeLoader.SubNodeNames[pindex].rstrip("'").lstrip("'").split(",")
        siblings.sort()
        
        ConsoleUtil.writeInfo("n="+str(n)+", parent="+parent+",  subnodes="+nodeLoader.SubNodeNames[pindex])

        subnodes = nodeLoader.SubNodeNames[pindex].rstrip("'").lstrip("'").split(",")
        widget.setPropertyValue("items",Arrays.asList(subnodes) )
        widget.setPropertyValue("height",24*len(subnodes) )

        selectedPV = pvArray[0]
        selectedPV.setValue(shortnode)

        #init=int(PVUtil.getLong(pvArray[2]))
        #init+=1
        #ConsoleUtil.writeInfo(str(init))
        #pvArray[2].setValue(init)
        
