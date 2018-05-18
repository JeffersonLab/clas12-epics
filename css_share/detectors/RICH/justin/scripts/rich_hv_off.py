from org.csstudio.opibuilder.scriptUtil import PVUtil


PREFIX = "B_DET_RICH_HV_SEC1"

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

for i in ARRAY:
	for j in i:
		pv = PREFIX+"_ROW"+str(rowcount)+"_PANEL"+str(panelnum)+":pwonoff"
		PVUtil.writePV(pv,0)
		panelnum+=1
	rowcount+=1
	panelnum=1
		
