#!../../bin/linux-x86_64/agilent

epicsEnvSet("GPIB","hallb-gpib07")
epicsEnvSet("PORT","S6R3")
epicsEnvSet("SECREG","SEC6_R3")
epicsEnvSet("ADDR","1")
epicsEnvSet("SCAN","2 second")

< st-generic.cmd

