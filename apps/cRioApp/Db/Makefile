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
DB += gas_cRIO_LTCC.db gas_cRIO_LTCC_SEC.db gas_cRIO_LTCC_distill.db gas_cRIO_LTCC_distill2.db
DB += gas_cRIO_RICH.db
DB += gas_cRIO_SVT.db
DB += gas_cRIO_MVT_mixing.db
DB += gas_cRIO_HTCC-calc.db
DB += gas_cRIO_BONUS.db
DB += gas_cRIO_AHDC.db
DB += gas_cRIO_BONUS_intlk.db
DB += gas_cRIO_BONUS_intlk.substitutions

DB += gas_cRIO_MFCINIT.db

DB += weather_cRIO.db
DB += labWeather_cRIO.db

DB += gas_cRIO_RICH_drybox.db

DB += flow_cRIO_TEDF.db

BEAST += gas_cRIO_COMM.xml
BEAST += gas_cRIO_DC.xml
BEAST += gas_cRIO_HTCC.xml
BEAST += gas_cRIO_IOCS.xml
BEAST += gas_cRIO_LTCC.xml
BEAST += gas_cRIO_SVT.xml
BEAST += gas_cRIO_MVT_mixing.xml

# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_TEMPLATE = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

