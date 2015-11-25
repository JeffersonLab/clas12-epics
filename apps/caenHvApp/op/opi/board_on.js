importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var argh  = widget.getMacroValue("ARGH");
var crate = widget.getMacroValue("CRATE");
var slot  = widget.getMacroValue("SLOT");
var nchan = widget.getMacroValue("NCHAN");

for (var chan=0; chan<nchan; chan++)
{
  if (argh == 1) { pv = "B_" + crate + "_HV000_" + slot + "_" + chan + ":pwonoff"; }
  else           { pv = "B_" + crate + "_Sl" + slot + "_Ch" + chan + ":pwonoff"; }
  //var pv = "B_" + crate + "_Sl" + slot + "_Ch" + chan + ":pwonoff";
  PVUtil.writePV(pv,1);
}