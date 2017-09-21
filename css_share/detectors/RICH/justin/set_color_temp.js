importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var istatus;
try { istatus = PVUtil.getDouble(pvs[0]) | 0; }
catch (ee) { }

//var type = widget.getMacroValue("TYPE");

//java.lang.System.out.println("set_color_temp.js");

var min=0;
var max=100;
var nbins=10;


var temp = PVUtil.getDouble(pvs[0]);

//java.lang.System.out.println(temp);

bin = Math.floor((temp-min)/(max-min)*nbins);

//java.lang.System.out.println(bin);

var bgcolors=["MEDM_COLOR_28","MEDM_COLOR_52","MEDM_COLOR_50","MEDM_COLOR_61","MEDM_COLOR_63","MEDM_COLOR_30","MEDM_COLOR_32","MEDM_COLOR_34","MEDM_COLOR_20","MEDM_COLOR_23"];

widget.setPropertyValue("background_color",bgcolors[bin]);
