importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var PREFIX = "B_DET_DC_LV"

var SECTOR = 0;//widget.getMacroValue("SECTOR");
var REGION = 0;//widget.getMacroValue("REGION");

var label = "Turn ON ALL DCLV?";

var response = GUIUtil.openConfirmDialog(label);

if (response)
{
  var NSECTORS=6;
  var NREGIONS=3;

  for (var isec=1; isec<=NSECTORS; isec++) {
      if (SECTOR!="0" && SECTOR!=isec) continue;
      for (var ireg=1; ireg<=NREGIONS; ireg++) {
          if (REGION!="0" && REGION!=ireg) continue;
          var suffix = "_SEC"+isec+"_R"+ireg+":pwset";
          java.lang.System.err.println(suffix);
          PVUtil.writePV(PREFIX+suffix,1);
      } 
  }
}
