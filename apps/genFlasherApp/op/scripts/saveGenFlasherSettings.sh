#!/bin/sh
P=$1
outfile=`caget -S -t ${1}:DATA_FILE_SAVE`


if [ -e "$outfile" ]; then

    if ! zenity --title="Confirm overwrite" --question --text "$outfile already exists. Overwrite?"; then
	exit;
    else
	/bin/rm $outfile
    fi
fi


for reg in "RO0" "RO1" "RO2" "RO3" "RO4" "RO5" "RO6" "RO7" "RO8" "RO9" "RO10" "J3_FREQ" "J4_FREQ"
do
    chan=${P}:${reg}
    val=`caget -t ${chan}`
    echo "saving: $chan $val"
    echo "$chan $val" >> ${outfile}
done

exit
