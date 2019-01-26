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

function checkssh {
  hostname=$1
  maxtries=$2
  tries=0
  while [ 1 ]
  do
    let tries=$tries+1
    echo -n -e "Attempting ssh ... " | $log
    ssh -q $1 exit
    if [ $? -eq 0 ]
    then
        echo " SUCCESS." | $log
        break
    else
        echo " failed.  Retrying ..." | $log
    fi
    if [ $tries -gt $maxtries ]
    then
        echo "ERROR:  FAILED TO SSH.  Terminated." | $log
        exit
    fi
    sleep 1
  done
}

############################################################

date | $log

echo -e "\n!!!!   RICH RECOVERY   !!!!\n\nTurning RICH LV OFF ...\n" | $log

lvcycle B_DET_RICH_LV:OFF B_DET_RICH_LV:isOff

echo -e "\nRICH LV OFF succecsfull.\n\nTurning RICH LV ON ...\n" | $log

lvcycle B_DET_RICH_LV:ON B_DET_RICH_LV:isOn

echo -e "\nRICH LV ON succesfull.\n\nRebooting rich4 ...\n" | $log

roc_reboot rich4 | $log

echo -e "\nWaiting 55 seconds before trying to connect to rich4 ..." | $log
for xx in `seq 55`
do
    echo -n '.' | $log
    sleep 1
done

checkssh rich4 60
sleep 5

echo -e "\nrunning rich_init" | $log
ssh rich4 rich_init | $log

sleep 5
softioc_console -R iocjscalersRICH | $log

echo  | $log
echo "####################################################" | $log
echo "#                                                  #" | $log
echo "#           rich-lvcycle.sh COMPLETE               #" | $log
echo "#                                                  #" | $log
echo "####################################################" | $log
date | $log

echo "press Return to continue"
read

