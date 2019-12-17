TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Install databases, templates & substitutions like this
DB += mpod8008l.db
DB += mpodClearEvents.db
DB += rebootDivider.db
DB += iseg-module.db
DB += iseg-channel.db
DB += mpod-crate.db
DB += bonus-hv-watchdog.db
DB += $(wildcard ../*.substitutions)

# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_TEMPLATE = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

