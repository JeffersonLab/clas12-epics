importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

//widget.removeAllChildren();

var novice = PVUtil.getDouble(pvs[0]);

var IMO=["Inner","Middle","Outer"];
var nch=0;

for (var seg=1; seg<=24; seg++)
{
  for (var imo=0; imo<IMO.length; imo++)
  {
    for (var ich=1; ich<=2; ich++)
    {
        var ch=ich;
        //if (ich<10) ch="0"+ich;
        var pvprefix="B_DET_CND_HV_"+IMO[imo]+"_Seg"+seg+"_E"+ch;
        
        var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
        if (novice>0) { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel_novice.opi"); }
        else          { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel.opi"); }
        //try   { lc.setPropertyValue("resize_behaviour",1); }
        //catch (err) { lc.setPropertyValue("auto_size",true); }
        lc.setPropertyValue("auto_size",true);
        lc.setPropertyValue("zoom_to_fit",false);
        lc.setPropertyValue("border_style",0);
        lc.setPropertyValue("background_color","Header_Background");
        lc.addMacro("C",nch);
        lc.addMacro("P",pvprefix);
        widget.addChildToBottom(lc);
        nch++;
    }
  }
}


