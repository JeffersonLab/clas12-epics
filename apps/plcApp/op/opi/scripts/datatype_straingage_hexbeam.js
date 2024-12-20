importPackage(Packages.org.csstudio.opibuilder.scriptUtil);


var run = PVUtil.getDouble(pvs[0]);

var P = widget.getMacroValue("P");
var R = widget.getMacroValue("R");

var ELM = ["HB_US_S1", "HB_US_S2", "HB_US_S3", "HB_US_S4", "HB_US_S5", "HB_US_S6", 
		   "HB_DS_S1", "HB_DS_S2","HB_DS_S3","HB_DS_S4","HB_DS_S5", "HB_DS_S6"];
var ID  = ["U1HB", "U2HB", "U3HB", "U4HB", "U5HB", "U6HB",
		   "D1HB", "D2HB", "D3HB", "D4HB", "D5HB", "D6HB"];
var CNT = 2;


for (var i=0; i<ELM.length; i++) {
	for (var n=1; n<=CNT; n++) {
		var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
		lc.setPropertyValue("opi_file","datatype_straingage_row.opi");
		lc.setPropertyValue("auto_size",true);
		lc.setPropertyValue("zoom_to_fit",false);
		lc.setPropertyValue("border_style",0);
		lc.setPropertyValue("background_color","OPI_Background");
		lc.addMacro("ELM", ELM[i]);
		lc.addMacro("ID", ID[i]);
		lc.addMacro("N", n);
		widget.addChildToBottom(lc);
	}
}

var ELM = ["HB_US_S1_VS", "HB_US_S4_VS", "HB_DS_S1_VS", "HB_DS_S4_VS"];
var ID  = ["U1HB", "U4HB", "D1HB", "D4HB"];

for (var i=0; i<ELM.length; i++) {
	for (var n=3; n<=4; n++) {
		var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
		lc.setPropertyValue("opi_file","datatype_straingage_row.opi");
		lc.setPropertyValue("auto_size",true);
		lc.setPropertyValue("zoom_to_fit",false);
		lc.setPropertyValue("border_style",0);
		lc.setPropertyValue("background_color","OPI_Background");
		lc.addMacro("ELM", ELM[i]);
		lc.addMacro("ID", ID[i]);
		lc.addMacro("N", n);
		widget.addChildToBottom(lc);
	}
}
