from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
slot = PVUtil.getDoubleArray(pvArray[0])
chan = PVUtil.getDoubleArray(pvArray[1])

wlayer  = int(widget.getMacroValue("LAYER"))
#P       = widget.getMacroValue("P")

side=24

#ConsoleUtil.writeInfo(str(xcoords[5]))
for n in range(0,232):
        linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
        linkingContainer.setPropertyValue("opi_file", "tile.opi")
        if (n==224):
                linkingContainer.addMacro("ID",str(225).zfill(3))
        elif (n==225):
                linkingContainer.addMacro("ID",str(227).zfill(3))
        elif (n==226):
                linkingContainer.addMacro("ID",str(228).zfill(3))
        elif (n==227):
                linkingContainer.addMacro("ID",str(230).zfill(3))
        elif (n==228):
                linkingContainer.addMacro("ID",str(233).zfill(3))
        elif (n==229):
                linkingContainer.addMacro("ID",str(235).zfill(3))
        elif (n==230):
                linkingContainer.addMacro("ID",str(236).zfill(3))
        elif (n==231):
                linkingContainer.addMacro("ID",str(238).zfill(3))
        else:
                linkingContainer.addMacro("ID", str(n).zfill(3))
        #linkingContainer.addMacro("ID", str(n).zfill(3))
        linkingContainer.setPropertyValue("resize_behaviour", 2)
        linkingContainer.setPropertyValue("border_style", 2)
        s = int(slot[n])
        c = int(chan[n])
        print n," ",s," ",c," ",str(n).zfill(3)
        #ConsoleUtil.writeInfo(str(l) + "    " + str(wlayer))
        posx=s*side - 40;
        posy=c*side;
        linkingContainer.setPropertyValue("x", posx)
        linkingContainer.setPropertyValue("y", posy)
        linkingContainer.setPropertyValue("width", str(side-1))
        linkingContainer.setPropertyValue("height",str(side-1))
        widget.addChild(linkingContainer)

