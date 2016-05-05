from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
import fnmatch
import nodeLoader
from java.util import Arrays

nodeLoader.readTree()                              #Read in the node tree

topnode    = widget.getMacroValue("TOP")           #Get the top node
nodesearch = PVUtil.getString(pvArray[0])          #Get the search string

if nodesearch.find(topnode) <0:                    #if the search doesn't contain topnode
	nodesearch = topnode+"*"                   #force to top + wildcard

if nodesearch in nodeLoader.NodeIndex:             #if it's a node, tag a wildcard on the end 
	nodesearch = nodesearch+"*"

nlist=fnmatch.filter(nodeLoader.NodeNames,nodesearch)       #filter on the node search
nlist.sort()                                                #make a sorted list of them
widget.setPropertyValue("items",Arrays.asList(nlist) )      #set the choice list
widget.setPropertyValue("pv_value",nlist[0] )               #set selected as first in the list
