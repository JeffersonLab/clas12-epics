#!/bin/sh

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &&  pwd )"

# companion script:
DGSRESTARTSCRIPT=$DIR/dgsRestart.sh

USAGE='dgsIocRestart.sh [sector# OR crateName]'

CRATES=( adcecal tdcecal adcpcal tdcpcal adcftof tdcftof )

function iocReboot
{
    sector=$1
    echo Rebooting jscaler IOC for sector $sector ...
    softioc_console -R iocjscalers$sector
}

function iocRebootByCrate
{
    crate=$1
    ii=$((${#crate}-1))
    sector=${crate:$ii:1}
    iocReboot $sector
}

function dgsReboot
{
    crate=$1
    echo Rebooting DiagGuiServer on $crate ...
    ssh $crate $DGSRESTARTSCRIPT
}

function dgsAndIocRebootByCrate
{
    crate=$1
    dgsReboot $crate
    sleep 2
    iocRebootByCrate $crate
}

function sectorReboot
{
    sector=$1
    for crate in ${CRATES[@]}
    do
        dgsReboot $crate$sector
    done
    sleep 2
    iocReboot $sector
}

if [ -z $1 ] || ! [ -z $2 ]
then
    echo $USAGE
    exit
fi

if [[ $1 == 1 || $1 == 2 || $1 == 3 || $1 == 4 || $1 == 5 || $1 == 6 ]]
then
    sectorReboot $1
else
    crate=$1
    ii=$((${#crate}-1))
    sec=${crate:$ii:1}
    cratestub=${crate:0:$ii}
    found=0
    for crate in ${CRATES[@]}
    do
        if [ "$crate" = "$cratestub" ]
        then
            found=1
            break
        fi
    done
    if [ $found != 1 ]
    then
        echo Invalid Crate:  $1
        echo $USAGE
        exit
    fi
    if [[ $sec != 1 && $sec != 2 && $sec != 3 && $sec != 4 && $sec != 5 && $sec != 6 ]]
    then
        echo Invalid Sector:  $1
        echo $USAGE
        exit
    fi

    dgsAndIocRebootByCrate $crate$sec
fi




#exit

#crate=$1
#
#ii=$((${#crate}-1))
#sector=${crate:$ii:1}
#
#echo ssh $crate 'echo 18 | xxd -r -p | nc localhost 20030'
#echo softioc_console -R iocjscalersS$sector
#
#crates=( adcecal tdcecal adcpcal tdcpcal adcftof tdcftof )
#
#
#sector=4
#for crate in ${crates[@]}
#do
#    echo $crate
#    echo ssh $crate$sector 'echo 18 | xxd -r -p | nc localhost 20030'
##    rebootdgs $crate$sector
#done
#
##rebootioc $sector



