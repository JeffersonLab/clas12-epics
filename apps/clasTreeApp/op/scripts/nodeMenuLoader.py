from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil

#This script makes NTOT button chioce widgets go be used to browse the EPICS hierarchy.
#There are 2 more scripts associated with menu.opi to make the menuse behave correctly.

#Get the macro NTOT  associated with the widget
NTOT = int(widget.getMacroValue("NTOT"))   #the no of menus to create
for n in range(1, NTOT+1):
    linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer")
    #linkingContainer.setPropertyValue("opi_file", "nodeMenu.opi")
    linkingContainer.setPropertyValue("opi_file", "nodeCombo2.opi")
    linkingContainer.addMacro("N", str(n))
    linkingContainer.setPropertyValue("resize_behaviour", 1)
    linkingContainer.setPropertyValue("border_style", 0)
    #linkingContainer.setPropertyValue("width", 136)
    #linkingContainer.setPropertyValue("height", 150)
    linkingContainer.setPropertyValue("background_color", "OPI_Background")
    widget.addChildToRight(linkingContainer)

#Transfer the to the local NODE variable
pvArray[0].setValue(widget.getMacroValue("P"))
