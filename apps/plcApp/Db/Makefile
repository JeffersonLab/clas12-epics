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

## Torus
DB  += cryodbox_torus_cryocon.db
DB  += cryodbox_torus_LHe.substitutions
DB  += cryodbox_torus_LN2.db
DB  += cryodbox_torus_LN2.substitutions
DB  += datatype_ccm_cernox.db
DB  += datatype_ccm_pt100.db
DB  += datatype_cpid.db
DB  += datatype_loadcell.db
REQ += datatype_loadcell.req
DB  += datatype_straingage.db
REQ += datatype_straingage.req
DB  += torus_cryocon.db
DB  += torus_force.substitutions
REQ += torus_force_settings.req
DB  += torus_LHe.db
DB  += torus_LHe.substitutions
DB  += torus_LN2.db
DB  += torus_LN2.substitutions
DB  += torus_mps.db
DB  += torus_qd.db
DB  += torus_vacuum.db
REQ += torus_vacuum_settings.req

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

