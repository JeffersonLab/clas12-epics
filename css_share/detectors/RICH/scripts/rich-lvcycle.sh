#!/bin/bash
# quick hack to cycle RICH LV and reinitialize FPGAs, and output to log file

logfile="/usr/clas12/DATA/logs/rich-lvcycle.logtmp"
log="tee -a $logfile"

# this was probably because ssh keys are required:
me=`whoami`
if ! [ $me == "clasrun" ]
then
    echo "You must be clasrun, but you are $me" | $log
    exit
fi

function date_msg {
    date | $log
}

function start_msg {
    date_msg
    echo "-----------------------------------------------------" | $log
    echo "|                                                   |" | $log
    echo "| NOTE: this will trigger some RICH alarms, which   |" | $log
    echo "|   can be ignored until this recovery exits.       |" | $log
    echo "|                                                   |" | $log
    echo "| NOTE: the DAQ will need to be reinitialized after |" | $log
    echo "|  ***AFTER*** this script is complete:             |" | $log
    echo "|                                                   |" | $log
    echo "|   Cancel->Reset->Configure->Download->Prestart    |" | $log
    echo "|                                                   |" | $log
    echo "-----------------------------------------------------" | $log
    echo  | $log
}

function failure_msg {
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" | $log
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" | $log
    echo "!                                                  !" | $log
    echo "!  $@" | $log
    echo "!                                                  !" | $log
    echo "!            !!  Contact RICH Expert !!            !" | $log
    echo "!                                                  !" | $log
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" | $log
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" | $log
    date_msg
    echo "press Return to continue, which will close this window!"
    read
    exit 1
}

function success_msg {
    echo  | $log
    echo "-----------------------------------------------------" | $log
    echo "|                                                   |" | $log
    echo "|    RICH RECOVERY SUCCESFUL!!!   ($@)   |" | $log
    echo "|                                                   |" | $log
    echo "| -----------   WARNING, SEE BELOW   -------------  |" | $log
    echo "|                                                   |" | $log
    echo "| NOTE1: RICH temperatures and scalers can take up  |" | $log
    echo "|     to one minute to update after this recovery.  |" | $log
    echo "|                                                   |" | $log
    echo "| NOTE2: the DAQ will now need to be reinitialized: |" | $log
    echo "|   Cancel->Reset->Configure->Download->Prestart    |" | $log
    echo "|                                                   |" | $log
    echo "-----------------------------------------------------" | $log
    date_msg
    echo "press Return to continue, which will close this window!"
    read
    exit 0
}

#function checkscalers {
  #maxattempts=$1
  #waits=$2
  #nattempts=0
  #while [ $nattempts -lt $maxattempts ]
  #do
#    stat=`caget -t B_DET_RICH_SCALERS_PMTS:max`
#    if [ $stat -le 0 ]
#    then
#        return 1
#    fi
#    stat=`caget -t B_DET_RICH2_SCALERS_PMTS:max`
#    if [ $stat -le 0 ]
#    then
#        return 1
#    fi
  #done
#  return 0
#}

function iocreboot {
    comms=`caget -t B_DET_RICH_ALL_LV:isComm`
    [ $? -eq 0 ] && [ $comms -eq 1 ] && return
    echo -e "\nRebooting RICH HVCAEN IOC ...\n" | $log
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
  caput $pvGo 1 | $log
  sleep 5
  while [ 1 ]
  do
      sleep 1
      echo -n '.'
      stat=`caget -t $pvCheck`
      if [ $stat -eq 1 ]
      then
          sleep 1
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
              caput B_HW_HVRICH2:ClearAlarm 1 | $log
              sleep 5
              caput $pvGo 1 | $log
              sleep 5
              let cnt=$cnt-15
          else
              failure_msg ERROR on $pvCheck or ClearAlarm
          fi
      fi
  done
}

function checkssh {
  hostname=$1
  maxtries=$2
  delay=$3
  tries=0
  echo -e "\nWaiting $delay seconds before trying to connect to rich4 ..." | $log
  for xx in `seq $delay`
  do
      echo -n '.' | $log
      sleep 1
  done
  while [ 1 ]
  do
    let tries=$tries+1
    echo && echo -n -e "\nAttempting ssh ... " | $log
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
        failure_msg ERROR on SSH to $hostname
    fi
    sleep 1
  done
}

############################################################
############################################################
############################################################
############################################################
############################################################

start_msg

maxattempts=4
nattempts=0

# if scalers are all zero, skip the 1st iteration to make 
# roc_reboot happen first: 
#checkscalers
#if [ $? -ne 0 ]
#then
#    let nattempts=$nattempts+1
#    let maxattempts=$maxattempts+1
#fi

echo -e "\n!!!!   RICH RECOVERY   !!!!\n\n" | $log

iocreboot

while [ 1 ]
do

    let nattempts=$nattempts+1

    echo -e "\n!!!!   RICH RECOVERY #$nattempts  !!!!\n\n" | $log
    
    echo -e "\nTurning RICH LV OFF ...\n" | $log

    lvcycle B_DET_RICH_ALL_LV:OFF B_DET_RICH_ALL_LV:isOff

    echo -e "\nRICH LV OFF succecsfull.\n\nTurning RICH LV ON ...\n" | $log

    lvcycle B_DET_RICH_ALL_LV:ON B_DET_RICH_ALL_LV:isOn

    echo -e "\nRICH LV ON succesfull.\n" | $log

    let odd=$nattempts%2

    if [ $odd -eq 0 ]
    then
        # need to change the BIOS for this to do what Ben wants:
        #ssh rich4 'vme_sysreset && tiinit && rich_init' | $log
        # meanwhile, stick to this:
        echo -e "\nRebooting rich4 ...\n" | $log
        roc_reboot rich4 | $log
        checkssh rich4 60 70
        sleep 10
    fi

    echo -e "\nrunning rich_init ..." | $log
    ssh rich4 rich_init | $log
    ntiles=`tail -100 $logfile | grep 'Total Tiles' | awk '{print$4}'`
    echo $ntiles
  
    #sleep 10
    #check_scalers
    #if [ $? -eq 0 ] &&
    if [ $ntiles -eq 276 ]
    then
        success_msg "on attempt #$nattempts"
        break
    elif [ $nattempts -gt $maxattempts ]
    then
        failure_msg TERMINAL FAILURE, $maxattempts TIMES, CANNOT SUCCEED
        break
    else
        echo -e "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" | $log
        echo -e "FAILURE on attempt #$nattempts !!!!!!!!!!!!!!!!!!!!!!!!!!!!" | $log
        echo -e "RETRYING ...           !!!!!!!!!!!!!!!!!!!!!!!!!!!!" | $log
        date_msg
        echo -e "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" | $log
    fi
done


