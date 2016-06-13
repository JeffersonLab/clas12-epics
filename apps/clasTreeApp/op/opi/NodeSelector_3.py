from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil

combo    = display.getWidget("Element_Selector_Combo")
nodelist = combo.getPropertyValue("items")

listlen  = len(nodelist)
nodefull = PVUtil.getString(pvArray[1])
inc      = int(PVUtil.getLong(pvArray[0]))
node     = "Element"

if (not inc == 0) and not (nodelist[0] == "Element"):
    index    = nodelist.index(nodefull)
    #ConsoleUtil.writeInfo(nodefull + " inc " + str(inc)+ "  index " + str(index) + " len " + str(listlen))

    index   += inc
    if (index >=0) and (index < listlen):
        node = nodelist[index]
        combo.setPropertyValue("pv_value",node )   
    if not node == "Element":
        pvArray[1].setValue(node)

pvArray[0].setValue("0")

       


        
