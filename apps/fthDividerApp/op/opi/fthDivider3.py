from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil

hvstr  =  PVUtil.getString(pvArray[0])
hvinfo = hvstr.split(",")

hv = hvinfo[3]
board =  hvinfo[4]
half =  hvinfo[5]


chstr  = PVUtil.getString(pvArray[1])
chlist = chstr.split(",")
nchan = len(chlist)

ch2 = PVUtil.getString(pvArray[2])

ConsoleUtil.writeInfo("pv0=" + hvstr)
ConsoleUtil.writeInfo("pv1=" + chstr)
ConsoleUtil.writeInfo("pv2=" + ch2)

#ConsoleUtil.writeInfo(str(xcoords[5]))
for n in range(0,nchan):
        ConsoleUtil.writeInfo("Chann" + str(n));
        linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
        linkingContainer.setPropertyValue("opi_file", "chan1.opi")
        linkingContainer.addMacro("ID", chlist[n])
        linkingContainer.setPropertyValue("resize_behaviour", 1)
        linkingContainer.setPropertyValue("border_style", 0)
        widget.addChildToBottom(linkingContainer)

linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
linkingContainer.setPropertyValue("opi_file", "grouphv.opi")
linkingContainer.addMacro("HV", hv)
linkingContainer.addMacro("BOARD", board)
linkingContainer.addMacro("HALF", half)
linkingContainer.setPropertyValue("resize_behaviour", 1)
linkingContainer.setPropertyValue("border_style", 0)
widget.addChildToBottom(linkingContainer)
