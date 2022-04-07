#!/bin/sh

#windowID=$1
#windowTitle=$2

D=`dirname $0`

#export JAVA_HOME=/usr/lib/jvm/java-1.8.0-oracle
#export PATH=$JAVA_HOME/bin:$PATH
#export JAVA_HOME=/usr/clas12/third-party-libs/jdk/1.8.0_31
#export PATH=$JAVA_HOME/bin:$PATH

export SESSION=clasprod
export EXPID=clasrun

CLASSPATH="${D}/../tools/logEntry/src/main/java"
CLASSPATH="${CLASSPATH}:${D}/../tools/logEntry/lib/jlog-4.0.1.jar"
CLASSPATH="${CLASSPATH}:${D}/../tools/logEntry/lib/mysql-connector-java-5.1.32-bin.jar"
export CLASSPATH

exec java org/jlab/hallb/AutoLogEntry/MakeLogEntry $@ &

