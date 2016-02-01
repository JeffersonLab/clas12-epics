importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var prefix = "B_DET_FTC_LV_";
var qg=["Q1Q4","Q2Q3"];
var pn=["P","N"];

for (var iqg=0; iqg<2; iqg++)
{
    for (var ipn=0; ipn<2; ipn++)
    {
      pv = prefix + qg[iqg] + pn[ipn] + ":switch";
      PVUtil.writePV(pv,1);
  }
}
