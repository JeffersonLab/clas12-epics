#!../../bin/linux-x86_64/agilent

epicsEnvSet("GPIB","hallb-gpib19")
epicsEnvSet("PORT","S3R1")
epicsEnvSet("SECREG","SEC3_R1")
epicsEnvSet("ADDR","1")
epicsEnvSet("SCAN","2 second")

< st-generic.cmd

