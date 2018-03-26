importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var fileName=widget.getMacroValue("F");
var i1=widget.getMacroValue("FIRST");
var i2=widget.getMacroValue("LAST");

var pvPrefix="B_DAQ:ROCS_BUSY:";
var opiFile="rocBusy.opi";

function insertRoc(rocName) {
    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    lc.setPropertyValue("opi_file",opiFile);
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    lc.addMacro("P",pvPrefix+rocName);
    widget.addChildToBottom(lc);
}
    
var lines=FileUtil.readTextFile(fileName,widget).split("\n");
if (i1<0 || i2>=lines.length) {
}

for (var ii=i1; ii<=i2; ii++) {
    var columns = lines[ii].split(" ");
    var rocName = columns[columns.length-1];
    insertRoc(rocName);
}

