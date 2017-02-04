#!/bin/sh

d=$EPICS/tools/stripCharts

x='-xrm StripTool.StripGraph.width:1000'
y='-xrm StripTool.StripGraph.height:300'

#StripTool $x $y $d/beamline_xpos.stp    >& /dev/null &
#StripTool $x $y $d/beamline_ypos.stp    >& /dev/null &
#StripTool $x $y $d/beamline_current.stp >& /dev/null &
#StripTool $x $y $d/beamline_scalers.stp >& /dev/null &

StripTool $x $y $d/BLINE2/Current    >& /dev/null &
StripTool $x $y $d/BLINE2/Scalers    >& /dev/null &
StripTool $x $y $d/BLINE2/X-Position >& /dev/null &
StripTool $x $y $d/BLINE2/Y-Position >& /dev/null &

