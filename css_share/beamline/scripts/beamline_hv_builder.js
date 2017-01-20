importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var novice = PVUtil.getDouble(pvs[0]);

var ss=[
  "UpstreamLeft",
  "UpstreamRight",
  "TaggerLeft",
  "TaggerRight",
  "TaggerT2",
  "HPSLeft",
  "HPSRight",
  "ECalCosm1",
  "ECalCosm2",
  "HPSTop",
  "HPSSC",
  "ECalCosm5",
  "MollerRight",
  "MollerLeft",
  "BLM1",
  "BLM2",
  "BLM3",
  "BLM4",
  "DSHaloBottom",
  "DSHaloTop",
  "DSHaloLeft",
  "DSHaloRight"
];

function mkGap()
{
  var gap=WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.Label");
  gap.setPropertyValue("width",1);
  gap.setPropertyValue("height",10);
  widget.addChildToBottom(gap);
}

mkGap();

{
    for (var ii=0; ii<ss.length; ii++)
    {
//      java.lang.System.err.println(ss[ii]);

      var pv="B_DET_BLINE_HV_"+ss[ii];

        var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
        if (novice>0) { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel_novice.opi"); }
        else          { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel.opi"); }
        //try   { lc.setPropertyValue("resize_behaviour",1); }
        //catch (err) { lc.setPropertyValue("auto_size",true); }
        lc.setPropertyValue("auto_size",true);
        lc.setPropertyValue("zoom_to_fit",false);
        lc.setPropertyValue("border_style",0);
        lc.setPropertyValue("background_color","Header_Background");
        lc.addMacro("C",ii);
        lc.addMacro("P",pv);
        widget.addChildToBottom(lc);

        if (ss[ii]=="UpstreamRight" ||
            ss[ii]=="TaggerT2" ||
            ss[ii]=="ECalCosm5" ||
            ss[ii]=="MollerLeft" ||
            ss[ii]=="BLM4" ||
            ss[ii]=="DSHaloRight")
        { mkGap(); }
    }
}


