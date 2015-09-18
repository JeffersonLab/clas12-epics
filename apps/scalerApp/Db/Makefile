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
DB += scaler16m_addons.db
DB += fcup_calc.db
DB += joerger_classc1.substitutions
DB += joerger_classc4.substitutions

REQ += scaler16m_addons_settings.req
REQ += fcup_calc_settings.req
REQ += joergerN_settings.req
REQ += joerger_settings.req

#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_TEMPLATE = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

