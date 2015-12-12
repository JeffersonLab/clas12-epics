importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

//widget.removeAllChildren();

var novice = PVUtil.getDouble(pvs[0]);

var crate = "HVFTAG";
var nchan = 12;

for (var slot=0; slot<=4; slot+=2)
{
  for (var chan=0; chan<nchan; chan++)
  {
    var pvprefix = "B_HW_" + crate + "_Sl" + slot + "_Ch" + chan;

    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    if (novice>0) { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel_novice.opi"); }
    else          { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel.opi"); }
    //try   { lc.setPropertyValue("resize_behaviour",1); }
    //catch (err) { lc.setPropertyValue("auto_size",true); }
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.addMacro("C",chan);
    lc.addMacro("P",pvprefix);
    widget.addChildToBottom(lc);
  }
}