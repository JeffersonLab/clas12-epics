importPackage(Packages.org.csstudio.opibuilder.scriptUtil);


java.lang.System.err.println("doggy");


var parts=["1","2","3"];
var chans=["00","01","02","03","04","05","06","07","08","09","10","11"];

/*
var prefix = "B_DET_FTH_HV_H";
for (var ii=1; ii<=30; ii++)
{
  var chan=ii;
  if (chan<10) chan="0"+chan;
  var pv = prefix+chan+":pwonoff";
  PVUtil.writePV(pv,0);    
}
*/


var prefix = "B_DET_FTH_HV_";
for (var iparts=0; iparts<parts.length; iparts++)
{
  for (var ichans=0; ichans<chans.length; ichans++)
  {
    
pv = prefix + parts[iparts] + "_" + chans[ichans] + ":pwonoff";
//java.lang.System.err.println(pv);
PVUtil.writePV(pv,0);    
    
  }
}



