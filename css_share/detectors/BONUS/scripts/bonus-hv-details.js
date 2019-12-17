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

var name = ["GEM1_IN","GEM1_OUT","GEM2_IN","GEM2_OUT","GEM3_IN","GEM3_OUT","CATHODE"];
var slot= [0,0,0,0,0,0,1]
var chan= [5,4,3,2,1,0,0]

//var name = ["GEM3_OUT","GEM3_IN","GEM2_OUT","GEM2_IN","GEM1_OUT","GEM1_IN","CATHODE"];
//var slot= [0,0,0,0,0,0,1]
//var chan= [0,1,2,3,4,5,0]

for (var iname=0; iname<name.length; iname++)
{
        if (nch%2==0) {
          var line=WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.Label");
          line.setPropertyValue("width",160);
          line.setPropertyValue("height",6);
          line.setPropertyValue("text","");
          line.setPropertyValue("foreground_color","Header_Foreground");
          line.setPropertyValue("horizontal_alignment","Left");
          widget.addChildToBottom(line);
        }
        
        var pvprefix="B_BONUS_HV_"+name[iname];
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
        lc.addMacro("C",name[iname]);
        lc.addMacro("P",pvprefix);
        lc.addMacro("M",":"+(slot[iname]+1));
        lc.addMacro("N",chan[iname]+1);
        widget.addChildToBottom(lc);
        nch++;
        

}

