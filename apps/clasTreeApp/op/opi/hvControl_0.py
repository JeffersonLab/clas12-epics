from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
import nodeLoader
from java.util import Arrays

#Update the list of items in combo widget to choose an element from under a node of the CLAS EPICS tree. 
#Triggered by selection of a new node using the local PV loc://$(DID)_NODE
#It makes the item list of all the elements under that node and sets the selected to 1st in the list

nodeLoader.readTree()                        #make sure the node tree is made

nodefull = PVUtil.getString(pvArray[0])      #Full name of the node Eg. B_SYS_HV_ECAL_SEC1
element = PVUtil.getString(pvArray[1])      #Full name of the node Eg. B_SYS_HV_ECAL_SEC1

widget.removeAllChildren()

#only proceed if the node is the parent of the element.
parent = element.split("_"+element.split("_")[len(element.split("_"))-1])[0]

if parent == nodefull:

    #if the element is valid fill this box with relevant opi files to display things
    if not element == "Element":
        elem=element.split()[0]
        linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer")
        linkingContainer.setPropertyValue("opi_file", "hvHeaderWrapper.opi")
        linkingContainer.addMacro("ELEMENT", elem)  #
        linkingContainer.addMacro("NODE", nodefull)  #
        linkingContainer.setPropertyValue("resize_behaviour", 1)  #size container to .opi
        linkingContainer.setPropertyValue("border_style", 0)      #no border
        linkingContainer.setPropertyValue("background_color", "OPI_Background")
        widget.addChildToBottom(linkingContainer)     #add to bottom of current group
        
        linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer")
        linkingContainer.setPropertyValue("opi_file", "hvChanWrapper.opi")
        linkingContainer.addMacro("P", elem)  #
        linkingContainer.addMacro("TYPE", "1527")  #
       #linkingContainer.addMacro("NODE", nodefull)  #
        linkingContainer.setPropertyValue("resize_behaviour", 1)  #size container to .opi
        linkingContainer.setPropertyValue("border_style", 0)      #no border
        linkingContainer.setPropertyValue("background_color", "OPI_Background")
        widget.addChildToBottom(linkingContainer)     #add to bottom of current group
    
        linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer")
        linkingContainer.setPropertyValue("opi_file", "HVSiblingHeader.opi")
        linkingContainer.setPropertyValue("resize_behaviour", 1)  #size container to .opi
        linkingContainer.setPropertyValue("border_style", 0)      #no border
        linkingContainer.setPropertyValue("background_color", "OPI_Background")
        widget.addChildToBottom(linkingContainer)     #add to bottom of current group

        linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer")
        linkingContainer.setPropertyValue("opi_file", "HVSiblings.opi")
        linkingContainer.setPropertyValue("resize_behaviour", 1)  #size container to .opi
        linkingContainer.setPropertyValue("border_style", 0)      #no border
        linkingContainer.setPropertyValue("background_color", "OPI_Background")
        widget.addChildToBottom(linkingContainer)     #add to bottom of current group
        
        
