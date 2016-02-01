#import the nodes dictionary describing the Hall-B tree
#from NodesDict import SubNodeNames
import nodeLoader
from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
import os.path


#This is called from HallBTree.opi; a very a generic GUI
#which will display a node, parent, siblings subnodes and elements
#with the asscoiated .opi files embedded for each.

nodeLoader.readTree()


#Get the macro(s) associated with the widget
#The standard EPICS marco P=prefix is always passed. It is the name of the node or element.
node = widget.getMacroValue("P")   #main node for the GUI

if not node in nodeLoader.NodeIndex:                      # check node defined, or print error and ret  
        print "Error: There is no Key for \""+node+"\" in NodeIndex[]" 
        exit
ConsoleUtil.writeInfo("thisnode = "+node)
index=int(nodeLoader.NodeIndex[node])                          #find the index of the node for the lists

#get the widgets of all the grouping containers to be filled with our opis

widgetParent    = display.getWidget("ParentContainer")
widgetSiblings  = display.getWidget("SiblingContainer")
widgetNode      = display.getWidget("NodeContainer")
widgetSubnodes  = display.getWidget("SubNodeContainer")
widgetElements  = display.getWidget("ElementContainer")
widgetElementHeader  = display.getWidget("ElementHeaderContainer")

#get all the information for this node from the dictionaries look in clas12NodesDict to see what else is available.
#Check if we're requesting the top node. If so, set node to 1st subnode down from top
if node.find("_"): 
        parent = node.split("_"+node.split("_")[len(node.split("_"))-1])[0]
else:
        parent = node

pindex =  int(nodeLoader.NodeIndex[parent])  
     
siblings = nodeLoader.SubNodeNames[pindex].rstrip("'").lstrip("'").split(",")
siblings.sort()
subnodes = nodeLoader.SubNodeNames[index].rstrip("'").lstrip("'").split(",")
subnodes.sort()
elements = nodeLoader.ElementNames[index].rstrip("'").lstrip("'").split(",")
elements.sort()

#Do the GUI from the top down. The standard EPICS marco P=prefix is always passed. It is the name of the node or element.
#ConsoleUtil.writeInfo("thisnode = "+node)

# Fill the parent group with the .opi
ConsoleUtil.writeInfo("parent = "+parent)
linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
linkingContainer.setPropertyValue("opi_file", "ntree_parent.opi" )
linkingContainer.addMacro("P", parent)
linkingContainer.setPropertyValue("resize_behaviour", 1)
linkingContainer.setPropertyValue("border_style", 0)
widgetParent.addChildToBottom(linkingContainer)


# Fill the Siblings group container with relevant .opi files
# header first
linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
linkingContainer.setPropertyValue("opi_file", "ntree_sibling_header.opi" )
linkingContainer.addMacro("P", parent)
linkingContainer.setPropertyValue("resize_behaviour", 1)
linkingContainer.setPropertyValue("border_style", 0)
widgetSiblings.addChildToBottom(linkingContainer)

# loop over siblings adding in them in a row. 
# flag the sibling which is the selected node with a macro
for s in siblings:
        if s != "":
                ConsoleUtil.writeInfo("sibling = "+s)
                linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
                linkingContainer.setPropertyValue("opi_file", "ntree_sibling.opi")
                linkingContainer.addMacro("P", parent+"_"+s) #full name
                linkingContainer.addMacro("S", s)            #short name 
                if node == parent+"_"+s: #check to see if the sibling is the selected node
                        isnode="1"
                else:
                        isnode="0"
                linkingContainer.addMacro("SiblingIsNode", isnode)
                linkingContainer.setPropertyValue("resize_behaviour", 1)
                linkingContainer.setPropertyValue("border_style", 0)
                widgetSiblings.addChildToRight(linkingContainer)
                
# Fill the Node group container with relevant .opi files
linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
linkingContainer.setPropertyValue("opi_file", "ntree_node.opi" )
linkingContainer.addMacro("P", node)
linkingContainer.setPropertyValue("resize_behaviour", 1)
linkingContainer.setPropertyValue("border_style", 0)
widgetNode.addChildToBottom(linkingContainer)


# Fill the Subnodes group container with relevant .opi files
# header first
linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
linkingContainer.setPropertyValue("opi_file", "ntree_subnode_header.opi" )
linkingContainer.addMacro("P", parent)
linkingContainer.setPropertyValue("resize_behaviour", 1)
linkingContainer.setPropertyValue("border_style", 0)
widgetSubnodes.addChildToBottom(linkingContainer)

for s in subnodes:
        if s != "":
                ConsoleUtil.writeInfo("subnodes = "+s)
                linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
                linkingContainer.setPropertyValue("opi_file", "ntree_subnode.opi")
                linkingContainer.addMacro("P", node+"_"+s) #fill node name
                linkingContainer.addMacro("S", s)          #short name
                linkingContainer.setPropertyValue("resize_behaviour", 1)
                linkingContainer.setPropertyValue("border_style", 0)
                widgetSubnodes.addChildToRight(linkingContainer)

# Fill the Elemements group container with relevant .opi files
# header first
linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
linkingContainer.setPropertyValue("opi_file", "ntree_element_header.opi" )
linkingContainer.addMacro("P", parent)
linkingContainer.setPropertyValue("resize_behaviour", 1)
linkingContainer.setPropertyValue("border_style", 0)

if len(elements) > 1:
        widgetElementHeader.addChildToBottom(linkingContainer)
        c=0
        for e in elements:
                if e != "":
                        ConsoleUtil.writeInfo("elements = "+e)
                        linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
                        linkingContainer.setPropertyValue("opi_file", "ntree_element.opi")
                        linkingContainer.addMacro("P", node+"_"+e)
                        linkingContainer.addMacro("S", e)
                        linkingContainer.addMacro("C", str(c))
                        linkingContainer.setPropertyValue("resize_behaviour", 1)
                        linkingContainer.setPropertyValue("border_style", 0)
                        widgetElements.addChildToBottom(linkingContainer)
                        c+=1
exit
