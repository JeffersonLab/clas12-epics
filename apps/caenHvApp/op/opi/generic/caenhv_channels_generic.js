importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var novice = PVUtil.getDouble(pvs[0]);
var filename = widget.getMacroValue("FILE");

function mkChan(count,prefix) {
    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    if (novice>0) { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel_novice.opi"); }
    else          { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel.opi"); }
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    lc.addMacro("C",count);
    lc.addMacro("P",prefix);
    widget.addChildToBottom(lc);
}

var lines=FileUtil.readTextFile(filename,widget);
lines=lines.split("\n");
for (var ii=0; ii<lines.length; ii++) {
    mkChan(ii+1,lines[ii]);
}

