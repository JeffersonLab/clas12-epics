importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

E=widget.getMacroValue("E")
IMO=widget.getMacroValue("IMO")

//PREFIX="B_DET_CND_FADC_"
//Inner_Segment%.2d_E1

var lc=WidgetUtil.createWidgetModel
           ("org.csstudio.opibuilder.widgets.linkingContainer");
    lc.setPropertyValue("opi_file","jscaler_fadc_channel_header.opi");
    lc.setPropertyValue("background_color","Text_Background");
    lc.setPropertyValue("foreground_color","Header_Foreground");
    lc.setPropertyValue("width",230);
    lc.setPropertyValue("height",15);
    
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);

    widget.addChildToBottom(lc);      

for (var cc=1; cc<=24; cc++) {

    chan=cc;
    if (cc<10) chan="0"+chan;

    a=IMO+"_Seg"+chan+"_E"+E

    var lc=WidgetUtil.createWidgetModel
           ("org.csstudio.opibuilder.widgets.linkingContainer");
    lc.setPropertyValue("opi_file","jscaler_fadc_channel.opi");
    lc.setPropertyValue("background_color","Text_Background");
    lc.setPropertyValue("foreground_color","Header_Foreground");
    lc.setPropertyValue("width",230);
    lc.setPropertyValue("height",15);
    
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
  
    lc.addMacro("L",IMO+" Seg"+chan+" E"+E);
    lc.addMacro("P","B_DET_CND");
    lc.addMacro("C",a);

    widget.addChildToBottom(lc);      

}


