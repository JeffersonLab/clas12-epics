#!/bin/bash

function failure_msg {
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    echo "!                                                  !"
    echo "!  $@"
    echo "!                                                  !"
    echo "!            !!  Contact RICH Expert !!            !"
    echo "!                                                  !"
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    date
#sergey: commemnt out for batch execution
#    echo "press Return to continue, which will close this window!"
#    read
    exit 1
}

function iocreboot {
    comms=`caget -t B_DET_RICH_ALL_LV:isComm`
    [ $? -eq 0 ] && [ $comms -eq 1 ] && return
    echo -e "\nRebooting RICH HVCAEN IOC ...\n"
    pv=ioccaenhv_HVRICH:SysReset
    caput $pv 1
    sleep 5
    count=0
    while [ 1 ]
    do
        if [ $count -gt 20 ]
        then
            failure_msg ERROR on $pv reboot
        fi
        stat=`caget -w 0.1 -t $pv`
        if [ $? -eq 0 ]
        then
            sleep 1
            break
        fi
        let count=$count+1
        sleep 1
    done
}

function lvcycle {
  pvGo=$1
  pvCheck=$2
  cnt=0
  cnterr=0
  caput $pvGo 1
  sleep 3
  while [ 1 ]
  do
      sleep 1
      echo -n '.'
      stat=`caget -t $pvCheck`
      if [ $stat -eq 1 ]
      then
          break
      fi
      let cnt=$cnt+1
      if [ $cnt -gt 10 ]
      then
          let cnterr=$cnterr+1
          if [ $cnterr -lt 3 ]
          then
              echo "Trying Again to Clear Errors ..."
              caput B_HW_HVRICH1:ClearAlarm 1
              caput B_HW_HVRICH2:ClearAlarm 1
              sleep 2
              caput $pvGo 1
              sleep 3
              let cnt=$cnt-15
          else
              failure_msg ERROR on $pvCheck or ClearAlarm
              return 1
          fi
      fi
  done
  return 0
}

############################################################
############################################################
############################################################
############################################################
############################################################

date

maxattempts=4
nattempts=0

echo -e "\n!!!!   RICH RECOVERY   !!!!\n\n"

iocreboot

let nattempts=$nattempts+1

echo -e "\n!!!!   RICH RECOVERY #$nattempts  !!!!\n\n"
    
echo -e "\nTurning RICH LV OFF ...\n"

lvcycle B_DET_RICH_ALL_LV:OFF B_DET_RICH_ALL_LV:isOff
#[ $? -ne 0 ] && exit 1

echo -e "\nRICH LV OFF succecsfull.\n\nTurning RICH LV ON ...\n"

lvcycle B_DET_RICH_ALL_LV:ON B_DET_RICH_ALL_LV:isOn
#[ $? -ne 0 ] && exit 2

echo -e "\nRICH LV ON succesfull.\n"

exit 0

