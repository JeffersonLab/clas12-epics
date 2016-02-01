importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

//widget.removeAllChildren();

importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var novice = PVUtil.getDouble(pvs[0]);

var pio    = widget.getMacroValue("PIO"); 
var uvw    = widget.getMacroValue("UVW");
var sector = widget.getMacroValue("SECTOR");

var nsectors=6;
var uvws=["U","V","W"];
var pios=["","I","O"];
var nchans=[68,36,36];

for (var isec=1; isec<=nsectors; isec++)
{
    if (sector!=0 && isec!=sector) continue;

    for (var ipio=0; ipio<pios.length; ipio++)
    {
        if (pio!="0") {
            if (pio=="I" || pio=="O" || pio=="IO") {
                if (ipio==0) continue;
                if (pio.toString().indexOf(pios[ipio])<0) continue;
            }
            else if (ipio!=0)  continue;
        }

        var prefix;
        if (pios[ipio]=="") prefix="B_DET_PCAL_HV";
        else                 prefix="B_DET_ECAL_HV";

        for (var iuvw=0; iuvw<uvws.length; iuvw++)
        {
            if (uvw!=0 && uvws[iuvw]!=uvw) continue;

            for (var ichan=1; ichan<=nchans[ipio]; ichan++)
            {
                if (pios[ipio]=="" && uvws[iuvw]!="U" && ichan>62) continue;

                var thischan=ichan<10?"0"+ichan:ichan;

                var thispio=pios[ipio]==""?"":pios[ipio];

                var suffix="_SEC"+isec+
                    "_"+uvws[iuvw]+thispio+
                    "_E"+thischan;

//                java.lang.System.err.println(suff);
                
                
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
}

