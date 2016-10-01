JAVA_HOME := /apps/java/jdk1.7.0_67
PATH      := ${JAVA_HOME}/bin:${PATH}

export JAVA_HOME
export PATH

CLASSPATH :=.:lib/jlog2.jar:lib/mysql-connector-java-5.1.32-bin.jar:src/main/java


.PHONY: all clean install uninstall print


all:
	javac -cp $(CLASSPATH) src/main/java/org/jlab/AutoLogEntry/MakeLogEntry.java

clean:
	rm -f src/main/java/org/jlab/AutoLogEntry/*.class

print:
	echo ${PATH}
	echo $(CLASSPATH)
