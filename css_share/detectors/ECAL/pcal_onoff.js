importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var onoff = widget.getMacroValue("ONOFF");
var sec   = widget.getMacroValue("SECTOR");

var uvw = ["U","V","W"];

for (var sec=1; sec<=6; sec++)
{
  for (var iuvw=0; iuvw<uvw.length; iuvw++)
  {
    var nchan;
    if (uvw[iuvw] == "U") { nchan=68; }
    else                  { nchan=62; }
    for (var chan=1; chan<=nchan; chan++)
    {
      var pv = B_SYS_HV_PCAL_Sec + sec + "_" + uvw[iuvw];
      if (chan<10) { pv += "0" + chan; }
      else         { pv += chan; }
      PVUtil.writePV(pv,onoff);
    }
  }
}