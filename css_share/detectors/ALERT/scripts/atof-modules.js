importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

for (var module=0; module<15; module++) {        
    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    lc.setPropertyValue("opi_file","/CLAS12_Share/detectors/ALERT/atof-module.opi");
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    lc.addMacro("M",module);
    widget.addChildToBottom(lc);

}
