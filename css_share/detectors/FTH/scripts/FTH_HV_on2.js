importPackage(Packages.org.csstudio.opibuilder.scriptUtil);


var label = "Turn ON ALL HV for FTH?"

var response = GUIUtil.openConfirmDialog(label);
if (response)
{


    
    var prefix = "B_DET_FTH_HV_H";
    for (var ii=1; ii<=30; ii++)
    {
       var chan=ii;
       if (chan<10) chan="0"+chan;
       var pv = prefix+chan+":pwonoff";
       PVUtil.writePV(pv,1);    
    }
    

}

