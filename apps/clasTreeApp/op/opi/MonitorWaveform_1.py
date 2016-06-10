from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
import fnmatch
import nodeLoader
import array
import math

element    = PVUtil.getString(pvArray[0])          #Get the current node from local pv
rangepv    = PVUtil.getDoubleArray(pvArray[1])

elem  = ""
index = -100

#ConsoleUtil.writeInfo("Element = " + element )
if len(element.split()) >= 2:
        elem = element.split()[0]
        selem = elem.split("_")[len(elem.split("_"))-1]
        index = int( element.split()[1])

        #ConsoleUtil.writeInfo("Element = " + element + "  " + elem + "  " + str(index))

        limitArray = array.array('d', [index,index])
        pvArray[1].setValue(limitArray)  #set the limits 
                        
        widget.setPropertyValue("trace_1_visible","true")
        widget.setPropertyValue("trace_1_name",selem)
        widget.setPropertyValue("trace_1_trace_color","OPI_Background")
                                        
else:
        widget.setPropertyValue("trace_1_visible","false")
        widget.setPropertyValue("trace_1_trace_color","Write_Background")
