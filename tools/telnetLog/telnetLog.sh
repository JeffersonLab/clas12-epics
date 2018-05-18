#!/bin/sh
#
# log a non-interactive telnet session
#
# depending on the host, this may block the $port
#
# implemented to just log console messages from cRios
#

host=$1
port=$2

logDir=/usr/clas12/DATA/logs
logFile=$host:$port.log

touch $logDir/$logFile

script -f -a -c "telnet $host $port" $logDir/$logFile

