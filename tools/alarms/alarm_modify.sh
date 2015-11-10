#!/bin/sh

if [ ${HOST} != ${ALARM_HOST} ]; then
    echo "ERROR: $0 needs to be run as ${ALARM_USER}@${ALARM_HOST}";
    exit;
fi

if [ $# -lt 2 ] || [ $1 = "-h" ]; then
    echo 
    echo "Usage: $0 <alarm_name> <xml_file>"
    echo
    echo "Modifies current alarm, adding components from xml_file" 
    echo
    echo "Current alarms are:"
    AlarmConfigTool -list | grep -v "Tool"
    echo
    echo
    exit
fi

name=$1
file=$2

read -p "This will add components from ${file} to this alarm: ${name}. OK? (y/n)"
if [ "$REPLY" != "y" ]; then
   exit
fi

echo "AlarmConfigTool -root ${name} -modify -file ${file} -pluginCustomization ${ALARM_DIR}/alarmsettings.ini"
AlarmConfigTool -root ${name} -modify -file ${file} -pluginCustomization ${ALARM_DIR}/alarmsettings.ini

