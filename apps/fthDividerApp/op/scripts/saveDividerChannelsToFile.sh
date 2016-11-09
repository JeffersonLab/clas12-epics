#!/bin/sh
#script to save the channel widths and amplitudes for the LED flasher
#1st arg is the Prefix for the EPICS device. Eg B_FT_FLASHER

ampChan="${1}:GET_AMP_ALL";
outfile=`caget -S -t ${1}:DATA_FILE_SAVE`
echo $outfile

#Get all the values from the waveform arrays. and write a file like this:
#nchan
#ID amp
#0  240
#1  240
#...
#...
#This is a format that can be sent to the device via the tftp server, or using the loadFlasherChannelsFromFile.sh command.
caget -t $ampChan | \
    gawk '{\
       chan=$1;print chan;\
       for(n=2;n<chan+2;n++){ amp[n-2]=$n};\
    }\
    END{for (n=0;n<chan;n++){print n,amp[n]}}' > $outfile
