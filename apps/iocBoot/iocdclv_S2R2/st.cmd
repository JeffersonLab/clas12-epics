#!../../bin/linux-x86_64/agilent

epicsEnvSet("GPIB","hallb-gpib12")
epicsEnvSet("PORT","S2R2")
epicsEnvSet("SECREG","SEC2_R2")
epicsEnvSet("ADDR","1")
epicsEnvSet("SCAN","2 second")

< st-generic.cmd

