This project was designed for the PC MONITORING purpose
There are following files created:

- devSysMon.c        : This file contains all of the device support functions
                       required by the PC monitoring server.
- pcMonitor.subs     : EPICS substitution file which contains the name of your PC
- pcMonitor.template : EPICS template file
- pcDB.dbd           : EPICS dbd file
- Makefile           : modified version of the MAKE file based on the
                       Makefile.org
- pcMonitor.script   : EPICS startup script
- G_PCMON_status.adl : MEDM config file which corresponds to the 
                       pcMonitor.subs and pcMonitor.template

#-------------- How to build the project ----------------------
This project was build for EPICS 3.14.7
It was tested with Linux:  Red Hat, Scientific Linux  and Fedora Core one

In order to build the project do as following:

make clean
make

To start the client medm application type the command:

medm -x -macro PC=PC-MONITOR G_PCMON_status.adl

To start the EPICS server type the command:
O.linux-x86/pcMonitor pcMonitor.script

# This project was created by Miroslaw Dach SLS/PSI 2006
# In case of problems please send an e-mail to the author
# miroslaw.dach@psi.ch
