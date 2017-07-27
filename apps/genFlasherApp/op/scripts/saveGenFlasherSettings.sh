#!/bin/sh
if [ $# -ne 2 ]; then
    echo "Usage: $0 <module> <0|1>"
    exit 
fi

P="$1:F$2"
today=`date`

outfile=`caget -S -t ${P}_DATA_FILE_SAVE`

echo "#Settings for ${P} saved on ${today}" > ${outfile}
echo "#To load these back into flasher F0/F1 of the module, run the following command:" >> ${outfile}
echo "#./loadGenFlasherSettings.sh ${1} <0|1>" >> ${outfile}
echo "#These load/save would normally be done by clicking the relevant button on the CSS GUI" >> ${outfile}
echo  >> ${outfile}
echo "#The Voltage are the raw numbers on the digital potentiometers in the module" >> ${outfile}
echo "#The equivalent coltages are shown in the commented lines below" >> ${outfile}
echo >> ${outfile}
for pv in "V1_WRITE" "V2_WRITE" "VLED_WRITE" "FREQ_WRITE"
do
    val=`caget -t ${P}_${pv}`
    echo "saving: ${P}_$pv $val"
    echo "$pv $val" >> ${outfile}
done
for pv in "V1_SET" "V2_SET" "VLED_SET"
do
    val=`caget -t ${P}_${pv}`
    echo "#$pv $val" >> ${outfile}
done

exit
