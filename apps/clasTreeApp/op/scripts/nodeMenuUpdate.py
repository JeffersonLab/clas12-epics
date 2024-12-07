#import the nodes dictionary describing the Hall-B tree
import nodeLoader
from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
from java.util import Arrays
import os.path

#This one of a pair of partner scripts nodeMenuAction.py and nodeMenuUpdate.py
#Together they are used to choose a NODE in the epics tree.
#There is a node selection menu for each level in the hierarchy 
#Each time the NODE is modified, all menus call nodeMenuUpdate.py.
#Each menu then sets its state and list of choices according to the loaded dictionary of nodes.

#They would be run inside allNodeMenuContainer.opi, which needs to be called wth a macro specifying
#the initial node, and the maximum depth. Eg. defaults TOP="B" P="B", NTOT=6.

#When a choice is made in one of the menus,
#loc://$(LCID)_MOUT  (pv[1]) is changed, tiggering nodeMenuAction.py for ChoiceButton_N, which makes
#loc://$(LCID)_NODE  (pv[0]) change, triggering nodeMenuUpdate.py for all buttons.
#Warning - some danger of infinite recursion here. Careful"

#The $(LCID) macro is used to make local PVs per instance. So several instances could be run from the same CSS
#without interfering.


#For example loc://$(LCID)_NODE pv is like this:         B_SYS_HV_ECAL_SEC1_.....
#split into list with elements                           0 1   2  3    4    5
#eg - with N for the menu N = 3                                   *
#

nodeLoader.readTree()                            #Read in the node tree

n = int(widget.getMacroValue("N"))               #Get N,B and NODE
topnode=widget.getMacroValue("TOP")
node = PVUtil.getString(pvArray[0])

if not node in nodeLoader.NodeIndex:             # check node defined, or force to top node   
        node=topnode

nlist=node.split("_")                            #make a list of the parts of node   nlist = (B,SYS,HV,ECAL,SEC1,....)

#widget.setPropertyValue("height",24 )            #and size
#widget.setPropertyValue("visible","false")       #assume invisible until other decision made
widget.setPropertyValue("enabled","false")       #assume invisible until other decision made
widget.setPropertyValue("background_color","OPI_Background")       #assume invisible until other decision made

if n<=len(nlist):                                #if this level is included in the node
        parent=topnode
        if n>1:
                for e in range(1,n):
                        parent+="_"+nlist[e]
        #ConsoleUtil.writeInfo("Update:"+str(n)+", parent="+parent)
                        
        pindex =  int(nodeLoader.NodeIndex[parent])  #get its parent index
        if len(nodeLoader.SubNodeNames[pindex])>2:   #if there are siblings
                #ConsoleUtil.writeInfo("Update: sibilng list="+nodeLoader.SubNodeNames[pindex])
                widget.setPropertyValue("enabled","true")
                widget.setPropertyValue("background_color","Write_Background")       #assume invisible until other decision made
                siblings = nodeLoader.SubNodeNames[pindex].rstrip("'").lstrip("'").split(",")
                siblings.sort()                                             #make a sorted list of them
                #siblings.insert(0,"select..")
                widget.setPropertyValue("items",Arrays.asList(siblings) )   #set the choice list
                #widget.setPropertyValue("height",24*len(siblings) )         #and size

                if n<len(nlist):                                            #if not the last one
                        pvArray[1].setValue(nlist[n])                       #set the selected value
                #else:
                #pvArray[1].setValue(siblings[0])


