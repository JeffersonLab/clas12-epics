importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

//widget.removeAllChildren();

var novice = PVUtil.getDouble(pvs[0]);

var crate = "HVFTAG";

var slots=["13"];
var chans=["02","03","04","05","08","09","10","11"];

for (var islot=0; islot<slots.length; islot++)
{
  var slot=slots[islot];
  
  for (var ichan=0; ichan<chans.length; ichan++)
  {
    var pvprefix = "B_HW_" + crate + "_Sl" + slot + "_Ch" + chans[ichan];

    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    if (novice>0) { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel_novice.opi"); }
    else          { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel.opi"); }
    //try   { lc.setPropertyValue("resize_behaviour",1); }
    //catch (err) { lc.setPropertyValue("auto_size",true); }
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    lc.addMacro("C",chans[ichan]);
    lc.addMacro("P",pvprefix);
    widget.addChildToBottom(lc);
  }
}