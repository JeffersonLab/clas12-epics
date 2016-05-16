importPackage(Packages.org.csstudio.opibuilder.scriptUtil);


var run = PVUtil.getDouble(pvs[0]);

var P = widget.getMacroValue("P");
var R = widget.getMacroValue("R");

var ELM = ["HB_US_S1", "HB_US_S2", "HB_US_S3", "HB_US_S4", "HB_US_S5", 
		   "HB_DS_S1", "HB_DS_S2","HB_DS_S3","HB_DS_S4","HB_DS_S5"];
var ID  = ["U1HB", "U2HB", "U3HB", "U4HB", "U5HB",
		   "D1HB", "D2HB", "D3HB", "D4HB", "D5HB"];
var CNT = 2;


for (var i=0; i<ELM.length; i++) {
	for (var n=1; n<=CNT; n++) {
		var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
		lc.setPropertyValue("opi_file","/CLAS12_Share/apps/plcApp/datatype_straingage_alarm_row.opi");
		lc.setPropertyValue("auto_size",true);
		lc.setPropertyValue("zoom_to_fit",false);
		lc.setPropertyValue("border_style",0);
		// example: B_TORUS:FOR:CCM_A:LC817A1
		lc.setPropertyValue("background_color","OPI_Background");
		lc.setPropertyValue("x", 10);
		DESC = "SG817" + ID[i] + n + ":Force";
		PV_NAME = P + R + ELM[i] + ":SG817" + ID[i] + n + ":Force";
		lc.addMacro("LABEL", DESC);
		lc.addMacro("PV", PV_NAME);
		widget.addChildToBottom(lc);
	}
}

var ELM = ["HB_US_S1_VS", "HB_US_S4_VS", "HB_DS_S1_VS", "HB_DS_S4_VS"];
var ID  = ["U1HB", "U4HB", "D1HB", "D4HB"];

for (var i=0; i<ELM.length; i++) {
	for (var n=3; n<=4; n++) {
		var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
		lc.setPropertyValue("opi_file","/CLAS12_Share/apps/plcApp/datatype_straingage_alarm_row.opi");
		lc.setPropertyValue("auto_size",true);
		lc.setPropertyValue("zoom_to_fit",false);
		lc.setPropertyValue("border_style",0);
		// example: B_TORUS:FOR:CCM_A:LC817A1
		lc.setPropertyValue("background_color","OPI_Background");
		lc.setPropertyValue("x", 10);
		DESC = "SG817" + ID[i] + n + ":Force";
		PV_NAME = P + R + ELM[i] + ":SG817" + ID[i] + n + ":Force";
		lc.addMacro("LABEL", DESC);
		lc.addMacro("PV", PV_NAME);
		widget.addChildToBottom(lc);
	}
}
