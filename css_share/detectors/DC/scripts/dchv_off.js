importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var PREFIX = "B_DET_DC_HV"

var SECTOR = widget.getMacroValue("SECTOR");
var REGION = widget.getMacroValue("REGION");
var SLAYER = widget.getMacroValue("SLAYER");
var SFG    = widget.getMacroValue("SFG");


var NSECTORS=6;
var NREGIONS=3;
var SLREG = { 1:[1,2], 2:[3,4], 3:[5,6] };
var W_S = ["01-08","09-16","17-24","25-32","33-48","49-64","65-80","81-112"];
var W_F = ["01-08","09-16","17-24","25-32","33-48","49-64","65-80","81-112"];
var W_G = ["01-32","33-112"];
var WSFG = {"S":W_S,"F":W_F,"G":W_G};

var ichan=0;

for (var isec=1; isec<=NSECTORS; isec++) {
  if (SECTOR!="0" && SECTOR!=isec) continue;
  for (var ireg=1; ireg<=NREGIONS; ireg++) {
    if (REGION!="0" && REGION!=ireg) continue;
    for (var islay=0; islay<SLREG[ireg].length; islay++) {
      var slay=SLREG[ireg][islay];
      if (SLAYER!="0" && SLAYER!=slay) continue;
      for (var sfg in WSFG) {
        for (var iwire=0; iwire<WSFG[sfg].length; iwire++) {
          var wires=WSFG[sfg][iwire];

            var suffix = "_SEC"+isec+"_R"+ireg+"_SL"+slay+"_"+sfg+wires;
            java.lang.System.err.println(suffix);
            PVUtil.writePV(PREFIX+suffix,0);
        } 
      }
    }
  }
}

