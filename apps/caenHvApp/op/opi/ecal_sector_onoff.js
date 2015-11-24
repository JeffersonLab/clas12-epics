importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var onoff = widget.getMacroValue("ONOFF");
var sec   = widget.getMacroValue("SECTOR");

var io = ["I","O"];
var uvw = ["U","V","W"];

for (var iuvw=0; iuvw<uvw.length; iuvw++)
{
  for (var iio=0; iio<io.length; iio++)
  {
    for (var chan=1; chan<=36; chan++)
    {
      var pv = B_HV_ECAL_Sec + sec + "_" + uvw[iuvw] + io[iio];
      if (chan<10) { pv += "0" + chan; }
      else         { pv += chan; }
      PVUtil.writePV(pv,onoff);
    }
  }
}