#!../../bin/linux-x86_64/agilent

epicsEnvSet("GPIB","hallb-gpib16")
epicsEnvSet("PORT","S5R3")
epicsEnvSet("SECREG","SEC5_R3")
epicsEnvSet("ADDR","1")
epicsEnvSet("SCAN","2 second")

< st-generic.cmd

