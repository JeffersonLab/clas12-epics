importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

NCHAN=widget.getMacroValue("N")
PREFIX=widget.getMacroValue("P")
SCALER=widget.getMacroValue("S")

for (var cc=0; cc<NCHAN; cc++) {

    chan=cc;
    if (cc<10) chan="0"+chan;

    var lc=WidgetUtil.createWidgetModel
           ("org.csstudio.opibuilder.widgets.TextUpdate");

    lc.setPropertyValue("background_color","Text_Background");
    lc.setPropertyValue("foreground_color","Header_Foreground");
    lc.setPropertyValue("width",60);
    lc.setPropertyValue("height",15);
    lc.setPropertyValue("horizontal_alignment",1);
    lc.setPropertyValue("font","Fine Print");
    lc.setPropertyValue("precision_from_pv",0);
    lc.setPropertyValue("precision",0);
    lc.setPropertyValue("pv_name",PREFIX+chan+":c"+SCALER);
    
    //java.lang.System.err.println(PREFIX+chan+":c"+SCALER);

    widget.addChildToBottom(lc);      
}