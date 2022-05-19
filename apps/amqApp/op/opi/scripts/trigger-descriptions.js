importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

  for (var chan=0; chan<32; chan++)
  {

    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    lc.setPropertyValue("opi_file","trigger-description.opi");
    
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    if (chan<10) chan="0"+chan;
    lc.addMacro("BIT",chan);
    widget.addChildToBottom(lc);
  }
