#!/svt/csh -f

#@(#) svt.csh v1 2015/05/28 carlino@jlab.org

# common_setup sets PATH, rebootpath, and umask
#source /cs/opshome/burt/REBOOT/scripts/common_setup

#dd=/cs/opshome/burt/SVT
dd=/usr/clas12/DATA/burt/SVT

if ( $1 == "LVON" ) then
  set keyword = "AutoLog - Turn on LV to SVT"
  burtwb -f $dd/svt-lvon.snap
endif
if ( $1 == "LVOFF" ) then
  set keyword = "AutoLog - Turn off LV to SVT"
  burtwb -f $dd/svt-lvoff.snap
endif
if ( $1 == "HVON" ) then
  set keyword = "AutoLog - Turn on HV to SVT"
  burtwb -f $dd/svt-hvon.snap
endif
if ( $1 == "HVOFF" ) then
  set keyword = "AutoLog - Turn off HV to SVT"
  burtwb -f $dd/svt-hvoff.snap
endif
if ( $1 == "LVR1ON" ) then
  set keyword = "AutoLog - Turn on LV Region 1 to SVT"
  burtwb -f $dd/svt-lvr1on.snap
endif
if ( $1 == "LVR2ON" ) then
  set keyword = "AutoLog - Turn on LV Region 2 to SVT"
  burtwb -f $dd/svt-lvr2on.snap
endif
if ( $1 == "LVR3ON" ) then
  set keyword = "AutoLog - Turn on LV Region 3 to SVT"
  burtwb -f $dd/svt-lvr3on.snap
endif
if ( $1 == "LVR4ON" ) then
  set keyword = "AutoLog - Turn on LV Region 4 to SVT"
  burtwb -f $dd/svt-lvr4on.snap
endif
if ( $1 == "HVR1ON" ) then
  set keyword = "AutoLog - Turn on HV Region 1 to SVT"
  burtwb -f $dd/svt-hvr1on.snap
endif
if ( $1 == "HVR2ON" ) then
  set keyword = "AutoLog - Turn on HV Region 2 to SVT"
  burtwb -f $dd/svt-hvr2on.snap
endif
if ( $1 == "HVR3ON" ) then
  set keyword = "AutoLog - Turn on HV Region 3 to SVT"
  burtwb -f $dd/svt-hvr3on.snap
endif
if ( $1 == "HVR4ON" ) then
  set keyword = "AutoLog - Turn on HV Region 4 to SVT"
  burtwb -f $dd/svt-hvr4on.snap
endif
if ( $1 == "R1ON" ) then
  set keyword = "AutoLog - Turn on Region 1 to SVT"
  burtwb -f $dd/svt-r1on.snap
endif
if ( $1 == "R2ON" ) then
  set keyword = "AutoLog - Turn on Region 1 to SVT"
  burtwb -f $dd/svt-r2on.snap
endif
if ( $1 == "R3ON" ) then
  set keyword = "AutoLog - Turn on Region 1 to SVT"
  burtwb -f $dd/svt-r3on.snap
endif
if ( $1 == "R4ON" ) then
  set keyword = "AutoLog - Turn on Region 1 to SVT"
  burtwb -f $dd/svt-r4on.snap
endif
if ( $1 == "R1OFF" ) then
  set keyword = "AutoLog - Turn off Region 1 to SVT"
  burtwb -f $dd/svt-r1off.snap
endif
if ( $1 == "R2OFF" ) then
  set keyword = "AutoLog - Turn off Region 1 to SVT"
  burtwb -f $dd/svt-r2off.snap
endif
if ( $1 == "R3OFF" ) then
  set keyword = "AutoLog - Turn off Region 1 to SVT"
  burtwb -f $dd/svt-r3off.snap
endif
if ( $1 == "R4OFF" ) then
  set keyword = "AutoLog - Turn off Region 1 to SVT"
  burtwb -f $dd/svt-r4off.snap
endif


