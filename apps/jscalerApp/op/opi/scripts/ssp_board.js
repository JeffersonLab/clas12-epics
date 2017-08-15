importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var crate = widget.getMacroValue("CRATE");
var slot=widget.getMacroValue("SLOT");
var nchan=widget.getMacroValue("NCHAN");

for (var chan=0; chan<nchan; chan++)
{
    if (chan<10) chan="0"+chan;
    var pvprefix = "B_HW_" + crate + "_Sl" + slot + "_Fi" + chan;

    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    lc.setPropertyValue("opi_file","ssp_fiber.opi");
    //try   { lc.setPropertyValue("resize_behaviour",1); }
    //catch (err) { lc.setPropertyValue("auto_size",true); }
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    lc.addMacro("Sl",slot);
    lc.addMacro("Fi",chan);
    lc.addMacro("P","B_HW_"+crate+"_Sl"+slot+"_Fi"+chan);
    widget.addChildToBottom(lc);

}

