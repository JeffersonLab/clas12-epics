importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

//widget.removeAllChildren();

var novice = PVUtil.getDouble(pvs[0]);

var nch=0;

var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
lc.setPropertyValue("opi_file","/CLAS12_Share/apps/mpodLvApp/iseg-channel-header.opi");
lc.setPropertyValue("auto_size",true);
lc.setPropertyValue("zoom_to_fit",false);
lc.setPropertyValue("border_style",0);
lc.setPropertyValue("background_color","Header_Background");
widget.addChildToBottom(lc);
        
        
for (var slot=0; slot<2; slot++)
{
  var nchan=8;
  if (slot>0) nchan=4;
  for (var chan=0; chan<nchan; chan++)
  {
        var pvprefix="B_BONUS_HV_Sl"+slot+"_Ch"+chan;
//        java.lang.System.err.println(pvprefix);
        
        
        var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
        lc.setPropertyValue("opi_file","/CLAS12_Share/apps/mpodLvApp/iseg-channel-row.opi");
        //if (novice>0) { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel_novice.opi"); }
        //else          { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel-WITHTRIP.opi"); }
        //try   { lc.setPropertyValue("resize_behaviour",1); }
        //catch (err) { lc.setPropertyValue("auto_size",true); }
        lc.setPropertyValue("auto_size",true);
        lc.setPropertyValue("zoom_to_fit",false);
        lc.setPropertyValue("border_style",0);
        lc.setPropertyValue("background_color","Header_Background");
        lc.addMacro("C",nch);
        lc.addMacro("P",pvprefix);
        lc.addMacro("M",":"+(slot+1));
        lc.addMacro("N",chan+1);
        widget.addChildToBottom(lc);
        nch++;
        
  }
}
/*
var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
lc.setPropertyValue("opi_file","/CLAS12_Share/apps/mpodLvApp/mpod-crate.opi");
lc.setPropertyValue("auto_size",true);
lc.setPropertyValue("zoom_to_fit",false);
lc.setPropertyValue("border_style",0);
lc.setPropertyValue("background_color","Header_Background");
lc.addMacro("HOST","hbmpod5");
lc.addMacro("ioc","iocgasSystem86");
lc.addMacro("TITLE","asdf");
widget.addChildToBottom(lc);
*/
