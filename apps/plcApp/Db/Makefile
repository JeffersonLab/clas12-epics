TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES


#----------------------------------------------------
# Create and install (or just install)
# databases, templates, substitutions like this

## Solenoid/Torus
DB  += $(wildcard ../*.db) $(wildcard ../*.substitutions)

REQ += datatype_loadcell.req
REQ += datatype_straingage.req
REQ += torus_force_settings.req
REQ += torus_vacuum_settings.req

BEAST += solenoid_comm.xml
BEAST += solenoid_cooldown.xml
BEAST += solenoid_force.xml
BEAST += solenoid_interlocks.xml
BEAST += solenoid_LHe.xml
BEAST += solenoid_vacuum.xml

BEAST += torus_comm.xml
BEAST += torus_cooldown_interlocks.xml
BEAST += torus_cooldown.xml
BEAST += torus_force_loadcells.xml
BEAST += torus_force_straingages.xml
BEAST += torus_interlocks.xml
BEAST += torus_LHe.xml
BEAST += torus_LN2.xml
BEAST += torus_import.xml
BEAST += torus_vacuum.xml

#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_TEMPLATE = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

#
# These are the rules of how to crate PLCout, PLCin and PLCarr DB file for PLC-to-EPICS interface. 
# 
../O.Common/%_PLCout.db: ../%.L5X 
	$(TOP)/../tools/RSLogixToEPICS/convertRSLogix2EPICS.py -c $(TOP)/../tools/RSLogixToEPICS/convert.cfg -x $< -o $@

../O.Common/%_PLCin.db: ../%.L5X 
	$(TOP)/../tools/RSLogixToEPICS/convertRSLogix2EPICS.py -c $(TOP)/../tools/RSLogixToEPICS/convert.cfg -x $< -i $@

../O.Common/%_PLCarr.db: ../%.L5X 
	$(TOP)/../tools/RSLogixToEPICS/convertRSLogix2EPICS.py -c $(TOP)/../tools/RSLogixToEPICS/convert.cfg -x $< -a $@

../%_PLC.req: ../%.L5X 
	$(TOP)/../tools/RSLogixToEPICS/convertRSLogix2EPICS.py -c $(TOP)/../tools/RSLogixToEPICS/convert.cfg -x $< -s $@

../%.xml: ../%.csv
	$(TOP)/../bin/csv2beast.py $<

