importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var istatus = PVUtil.getDouble(pvs[0]) | 0;

var statuses=["ON","RUP",  "RDN",  "OVC",  "OVV",  "UNV",  "ExTrip","MAXV", "ExDis",       "InTrip","CalEr","ChUn"];
var bgcolors=["On","Minor","Minor","Major","Major","Major","Major", "Major","Disconnected","Major","Major","Disconnected"];

var theStatus=-1;

for (var ii=0; ii<12; ii++)
{
  if ((1<<ii) & istatus)
  {
    theStatus=ii;
  } 
}
if (istatus == 0) { 
  widget.setPropertyValue("text","OFF");
  widget.setPropertyValue("background_color","Header_Background");
  widget.setPropertyValue("foreground_color","Header_ForeGround");
}
else
{
  widget.setPropertyValue("text",statuses[theStatus]);
  widget.setPropertyValue("foreground_color","Text_BackGround");
  widget.setPropertyValue("background_color",bgcolors[theStatus]);
}
