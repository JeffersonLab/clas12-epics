from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
slotlist   = PVUtil.getString(pvArray[0])
#P should be the Crate. eg B_DET_MM_FEU_Cr1
P          = widget.getMacroValue("P")
C          = widget.getMacroValue("CRATE")

slots = slotlist.split()
#ConsoleUtil.writeInfo(str(slots))
for n in range(0,len(slots)):
        linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer") 
        linkingContainer.setPropertyValue("opi_file", "slot_full.opi")
        newP = P+"_Cr"+C+"_Sl"+slots[n]
        #ConsoleUtil.writeInfo(newP)
        linkingContainer.addMacro("P",newP)
        linkingContainer.setPropertyValue("resize_behaviour", 1)
        #linkingContainer.setPropertyValue("border_style", 2)
        widget.addChildToBottom(linkingContainer)
