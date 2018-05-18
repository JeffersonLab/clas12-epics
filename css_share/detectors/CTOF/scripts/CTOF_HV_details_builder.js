importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

//widget.removeAllChildren();

var novice = PVUtil.getDouble(pvs[0]);

/*
var crate = "HVCTOF0";
var nchan = 24;
var ichan=0;
for (var slot=0; slot<4; slot++)
{
  if (slot<10) slot="0"+slot;
  for (var chan=0; chan<nchan; chan++)
  {
    if (chan<10) chan="0"+chan;
    var pvprefix = "B_HW_" + crate + "_Sl" + slot + "_Ch" + chan;

    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    if (novice>0) { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel_novice.opi"); }
    else          { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel.opi"); }
    //try   { lc.setPropertyValue("resize_behaviour",1); }
    //catch (err) { lc.setPropertyValue("auto_size",true); }
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    lc.addMacro("C",ichan++);
    lc.addMacro("P",pvprefix);
    widget.addChildToBottom(lc);
  }
}
*/

var ud=["U","D"];
for (var ich=1; ich<=48; ich++)
{
    if (ich==14) continue;

    for (var iud=0; iud<ud.length; iud++)
    {
        var ch=ich;
        if (ich<10) ch="0"+ich;
        var pvprefix="B_DET_CTOF_HV_"+ud[iud]+ch;
        
        var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
        if (novice>0) { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel_novice.opi"); }
        else          { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel.opi"); }
        //try   { lc.setPropertyValue("resize_behaviour",1); }
        //catch (err) { lc.setPropertyValue("auto_size",true); }
        lc.setPropertyValue("auto_size",true);
        lc.setPropertyValue("zoom_to_fit",false);
        lc.setPropertyValue("border_style",0);
        lc.setPropertyValue("background_color","Header_Background");
        lc.addMacro("C",ch);
        lc.addMacro("P",pvprefix);
        widget.addChildToBottom(lc);

    }
}


