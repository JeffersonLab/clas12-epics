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
##DB += dbExample1.db
##DB += dbExample2.db
##DB += dbSubExample.db
##DB += user.substitutions
##DB += userHost.substitutions

DB += asym_file.db
DB += asym_fdbk.db
DB += asym_scaler_common.db
DB += asym_scaler.db
DB += asym_scaler_macro.db
DB += asym_scaler_macro_sums.db
DB += polarization.db

# 2018 additions:
DB += asy-generic.db
DB += asy-withsums-generic.db
DB += bca.substitutions

#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_TEMPLATE = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

