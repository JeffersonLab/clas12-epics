#!/bin/sh
if [ $# -lt 2 ] || [ $1 = "-h" ]; then
    echo;
    echo "Usage: $0 -h: print this message";
    echo;
    echo "Usage: $0 <old_xml> <new_xml>"; 
    echo;
    echo "Compare a new xml dump with an older one to make a .xml for importing new components";
    echo;
    exit;
fi

old=$1;new=$2;
#diff, and grab only new pvs (indicated by ">" in the diff) into a list (with quotes stripped off)
diff  ${old} ${new} | awk '{if(($1~">")&&($0~"pv name")){split($0,a,"\"");print a[2]}}' > pvlist;

if [ ! -s "pvlist" ]; then #no different pvs
    echo "Warning: There were no new PVs in ${new}";
    exit;
fi

confname=`grep "config name=" ${new}`
echo ${confname} #start the output with the alarm name

#Do embedded awk. Find the new pvs and write each as a whole hierarchy of nested components to be added 
#with a alarm_modify.sh command Get the expert (Ken) to edit this if needed.
awk 'BEGIN{while(getline < "pvlist"){list[$1]++;}}\
{\
    if ($0~"<component")compstart[level++]=$0;  if ($0~"</component")level--;\
    if ($0~"<pv name"){\
	for(x in list){\
	    if($0~x){\
		for(n=0;n<level;n++)print compstart[n];\
		print $0;\
		while($0 !~ "</pv"){getline;print $0;}\
		for(n=level;n>0;n--){for(p=0;p<n;p++)printf"    ";print"</component>";}\
	    }\
	}\
    }\
}' ${new}

echo "</config>"
exit;
