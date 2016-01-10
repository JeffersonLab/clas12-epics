importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

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
        if (pio!="0" && pios[ipio]!=pio) continue;

        var prefix;
        if (pios[ipio]=="") prefix="B_DET_PCAL_HV";
        else                prefix="B_DET_ECAL_HV";

        for (var iuvw=0; iuvw<uvws.length; iuvw++)
        {
            if (uvw!=0 && uvws[iuvw]!=uvw) continue;

            for (var ichan=1; ichan<=nchans[ipio]; ichan++)
            {
                if (pios[ipio]=="" && uvws[iuvw]!="U" && ichan>62) continue;

                var thischan=ichan<10?"0"+ichan:ichan;

                var thispio=pios[ipio]==""?"":pios[ipio];

                var suff="_SEC"+isec+
                    "_"+uvws[iuvw]+thispio+
                    "_E"+thischan;

                        PVUtil.writePV(prefix+suff+":pwonoff",1);
                
                //java.lang.System.err.println(prefix+suff);


            }
        }
    }
}

