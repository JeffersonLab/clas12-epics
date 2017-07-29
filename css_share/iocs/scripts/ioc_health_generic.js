importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

// Macro "F" is the name of a file containing a list of ioc names, one per row.
// It can also be a comma-separated list of file names.
//
// If a line doesn't start with "ioc", insert a blank gap instead.  Additional
// columns are options (the only currently valid one is "noautosave");

var fileNames=widget.getMacroValue("F").split(",");

function insertLine()
{
    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.Rectangle");
    lc.setPropertyValue("border_style",1);
    lc.setPropertyValue("line_width",0);
    lc.setPropertyValue("height",5);
    lc.setPropertyValue("width",1386);
    lc.setPropertyValue("border_width",1);
    lc.setPropertyValue("border_color","MEDM_COLOR_5");
    lc.setPropertyValue("background_color","Read_Background");
    widget.addChildToBottom(lc);
}
function insertGap(size)
{
    var line = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.Label");
    line.setPropertyValue("width",1);
    line.setPropertyValue("height",size);
    line.setPropertyValue("text","");
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
    lc.addMacro("ioc",iocName);
    widget.addChildToBottom(lc);
}


for (var iFile=0; iFile<fileNames.length; iFile++) {

    if (iFile>0) insertGap(15);

    var lines=FileUtil.readTextFile(fileNames[iFile],widget);
    lines=lines.split("\n");

    for (var ii=0,jj=0; ii<lines.length; ii++)
    {
        if (!lines[ii].startsWith("ioc")) {
            insertGap(7);
            insertLine();
            insertGap(7);
            continue;
        }

        var iocName=lines[ii];
        var autosave=true;
        var vxworks=false;

        columns=lines[ii].split(" ");
        if (columns.length>1) {
            iocName=columns[0];
            for (var kk=1; kk<columns.length; kk++) {
                if (columns[kk].equals("noautosave")) autosave=false;
                else if (columns[kk].equals("vxworks")) vxworks=true;
            }
        }

        var opiFile = "ioc_chan";
        if (!vxworks) opiFile += "_soft";
        else opiFile += "_vxworks";
        if (!vxworks && jj%2) opiFile += "_light";
        if (autosave) opiFile += "_autosave";
        opiFile += ".opi";

        insertIoc(iocName,opiFile);
        insertGap(1);
        jj++;
    }
}

insertGap(7);
insertLine();




