importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

//widget.removeAllChildren();

//var crate  = PVUtil.getString(pvs[0]);
//var slot   = PVUtil.getDouble(pvs[1]); 
//var nchans = PVUtil.getDouble(pvs[2]);

var argh  = widget.getMacroValue("ARGH");
var crate = widget.getMacroValue("CRATE");
var slot  = widget.getMacroValue("SLOT");
var nchan = widget.getMacroValue("NCHAN");

//if (slot<10) slot="0"+slot;

for (var chan=0; chan<nchan; chan++)
{
  if (chan<10) chan="0"+chan;

  var pvprefix;
  if (argh == 1) { pvprefix = "B_HW_" + crate + "_HV000_" + slot + "_" + chan; }
  else           { pvprefix = "B_HW_" + crate + "_Sl" + slot + "_Ch" + chan; }

  var lc = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
  lc.setPropertyValue("opi_file","caenhv_channel-lv.opi");
  //try   { lc.setPropertyValue("resize_behaviour",1); }
  //catch (err) { lc.setPropertyValue("auto_size",true); }
  lc.setPropertyValue("auto_size",true);
  lc.setPropertyValue("zoom_to_fit",false);
  lc.setPropertyValue("border_style",0);
  lc.addMacro("C",chan);
  lc.addMacro("P",pvprefix);
  widget.addChildToBottom(lc);
}