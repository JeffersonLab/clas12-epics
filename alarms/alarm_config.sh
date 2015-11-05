#!/bin/sh

if [ $# -lt 0 ] || [ $1 = "-h" ]; then
    echo 
    echo "Usage: $0 -h: print this message"
    echo
    echo "Usage: $0 <alarm> <xmlfile>"
    echo "Install <alarm> from <xmlfile.xml>"
    echo
    echo "<alarm> should have the same name as in <config name=...> line  at the top of <xmlfile>"
    echo
    echo "Current alarms are:"
    AlarmConfigTool -list | grep -v "Tool"
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

name=$1
file=$2

read -p "This will install / replace the alarm=${name} from ${file}.xml. OK? (y/n)"
if [ "$REPLY" != "y" ]; then
   exit
fi

AlarmConfigTool -root ${name} -import -file ${file} -pluginCustomization ${ALARM_DIR}/alarmsettings.ini

