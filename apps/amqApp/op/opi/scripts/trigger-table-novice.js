importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var ignores=[0,10,15,19,20,21,23,25,26,29,30,31];

  for (var chan=0; chan<32; chan++)
  {
      var ignore=false;
      for (var ii=0; ii<ignores.length; ii++) {
          if (chan==chans[ii]) {
              ignore=true;
              break;
          }
      }

      if (ignore) continue;

    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    lc.setPropertyValue("opi_file","/CLAS12_Share/apps/amqApp/trigger-row.opi");
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    lc.addMacro("BIT",chan);
    widget.addChildToBottom(lc);
  }
