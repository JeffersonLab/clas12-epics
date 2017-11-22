importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

// Macro "F" is the name of a file containing a list of ioc names, one per row.
// It can also be a comma-separated list of file names.
//
// If a line doesn't start with "ioc", insert a blank gap instead.  Additional
// columns are options (the only currently valid one is "noautosave");

var fileNames=widget.getMacroValue("F").split(",");
var alarms=widget.getMacroValue("A")

function insertLine(width)
{
    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.Rectangle");
    lc.setPropertyValue("border_style",1);
    lc.setPropertyValue("line_width",0);
    lc.setPropertyValue("height",width);
    lc.setPropertyValue("width",385);
    lc.setPropertyValue("border_width",1);
    lc.setPropertyValue("border_color","MEDM_COLOR_5");
    lc.setPropertyValue("background_color","Read_Background");
    widget.addChildToBottom(lc);
}
function insertGap(size,text)
{
    var line = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.Label");
    if (text.equals("")) {
        line.setPropertyValue("width",1);
        line.setPropertyValue("text","");
    }
    else {
        line.setPropertyValue("width",500);
        line.setPropertyValue("text","  "+text);
        line.setPropertyValue("font","Default Bold");
        line.setPropertyValue("foreground_color","Read_Foreground");
    }
    line.setPropertyValue("height",size);
    line.setPropertyValue("horizontal_alignment","Left");
    line.setPropertyValue("auto_size",true);
    widget.addChildToBottom(line);
}
function insertIoc(iocName,opiFile)
{
    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    lc.setPropertyValue("opi_file",opiFile);
    //try   { lc.setPropertyValue("resize_behaviour",1); }
    //catch (err) { lc.setPropertyValue("auto_size",true); }
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    lc.addMacro("P",iocName);
    name=iocName.replace("B_DET_MVT_GAS_","");
    lc.addMacro("N",name);
    widget.addChildToBottom(lc);
}

for (var iFile=0; iFile<fileNames.length; iFile++) {

    var lines=FileUtil.readTextFile(fileNames[iFile],widget);
    lines=lines.split("\n");

    for (var ii=0,jj=0; ii<lines.length; ii++)
    {
        if (lines[ii].startsWith("#") || lines[ii].equals("") ) {
    insertGap(1,"");
    insertLine(1);
            var label=lines[ii].slice(1);
            if (label.length>0) {
    insertGap(1,"");
              insertGap(10,label);
    insertGap(1,"");
            }
            continue;
        }

        var iocName=lines[ii];
        var autosave=true;
        var vxworks=false;

        columns=lines[ii].split(" ");
        if (columns.length>1) iocName=columns[0];

        var opiFile = "../../../general/name-value.opi";
        //if (alarms>0) opiFile = "rollAvg-alarms.opi";

        insertIoc(iocName,opiFile);
        jj++;
    }
}

insertGap(7,"");
insertLine(5);


