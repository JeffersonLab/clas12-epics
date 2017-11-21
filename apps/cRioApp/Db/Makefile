TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Install databases, templates & substitutions like this
DB += cRIO_heartbeat.db
DB += cRIO_heartbeat_bi.db

DB += gas_cRIO_DC.db
DB += gas_cRIO_FTC.db
DB += gas_cRIO_HTCC.db
DB += gas_cRIO_LTCC.db gas_cRIO_LTCC_SEC.db
DB += gas_cRIO_RICH.db
DB += gas_cRIO_SVT.db
DB += gas_cRIO_MVT_mixing.db

DB += weather_cRIO.db

BEAST += gas_cRIO_COMM.xml
BEAST += gas_cRIO_DC.xml
BEAST += gas_cRIO_HTCC.xml
BEAST += gas_cRIO_IOCS.xml
BEAST += gas_cRIO_LTCC.xml
BEAST += gas_cRIO_SVT.xml

# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_TEMPLATE = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

