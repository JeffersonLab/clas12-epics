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

xt='xterm -bg red -fg white'

$xt -e dgsIocRestart.sh 1 &
$xt -e dgsIocRestart.sh 2 &
$xt -e dgsIocRestart.sh 3 &
$xt -e dgsIocRestart.sh 4 &
$xt -e dgsIocRestart.sh 5 &
$xt -e dgsIocRestart.sh 6 &
$xt -e dgsIocRestart.sh C &
#$xt -e dgsIocRestart.sh T &

