/* 
   if the total number of epics records exceeds 50, 
   you will need to extend the tmp_float array in
   scan.h to accomodate this increase.  And you will
   need to add addition "assign" statements in scan.h
   as well
*/

struct epics_rec {
  char real_name[50];
  char epics_name[24];
} hallb_string[] = {
  {"2C21 Current (nA)"                ,  "IPM2C21A.VAL"},
  {"2C24 Current (nA)"                ,  "IPM2C24A.VAL"},  
  {"2H00 Current (nA)"                ,  "IPM2H00.VAL"},
  {"2H01 Current (nA)"                ,  "IPM2H01.VAL"},
  {"2H02 Current (nA)"                ,  "IPM2H02.VAL"},
  {"2C21 X position (mm)"             ,  "IPM2C21A.XPOS"},
  {"2C24 X position (mm)"             ,  "IPM2C24A.XPOS"},
  {"2H00 X position (mm)"             ,  "IPM2H00.XPOS"},
  {"2H01 X position (mm)"             ,  "IPM2H01.XPOS"},
  {"2H02 X position (mm)"             ,  "IPM2H02.XPOS"},
  {"2C21 Y position (mm)"             ,  "IPM2C21A.YPOS"},
  {"2C24 Y position (mm)"             ,  "IPM2C24A.YPOS"},
  {"2H00 Y position (mm)"             ,  "IPM2H00.YPOS"},
  {"2H01 Y position (mm)"             ,  "IPM2H01.YPOS"},
  {"2H02 Y position (mm)"             ,  "IPM2H02.YPOS"},
  {"Tagger Current (Amps)"            ,  "TMIRBCK.VAL"},
  {"Faraday Cup Current (nA)"         ,  "scaler_calc1.VAL"},
  {"Beam Energy (MeV)"                ,  "MBSY2C_energy.VAL"},
  {"2C21 H corrector BDL (gauss-cm)"  ,  "MBC2C21H.BDL"},
  {"2C21 V corrector BDL (gauss-cm)"  ,  "MBC2C21V.BDL"},
  {"2C22 H corrector BDL (gauss-cm)"  ,  "MBC2C22H.BDL"},
  {"2C23 V corrector BDL (gauss-cm)"  ,  "MBC2C23V.BDL" },
  {"2H00 H corrector BDL (gauss-cm)"  ,  "MBC2H00H.BDL" },
  {"2H00 V corrector BDL (gauss-cm)"  ,  "MBC2H00V.BDL" },
  {"2H02 H corrector BDL (gauss-cm)"  ,  "MBC2H02H.BDL" },
  {"2H02 V corrector BDL (gauss-cm)"  ,  "MBC2H02V.BDL" },
  {"EOL"                              ,  "EOL"}
};

