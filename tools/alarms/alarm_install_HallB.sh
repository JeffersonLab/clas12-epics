#!/bin/sh

if [ $# -gt 0 ]; then
    echo 
    echo "Usage: $0 -h: print this message"
    echo
    echo "Usage: $0"
    echo "Install the HallB alarm from all xml sources in ${ALARM_DIR}/hallb_configs/alarm_list"
    echo "Must be run as ${ALARM_USER}@${ALARM_HOST}"
    echo
    exit
fi

if [ ${HOST} != ${ALARM_HOST} ]; then
    echo "ERROR: $0 needs to be run as ${ALARM_USER}@${ALARM_HOST}";
    exit;
fi

if [ ${USER} != ${ALARM_USER} ]; then
    echo "ERROR: $0 needs to be run as ${ALARM_USER}@${ALARM_HOST}";
    exit;
fi


echo
read -p "This will install HallB alarm from xml sources, replacing the currently installed one. OK? (y/n) "
if [ "$REPLY" != "y" ]; then
   exit
fi

#figure out if it's already running
running=`ps x | grep AlarmServer | grep "/bin/java" | awk '{print $1}'`
if [ -n "${running}" ]; then
    echo "ERROR: AlarmServer is running  (pid = ${running})" 
    echo "This needs to be stopped  first, with \"alarm_server.sh HallB stop\", or otherwise."
    exit;
fi

date=`date '+%d_%m_%y:%H_%M'`
# Get the full date
fulldate=`date -R`

#create a date stamped xml dump of the current state of the alarm before replacing it
dumpfile="${ALARM_DIR}/hallb_dumps/alarm_HallB_live_${date}.xml"
echo "AlarmConfigTool -root HallB -export -file ${dumpfile} -pluginCustomization ${ALARM_DIR}/alarmsettings.ini"
AlarmConfigTool -root HallB -export -file ${dumpfile} -pluginCustomization ${ALARM_DIR}/alarmsettings.ini

#import the skeleton, which creates an empty alarm called HallB, overwriting the old one.
AlarmConfigTool -root HallB -import -file ${ALARM_DIR}/hallb_configs/HallB_skeleton.xml -pluginCustomization ${ALARM_DIR}/alarmsettings.ini
echo "AlarmConfigTool -root ${name} -import -file ${ALARM_DIR}/hallb_configs/HallB_skeleton.xml -pluginCustomization ${ALARM_DIR}/alarmsettings.ini"

while read line           
do           
    [[ "$line" =~ ^#.*$ ]] && continue #skip comment lines
    AlarmConfigTool -root HallB -modify -file ${line} -pluginCustomization ${ALARM_DIR}/alarmsettings.ini  
    echo "AlarmConfigTool -root HallB -modify -file ${ALARM_DIR}/hallb_configs/${line} -pluginCustomization ${ALARM_DIR}/alarmsettings.ini"  
done <  ${ALARM_DIR}/hallb_configs/alarm_list

# Get the full date
fulldate=`date -R`
#create a date stamped xml dump of the current state of the alarm before replacing it
dumpfile="${ALARM_DIR}/hallb_dumps/alarm_HallB_persistent_${date}.xml"
echo "AlarmConfigTool -root HallB -export -file ${dumpfile} -pluginCustomization ${ALARM_DIR}/alarmsettings.ini"
AlarmConfigTool -root HallB -export -file ${dumpfile} -pluginCustomization ${ALARM_DIR}/alarmsettings.ini

echo
echo "If there were no errors above, it is now safe to start the AlarmServer"
echo "With \"alarm_server.sh HallB start\", or otherwise."

exit
