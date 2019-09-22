#!/bin/sh
#
# wave2rootReader.sh
#
# Used to interface with Read_60Hz, the pdf creator.
#
# Notes:
#   ROOTSYS is hard-coded to prevent various versions of root being used from 
#   user environments.
#
#   Call using xterm -e as needed (ex. xterm -geometry 80x70 -e wave2rootReader.sh)
#
# Author: Wesley Moore
# Date:   Dec 2014
#

export ROOTSYS=/apps/root/5.34.21
export PATH=$ROOTSYS/bin:$PATH
export LD_LIBRARY_PATH=$ROOTSYS/lib
export READER=/usr/clas12/hps/prod/apps/bin/linux-x86/Read_60Hz
export WF_PATH=/usr/clas12/hps/DATA/waveforms

cd $WF_PATH

while [ 1 ]
do
    echo ""
    echo "Path: `pwd`"
    ls -l *.root
    echo ""
    echo "Enter the file name to read [Ctrl-c to quit]:"
    echo -n "> "
    read fn
    if [ -e $fn ]; then
        $READER $fn
	    if [ $? -eq 0 ]; then
	        # if owner, ensure all others can overwrite these files
	    	if [ -O sixtyHz_raw_14_vs_time.eps ]; then
	    		chmod 666 sixtyHz_raw_14_vs_time.eps
	    		chmod 666 sixtyHz_raw_14_vs_time.gif
	    		chmod 666 sixtyHz_raw_14_vs_time.pdf
	    	fi
	    	pdf=$(basename "$fn" .root).pdf
	    	cp sixtyHz_raw_14_vs_time.pdf $pdf
	    	if [ -O $pdf ]; then
        	    chmod 666 $pdf
        	fi
            evince $pdf &
        fi
    else
    	echo ""
    	echo "!!! File does not exist !!!"
    	echo ""
    fi
done

exit 0
