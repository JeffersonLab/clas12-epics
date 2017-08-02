importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var istatus;
try { istatus = PVUtil.getDouble(pvs[0]) | 0; }
catch (ee) { }

//var type = widget.getMacroValue("TYPE");

//java.lang.System.out.println("set_color_temp.js");

var min=0;
var max=100;
var nbins =10;


var temp = PVUtil.getDouble(pvs[0]);

//java.lang.System.out.println(temp);

bin = Math.floor((temp-min)/(max-min)*nbins);

//java.lang.System.out.println(bin);


var bgcolors=["c1","c2","c3","c4","c5","c6","c7","c8","c9","c10"];

widget.setPropertyValue("background_color",bgcolors[bin]);