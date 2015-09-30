importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

if (widget.getMacroValue("TYPE") != "527")
{
   exit();
}

var istatus = PVUtil.getDouble(pvs[0]) | 0;

var statuses=["ON","RUP",  "RDN",  "OVC",  "UNV",  "OVV",  "ExTrip","MAXV", "    ", "Kill", "InTrip"];
var bgcolors=["On","Minor","Minor","Major","Major","Major","Major", "Major","Major","Major","Major"];

var theStatus=-1;
var j10=-1

var sstatus="OFF";

for (var ii=15; ii>=0; ii--)
{
java.lang.System.out.print(ii+" ");

  j10++;
  if (ii==7 || ii==6) continue;
  if ((1<<ii) & istatus) 
  {  
    theStatus = ii;
    sstatus = statuses[ii];//j10];
  }
}

java.lang.System.out.println("----- "+theStatus+" "+sstatus);

if ( ((1<<6)  & istatus)) { sstatus="Kill"; }
if ( ((1<<13) & istatus)) { sstatus="RDN"; }
if (!((1<<0)  & istatus)) { sstatus=("NotPrt"); }

widget.setPropertyValue("text",sstatus);


if (sstatus == "OFF") { 
 // widget.setPropertyValue("text","OFF");
  widget.setPropertyValue("background_color","Header_Background");
  widget.setPropertyValue("foreground_color","Header_ForeGround");
}
else
{
 // widget.setPropertyValue("text",statuses[theStatus]);
  widget.setPropertyValue("foreground_color","Text_BackGround");
  widget.setPropertyValue("background_color",bgcolors[theStatus]);
}


