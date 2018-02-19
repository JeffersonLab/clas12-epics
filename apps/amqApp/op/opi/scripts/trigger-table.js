importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var novice=widget.getMacroValue("NOVICE");

var prefix="B_DAQ_GTTrigBit";

var enpvs=[];
for (var chan=0; chan<32; chan++) {
    pvname=prefix+":"+chan+":enable"
    enpvs[chan]=PVUtil.createPV(pvname,widget);
}


var keepers=[1,2,3,4,5,6];
//var keepers=[0,1,2,3,4,5,6,10,15,19,20,21,23,25,26,30,31];

  for (var chan=0; chan<32; chan++)
  {

    if (novice==1) {
        var enabled=0;
        while (true) {
            try {
                // pv is created in different threadh,
                // wait to get a value
                enabled=PVUtil.getLong(enpvs[chan]);
                break;
            }
            catch (ss) { }
        }
        for (var ii=0; ii<keepers.length; ii++) {
            if (chan==keepers[ii]) {
                enabled=1;
                break;
            }
        }
        if (enabled==0) continue;
    }


/*
    if (novice==1) {
        var ignore=true;
        for (var ii=0; ii<keepers.length; ii++) {
            if (chan==keepers[ii]) {
                ignore=false;
                break;
            }
        }
        if (ignore) continue;
    } 
*/    
    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    lc.setPropertyValue("opi_file","/CLAS12_Share/apps/amqApp/trigger-row.opi");
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    lc.addMacro("P",prefix);
    lc.addMacro("BIT",chan);
    widget.addChildToBottom(lc);
  }
