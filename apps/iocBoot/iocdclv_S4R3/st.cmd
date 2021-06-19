#!../../bin/linux-x86_64/agilent

epicsEnvSet("GPIB","hallb-gpib20")
epicsEnvSet("PORT","S4R3")
epicsEnvSet("SECREG","SEC4_R3")
epicsEnvSet("ADDR","1")
epicsEnvSet("SCAN","2 second")

< st-generic.cmd

