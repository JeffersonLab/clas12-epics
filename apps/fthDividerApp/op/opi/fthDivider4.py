from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
slot = PVUtil.getDoubleArray(pvArray[0])
chan = PVUtil.getDoubleArray(pvArray[1])
xarray = PVUtil.getDoubleArray(pvArray[3])

wlayer  = int(widget.getMacroValue("LAYER"))
#P       = widget.getMacroValue("P")

side=24

#ConsoleUtil.writeInfo(str(xcoords[5]))
for n in range(0,240):
        linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
        linkingContainer.setPropertyValue("opi_file", "tile.opi")
        if(xarray[n]<900):
	       	linkingContainer.addMacro("ID", str(n).zfill(3))
    	    #linkingContainer.addMacro("ID", str(n).zfill(3))
        	linkingContainer.setPropertyValue("resize_behaviour", 2)
        	linkingContainer.setPropertyValue("border_style", 2)
        	s = int(slot[n])
        	c = int(chan[n])
        	print n," ",s," 	",c," ",str(n).zfill(3)
        	#ConsoleUtil.writeInfo(str(l) + "    " + str(wlayer))
        	posx=s*side - 40;
        	posy=c*side;
        	linkingContainer.setPropertyValue("x", posx)
        	linkingContainer.setPropertyValue("y", posy)
        	linkingContainer.setPropertyValue("width", str(side-1))
        	linkingContainer.setPropertyValue("height",str(side-1))
        	widget.addChild(linkingContainer)

