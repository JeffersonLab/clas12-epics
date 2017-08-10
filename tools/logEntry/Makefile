JAVA_HOME := /usr/lib/jvm/java-1.8.0
PATH      := ${JAVA_HOME}/bin:${PATH}
export JAVA_HOME
export PATH
CLASSPATH :=.:lib/jlog2.jar:lib/mysql-connector-java-5.1.32-bin.jar:src/main/java

.PHONY: all clean install uninstall print

all:
	javac -Xlint:unchecked -cp $(CLASSPATH) src/main/java/org/jlab/hallb/AutoLogEntry/MakeLogEntry.java src/main/java/org/jlab/hallb/AutoLogEntry/CheckComboBox.java

clean:
	rm -f src/main/java/org/jlab/hallb/AutoLogEntry/*.class

