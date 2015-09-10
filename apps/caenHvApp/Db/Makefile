TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

#----------------------------------------------------
#DB    += b_templates.db
#DB    += ctof.substitutions
#DB    += ecal.substitutions
#DB    += hv.substitutions
DB    += caenhv.db
DB    += $(wildcard *.hv_substitutions)


#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_TEMPLATE = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

