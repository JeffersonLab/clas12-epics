#!../../bin/linux-x86_64/agilent

epicsEnvSet("GPIB","hallb-gpib03")
epicsEnvSet("PORT","S2R1")
epicsEnvSet("SECREG","SEC2_R1")
epicsEnvSet("ADDR","1")
epicsEnvSet("SCAN","2 second")

< st-generic.cmd

