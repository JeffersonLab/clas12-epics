importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var label="\n     Really set All DC HV to        \n";
label   +="\n              10 V ?            \n";

if (GUIUtil.openConfirmDialog(label))
{

  var PREFIX = "B_DET_DC_HV";

  var NSECTORS=6;
  var NREGIONS=3;

  var W_S = ["01-08","09-16","17-24","25-32","33-48","49-64","65-80","81-112"];
  var W_F = ["01-08","09-16","17-24","25-32","33-48","49-64","65-80","81-112"];
  var W_G = ["01-32","33-112"];
  
  var SLREG = { 1:[1,2] , 2:[3,4] , 3:[5,6] };
  var WSFG  = { "S":W_S , "F":W_F , "G":W_G };

  //java.lang.System.err.println("dchv_10V.js:  ENTER");

  for (var isec=1; isec<=NSECTORS; isec++) {
    for (var ireg=1; ireg<=NREGIONS; ireg++) {
      for (var islay=0; islay<SLREG[ireg].length; islay++) {
        var slay=SLREG[ireg][islay];
        for (var sfg in WSFG) {
          for (var iwire=0; iwire<WSFG[sfg].length; iwire++) {
            var wires=WSFG[sfg][iwire];

            var suffix = "_SEC"+isec+"_R"+ireg+"_SL"+slay+"_"+sfg+wires;
            var pv = PREFIX+suffix+":vset";

            //          java.lang.System.err.println(pv);
            PVUtil.writePV(PREFIX+suffix+":vset",10);
          } 
        }
      }
    }
  }

}

