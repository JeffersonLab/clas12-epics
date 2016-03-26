importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var lr     = widget.getMacroValue("LR"); 
var sector = widget.getMacroValue("SECTOR");

var prefix="B_DET_HTCC_HV";
var nsectors=6;
var lrs=["L","R"];
var nchans=4;

for (var isec=1; isec<=nsectors; isec++)
{
    if (sector!=0 && isec!=sector) continue;

    for (var ilr=0; ilr<lrs.length; ilr++)
    {
        if (lr!="0" && lr!=lrs[ilr] && lr!=lrs[ilr]) continue;

            for (var ichan=1; ichan<=nchans; ichan++)
            {
                var thischan=ichan<10?"0"+ichan:ichan;

                var suffix="_SEC"+isec+"_"+lrs[ilr]+"_E"+thischan;

//                java.lang.System.err.println(suffix);              
            PVUtil.writePV(prefix+suffix+":pwonoff",1);

           
        }
    }
}

