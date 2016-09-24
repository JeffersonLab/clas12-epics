importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var prefix = "B_DET_FTT_HV_";

var parts = ["1","2"];
var sides = ["TOP","BOT"];
var types = ["STR","DR"];

for (var iparts=0; iparts<parts.length; iparts++)
{
  for (var isides=0; isides<sides.length; isides++)
  {
    for (var itypes=0; itypes<types.length; itypes++)
    {
    
pv = prefix + parts[iparts] + "_" + sides[isides] + types[itypes] + ":pwonoff";
PVUtil.writePV(pv,0);    
    
    }
  }
}
