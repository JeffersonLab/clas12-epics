importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var novice = PVUtil.getDouble(pvs[0]);

var ss=[
  "UpstreamLeft",
  "UpstreamRight",
  "TaggerLeft",
  "TaggerRight",
  "TaggerTop",
  "MollerLeft",
  "MollerRight",
  "MidstreamLeft",
  "MidstreamRight",
  "MidstreamTop",
  "MidstreamBottom",
  "DownstreamLeft",
  "DownstreamRight",
  "DownstreamTop",
  "DownstreamBottom",
  "SLM",
  "BOM",
  "HaloLeft",
  "HaloRight",
  "HaloTop",
  "HaloSC"
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

        var pv="B_DET_BLINE_HV_"+ss[ii];
        if (ss[ii].indexOf("Halo")==0) {
            pv="B_DET_HPS_HV_"+ss[ii];
        }

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
        if (ss[ii].indexOf("Midstream")==0 || ss[ii]=="BOM") 
          lc.addMacro("TYPE","527");
        widget.addChildToBottom(lc);

        if (ss[ii]=="UpstreamRight" ||
            ss[ii]=="TaggerTop" ||
            ss[ii]=="ECalCosm5" ||
            ss[ii]=="MollerRight" ||
            ss[ii]=="BLM4" ||
            ss[ii]=="MidstreamBottom" ||
            ss[ii]=="DownstreamBottom" ||
            ss[ii]=="SLM" ||
            ss[ii]=="BOM")
        { mkGap(); }
    }
}

