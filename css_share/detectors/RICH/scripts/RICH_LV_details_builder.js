importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

//widget.removeAllChildren();

var novice = PVUtil.getDouble(pvs[0]);

var prefixes = ["B_DET_RICH_LV_GRP","B_DET_RICH2_LV_GRP"];
var nchan = 40;

for (var iprefix=0; iprefix<2; iprefix++)
{
  var prefix = prefixes[iprefix];
  for (var chan=1; chan<=nchan; chan++)
  {
    if (chan==13 || chan==14 || chan==37 || chan==38) continue;

    if (chan<10) chan="0"+chan;

    var pv = prefix+chan;

    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    if (novice>0) { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/mpodLvApp/mpod8008l_channel_novice2.opi"); }
    else          { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/mpodLvApp/mpod8008l_channel_expert.opi"); }
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
  }

