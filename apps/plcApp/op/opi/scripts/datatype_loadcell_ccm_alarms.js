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
		lc.setPropertyValue("opi_file","alarm_aiao_row.opi");
		lc.setPropertyValue("auto_size",true);
		lc.setPropertyValue("zoom_to_fit",false);
		lc.setPropertyValue("border_style",0);
		// example: B_TORUS:FOR:CCM_A:LC817A1
		lc.setPropertyValue("background_color","OPI_Background");
		lc.setPropertyValue("x", 10);
		DESC = ELM[i] + ":LC817" + ID[i] + n;
		PV_NAME = P + R + ELM[i] + ":LC817" + ID[i] + n;
		lc.addMacro("LABEL", DESC);
		lc.addMacro("PV", PV_NAME);
		widget.addChildToBottom(lc);
	}
}

var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
lc.setPropertyValue("opi_file","alarm_aiao_row.opi");
lc.setPropertyValue("auto_size",true);
lc.setPropertyValue("zoom_to_fit",false);
lc.setPropertyValue("border_style",0);
lc.setPropertyValue("background_color","OPI_Background");
lc.setPropertyValue("x", 10);
DESC = "HUB:" + "LC817H1";
PV_NAME = P + R + "HUB:LC817H1";
lc.addMacro("LABEL", DESC);
lc.addMacro("PV", PV_NAME);
widget.addChildToBottom(lc);

var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
lc.setPropertyValue("opi_file","alarm_aiao_row.opi");
lc.setPropertyValue("auto_size",true);
lc.setPropertyValue("zoom_to_fit",false);
lc.setPropertyValue("border_style",0);
lc.setPropertyValue("background_color","OPI_Background");
lc.setPropertyValue("x", 10);
DESC = "HUB:" + "LC817H4";
PV_NAME = P + R + "HUB:LC817H4";
lc.addMacro("LABEL", DESC);
lc.addMacro("PV", PV_NAME);
widget.addChildToBottom(lc);
