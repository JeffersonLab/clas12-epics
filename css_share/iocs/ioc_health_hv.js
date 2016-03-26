importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

//widget.removeAllChildren();

dets=["ECAL","FTOF"];

for (var idet=0; idet<dets.length; idet++) {
for (var sector=1; sector<=6; sector++) {
    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    lc.setPropertyValue("opi_file","/CLAS12_Share/iocs/ioc_chan_soft.opi"); 
    //try   { lc.setPropertyValue("resize_behaviour",1); }
    //catch (err) { lc.setPropertyValue("auto_size",true); }
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    var ioc="ioccaenhv_HV"+dets[idet]+sector;
    lc.addMacro("ioc",ioc);
    widget.addChildToBottom(lc);
}
}

iocs=["FTAG","DC","CTOF0","LTCC0","HVTEST0"];
for (var ii=0; ii<iocs.length; ii++) {
    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    lc.setPropertyValue("opi_file","/CLAS12_Share/iocs/ioc_chan_soft.opi"); 
    //try   { lc.setPropertyValue("resize_behaviour",1); }
    //catch (err) { lc.setPropertyValue("auto_size",true); }
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    lc.addMacro("ioc","ioccaenhv_HV"+iocs[ii]);
    widget.addChildToBottom(lc);
}