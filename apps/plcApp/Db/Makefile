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

DB += HPS_SVT_Interlock_v5_PLCarr.db 
DB += HPS_SVT_Interlock_v5_PLCin.db 
DB += HPS_SVT_Interlock_v5_PLCout.db 

REQ += HPS_SVT_Interlock_v5_PLC.req  # generated file
#REQ += HPS_SVT_Interlocks.req        # nested calls to generated file (inputs/outputs)

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

