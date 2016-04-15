importPackage(Packages.org.csstudio.opibuilder.scriptUtil);


var run = PVUtil.getDouble(pvs[0]);

var P = widget.getMacroValue("P");
var R = widget.getMacroValue("R");

var ELM = ["CCM_A", "CCM_B", "CCM_C", "CCM_D", "CCM_E", "CCM_F"];
var CNT = 4;


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

