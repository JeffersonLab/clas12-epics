#!../../bin/linux-x86_64/agilent

epicsEnvSet("GPIB","hallb-gpib11")
epicsEnvSet("PORT","S4R1")
epicsEnvSet("SECREG","SEC4_R1")
epicsEnvSet("ADDR","1")
epicsEnvSet("SCAN","2 second")

< st-generic.cmd

