importPackage(Packages.org.csstudio.opibuilder.scriptUtil);


var prefix = "hallb-gpib";

for (var ii=1; ii<=20; ii++)
{

  if (ii==12 || ii==17) continue;

  var chan=ii;
  if (chan<10) chan="0"+chan;
  var pv = prefix + chan;

    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    lc.setPropertyValue("opi_file","/CLAS12_Share/apps/prologixApp/prologix_chan_slim.opi");
    //try   { lc.setPropertyValue("resize_behaviour",1); }
    //catch (err) { lc.setPropertyValue("auto_size",true); }
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",1);
    lc.setPropertyValue("border_color","Text_Background");
    lc.setPropertyValue("background_color","Header_Background");
    lc.addMacro("P",pv);
    lc.addMacro("R",":");
    widget.addChildToBottom(lc);
}