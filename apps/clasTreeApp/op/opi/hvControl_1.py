from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
import nodeLoader
#from java.util import Arrays

#Update the list of items in combo widget to choose an element from under a node of the CLAS EPICS tree. 
#Triggered by selection of a new node using the local PV loc://$(DID)_NODE
#It makes the item list of all the elements under that node and sets the selected to 1st in the list

nodeLoader.readTree()                        #make sure the node tree is made

nodefull = PVUtil.getString(pvArray[0])      #Full name of the node Eg. B_SYS_HV_ECAL_SEC1
if nodeLoader.NodeIndex[nodefull]:           #if its a node
    index =  int(nodeLoader.NodeIndex[nodefull]) #get index of node

widget.removeAllChildren()

if ((len(nodeLoader.ElementRange[index])>2)and(len(nodeLoader.ElementNames[index])>2)):

    elementList = nodeLoader.ElementNames[index].strip("'").split(",") #get element names
    
    for t in range(0,len(elementList)): 
        ConsoleUtil.writeInfo("elem: " + elementList[t])
        linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer")
        linkingContainer.setPropertyValue("opi_file", "hvChanWrapper.opi")
        linkingContainer.addMacro("P", nodefull+"_"+elementList[t])  #
        linkingContainer.addMacro("TYPE", "1527")  #
        linkingContainer.setPropertyValue("resize_behaviour", 1)  #size container to .opi
        linkingContainer.setPropertyValue("border_style", 0)      #no border
        linkingContainer.setPropertyValue("background_color", "OPI_Background")
        widget.addChildToBottom(linkingContainer)     #add to bottom of current group
    
