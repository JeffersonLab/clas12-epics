importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var istatus;
try { istatus = PVUtil.getDouble(pvs[0]) | 0; }
catch (ee) { }

//var type = widget.getMacroValue("TYPE");

//java.lang.System.out.println("set_color_temp.js");

var min=0;
var max=1;
var nbins=10;


var temp = PVUtil.getDouble(pvs[0]);
var screen = widget.getMacroValue("SCREEN");

if(screen== "temp:fpga"||screen=="temp:reg0"||screen=="temp:reg1"){
	min=1;
	max=70;
}
else if(screen=="volt:pcb5"||screen=="volt:pcb3_3"||screen=="volt:int1"||screen=="volt:aux1_8"||screen=="volt:mgt1"||screen=="volt:mgt1_2"){
	min=0;
	max=6;
}
else if (screen=="scalers"){
    max=100;
    min=1;
}
else{
	max=100;
	min=0;
}

display.getWidget("ScaleMax").setPropertyValue("text", max.toString());
display.getWidget("ScaleMin").setPropertyValue("text", min.toString());

if(temp>max)
	bin=10;
else if(temp<min)
	bin=11;
else
	bin = Math.floor((temp-min)/(max-min)*nbins);

//java.lang.System.out.println(bin);

var bgcolors=["MEDM_COLOR_28","MEDM_COLOR_52","MEDM_COLOR_50","MEDM_COLOR_61","MEDM_COLOR_63","MEDM_COLOR_30","MEDM_COLOR_32","MEDM_COLOR_34","MEDM_COLOR_22","MEDM_COLOR_23","Major","Write_Foreground"];

widget.setPropertyValue("background_color",bgcolors[bin]);
