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
var suffix = widget.getMacroValue("SUFFIX");
var max = PVUtil.getDouble(pvs[1]);
var min = PVUtil.getDouble(pvs[2]);

/*
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
*/

//display.getWidget("ScaleMax").setPropertyValue("text", max.toString());
//display.getWidget("ScaleMin").setPropertyValue("text", min.toString());

if(temp>max)
	bin=10;
else if(temp<min)
	bin=11;
else
	bin = Math.floor((temp-min)/(max-min)*nbins);

//java.lang.System.out.println(bin);
//#ffa500 #ff8d00 #fa7700 #f26000 #e74b00 #d93800 #c82601 #b51402 #a00502 #8b0000
var color0 = ColorFontUtil.getColorFromRGB(0,0,255);
var color1 = ColorFontUtil.getColorFromRGB(90,0,237);
var color2 = ColorFontUtil.getColorFromRGB(127,0,217);
var color3 = ColorFontUtil.getColorFromRGB(155,0,194);
var color4 = ColorFontUtil.getColorFromRGB(177,0,170);
var color5 = ColorFontUtil.getColorFromRGB(196,0,144);
var color6 = ColorFontUtil.getColorFromRGB(213,0,118);
var color7 = ColorFontUtil.getColorFromRGB(229,0,87);
var color8 = ColorFontUtil.getColorFromRGB(243,0,53);
var color9 = ColorFontUtil.getColorFromRGB(255,0,0);

var bgcolors=[color0,color1,color2,color3,color4,color5,color6,color7,color8,color9,"MEDM_COLOR_23","MEDM_COLOR_29"];

widget.setPropertyValue("background_color",bgcolors[bin]);
