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
DB += amqInt.db amqIntArray.db amqDouble.db amqDoubleArray.db amqFloatArray.db amqStringArray.db amqHistogram.db

DB += amqTriggerBits.substitutions
DB += amqTrigBit.template
DB += amqTrigBit-alarms.db
DB += amqTrigBit-alias.db
DB += amqTrigBit-stage2.template
DB += amqMergeFT.db
DB += amqSplitFT.db
DB += amqTrigBit-sums.db
DB += amqSvt.substitutions
DB += amqSvt2.substitutions
DB += amqSvt3.substitutions
DB += amqSvt-calc-slot.db
DB += amqSvt-calc-sector.db
DB += amqSvt-calc.db
DB += amqSvt-calcGlobal.db
DB += daq2epics.db
DB += tsBusy-alarm.db
DB += amqRocsBusy.db
DB += amqRocsRate.db
DB += amqRocsRate.substitutions
DB += amqRocsRate-sums.db

#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_template = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

