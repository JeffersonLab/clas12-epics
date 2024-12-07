#!/bin/sh
if [ -n "$(echo $@ | grep .C)" ]; then
    rootargs=`echo $@ | awk '{for(n=1;n<=NF;n++){if($n~".C"){printf"${GREEPER}/grLoad.C "}printf"%s ",$n}}'`
else
    rootargs=$@
fi

echo "root -l $rootargs"

exit

