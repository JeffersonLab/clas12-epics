#!/bin/sh

if [ $# -ne 2 ]; then
    echo "Usage: $0 <module> <0|1>"
    exit 
fi



P="$1:F$2"

infile=`caget -S -t ${P}_DATA_FILE_LOAD`

while read line; do
    comment=`echo ${line} | awk '{if ($0~"#") print "comment line"}'`
    #echo "comment = $comment"
    if [ -z "${comment}" ] && [ -n "${line}" ]; then
    #if [ -z "${comment}" ]; then
	echo "caput  ${P}_${line}"
    fi
done < $infile

exit
