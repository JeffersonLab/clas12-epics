importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

NCHAN=widget.getMacroValue("N")
PREFIX=widget.getMacroValue("P")

for (var cc=1; cc<=NCHAN; cc++) {

    chan=cc;
    if (cc<10) chan="0"+chan;

    var lc=WidgetUtil.createWidgetModel
           ("org.csstudio.opibuilder.widgets.Label");

    lc.setPropertyValue("background_color","Text_Background");
    lc.setPropertyValue("foreground_color","Header_Foreground");
    lc.setPropertyValue("width",230);
    lc.setPropertyValue("height",15);
    lc.setPropertyValue("horizontal_alignment",0);
    lc.setPropertyValue("font","Fineprint");
    lc.setPropertyValue("text",PREFIX+chan);
    lc.setPropertyValue("transparent",0);

    widget.addChildToBottom(lc);      

}


/*
importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

NCHAN=widget.getMacroValue("N")
PREFIX=widget.getMacroValue("P")

for (var cc=1; cc<=NCHAN; cc++) {

    chan=cc;
    if (cc<10) chan="0"+chan;

    var lc=WidgetUtil.createWidgetModel
           ("org.csstudio.opibuilder.widgets.TextUpdate");

    lc.setPropertyValue("background_color","Text_Background");
    lc.setPropertyValue("foreground_color","Header_Foreground");
    lc.setPropertyValue("width",150);
    lc.setPropertyValue("height",15);
    lc.setPropertyValue("horizontal_alignment",1);
    lc.setPropertyValue("font","Fineprint");
    lc.setPropertyValue("precision_from_pv",0);
    lc.setPropertyValue("precision",0);
    lc.setPropertyValue("border_alarm_sensitive",0);
    lc.setPropertyValue("pv_name",PREFIX+chan+".DESC");
    
    //java.lang.System.err.println(PREFIX+chan+".NAME");

    widget.addChildToBottom(lc);      

}
*/
