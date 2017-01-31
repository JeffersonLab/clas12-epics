importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var ss=[
  "UpstreamLeft",
  "UpstreamRight",
  "TaggerLeft",
  "TaggerRight",
  "TaggerTop",
  "MollerRight",
  "MollerLeft",
  "MidstreamBottom",
  "MidstreamTop",
  "MidstreamLeft",
  "MidstreamRight",
  "DownstreamBottom",
  "DownstreamTop",
  "DownstreamLeft",
  "DownstreamRight"
  "SLM"
];

{
    for (var ii=0; ii<ss.length; ii++)
    {
 //     java.lang.System.err.println(ss[ii]);

      PVUtil.writePV("B_DET_BLINE_HV_"+ss[ii]+":pwonoff",0);

    }
}


