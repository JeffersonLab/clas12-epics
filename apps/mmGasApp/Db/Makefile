TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Install databases, templates & substitutions like this
DB += mmgas_asyn_aiFloat64.template
DB += mmgas_asyn_aoFloat64.template
DB += mmgas_asyn_bi_bit.template
DB += mmgas_asyn_bo_bit.template
DB += mmgas_asyn_bo_bit_FLNK.template
DB += mmgas_status_alarm.template
DB += mmgas_status_calc.template
DB += mmgas_status_flowdiff.template
DB += mmgas_status_ovrflow.template
DB += mmgas_global_status.template

DB += mmgas_bmt.substitutions
DB += mmgas_fmt.substitutions
DB += mmgas_ftt.substitutions

DB += mmgas_weather.substitutions
DB += mmgas_weather_aliases.db
DB += mmgas_weather_avg.db

DB += mvt_gasOnOff.db

# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_TEMPLATE = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

