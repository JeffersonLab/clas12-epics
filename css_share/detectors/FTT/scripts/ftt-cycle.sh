#!/bin/bash
# quick hack to cycle FTT LV and reinitialize FPGAs, and output to log file

log="tee -a /usr/clas12/DATA/logs/ftt-cycle.logtmp"

me=`whoami`
if ! [ $me == "clasrun" ]
then
    echo "You must be clasrun, but you are $me" | $log
    exit
fi

function control {
  action=$1
  pvOn=B_DET_FTT_LV:pwon
  pvOff=B_DET_FTT_LV:pwoff
  pvChecks=(B_DET_FTT_LV_0:parsed:stat_string
            B_DET_FTT_LV_1:parsed:stat_string
            B_DET_FTT_LV_2:parsed:stat_string)

  if [ $action == 'LVON' ]
  then
      pvGo=B_DET_FTT_LV:pwon
      statCheck='ON'
  elif [ $action == 'LVOFF' ]
  then
      pvGo=B_DET_FTT_LV:pwoff
      statCheck='OFF'
  elif [ $action == 'HVON' ]
  then
      pvGo=B_DET_FTT_HV:ON
      pvCheck=B_DET_FTT_HV:isOn
  elif [ $action == 'HVOFF' ]
  then
      pvGo=B_DET_FTT_HV:OFF
      pvCheck=B_DET_FTT_HV:isOff
  else
      echo NO
      exit
  fi

#  echo $pvGo $statCheck

  cnt=0
  cnterr=0
  
  caput $pvGo 1 | $log
  sleep 17
  
  while [ 1 ]
  do
      sleep 2
      echo -n '.'
      stat=1

      if [[ $action =~ "LV" ]]
      then
        for pvCheck in ${pvChecks[@]}
        do
            x=`caget -t $pvCheck`
#            echo $x
            if [ $x != $statCheck ]
            then
                stat=0
                break
            fi
        done
      else
          stat=`caget -t $pvCheck`
      fi

      if [ $stat -eq 1 ]
      then
          sleep 4
          break
      fi
      let cnt=$cnt+1
      if [ $cnt -gt 20 ]
      then
          let cnterr=$cnterr+1
          if [ $cnterr -gt 3 ]
          then
              echo "####################################################" | $log
              echo "#                                                  #" | $log
              echo "#  ERROR ON $pvCheck       #" | $log
              echo "#                                                  #" | $log
              echo "#            !!  Contact FTT Expert !!             #" | $log
              echo "#                                                  #" | $log
              echo "####################################################" | $log
              exit
          fi
      fi
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
echo "#####################################################" | $log
echo "#                                                   #" | $log
echo "# NOTE: the DAQ will need to be reinitialized after #" | $log
echo "#  ***AFTER*** this script tis complete:            #" | $log
echo "#                                                   #" | $log
echo "#   Cancel->Reset->Configure->Download->Prestart    #" | $log
echo "#                                                   #" | $log
echo "#####################################################" | $log
echo  | $log

echo -e "\n!!!!   FTT RECOVERY   !!!!\n\nTurning FTT HV OFF ...\n" | $log

control HVOFF

echo -e "\nFTT HV OFF succecsfull.\n\nTurning FTT LV OFF ...\n" | $log

control LVOFF

echo -e "\nFTT LV OFF succecsfull.\n\nTurning FTT LV ON ...\n" | $log

control LVON

echo -e "\nFTT LV ON succesfull.\n\nRebooting mmft1 ...\n" | $log

roc_reboot mmft1 | $log

echo -e "\nWaiting 65 seconds before trying to connect to mmft1 ..." | $log
for xx in `seq 55`
do
    echo -n '.' | $log
    sleep 1
done

echo
checkssh mmft1 60
sleep 5

echo -e "\nReboot mmft1 succecsfull.\n\nTurning FTT HV ON ...\n" | $log

control HVON

echo  | $log
echo "####################################################" | $log
echo "#                                                  #" | $log
echo "#           ftt-cycle.sh COMPLETE                  #" | $log
echo "#                                                  #" | $log
echo "# !!!!!!!!!!!   WARNING, SEE BELOW   !!!!!!!!!!!!! #" | $log
echo "#                                                  #" | $log
echo "# NOTE: the DAQ will now need to be reinitialized: #" | $log
echo "#   Cancel->Reset->Configure->Download->Prestart   #" | $log
echo "#                                                  #" | $log
echo "####################################################" | $log
date | $log

echo "press Return to continue"
read

