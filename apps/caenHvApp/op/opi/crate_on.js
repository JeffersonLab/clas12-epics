importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var argh  = widget.getMacroValue("ARGH");
var crate = widget.getMacroValue("CRATE");
var nchan = widget.getMacroValue("NCHAN");
var nslot = widget.getMacroValue("NSLOT");

for (var slot=0; slot<nslot; slot++)
{
  if (slot<10) slot="0"+slot;
  for (var chan=0; chan<nchan; chan++)
  {
    if (chan<10) chan="0"+chan;
    var pv;
    if (argh == 1) { pv = "B_HW_" + crate + "_HV000_" + slot + "_" + chan + ":pwonoff"; }
    else           { pv = "B_HW_" + crate + "_Sl" + slot + "_Ch" + chan + ":pwonoff"; }
    //var pv = "B_" + crate + "_Sl" + slot + "_Ch" + chan + ":pwonoff";
    PVUtil.writePV(pv,1);
  }
}
