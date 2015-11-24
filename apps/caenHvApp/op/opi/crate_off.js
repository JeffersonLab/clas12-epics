importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var argh  = widget.getMacroValue("ARGH");
var crate = widget.getMacroValue("CRATE");
var nchan = widget.getMacroValue("NCHAN");
var nslot = widget.getMacroValue("NSLOT");

for (var slot=0; slot<nslot; slot++)
{
  for (var chan=0; chan<nchan; chan++)
  {
    var pv;
    if (argh == 1) { pv = "B_" + crate + "_HV000_" + slot + "_" + chan + "_pwonoff"; }
    else           { pv = "B_" + crate + "_Sl" + slot + "_Ch" + chan + "_pwonoff"; }
    //var pv = "B_" + crate + "_Sl" + slot + "_Ch" + chan + "_pwonoff";
    PVUtil.writePV(pv,0);
  }
}
