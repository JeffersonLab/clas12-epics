importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var novice = PVUtil.getDouble(pvs[0]);

var lr     = widget.getMacroValue("LR"); 
var sector = widget.getMacroValue("SECTOR");

var prefix="B_DET_HTCC_HV";
var nsectors=6;
var lrs=["L","R"];
var nchans=4;

for (var isec=1; isec<=nsectors; isec++)
{
    if (sector!=0 && isec!=sector) continue;

            for (var ichan=1; ichan<=nchans; ichan++)
            {
                var thischan=ichan<10?"0"+ichan:ichan;

    for (var ilr=0; ilr<lrs.length; ilr++)
    {
        if (lr!="0" && lr!=lrs[ilr] && lr!=lrs[ilr]) continue;

                var suffix="_SEC"+isec+"_"+lrs[ilr]+ichan;

//                java.lang.System.err.println(suffix);
                
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
            lc.addMacro("C",ichan);
            lc.addMacro("P",prefix+suffix);
            widget.addChildToBottom(lc);

           
        }
    }
}

