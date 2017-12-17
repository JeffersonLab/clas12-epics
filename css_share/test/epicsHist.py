from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil
#PVs are
#0 $(P)_XMIN
#1 local XMIN
#2$(P)_XMAX
#3local XMAX
#4 $(P)_NBINSX
#5 local_NBINSX
#6 $(P)_DATA.NELM
#7 $(P)_XTITLE
#8 local_XTITLE
#9 $(P)_YTITLE
#10 local_YTITLE
#11 local TRACETYPE


init=widget.getPropertyValue("border_width") #misuse this as an init flag

if init==0: 									 #if not already initialised	
	xmin    = PVUtil.getDouble(pvArray[0])   #get all the PVs
	lxmin   = PVUtil.getDouble(pvArray[1])
	xmax    = PVUtil.getDouble(pvArray[2])
	lxmax   = PVUtil.getDouble(pvArray[3])
	nbinsx  = PVUtil.getLong(pvArray[4])
	lnbinsx = PVUtil.getLong(pvArray[5])
	nelm    = PVUtil.getLong(pvArray[6])
	xt      = PVUtil.getStringArray(pvArray[7])
	lxt     = PVUtil.getString(pvArray[8])
	yt      = PVUtil.getStringArray(pvArray[9])
	lyt     = PVUtil.getString(pvArray[10])
	trace   = PVUtil.getLong(pvArray[11])

	xt    = list(map(int, xt))              #convert the waveforms into strings - ugly!
	xtstr = "".join([chr(c) for c in xt])
	yt    = list(map(int, yt))
	ytstr = "".join([chr(c) for c in yt])
    

#in all cases we let the local PVs (from MACROS) override those from the ioc,

#for axes, if XMAX<XMIN it means the variables are not filled - do it anther way.

	if(lxmin<lxmax):     #test macro version first
		xminval=lxmin
		xmaxval=lxmax
	elif(xmin<xmax):
		xminval=xmin
		xmaxval=xmax
	else:
		xminval=0.0;
		xmaxval=nelm
		
	if(lnbinsx>0):
		nbinsval=lnbinsx
	elif(nbinsx>0):
		nbinsval=nbinsx
	else:
		nbinsval=nelm
					
	if len(lxt)>2:
		xtval=lxt
	elif(len(xtstr)>2):
		xtval=xtstr
	else:
		xtval=''
		
	if len(lyt)>2:
		ytval=lyt
	elif(len(ytstr)>2):
		ytval=ytstr
	else:
		ytval=''

	if((trace>=0) and (trace<=5)):
		traceval=trace	
	else:
		traceval=0
		
	widget.setPropertyValue("axis_2_axis_title", xtval)	
	widget.setPropertyValue("axis_1_axis_title", ytval)	
	widget.setPropertyValue("axis_2_minimum", xminval)	
	widget.setPropertyValue("axis_2_maximum", xmaxval)
	widget.setPropertyValue("trace_0_buffer_size", nbinsval)
	widget.setPropertyValue("trace_0_trace_type", traceval)
	
	widget.setPropertyValue("border_width",1) #misuse this as an init flag
