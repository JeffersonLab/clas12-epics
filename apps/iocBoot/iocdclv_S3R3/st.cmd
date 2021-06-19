#!../../bin/linux-x86_64/agilent

epicsEnvSet("GPIB","hallb-gpib18")
epicsEnvSet("PORT","S3R3")
epicsEnvSet("SECREG","SEC3_R3")
epicsEnvSet("ADDR","1")
epicsEnvSet("SCAN","2 second")

< st-generic.cmd

