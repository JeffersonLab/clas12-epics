#!../../bin/linux-x86_64/agilent

epicsEnvSet("GPIB","hallb-gpib01")
epicsEnvSet("PORT","S6R1")
epicsEnvSet("SECREG","SEC6_R1")
epicsEnvSet("ADDR","1")
epicsEnvSet("SCAN","2 second")

< st-generic.cmd

