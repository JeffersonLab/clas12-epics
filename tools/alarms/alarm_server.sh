#!/bin/sh

if [ $# -lt 2 ] || [ $1 = "-h" ]; then
    echo 
    echo "Usage: $0 -h: print this message"
    echo
    echo "Usage: $0 <alarm_name> <start|stop|restart>"
    echo
    echo "Starts the AlarmServer with the specified alarm"
    echo "Must be run as ${ALARM_USER}@${ALARM_HOST}"
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

name=$1;
action=$2;

#figure out if it's already running
running=`ps x | grep AlarmServer | grep "/bin/java" | awk '{print $1}'`

if [ ${action} = "start" ]; then
   if [ -n "${running}" ]; then
       echo "ERROR: AlarmServer already running (pid = ${running})."
       exit;
   fi
   AlarmServer -root ${name} -pluginCustomization ${ALARM_DIR}/alarmsettings.ini &
   exit;
fi

if [ ${action} = "stop" ]; then
   if [ -z ${running} ]; then
       echo "ERROR: AlarmServer not running  (not found with ps)"
       exit;
   fi
   kill -9 ${running}
   exit
fi

if [ ${action} = "restart" ]; then
   kill -9 ${running};
   AlarmServer -root ${name} -pluginCustomization ${ALARM_DIR}/alarmsettings.ini &
   exit;   
fi

#The requested action was none of the above
echo 
echo "Usage: $0 <alarm_name> [start|stop|restart]"
echo

exit;
