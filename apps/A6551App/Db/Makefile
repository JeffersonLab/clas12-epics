TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

#----------------------------------------------------
# Create and install (or just install) into <top>/db
# databases, templates, substitutions like this
DB_INSTALLS += $(ASYN)/db/asynRecord.db
DB_INSTALLS += $(AUTOSAVE)/asApp/Db/save_restoreStatus.db

DB += A6551.db
PROTO += A6551.proto
REQ += A6551_settings.req

DB += dclv.substitutions
REQ += dclv_settings.req

#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_template = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

