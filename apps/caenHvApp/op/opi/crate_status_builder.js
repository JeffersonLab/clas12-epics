importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var crate = widget.getMacroValue("CRATE");
var nslot = widget.getMacroValue("NSLOT");
var nchan = widget.getMacroValue("NCHAN");
var type = widget.getMacroValue("TYPE");
var argh = widget.getMacroValue("ARGH");

//java.lang.System.out.println("crate_status_builder.js  " + argh + " " + crate + " " + nslot + " " + nchan);


for (var chan=0; chan < 24+1; chan++)
{
    //java.lang.System.out.print(" " + chan);

	var head = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.Label");
	head.setWidth(50);
	head.setHeight(21);
	head.setPropertyValue("border_style",0);
	if (chan==0) head.setText("");
	else         head.setText(chan-1);
	head.setPropertyValue("foreground_color","Header_Foreground");
	head.setPropertyValue("background_color","Header_Background");
	widget.addChildToBottom(head);
}

for (var slot=0; slot<nslot; slot++)
{
  if (slot<10) slot="0"+slot;
  //java.lang.System.out.println(argh + " " + crate + " " + slot);

  var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
  lc.setPropertyValue("opi_file","status_board_channels.opi");
  lc.setPropertyValue("background_color","Header_Background");
  
  //try   { lc.setPropertyValue("resize_behaviour",1); }
  //catch (err) { lc.setPropertyValue("auto_size",true); }
  lc.setPropertyValue("auto_size",false);
  lc.setPropertyValue("zoom_to_fit",false);
  lc.setPropertyValue("resize_behaviour",2);
  
  //lc.setWidth(56);
  lc.setWidth(56);
  lc.setHeight(560);
  lc.setPropertyValue("border_style",0);
  lc.addMacro("SLOT",slot);
  lc.addMacro("NCHAN",nchan);
  lc.addMacro("CRATE",crate);
  lc.addMacro("TYPE",type);
  lc.addMacro("ARGH",argh);
  widget.addChildToRight(lc);
}