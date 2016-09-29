importPackage(Packages.org.csstudio.opibuilder.scriptUtil);
var prefix = "hallb-gpib";

for (var ii=1; ii<=20; ii++)
{

  if (ii==12 || ii==17) continue;

  var chan=ii;
  if (chan<10) chan="0"+chan;
  var pv = prefix + chan;

  PVutil.WritePV(pv+":RESET.PROC",1);
}