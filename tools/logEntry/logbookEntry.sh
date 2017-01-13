#!/bin/sh

#windowID=$1
#windowTitle=$2

export JAVA_HOME=/usr/lib/jvm/java-1.8.0-oracle
export PATH=$JAVA_HOME/bin:$PATH

CLASSPATH="${EPICS}/tools/logEntry/src/main/java"
CLASSPATH="${CLASSPATH}:${EPICS}/tools/logEntry/lib/jlog2.jar"
CLASSPATH="${CLASSPATH}:${EPICS}/tools/logEntry/lib/mysql-connector-java-5.1.32-bin.jar"
export CLASSPATH

exec java org/jlab/hallb/AutoLogEntry/MakeLogEntry $@ &

