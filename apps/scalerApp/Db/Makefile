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
#DB += joerger.db
#DB += fcup_calc.db
#DB += photon_ratio.db

#REQ += joerger_settings.req
#REQ += fcup_calc_settings.req

DB += scaler.db
DB += scaler-ped.db
DB += scaler-ped.substitutions
DB += scaler_calc1b.db

#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_TEMPLATE = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

