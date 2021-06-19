#!../../bin/linux-x86_64/agilent

epicsEnvSet("GPIB","hallb-gpib02")
epicsEnvSet("PORT","S1R1")
epicsEnvSet("SECREG","SEC1_R1")
epicsEnvSet("ADDR","1")
epicsEnvSet("SCAN","2 second")

< st-generic.cmd

