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
DB += crateAlarm.db
DB += svtApp.db
DB += HFCB.db
DB += alarm.db
DB += hfcb_r1.substitutions
DB += hfcb_r2.substitutions
DB += hfcb_r3.substitutions
DB += hfcb_r4.substitutions
DB += iseg.db
DB += mpv.db
DB += crate_r1.substitutions
DB += crate_r2.substitutions
DB += crate_r3.substitutions
DB += crate_r4.substitutions
DB += wienerCrate.db
DB += DUMMY.db
DB += DUMMYLV.db
DB += watchdog.db

#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_template = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
