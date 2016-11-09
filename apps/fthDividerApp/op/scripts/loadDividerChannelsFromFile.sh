#!/bin/sh
#script to load the channel widths and amplitudes for the LED flasher
#1st arg is the prefix for the EPICS device. Eg B_FT_FLASHER

dataChan="${1}";

#Get the file with the values
infile=`caget -S -t ${1}:DATA_FILE_LOAD`
echo $infile

#Check the file exists
#if [ !  -e "$infile" ]; then
#    zenity --title="No datafile" --question --text "$outfile doesn't exist"; 
#    exit;
#fi

#The input file is in this form:
#nchan
#id1 ampl1
#id2 ampl1
#...
#idn ampn

com="${1}:SET_DRIVER_STATUS ON"
caput $com;

#stop updating  readback until done
com="${1}:GET_AMP_ALL.DISV 0"
caput $com;

gawk -v pv=$dataChan 'BEGIN{n=0;e=1}\
      {if(NF==2){id[n]=$1;amp[n]=$2;tot=n++}}\
      END{\
          for(n=0;n<=tot;n++){\
             if(id[n]<232){\
                 #out=sprintf("sleep 0.2;caput -t  %s_ID%03d:AMPSET %d",pv,id[n],amp[n]);\
                 out=sprintf("caput -t  %s_ID%03d:AMPSET %d",pv,id[n],amp[n]);\
                 system(out);\
                 print out;\
             }\
          }\
       }\
       ' $infile

#now reaenable readback and read once
com="${1}:GET_AMP_ALL.DISV 1"
caput $com;
com="${1}:GET_AMP_ALL.PROC 1"
caput $com;
exit
