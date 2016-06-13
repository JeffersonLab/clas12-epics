from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
#select next or previous sibling in nodelist

combo    = display.getWidget("Node_Selector_Combo")
nodelist = combo.getPropertyValue("items")


listlen  = len(nodelist)
nodefull = PVUtil.getString(pvArray[1])
inc      = int(PVUtil.getLong(pvArray[0]))
index    = nodelist.index(nodefull)
nodelen  = len(nodefull.split("_"))

#ConsoleUtil.writeInfo(nodefull + " inc " + str(inc)+ "  index " + str(index) + " len " + str(listlen))

if not inc == 0:
    index   += inc
    if (index >=0) and (index < listlen):
        node = nodelist[index]
        if len(node.split("_")) == nodelen:
               combo.setPropertyValue("pv_value",node )   
               pvArray[1].setValue(node)
               pvArray[0].setValue("0")

        


        
