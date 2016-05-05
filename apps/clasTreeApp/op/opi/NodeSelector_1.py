from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
import nodeLoader
from java.util import Arrays

#This is the code to update the list of items in combo widget to chose a node
#in the CLAS EPICS tree. 
#It is triggered by selection of a new node using the local PV loc://$(DID)_NODE
#It makes the item list of all the ancestors, the node, and the subnodes

nodeLoader.readTree()                        #make sure the node tree is made

nodefull = PVUtil.getString(pvArray[0])      #Full name of the node Eg. B_SYS_HV_ECAL_SEC1
topnode  = widget.getMacroValue("TOP")       #Name of the top node  Eg. B_SYS_HV
ntop     = len(topnode.split("_"))           #Work out the no of levels in the top node (eg. 3 here)

if nodefull.find(topnode) < 0:               #if topnode not in fullnode
    nodefull=topnode                         #set to topnode

nlist    = nodefull.split("_")               #Split the full nodename into a list
node     = topnode                           #Start off the node that this combo will display
       
itemlist = []                                #start off the itemlist

for t in range(ntop,len(nlist)):             #Construct it's node name
    itemlist.append(node)                    #Append to the item list
    node = node+"_"+str(nlist[t])

itemlist.append(nodefull)                    #now add the node again

index =  int(nodeLoader.NodeIndex[node])     #get subnodes
subnodes = nodeLoader.SubNodeNames[index].rstrip("'").lstrip("'").split(",")
            
if len(subnodes[0]):                         #if there are subnodes
    for i in range(len(subnodes)):           #make a list, sort it and start it with this node
        subnodes[i]=node+"_"+subnodes[i]
    subnodes.sort()
    itemlist=itemlist+subnodes;

widget.setPropertyValue("items",Arrays.asList(itemlist) ) #set the relevant props
widget.setPropertyValue("height",24*len(subnodes) )
widget.setPropertyValue("pv_value",node )


        
