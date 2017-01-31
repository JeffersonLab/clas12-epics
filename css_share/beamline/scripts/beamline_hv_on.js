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
  "TaggerTop",
  "MollerRight",
  "MollerLeft",
  "MidstreamLeft",
  "MidstreamRight",
  "MidstreamTop",
  "MidstreamBottom",
  "DownstreamBottom",
  "DownstreamTop",
  "DownstreamLeft",
  "DownstreamRight",
  "SLM"
];

{
    for (var ii=0; ii<ss.length; ii++)
    {
 //     java.lang.System.err.println(ss[ii]);

      PVUtil.writePV("B_DET_BLINE_HV_"+ss[ii]+":pwonoff",1);

    }
}
}

