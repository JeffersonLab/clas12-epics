importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

for (var ss=1; ss<=6; ss++)
{
    var line = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.Label");
    line.setPropertyValue("width",1);
    line.setPropertyValue("height",10);
    line.setPropertyValue("text","");
    widget.addChildToBottom(line);

for (var rr=1; rr<=3; rr++)
{
  var crateName="DC"+ss+rr;

        var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
        lc.setPropertyValue("opi_file","vmeCrate_full.opi");
        //try   { lc.setPropertyValue("resize_behaviour",1); }
        //catch (err) { lc.setPropertyValue("auto_size",true); }
        lc.setPropertyValue("auto_size",true);
        lc.setPropertyValue("zoom_to_fit",false);
        lc.setPropertyValue("border_style",0);
        lc.setPropertyValue("background_color","OPI_Background");
        lc.addMacro("P","B_HW_"+crateName);//.toUpperCase());
        lc.addMacro("L",crateName);
        widget.addChildToBottom(lc);
    }
}

