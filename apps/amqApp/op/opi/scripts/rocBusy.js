importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var fileName=widget.getMacroValue("F");
var i1=widget.getMacroValue("FIRST");
var i2=widget.getMacroValue("LAST");
var type=widget.getMacroValue("TYPE");

var pvPrefix="B_DAQ:ROCS_BUSY:";

if (type==2) pvPrefix="B_DAQ:STA:";

var opiFile="rocBusy.opi";

function insertRoc(rocName,rocNumber) {
    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    lc.setPropertyValue("opi_file",opiFile);
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    if (type==2)
    lc.addMacro("P",pvPrefix+rocName+":dataRate");
    else
        lc.addMacro("P",pvPrefix+rocName);
    
    lc.addMacro("N",rocNumber);
    widget.addChildToBottom(lc);
}
    
var lines=FileUtil.readTextFile(fileName,widget).split("\n");

for (var ii=i1; ii<=i2; ii++) {
    if (ii==55) continue;
    var columns = lines[ii].split(" ");
    var rocName = columns[columns.length-1];
    //if (!rocName.includes("-") && !rocName.includes("svt3"))
    insertRoc(rocName,ii);
}

