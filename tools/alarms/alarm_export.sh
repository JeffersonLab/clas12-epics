#!/bin/sh

if [ $# -lt 2 ] || [ $1 = "-h" ]; then
    echo 
    echo "Usage: $0 <alarm_name> <xml_file>"
    echo
    echo "Export whole tree for <alarm_name>, putting all components <xml_file>" 
    echo
    echo "Current alarms are:"
    AlarmConfigTool -list | grep -v "Tool"
    echo
    echo
    exit
fi

if [ ${HOST} != ${ALARM_HOST} ]; then
    echo "ERROR: $0 needs to be run on ${ALARM_HOST}";
    exit;
fi

name=$1
file=$2

read -p "This will export alarm: ${name} to file: ${file}.  OK? (y/n)"
if [ "$REPLY" != "y" ]; then
   exit
fi

AlarmConfig -root ${name} -export -file $2 -pluginCustomization ${ALARM_DIR}/alarmsettings.ini

