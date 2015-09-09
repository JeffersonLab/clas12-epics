importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var argh  = widget.getMacroValue("ARGH");
var crate = widget.getMacroValue("CRATE");
var slot  = widget.getMacroValue("SLOT");
var nchan = widget.getMacroValue("NCHAN");

//java.lang.System.out.println(argh + " " + crate + " " + slot + " " + nchan);

var head = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.Label");
head.setWidth(50);
head.setHeight(20);
head.setPropertyValue("border_style",0);
head.setText(slot);
head.setPropertyValue("foreground_color","Header_ForeGround");
head.setPropertyValue("background_color","Header_Background");
widget.addChildToBottom(head);

for (var chan=0; chan<nchan; chan++)
{
  var pvprefix;
  if (argh == 1) { pvprefix = "B_" + crate + "_HV000_" + slot + "_" + chan; }
  else           { pvprefix = "B_" + crate + "_Sl" + slot + "_Ch" + chan; }

  var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
  lc.setPropertyValue("opi_file","status_channel.opi");
  //try   { lc.setPropertyValue("resize_behaviour",1); }
  //catch (err) { lc.setPropertyValue("auto_size",true); }
  lc.setPropertyValue("auto_size",true);
  lc.setPropertyValue("zoom_to_fit",false);
  lc.setPropertyValue("border_style",0);
  lc.addMacro("P",pvprefix);
  widget.addChildToBottom(lc);
//  java.lang.System.out.println(argh + " " + crate + " " + slot + " " + nchan + " " + chan + " " + pvprefix);
  
}