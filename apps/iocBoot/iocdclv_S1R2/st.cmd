#!../../bin/linux-x86_64/agilent

epicsEnvSet("GPIB","hallb-gpib05")
epicsEnvSet("PORT","S1R2")
epicsEnvSet("SECREG","SEC1_R2")
epicsEnvSet("ADDR","1")
epicsEnvSet("SCAN","2 second")

< st-generic.cmd

