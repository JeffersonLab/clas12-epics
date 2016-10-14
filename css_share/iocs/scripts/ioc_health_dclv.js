importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

//widget.removeAllChildren();

basename="iocdclv_";

var jj=0;
for (var ss=1; ss<=6; ss++)
{
  for (var rr=1; rr<=3; rr++)
  {
    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    if (jj%2==0) lc.setPropertyValue("opi_file","/CLAS12_Share/iocs/ioc_chan_soft.opi"); 
    else         lc.setPropertyValue("opi_file","/CLAS12_Share/iocs/ioc_chan_soft_light.opi"); 
    //try   { lc.setPropertyValue("resize_behaviour",1); }
    //catch (err) { lc.setPropertyValue("auto_size",true); }
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    var ioc="iocdclv_S"+ss+"R"+rr;
    lc.addMacro("ioc",ioc);
    widget.addChildToBottom(lc);
    var line = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.Label");
    line.setPropertyValue("width",1);
    line.setPropertyValue("height",2);
    line.setPropertyValue("text","");
    widget.addChildToBottom(line);
    jj++;
  }
}