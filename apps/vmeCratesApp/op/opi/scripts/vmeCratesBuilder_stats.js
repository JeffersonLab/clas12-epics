importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var hps=["HPS1","HPS2","HPS11","HPS12"];
var dets=["ADCCTOF1","TDCCTOF1","SVT1","SVT2","ADCFT1","ADCFT2","ADCFT3","ADCCND1"];//,"mtv1","trig1","trig2"];
var ecal1=["ADCECAL1","ADCECAL2","ADCECAL3","ADCECAL4","ADCECAL5","ADCECAL6"];
var ecal2=["TDCECAL1","TDCECAL2","TDCECAL3","TDCECAL4","TDCECAL5","TDCECAL6"];
var pcal1=["ADCPCAL1","ADCPCAL2","ADCPCAL3","ADCPCAL4","ADCPCAL5","ADCPCAL6"];
var pcal2=["TDCPCAL1","TDCPCAL2","TDCPCAL3","TDCPCAL4","TDCPCAL5","TDCPCAL6"];
var ftof1=["ADCFTOF1","ADCFTOF2","ADCFTOF3","ADCFTOF4","ADCFTOF5","ADCFTOF6"];
var ftof2=["TDCFTOF1","TDCFTOF2","TDCFTOF3","TDCFTOF4","TDCFTOF5","TDCFTOF6"];
var slow=["SVTVME1"]
var groups=[ecal1,ecal2,pcal1,pcal2,ftof1,ftof2,dets,slow];

for (var ii=0; ii<groups.length; ii++)
{
    var line = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.Label");
    line.setPropertyValue("width",1);
    line.setPropertyValue("height",10);
    line.setPropertyValue("text","");
    widget.addChildToBottom(line);

    for (var jj=0; jj<groups[ii].length; jj++) 
    {
        var crateName=groups[ii][jj];

        var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
        lc.setPropertyValue("opi_file","vmeCrate_stats.opi");
        //try   { lc.setPropertyValue("resize_behaviour",1); }
        //catch (err) { lc.setPropertyValue("auto_size",true); }
        lc.setPropertyValue("auto_size",true);
        lc.setPropertyValue("zoom_to_fit",false);
        lc.setPropertyValue("border_style",0);
        lc.setPropertyValue("background_color","OPI_Background");
        lc.addMacro("P","B_HW_"+crateName);//.toUpperCase());
        lc.addMacro("L",crateName);
        widget.addChildToBottom(lc);
    }
}

