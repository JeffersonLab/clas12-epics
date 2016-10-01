#!/bin/sh

# force java version

if [ "$HOSTNAME" == "clonpc19.jlab.org" ]; then
echo "Running on clonpc19"
  export JAVA_HOME=/usr/lib/jvm/java-1.8.0-oracle.x86_64
  #export JAVA_HOME=/usr/lib/jvm/java-1.7.0-oracle.x86_64
else
  export JAVA_HOME=/usr/lib/jvm/java-1.8.0-oracle
fi

export PATH=$JAVA_HOME/bin:$PATH

CLASSPATH="${EPICS}/tools/logEntry/src/main/java"
CLASSPATH="${CLASSPATH}:${EPICS}/tools/logEntry/lib/jlog2.jar"
CLASSPATH="${CLASSPATH}:${EPICS}/tools/logEntry/lib/mysql-connector-java-5.1.32-bin.jar"
export CLASSPATH

echo $JAVA_HOME
echo $CLASSPATH

java org/jlab/AutoLogEntry/MakeLogEntry $1 $2

