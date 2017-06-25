importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

NCHAN=widget.getMacroValue("N")
PREFIX=widget.getMacroValue("P")
SUFFIX=widget.getMacroValue("C")
LABEL=widget.getMacroValue("L")


var lc=WidgetUtil.createWidgetModel
           ("org.csstudio.opibuilder.widgets.linkingContainer");
    lc.setPropertyValue("opi_file","jscaler_det_channel_header.opi");
    lc.setPropertyValue("background_color","Text_Background");
    lc.setPropertyValue("foreground_color","Header_Foreground");
    lc.setPropertyValue("width",230);
    lc.setPropertyValue("height",15);
    
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);

    widget.addChildToBottom(lc);      

for (var cc=1; cc<=NCHAN; cc++) {

    chan=cc;
    if (cc<10) chan="0"+chan;

    var lc=WidgetUtil.createWidgetModel
           ("org.csstudio.opibuilder.widgets.linkingContainer");
    lc.setPropertyValue("opi_file","jscaler_det_channel.opi");
    lc.setPropertyValue("background_color","Text_Background");
    lc.setPropertyValue("foreground_color","Header_Foreground");
    lc.setPropertyValue("width",230);
    lc.setPropertyValue("height",15);
    
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
  
    lc.addMacro("L",LABEL+chan);
    lc.addMacro("P",PREFIX);
    lc.addMacro("C",SUFFIX+chan);

    widget.addChildToBottom(lc);      

}


