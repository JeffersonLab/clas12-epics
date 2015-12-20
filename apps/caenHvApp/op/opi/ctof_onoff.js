importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var prefix = "B_SYS_HV_CTOF_";

var onoff  = widget.getMacroValue("ONOFF");
var updown = widget.getMacroValue("UPDOWN");
var topbot = widget.getMacroValue("TOPBOT");

var c0=1;
var c1=48;
if      (topbot == "TOP") { c0=25; }
else if (topbot == "BOT") { c1=24; }

for (var cc=c0; cc<=c1; cc++)
{
  var ccc;
  if (cc<10) { ccc = "0" + cc; }
  else       { ccc = cc; }
  pvU = prefix + "U" + ccc + ":pwonoff";
  pvD = prefix + "D" + ccc + ":pwonoff";
  if (updown == "UP") 
  {
    PVUtil.writePV(pvU,onoff);
  } 
  else if (updown == "DOWN") 
  {
    PVUtil.writePV(pvD,onoff);
  }
  else
  {
    PVUtil.writePV(pvU,onoff);
    PVUtil.writePV(pvD,onoff);
  }
}