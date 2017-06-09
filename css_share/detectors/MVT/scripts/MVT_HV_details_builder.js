importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var novice = PVUtil.getDouble(pvs[0]);

var prefix = "B_DET_";

var nlayers=6;
var nsectors=3;
var ntypes=2;
var ninout=2;
var types=["DRIFT","STRIP"];
var inout=["IN","OUT"];
var ichan=0;

function makeWidget(pv)
{
    var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
    if (novice>0) { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel_novice-nA.opi"); }
    else          { lc.setPropertyValue("opi_file","/CLAS12_Share/apps/caenHvApp/caenhv_channel-nA.opi"); }
    //try   { lc.setPropertyValue("resize_behaviour",1); }
    //catch (err) { lc.setPropertyValue("auto_size",true); }
    lc.setPropertyValue("auto_size",true);
    lc.setPropertyValue("zoom_to_fit",false);
    lc.setPropertyValue("border_style",0);
    lc.setPropertyValue("background_color","Header_Background");
    lc.addMacro("C",ichan);
    lc.addMacro("P",pv);
    widget.addChildToBottom(lc);
    ichan++;
}


for (var isector=0; isector<nsectors; isector++)
{
    for (var itype=0; itype<ntypes; itype++)
    {
        for (var ilayer=0; ilayer<nlayers; ilayer++)
        {
            var pv=prefix+"BMT_HV_SEC"+(isector+1)+"_L"+(ilayer+1)+"_"+types[itype];
            makeWidget(pv);
        }
    }
}

for (var itype=0; itype<ntypes; itype++)
{
    for (var ilayer=0; ilayer<nlayers; ilayer++)
    {
        if (itype==0)
        {
            var pv=prefix+"FMT_HV_L"+(ilayer+1)+"_"+types[itype];
            makeWidget(pv);
        }
        else
        {
            for (var iinout=0; iinout<ninout; iinout++)
            {
                var pv=prefix+"FMT_HV_"+inout[iinout]+"_L"+(ilayer+1)+"_"+types[itype];
                makeWidget(pv);
            }
        }
    }
}


