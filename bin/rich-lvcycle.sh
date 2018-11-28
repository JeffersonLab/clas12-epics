#!/bin/bash
# quick hack to cycle RICH LV and reinitialize FPGAs, and output to log file

log="tee -a /usr/clas12/DATA/logs/rich-lvcycle.logtmp"

me=`whoami`
if ! [ $me == "clasrun" ]
then
    echo "You must be clasrun, but you are $me" | $log
    exit
fi

function lvcycle {
  pvGo=$1
  pvCheck=$2
  cnt=0
  cnterr=0
  caput $pvGo 1 | $log
  while [ 1 ]
  do
      echo -n '.'
      stat=`caget -t $pvCheck`
      if [ $stat -eq 1 ]
      then
          sleep 4
          break
      fi
      let cnt=$cnt+1
      if [ $cnt -gt 20 ]
      then
          let cnterr=$cnterr+1
          if [ $cnterr -lt 3 ]
          then
              echo "Trying Again to Clear Errors ..." | $log
              caput B_HW_HVRICH1:ClearAlarm 1 | $log
              sleep 5
              caput $pvGo 1 | $log
              sleep 5
              let cnt=$cnt-15
          else
              echo "####################################################" | $log
              echo "#                                                  #" | $log
              echo "#  ERROR ON $pvCheck or **ClearAlarm**  #" | $log
              echo "#                                                  #" | $log
              echo "#            !!  Contact RICH Expert !!            #" | $log
              echo "#                                                  #" | $log
              echo "####################################################" | $log
              exit
          fi
      fi
      sleep 1
  done
}

date | $log
echo -e "\n!!!!   RICH RECOVERY   !!!!\n\nTurning RICH LV OFF ...\n" | $log
lvcycle B_DET_RICH_LV:OFF B_DET_RICH_LV:isOff
echo -e "\nRICH LV OFF succecsfull.\n\nTurning RICH LV ON ...\n" | $log
lvcycle B_DET_RICH_LV:ON B_DET_RICH_LV:isOn
echo -e "\nRICH LV ON succesfull.\n\nRunning rich_init on rich4 ...\n" | $log
sleep 5
ssh rich4 rich_init | $log

echo  | $log
echo "####################################################" | $log
echo "#                                                  #" | $log
echo "#           rich-lvcycle.sh COMPLETE               #" | $log
echo "#                                                  #" | $log
echo "####################################################" | $log
date | $log

echo "press Return to continue"
read


