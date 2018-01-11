from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
ch = int(PVUtil.getDouble(pvArray[0]))

desc = widget.getPropertyValue("tooltip")
#ConsoleUtil.writeInfo(desc)
currhv = -1
if len(desc) > 2:
        ConsoleUtil.writeInfo("Desc = "+desc)
        currhv = int(desc[desc.find("HVChan")+7:])
        ConsoleUtil.writeInfo("Currhv = " + str(currhv) )
        if currhv < 0:
                hv="1"

        else:
                hv = PVUtil.getString(pvArray[1])

if (int(hv) != currhv):
        widget.removeAllChildren()                          #clean the area first


        linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
        linkingContainer.setPropertyValue("opi_file", "chan8.opi")
        linkingContainer.addMacro("ID", str(ch).zfill(3))
        #linkingContainer.addMacro("ID", ch)
        linkingContainer.addMacro("HV", str(hv.zfill(2)))
        linkingContainer.setPropertyValue("resize_behaviour", 1)
        linkingContainer.setPropertyValue("border_style", 0)
        widget.addChild(linkingContainer)
        
        widget.setPropertyValue("tooltip","ChanHV " + hv)
        
