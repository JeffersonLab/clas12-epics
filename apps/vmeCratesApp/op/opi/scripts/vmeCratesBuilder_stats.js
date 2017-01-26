importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var hps=["hps1","hps2","hps11","hps12"];
var test=["ltcc0","pcal0"];//,"highbtest3"];
var dets=["adcctof1","svt1","svt2","svt3"];//,"adcft1","adcft2","adcft3"];//,"mtv1","trig1","trig2"];
var dc=["dcrb1","dcrb2"];
var ecal1=["adcecal1","adcecal2","adcecal3","adcecal4","adcecal5","adcecal6"];
var ecal2=["tdcecal1","tdcecal2","tdcecal3","tdcecal4","tdcecal5","tdcecal6"];
var pcal1=["adcpcal1","adcpcal2","adcpcal3","adcpcal4","adcpcal5","adcpcal6"];
var pcal2=["tdcpcal1","tdcpcal2","tdcpcal3","tdcpcal4","tdcpcal5","tdcpcal6"];
var ftof1=["adcftof1","adcftof2","adcftof3","adcftof4","adcftof5","adcftof6"];
var ftof2=["tdcftof1","tdcftof2","tdcftof3","tdcftof4","tdcftof5","tdcftof6"];
var groups=[ecal1,ecal2,pcal1,pcal2,ftof1,ftof2,dets];

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
        lc.addMacro("P",crateName);
        widget.addChildToBottom(lc);
    }
}

