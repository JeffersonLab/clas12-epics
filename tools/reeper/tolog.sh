#!/bin/sh
LOGBOOK="TLOG"
COMMENT="GrimReeper:"

COMMENT="$COMMENT $1"

command="/site/ace/certified/apps/bin/logentry -l TLOG -t \"${COMMENT}\""

files=`ls epics_gr/*_latest.gif`
flist=""
for file in $files ; do 
    flist="$flist -a $file"
done
command="/site/ace/certified/apps/bin/logentry -l TLOG -t \"${COMMENT}\" $flist"

echo $command
 
