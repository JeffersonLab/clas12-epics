importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

function createRow(desc, pv_name) {
	var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
	lc.setPropertyValue("opi_file","torus_qd_stats_row.opi");
	lc.setPropertyValue("auto_size",true);
	lc.setPropertyValue("zoom_to_fit",false);
	lc.setPropertyValue("border_style",0);
	lc.setPropertyValue("background_color","OPI_Background");
	lc.setPropertyValue("x", 0);
	lc.addMacro("DESC", desc);
	lc.addMacro("P", pv_name);
	widget.addChildToBottom(lc);
}

var run = PVUtil.getDouble(pvs[0]);
var P 	= "B_SOL:QD:VT";

for (var i=1; i<=21; i++) {
	DESC = "VT" + i;
	PV_NAME = P + i;
	createRow(DESC, PV_NAME);
}

createRow("IDCCT1", "B_SOL:QD:IDCCT1");