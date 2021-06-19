#!../../bin/linux-x86_64/agilent

epicsEnvSet("GPIB","hallb-gpib09")
epicsEnvSet("PORT","S2R3")
epicsEnvSet("SECREG","SEC2_R3")
epicsEnvSet("ADDR","1")
epicsEnvSet("SCAN","2 second")

< st-generic.cmd

