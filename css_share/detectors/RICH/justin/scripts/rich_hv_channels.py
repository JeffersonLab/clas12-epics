from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import WidgetUtil
PREFIX = "B_DET_RICH_HV_SEC1"
novice = PVUtil.getDouble(pvs[0]);
ARRAY = [[2,3,3,3,3,3,3,3,3,2],
			[3,3,3,3,3,3,3,3,3],
			[2,3,3,3,3,3,3,3,3],
			[2,3,3,3,3,3,3,3,2],
			[3,3,3,3,3,3,3,3],
			[2,3,3,3,3,3,3,3],
			[2,3,3,3,3,3,3,2],
			[3,3,3,3,3,3,3],
			[2,3,3,3,3,3,3],
			[2,3,3,3,3,3,2],
			[3,3,3,3,3,3],
			[2,3,3,3,3,3],
			[2,3,3,3,3,2],
			[3,3,3,3,3],
			[2,3,3,3,3],
			[2,3,3,3,2],
			[3,3,3,3],
			[2,3,3,3],
			[2,3,3,2],
			[3,3,3],
			[3,2,3],
			[2,3,2],
			[3,3]];
			
panelnum=1
rowcount=1
count=1

for i in ARRAY:
	for j in i:
		lc =  WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer")
		if (novice>0): 
			lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel_novice.opi")
            	else:          
			lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel.opi")
		lc.setPropertyValue("auto_size",True)
		lc.setPropertyValue("zoom_to_fit",False)
            	lc.setPropertyValue("border_style",0)
            	lc.setPropertyValue("background_color","Header_Background")
            	lc.addMacro("C",str(count))
		pv = PREFIX+"_ROW"+str(rowcount)+"_PANEL"+str(panelnum)
            	lc.addMacro("P",pv)
           	widget.addChildToBottom(lc)
		panelnum+=1
		count+=1
	rowcount+=1
	panelnum=1
		
