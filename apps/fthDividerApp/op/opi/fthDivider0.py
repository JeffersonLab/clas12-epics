from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
xcoords = PVUtil.getDoubleArray(pvArray[0])
ycoords = PVUtil.getDoubleArray(pvArray[1])
size    = PVUtil.getDoubleArray(pvArray[2])
layer   = PVUtil.getDoubleArray(pvArray[3])
wlayer  = int(widget.getMacroValue("LAYER"))
#P       = widget.getMacroValue("P")

s=16

#ConsoleUtil.writeInfo(str(xcoords[5]))
for n in range(0,232):
	if not size[n]==999:
		linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
		linkingContainer.setPropertyValue("opi_file", "tile.opi")
		#linkingContainer.addMacro("ID",str(n))
                linkingContainer.addMacro("ID", str(n).zfill(3))
		linkingContainer.setPropertyValue("resize_behaviour", 2)
		linkingContainer.setPropertyValue("border_style", 2)
                l = int(layer[n])
                ConsoleUtil.writeInfo(str(l) + "    " + str(wlayer))
                if l==wlayer:
                    side=s*size[n]
                    posx=(220+s*xcoords[n])
                    posy=(160-s*ycoords[n])
                    if size[n] ==1:
                        posy=posy+s
                    #ConsoleUtil.writeInfo(str(posx) + "    " + str(posy))
                    linkingContainer.setPropertyValue("x", posx)
                    linkingContainer.setPropertyValue("y", posy)
                    linkingContainer.setPropertyValue("width", side)
                    linkingContainer.setPropertyValue("height", side)
                    widget.addChild(linkingContainer)

