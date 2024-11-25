importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var novice = PVUtil.getDouble(pvs[0]);

function makeWidget(pv, n)
{
    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    if (novice>0) { lc.setPropertyValue("opi_file","../../apps/caenHvApp/caenhv_channel_novice-nA.opi"); }
    else          { lc.setPropertyValue("opi_file","../../apps/caenHvApp/caenhv_channel-nA.opi"); }
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    lc.addMacro("C",n);
    lc.addMacro("P",pv);
    widget.addChildToBottom(lc);
}

var n=1;
for (var s=1; s<=9; ++s) {
    for (var w=1; w<=3; ++w) {
        makeWidget("B_DET_AHDC_HV_S" + s + "-" + w, n++);
    }
}

