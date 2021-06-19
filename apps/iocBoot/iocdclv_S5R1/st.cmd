#!../../bin/linux-x86_64/agilent

epicsEnvSet("GPIB","hallb-gpib10")
epicsEnvSet("PORT","S5R1")
epicsEnvSet("SECREG","SEC5_R1")
epicsEnvSet("ADDR","1")
epicsEnvSet("SCAN","2 second")

< st-generic.cmd

