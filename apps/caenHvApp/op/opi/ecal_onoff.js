importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var onoff = widget.getMacroValue("ONOFF");

var io = ["I","O"];
var uvw = ["U","V","W"];

for (var sec=1; sec<=6; sec++)
{
  for (var iuvw=0; iuvw<uvw.length; iuvw++)
  {
    if (iuvw<10) iuvw="0"+iuvw;
    for (var iio=0; iio<io.length; iio++)
    {
      if (iio<10) iio="0"+iio;
      for (var chan=1; chan<=36; chan++)
      {
        if (chan<10) chan="0"+chan;
        var pv = B_SYS_HV_ECAL_Sec + sec + "_" + uvw[iuvw] + io[iio];
        PVUtil.writePV(pv,onoff);
      }
    }
  }
}
