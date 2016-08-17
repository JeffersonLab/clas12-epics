importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var panel  = widget.getMacroValue("PANEL");
var sector = widget.getMacroValue("SECTOR");
var side   = widget.getMacroValue("SIDE");

var label = "            Turn  ON  HV\n\n";
label += "FTOF, ";
if (sector==0) label += "All Sectors, ";
else           label += "Sector "+sector+", ";
if (panel==0)  label += "All Panels, ";
else           label += "Panel "+panel+", ";
if (side==0)   label += "Left & Right";
else if (side=="L") label += "Left";
else if (side=="R") label += "Right";
label += "\n\n               Really??"

var response = GUIUtil.openConfirmDialog(label);
if (response)
{

    var nSectors=6;
    var sides=["L","R"];
    var panels=["1B","1A","2"];
    var nChans=[62,23,5];

    var prefix="B_DET_FTOF_HV";

    for (var iSec=1; iSec<=nSectors; iSec++)
    {
        if (sector!=0 && iSec!=sector) continue;

        for (var iPan=0; iPan<panels.length; iPan++)
        {
            if (panel!=0 && panels[iPan]!=panel) continue;

            for (var iChan=1; iChan<=nChans[iPan]; iChan++)
            {

                for (var iSide=0; iSide<sides.length; iSide++)
                {

                    if (side!=0 && sides[iSide]!=side) continue;

                    var thisChan=iChan<10?"0"+iChan:iChan;

                    var suff="_SEC"+iSec+
                        "_PANEL"+panels[iPan]+
                        "_"+sides[iSide]+
                        "_E"+thisChan;

                    PVUtil.writePV(prefix+suff+":pwonoff",1);
                    //java.lang.System.err.println(suff);


                }

            }

        }

    }

}
