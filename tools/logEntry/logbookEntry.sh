#!/bin/sh

#windowID=$1
#windowTitle=$2

D=`dirname $0`

export JAVA_HOME=/usr/clas12/third-party-libs/jdk/21.0.2
export PATH=$JAVA_HOME/bin:$PATH

export SESSION=clasprod
export EXPID=clasrun

CLASSPATH="${D}/../tools/logEntry/src/main/java"
CLASSPATH="${CLASSPATH}:${D}/../tools/logEntry/lib/jlog-5.1.0.jar"
CLASSPATH="${CLASSPATH}:${D}/../tools/logEntry/lib/mysql-connector-java-5.1.32-bin.jar"
CLASSPATH="${CLASSPATH}:${D}/../tools/logEntry/lib/jca-2.4.8.jar"
export CLASSPATH

exec java org/jlab/hallb/AutoLogEntry/MakeLogEntry $@ &

