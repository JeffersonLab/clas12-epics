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
#DB += xxx.db
DB += wienerR.db
DB += wienerW.db

DB += vmePedestals.db
DB += vmeCratesCommon.db 
DB += vmeCrateGroup.db 

DB += vmeCrates.substitutions

REQ += vmeCratePedestal.req
REQ += vmeGroupSettings.req

BEAST += vmeCrateAlarms.xml

#Install the IOC status reporting DB
#DEVIOCSTAT_LOC=$(DEVIOCSTATS)/db
#DB += $(DEVIOCSTAT_LOC)/iocAdminSoft.db

#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_template = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
