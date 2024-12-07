from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
import fnmatch
import nodeLoader
import array
import math

nodeLoader.readTree()                              #Read in the node tree
views=["B_SYS_HV","B_HW_HV"]                       #list of possible views

topnode    = str(widget.getMacroValue("TOP"))      #Get the top node
rangemode  = str(widget.getMacroValue("SCALE"))    #Get the scale for the (= Whole or Part)
title      = str(widget.getMacroValue("TITLE"))    #Get the title
node       = PVUtil.getString(pvArray[0])          #Get the current node from local pv
rangepv    = PVUtil.getDoubleArray(pvArray[1])

if node.find(topnode) <0:                    #if the node doesn't contain topnode
	node = topnode                             #force to top
#ConsoleUtil.writeInfo("Node = "+node+"  Top = "+topnode)
view=-1                                            #init index of view
for n in range(len(views)):                        #find the vew for this node
        if node.find(views[n]) > -1:
                view=n
                
if view > -1:                                      #if it's a valid view 

 
        widget.setPropertyValue("axis_1_auto_scale","true")
        if node in nodeLoader.NodeIndex:           #check for node and get index
                #ConsoleUtil.writeInfo("Node = "+node+"  Top = "+topnode)
                index  =  int(nodeLoader.NodeIndex[node])
                erange = nodeLoader.ElementRange[index].strip("'")
                #ConsoleUtil.writeInfo("Erange = "+erange)
 
                index = int(nodeLoader.NodeIndex[views[n]]) #find the range for the whole system
                fullrange = nodeLoader.ElementRange[index].strip("'")
                #ConsoleUtil.writeInfo("FullErange = "+fullrange)
                fulllow  = int(fullrange.split(",")[0]) #get element range values
                fullhigh = int(fullrange.split(",")[1])


                low=int(widget.getPropertyValue("axis_0_minimum")) #default to keeping current axisi limites
                high=int(widget.getPropertyValue("axis_0_maximum"))

                if len(erange)>1:
                        low  = int(erange.split(",")[0])-0.5 #get element range values
                        high = int(erange.split(",")[1])+0.5
                        limitArray = array.array('d', [low,low,high,high,low,low,high,high])
                        pvArray[1].setValue(limitArray)  #set the limits 
                        

                #if 'Whole' in wname:                    #if the name contains "Whole" the set the x range to full for the system 
                if rangemode =="Whole":                    #if the name contains "Whole" the set the x range to full for the system 
                        widget.setPropertyValue("show_legend","false")
                        widget.setPropertyValue("axis_1_visible","false")
                        
                        if len(fullrange)>1:
                                low  = fulllow
                                high = fullhigh
                                

                widget.setPropertyValue("axis_0_minimum",str(low))
                widget.setPropertyValue("axis_0_maximum",str(high))
                widget.setPropertyValue("trace_0_name",node)
                widget.setPropertyValue("title",title)

                limitArray = array.array('d', [-1000,-1000])
                pvArray[2].setValue(limitArray)  #set the limits                         

if widget.getMacroValue("NTRACE"):   #if there are some traces defined

        trace_count = int(widget.getPropertyValue("trace_count"))        #get the number already set
        ntrace      = 2+int(widget.getMacroValue("NTRACE"))              #Get the req number

        if not trace_count == ntrace:    # not created yet
                widget.setPropertyValue("trace_count",str(ntrace))
                #widget.setPropertyValue("show_toolbar","true")

                #Set some default values and see if there are macros to override them.
                title      = "Monitor graph"
                if str(widget.getMacroValue("TITLE")):
                        title      = str(widget.getMacroValue("TITLE")) 

                for n in range(2,ntrace): # look for values for each trace
                        macroname    = "TRACE"+str(n)
                        if widget.getMacroValue(macroname):
                                trace_pv     =  widget.getMacroValue(macroname)
                        else:
                                ConsoleUtil.writeInfo("ERROR: Need macro " + macroname + "to be defined to set the trace PV")      

                        point_size = 4 #defailt to 4   
                        macroname   = "POINT_SIZE_"+str(n)
                        if widget.getMacroValue(macroname):
                                point_size     =  widget.getMacroValue(macroname)

                        if trace_pv:
                                trace_name=views[view]+":"+trace_pv+"_wf"                
                                widget.setPropertyValue("trace_"+str(n)+"_x_axis_index","0")
                                widget.setPropertyValue("trace_"+str(n)+"_update_mode","3")
                                widget.setPropertyValue("trace_"+str(n)+"_point_size",point_size)
                                widget.setPropertyValue("trace_"+str(n)+"_name",trace_pv)
                                widget.setPropertyValue("trace_"+str(n)+"_point_style","1")
                                widget.setPropertyValue("trace_"+str(n)+"_y_pv",trace_name)
                                widget.setPropertyValue("trace_"+str(n)+"_y_axis_index","1")
                                widget.setPropertyValue("trace_"+str(n)+"_trace_type","2")
                                widget.setPropertyValue("trace_"+str(n)+"_plot_mode","0")
                                widget.setPropertyValue("trace_"+str(n)+"_concatenate_data","false")
                                widget.setPropertyValue("trace_"+str(n)+"_buffer_size",str(fullhigh+1))
                                
widget.setPropertyValue("axis_1_auto_scale","true")
#widget.setPropertyValue("axis_1_auto_scale","false")
