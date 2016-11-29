importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

function createAlarmRow(pv_name) {
	var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
	lc.setPropertyValue("opi_file","../../alarms/alarm_aiao_row.opi");
	lc.setPropertyValue("auto_size",true);
	lc.setPropertyValue("zoom_to_fit",false);
	lc.setPropertyValue("border_style",0);
	lc.setPropertyValue("background_color","OPI_Background");
	lc.setPropertyValue("x", 10);
	lc.addMacro("LABEL", pv_name);
	lc.addMacro("PV", pv_name);
	widget.addChildToBottom(lc);
}

var run = PVUtil.getDouble(pvs[0]);
var P 	= widget.getMacroValue("P");
var R 	= widget.getMacroValue("R");

createAlarmRow("B_TORUS:LHe:TR8114R");
createAlarmRow("B_TORUS:LHe:TR8114S");

//
// TR817[A-F][1-9], TR817[A-F][R-S] 
//
var ELM = "TR817";
var ID  = ["A", "B", "C", "D", "E", "F"];
var SUF = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "R", "S"];

for (var i=0; i<ID.length; i++) {
	for (var j=0; j<SUF.length; j++) {
		PV_NAME = P + R + ELM + ID[i] + SUF[j];
		createAlarmRow(PV_NAME);
	}
}

//
// TR817D[1-6]HB1
//
for (var j=1; j<=6; j++) {
	PV_NAME = P + R + "TR817D" + j + "HB1";
	createAlarmRow(PV_NAME);
}

//
// TR817U[1-6]HB[1-2]
//
for (var j=1; j<=6; j++) {
	PV_NAME = P + R + "TR817U" + j + "HB1";
	createAlarmRow(PV_NAME);
	PV_NAME = P + R + "TR817U" + j + "HB2";
	createAlarmRow(PV_NAME);
}

//
// cPIDs
//
var PID = ["EV8111BY", "EV8111CD", "EV8115JT"];
var SFX = ["", ":CVAL", ":VAL"];

for (var i=0; i<PID.length; i++) {
	for (var j=0; j<SFX.length; j++) {
		PV_NAME	= P + R + PID[i] + SFX[j];
		createAlarmRow(PV_NAME);
	}
}
