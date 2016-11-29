importPackage(Packages.org.csstudio.opibuilder.scriptUtil);


var run = PVUtil.getDouble(pvs[0]);

var P = widget.getMacroValue("P");
var R = widget.getMacroValue("R");

var ELM = ["CCM_A", "CCM_B", "CCM_C", "CCM_D", "CCM_E", "CCM_F"];
var ID  = ["A", "B", "C", "D", "E", "F"];
var CNT = 4;


for (var i=0; i<ELM.length; i++) {
	for (var n=1; n<=CNT; n++) {
		var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
		lc.setPropertyValue("opi_file","datatype_loadcell_row.opi");
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
	
var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
lc.setPropertyValue("opi_file","datatype_loadcell_row.opi");
lc.setPropertyValue("auto_size",true);
lc.setPropertyValue("zoom_to_fit",false);
lc.setPropertyValue("border_style",0);
lc.setPropertyValue("background_color","OPI_Background");
lc.addMacro("ELM", "HUB");
lc.addMacro("ID", "H");
lc.addMacro("N", 1);
widget.addChildToBottom(lc);

var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
lc.setPropertyValue("opi_file","datatype_loadcell_row.opi");
lc.setPropertyValue("auto_size",true);
lc.setPropertyValue("zoom_to_fit",false);
lc.setPropertyValue("border_style",0);
lc.setPropertyValue("background_color","OPI_Background");
lc.addMacro("ELM", "HUB");
lc.addMacro("ID", "H");
lc.addMacro("N", 4);
widget.addChildToBottom(lc);
