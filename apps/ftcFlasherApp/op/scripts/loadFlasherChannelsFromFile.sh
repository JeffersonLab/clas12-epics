#!/bin/sh
#script to load the channel widths and amplitudes for the LED flasher
#1st arg is the prefix for the EPICS device. Eg B_FT_FLASHER

dataChan="${1}:SET_DATA";

#Get the file with the values
infile=`caget -S -t ${1}:DATA_FILE_LOAD`
echo $infile

#Check the file exists
if [ !  -e "$infile" ]; then
    zenity --title="No datafile" --question --text "$outfile doesn't exist"; 
    exit;
fi

#The input file is in this form:
#nchan
#id1 ampl1 width1
#id2 ampl1 width1
#...
#idn ampn widthn

#it needs to be made into a load of caputs like this:
#only doing 10 lines at once due to buffer size
#caput -a dataChan Nelem nchan id1 ampl1 width1 id1 ampl2 width2 .... idn ampln widthn
#where Nelem = 3*nchan +1 

gawk -v pv=$dataChan 'BEGIN{n=0;e=1}\
      {if(NF==3){id[n]=$1;amp[n]=$2;width[n]=$3;tot=n++}}\
      END{\
          e=0;data="";\
          for(n=0;n<=tot;n++){\
             data=sprintf("%s %d %d %d",data,id[n],amp[n],width[n]);\
             e++;\
             if((e==10)||(n==tot)){\
                out=sprintf("sleep 0.2;caput -t -a %s %d %d%s",pv,3*e+1,e,data);\
                system(out);
                print out;\
                e=0;\
                data="";
             }\
          }\
       }\
       ' $infile
#now force update of some EPICS values FLINKED from SELECTED_CHANNEL
com="${1}:SELECTED_CHANNEL.PROC 1";
caput $com;
exit
