importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

//widget.removeAllChildren();

var novice = PVUtil.getDouble(pvs[0]);
var layer = widget.getMacroValue("LAYER");
var side  = widget.getMacroValue("SIDE");

var prefix="B_DET_BAND_HV_";
var nChans_noAB=10;
var layers=["1","2","3","4","5","V"];
var nChans_AB=[6,6,6,6,5,6];
var nChans_noAB2=[2,2,2,2,0,2];
var sides=[["L","R"],["L","R"],["L","R"],["L","R"],["L","R"],[""]];

java.lang.System.out.println(novice+" "+layer+" "+side);

function mkChan(layer,side,chan,suff) {
    
    var chan2 = chan<10 ? "0"+chan : chan;
    var pv = prefix+layer+chan2+suff+side;
    //java.lang.System.out.println("MK:"+pv);

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
    lc.addMacro("C",chan);
    lc.addMacro("P",pv);
    widget.addChildToBottom(lc);
}


for (var iLay=0; iLay<layers.length; iLay++)
{
    //java.lang.System.out.println("L"+iLay);

    if (layer!=0 && layers[iLay]!=layer) continue;
    for (var iSide=0; iSide<sides[iLay].length; iSide++) {

        //java.lang.System.out.println("S"+iSide);

        if (side!=0 && sides[iLay][iSide]!=side) continue;
        
        var thisSide = sides[iLay][iSide];
        if (thisSide!="") thisSide="_"+thisSide;
        //java.lang.System.out.println("SB"+thisSide);

        var iChan=1;
        
        //java.lang.System.out.println("NC"+nChans_noAB+nChans_AB[iLay]+nChans_noAB2[iLay]);

        while (iChan <= nChans_noAB+nChans_AB[iLay]+nChans_noAB2[iLay]) {

            //java.lang.System.out.println("C"+iChan);

            var chan;
            if (iChan > nChans_noAB + nChans_AB[iLay]) {
                mkChan(layers[iLay],thisSide,iChan,"");
            }
            else if (iChan > nChans_noAB) {
                mkChan(layers[iLay],thisSide,iChan,"A");
                mkChan(layers[iLay],thisSide,iChan,"B");
            }
            else {
                mkChan(layers[iLay],thisSide,iChan,"");
            }
            iChan++;
        }
    }
}

