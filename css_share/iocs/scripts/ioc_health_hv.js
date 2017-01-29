importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

//widget.removeAllChildren();

dets=["ECAL","FTOF"];

var jj=0;

for (var idet=0; idet<dets.length; idet++) {
for (var sector=1; sector<=6; sector++) {
    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    if (jj%2==0) lc.setPropertyValue("opi_file","/CLAS12_Share/iocs/ioc_chan_soft_autosave.opi"); 
    else         lc.setPropertyValue("opi_file","/CLAS12_Share/iocs/ioc_chan_soft_light_autosave.opi"); 
    //try   { lc.setPropertyValue("resize_behaviour",1); }
    //catch (err) { lc.setPropertyValue("auto_size",true); }
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    var ioc="ioccaenhv_HV"+dets[idet]+sector;
    lc.addMacro("ioc",ioc);
    widget.addChildToBottom(lc);
    jj++;
        var line = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.Label");
    line.setPropertyValue("width",1);
    line.setPropertyValue("height",2);
    line.setPropertyValue("text","");
    widget.addChildToBottom(line);
    
}
}

iocs=["FTAG","CTOF0","LTCC0","DCa","DCb","BLINE"];
//,"HVTEST0"];
for (var ii=0; ii<iocs.length; ii++) {
    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    if (jj%2==0) lc.setPropertyValue("opi_file","/CLAS12_Share/iocs/ioc_chan_soft_autosave.opi"); 
    else         lc.setPropertyValue("opi_file","/CLAS12_Share/iocs/ioc_chan_soft_light_autosave.opi"); 
    //try   { lc.setPropertyValue("resize_behaviour",1); }
    //catch (err) { lc.setPropertyValue("auto_size",true); }
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    lc.addMacro("ioc","ioccaenhv_HV"+iocs[ii]);
    widget.addChildToBottom(lc);
    jj++;
          var line = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.Label");
    line.setPropertyValue("width",1);
    line.setPropertyValue("height",2);
    line.setPropertyValue("text","");
    widget.addChildToBottom(line);
}