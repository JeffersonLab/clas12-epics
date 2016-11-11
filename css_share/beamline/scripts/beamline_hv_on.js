importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var label = "Turn ON ALL Beamline HV\n\n";
label +=    "      Really??"
if (GUIUtil.openConfirmDialog(label))
{
var ss=[
  "UpstreamLeft",
  "UpstreamRight",
  "TaggerLeft",
  "TaggerRight",
  "HPSLeft",
  "HPSRight",
  "ECalCosm1",
  "ECalCosm2",
  "HPSTop",
  "HPSSC",
  "ECalCosm5",
  "TaggerT2",
  "MollerRight",
  "MollerLeft",
  "BLM1",
  "BLM2",
  "BLM3",
  "BLM4",
  "DSHaloBottom",
  "DSHaloTop",
  "DSHaloLeft",
  "DSHaloRight"
];

{
    for (var ii=0; ii<ss.length; ii++)
    {
 //     java.lang.System.err.println(ss[ii]);

      PVUtil.writePV("B_DET_BLINE_HV_"+ss[ii]+":pwonoff",1);

    }
}
}

