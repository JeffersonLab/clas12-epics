from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
import fnmatch
import nodeLoader
import array
import math

nodeLoader.readTree()                              #Read in the node tree
views=["B_SYS_HV"]                                 #list of possible views

topnode    = str(widget.getMacroValue("TOP"))      #Get the top node
node       = PVUtil.getString(pvArray[0])          #Get the current node from local pv
rangepv    = PVUtil.getDoubleArray(pvArray[1])

if node.find(topnode) <0:                    #if the search doesn't contain topnode
	node = topnode                             #force to top
#ConsoleUtil.writeInfo("Node = "+node+"  Top = "+topnode)
view=-1                                            #init index of view
for n in range(len(views)):                        #find the vew for this node
        if node.find(views[n]) > -1:
                view=n
                
if view > -1:                                      #if it's a valid view 

 
        if node in nodeLoader.NodeIndex:           #check for node and get index
                ConsoleUtil.writeInfo("Node = "+node+"  Top = "+topnode)
                index  =  int(nodeLoader.NodeIndex[node])
                erange = nodeLoader.ElementRange[index].strip("'")
                #ConsoleUtil.writeInfo("Erange = "+erange)
 
                index = int(nodeLoader.NodeIndex[views[n]]) #find the range for the whole system
                fullrange = nodeLoader.ElementRange[index].strip("'")
                #ConsoleUtil.writeInfo("FullErange = "+fullrange)
                fulllow  = int(fullrange.split(",")[0]) #get element range values
                fullhigh = int(fullrange.split(",")[1])



                wname=widget.getPropertyValue("name")   #find the name of the widget

                low=int(widget.getPropertyValue("axis_0_minimum")) #default to keeping current axisi limites
                high=int(widget.getPropertyValue("axis_0_maximum"))

                if len(erange)>1:
                        low  = int(erange.split(",")[0]) #get element range values
                        high = int(erange.split(",")[1])
                        limitArray = array.array('d', [low,low,high,high,low,low,high,high])
                        pvArray[1].setValue(limitArray)  #set the limits 
                        

                if 'Whole' in wname:                    #if the name contains "Whole" the set the x range to full for the system 
                        widget.setPropertyValue("show_legend","false")
                        title="Full range of "+views[view]+" (with selected system highlighted)   ."
                        
                        if len(fullrange)>1:
                                low  = fulllow
                                high = fullhigh
                                
                else:
                        low = low  - 0.2*(high-low)   
                        high = high + 0.2*(high-low)
                        title="Expanded range on selected system (highlighted)  ."

                widget.setPropertyValue("axis_0_minimum",str(low))
                widget.setPropertyValue("axis_0_maximum",str(high))
                widget.setPropertyValue("trace_0_name",node)
                widget.setPropertyValue("title",title)
                                        

trace_count = int(widget.getPropertyValue("trace_count"))      #Get the current no of traces
ntrace      = int(widget.getMacroValue("NTRACE"))              #Get the req number

#xpv=widget.getPropertyValue("trace_0_x_pv")

if not ntrace == trace_count:    # if they are the same it's already been called
        widget.setPropertyValue("trace_count",str(ntrace+1))
        for n in range(1,ntrace+1):
                macroname    = "TRACE"+str(n)
                trace_pv =  widget.getMacroValue(macroname)
                ConsoleUtil.writeInfo("TRACE"+str(n)+"="+trace_pv)
                if trace_pv:
                        trace_name=views[view]+":"+trace_pv+"_wf"                
                        widget.setPropertyValue("trace_"+str(n)+"_x_axis_index","0")
                        widget.setPropertyValue("trace_"+str(n)+"_update_mode","3")
                        widget.setPropertyValue("trace_"+str(n)+"_point_size","4")
                        widget.setPropertyValue("trace_"+str(n)+"_name",trace_pv)
                        widget.setPropertyValue("trace_"+str(n)+"_point_style","1")
                        widget.setPropertyValue("trace_"+str(n)+"_y_pv",trace_name)
                        widget.setPropertyValue("trace_"+str(n)+"_y_axis_index","1")
                        widget.setPropertyValue("trace_"+str(n)+"_trace_type","2")
                        widget.setPropertyValue("trace_"+str(n)+"_plot_mode","0")
                        widget.setPropertyValue("trace_"+str(n)+"_concatenate_data","false")
                        widget.setPropertyValue("trace_"+str(n)+"_buffer_size",str(fullhigh+1))
