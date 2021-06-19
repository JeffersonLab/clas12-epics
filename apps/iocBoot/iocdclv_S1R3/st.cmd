#!../../bin/linux-x86_64/agilent

epicsEnvSet("GPIB","hallb-gpib08")
epicsEnvSet("PORT","S1R3")
epicsEnvSet("SECREG","SEC1_R3")
epicsEnvSet("ADDR","1")
epicsEnvSet("SCAN","2 second")

< st-generic.cmd

