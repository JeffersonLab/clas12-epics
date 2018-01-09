importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

//widget.removeAllChildren();

var novice = PVUtil.getDouble(pvs[0]);

var prefix = "B_DET_RICH_LV_GRP";
var nchan = 40;

  for (var chan=1; chan<=nchan; chan++)
  {
    if (chan==13 || chan==14 || chan==37 || chan==38) continue;

    if (chan<10) chan="0"+chan;

    var pv = prefix+chan;

    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    if (novice>0) { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/LV/caenhv_channel_novice-lv.opi"); }
    else          { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/LV/caenhv_channel-lv.opi"); }
    //try   { lc.setPropertyValue("resize_behaviour",1); }
    //catch (err) { lc.setPropertyValue("auto_size",true); }
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    lc.addMacro("C",chan);
    lc.addMacro("P",pv);
    widget.addChildToBottom(lc);
  }


