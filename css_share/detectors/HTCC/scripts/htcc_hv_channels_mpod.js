importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var novice = PVUtil.getDouble(pvs[0]);
var prefix = "B_DET_HTCC_HV_";
var lr = ["L","R"];

var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
if (novice) lc.setPropertyValue("opi_file","/CLAS12_Share/apps/mpodLvApp/iseg-channel-header-novice.opi");
else        lc.setPropertyValue("opi_file","/CLAS12_Share/apps/mpodLvApp/iseg-channel-header.opi");
lc.setPropertyValue("auto_size",true);
lc.setPropertyValue("zoom_to_fit",false);
lc.setPropertyValue("border_style",0);
lc.setPropertyValue("background_color","Header_Background");
widget.addChildToBottom(lc);

var index = 0;

for (var sector=1; sector<9; sector++) {
    for (var ring=1; ring<5; ring++) {
        for (var ilr=0; ilr<2; ilr++) {
            var pv = prefix + "SEC" + sector + "_" + lr[ilr] + ring;
            var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
            if (novice) lc.setPropertyValue("opi_file","/CLAS12_Share/apps/mpodLvApp/iseg-channel-row-novice.opi");
            else        lc.setPropertyValue("opi_file","/CLAS12_Share/apps/mpodLvApp/iseg-channel-row.opi");
            lc.setPropertyValue("auto_size",true);
            lc.setPropertyValue("zoom_to_fit",false);
            lc.setPropertyValue("border_style",0);
            lc.setPropertyValue("background_color","Header_Background");
            lc.addMacro("C","S"+sector+" "+lr[ilr]+ring);
            lc.addMacro("P",pv);
            var module = Math.floor(index/16) + 1;
            lc.addMacro("M",":"+module);
            lc.addMacro("N",module);
            widget.addChildToBottom(lc);
            index++;
        }
    }
}
