importPackage(Packages.org.csstudio.opibuilder.scriptUtil);


java.lang.System.err.println("doggy");



var prefix = "B_DET_FTH_HV_H";
for (var ii=1; ii<=30; ii++)
{
  var chan=ii;
  if (chan<10) chan="0"+chan;
  var pv = prefix+chan+":pwonoff";
  PVUtil.writePV(pv,0);    
}




