from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
import nodeLoader
from java.util import Arrays

#Update the list of items in combo widget to choose an element from under a node of the CLAS EPICS tree. 
#Triggered by selection of a new node using the local PV loc://$(DID)_NODE
#It makes the item list of all the elements under that node and sets the selected to 1st in the list

nodeLoader.readTree()                        #make sure the node tree is made

nodefull = PVUtil.getString(pvArray[0])      #Full name of the node Eg. B_SYS_HV_ECAL_SEC1
       
itemlist = ["Element"]                       #start off the default itemlist
count=1

index =  int(nodeLoader.NodeIndex[nodefull]) #get index of node

#if there are elements, make a list
if ((len(nodeLoader.ElementRange[index])>2)and(len(nodeLoader.ElementNames[index])>2)):
    count=0
    itemlist = []
    fullrange = nodeLoader.ElementRange[index].strip("'") #strip quotes
    fulllow  = int(fullrange.split(",")[0])               #get element range values
    fullhigh = int(fullrange.split(",")[1])

    elementList = nodeLoader.ElementNames[index].strip("'").split(",") #get element names
    
    for t in range(fulllow,fullhigh+1):                   #make list with names and indices
        itemlist.append(nodefull+"_"+elementList[count]+" "+str(t))
        count+=1

widget.setPropertyValue("items",Arrays.asList(itemlist) ) #set the relevant props
widget.setPropertyValue("height",24*count )
widget.setPropertyValue("pv_value", itemlist[0] )

pvArray[1].setValue(itemlist[0]) #make the pv the 1st item on the list
        
