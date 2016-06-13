from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
import nodeLoader
import os

#This is the code to put a set of combo widgets together to form a node chooser
#for nodes in the CLAS EPICS tree. 
#The chooser is made up of about 7 of these (depending on the no of layers in the hierarchy)

nodeLoader.readTree()                               #make sure the node tree is made

#Things from macros to initialise
node    = widget.getMacroValue("P")                 #Full name of the node Eg. B_SYS_HV_ECAL_SEC1
topnode = widget.getMacroValue("TOP")               #Name of the top node  Eg. B_SYS_HV
ntot    = int(widget.getMacroValue("NTOT"))         #total no of menu elements to make

if not node in nodeLoader.NodeIndex:                # check node defined, or try parent, or force to top node
    if node.find("_"):
        parent = node.split("_"+node.split("_")[len(node.split("_"))-1])[0]
        if parent in nodeLoader.NodeIndex:
            esel=node.split("_")[len(node.split("_"))-1]
            node=parent
        else:
            node=topnode
    else:
        node=topnode

dir = os.environ["CSS_SHARE_DIR"]                   #pick up the main share directory
opi_node_info=dir+"/apps/clasTreeApp/nodeInfo.opi"  #name of the .opi file with the combos
                
widget.removeAllChildren()                          #clean the area first

for i in range(ntot):                               #load a combo chooser menu for each
	linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
	linkingContainer.setPropertyValue("opi_file", opi_node_info)
	linkingContainer.addMacro("P", node)          #name of full node
        linkingContainer.addMacro("N", str(i))        #number index for combo
	linkingContainer.addMacro("NTOT", str(ntot))  #total number of combos
	linkingContainer.setPropertyValue("resize_behaviour", 1)  #size container to .opi
	linkingContainer.setPropertyValue("border_style", 0)      #no border
	linkingContainer.setPropertyValue("background_color", "OPI_Background")
	widget.addChildToBottom(linkingContainer)     #add to bottom of current group
        #ConsoleUtil.writeInfo("made i="+str(i))
