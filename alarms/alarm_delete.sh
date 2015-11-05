#!/bin/sh
if [ $# -lt 2 ] || [ $1 = "-h" ]; then
    echo 
    echo "Usage: $0 -h: print this message"
    echo
    echo "Usage: $0 <alarm_name> <component>"
    echo "Delete component from alarm name"
    echo "Examples:"
    echo "$0 HallB /HallB/B_HV/ECAL/SEC1/UI/B_HV_ECAL_SEC1_UI_E99.STAT"
    echo "$0 HallB /HallB/B_HV/ECAL/SEC1/UI"
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
component=$2

read -p "This will delete component ${component} from alarm: ${name}. OK? (y/n)"
if [ "$REPLY" != "y" ]; then
   exit
fi

AlarmConfigTool -root ${name} -delete ${component} -pluginCustomization ${ALARM_DIR}/alarmsettings.ini

