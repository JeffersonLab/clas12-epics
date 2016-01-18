importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

//widget.removeAllChildren();

var novice = PVUtil.getDouble(pvs[0]);

var panel  = widget.getMacroValue("PANEL");
var sector = widget.getMacroValue("SECTOR");
var side   = widget.getMacroValue("SIDE");

var sides=["L","R"];
var panels=["1B","1A","2"];
var nChans=[62,23,5];

var prefix="B_DET_FTOF_HV";

for (var iPan=0; iPan<panels.length; iPan++)
{
    if (panel!=0 && panels[iPan]!=panel) continue;

    for (var iChan=1; iChan<=nChans[iPan]; iChan++)
    {

        for (var iSide=0; iSide<sides.length; iSide++)
        {

            if (side!=0 && sides[iSide]!=side) continue;

            var thisChan=iChan<10?"0"+iChan:iChan;

            var suff="_SEC"+sector+
                "_PANEL"+panels[iPan]+
                "_"+sides[iSide]+
                "_E"+thisChan;

            var pv = prefix+suff;


            var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
            if (novice>0) { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel_novice.opi"); }
            else          { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel.opi"); }
            //try   { lc.setPropertyValue("resize_behaviour",1); }
            //catch (err) { lc.setPropertyValue("auto_size",true); }
            //    lc.setPropertyValue("resize_behavior",2);
            lc.setPropertyValue("auto_size",true);
            lc.setPropertyValue("zoom_to_fit",false);
            lc.setPropertyValue("border_style",0);
            lc.setPropertyValue("background_color","Header_Background");
            
            lc.addMacro("C",iChan);
            lc.addMacro("P",pv);
            widget.addChildToBottom(lc);

        }

    }

}
