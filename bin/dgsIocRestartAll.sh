#!/bin/sh

DGSOWNER=clasrun
if [[ `whoami` != $DGSOWNER ]]
then
    echo
    echo ERROR:  DiagGuiServer is owned by $DGSOWNER, but you are `whoami`.
    echo Exiting ....
    echo
    exit
fi

xt='xterm -bg red -fg white -geometry 90x30'

$xt+0+0     -e dgsIocRestart.sh 1 &
$xt+20+20   -e dgsIocRestart.sh 2 &
$xt+40+40   -e dgsIocRestart.sh 3 &
$xt+60+60   -e dgsIocRestart.sh 4 &
$xt+80+80   -e dgsIocRestart.sh 5 &
$xt+100+100 -e dgsIocRestart.sh 6 &
$xt+120+120 -e dgsIocRestart.sh C &
$xt+140+140 -e dgsIocRestart.sh T &

