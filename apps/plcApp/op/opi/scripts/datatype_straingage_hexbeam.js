importPackage(Packages.org.csstudio.opibuilder.scriptUtil);


var run = PVUtil.getDouble(pvs[0]);

var P = widget.getMacroValue("P");
var R = widget.getMacroValue("R");

var ELM = ["HB_US_S1", "HB_US_S2", "HB_US_S3", "HB_US_S4", "HB_US_S5", 
		   "HB_DS_S1", "HB_DS_S2","HB_DS_S3","HB_DS_S4","HB_DS_S5",];
var CNT = 2;


for (var i=0; i<ELM.length; i++) {
	for (var n=1; n<=CNT; n++) {
		var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
		lc.setPropertyValue("opi_file","/CLAS12_Share/apps/plcApp/datatype_straingage_row.opi");
		lc.setPropertyValue("auto_size",true);
		lc.setPropertyValue("zoom_to_fit",false);
		lc.setPropertyValue("border_style",0);
		lc.setPropertyValue("background_color","OPI_Background");
		lc.addMacro("ELM", ELM[i]);
		lc.addMacro("N", n);
		widget.addChildToBottom(lc);
	}
}
