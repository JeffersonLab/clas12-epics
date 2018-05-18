importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var prefix="B_DAQ_GTTrigBit";

  for (var chan=0; chan<32; chan++)
  {

    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    lc.setPropertyValue("opi_file","/CLAS12_Share/apps/amqApp/trigger-alarm.opi");
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    lc.addMacro("P",prefix);
    lc.addMacro("BIT",chan);
    widget.addChildToBottom(lc);
  }
