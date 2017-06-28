TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

#----------------------------------------------------
DB    += caenhv.db
DB    += caenlv.db
DB    += caenchassis.db
DB    += HVDC_VSCAN.db
DB    += $(wildcard ../*.substitutions)
DB    += $(wildcard ../subs/*.substitutions)
DB    += $(wildcard ../sums/*.db)
DB    += $(wildcard ../sums/*.substitutions)
DB    += $(wildcard ../seq/*.db)
DB    += $(wildcard ../seq/*.subsitutions)

BEAST += HValarm.xml HValarmDetBased.xml HValarmBeamline.xml

#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_TEMPLATE = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE


