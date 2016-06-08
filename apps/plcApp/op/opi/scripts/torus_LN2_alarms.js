importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

function createAlarmRow(desc, pv_name) {
	var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
	lc.setPropertyValue("opi_file","/CLAS12_Share/alarms/alarm_aiao_row.opi");
	lc.setPropertyValue("auto_size",true);
	lc.setPropertyValue("zoom_to_fit",false);
	lc.setPropertyValue("border_style",0);
	lc.setPropertyValue("background_color","OPI_Background");
	lc.setPropertyValue("x", 10);
	lc.addMacro("LABEL", desc);
	lc.addMacro("PV", pv_name);
	widget.addChildToBottom(lc);
}

var run = PVUtil.getDouble(pvs[0]);
var P 	= "B_TORUS:";
var R   = "LN2:";

//
// CCM_[A-F]:PT100_[1-5] 
//
var CCM = ["A", "B", "C", "D", "E", "F"];

for (var i=0; i<CCM.length; i++) {
	for (var j=1; j<=5; j++) {
		DESC 	= R + "CCM_" + CCM[i] + ":PT100_" + j;
		PV_NAME = P + DESC;
		createAlarmRow(DESC, PV_NAME);
	}
}

//
// cPIDs
//
var PID = ["EV8555T", "EV8556T", "HTR8559"];
var SFX = ["", ":CVAL", ":ORBV", ":VAL"];

for (var i=0; i<PID.length; i++) {
	for (var j=0; j<SFX.length; j++) {
		DESC 	= R + PID[i] + SFX[j];
		PV_NAME = P + DESC;
		createAlarmRow(DESC, PV_NAME);
	}
}

//
// Misc.
//
var PV = ["LL8152CP", "LL8152DP", "PT8151", "PT8152", "TC8559F", "TC8559M", "TP8151", "TP8152"];
for (var i=0; i<PV.length; i++) {
	DESC 	= R + PV[i];
	PV_NAME = P + DESC;
	createAlarmRow(DESC, PV_NAME);
}

//
// TP815* 
//
var PFX = "TP815";
var SFX = ["AR", "BR", "CR", "DR", "DSHRN", "DSHRS", "ER", "FR"];
for (var i=0; i<SFX.length; i++) {
	DESC 	= R + PFX + SFX[i];
	PV_NAME = P + DESC;
	createAlarmRow(DESC, PV_NAME);
} 