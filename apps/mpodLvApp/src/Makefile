TOP=../..

include $(TOP)/configure/CONFIG

# Build the IOC application
PROD_IOC_Linux = mpodLv

# mpodLv.dbd will be created and installed
DBD += mpodLv.dbd

# mpodLv.dbd will include these files:
mpodLv_DBD += snmp.dbd
mpodLv_DBD += devSnmp.dbd
mpodLv_DBD += calc.dbd
mpodLv_DBD += aCalcoutRecord.dbd
mpodLv_DBD += asSupport.dbd
mpodLv_DBD += devIocStats.dbd
mpodLv_DBD += mpodLvInclude.dbd
mpodLv_DBD += caPutLog.dbd
mpodLv_DBD += sCalcoutRecord.dbd

# mpodLv_registerRecordDeviceDriver.cpp derives from mpodLv.dbd
mpodLv_SRCS += mpodLv_registerRecordDeviceDriver.cpp
mpodLv_SRCS += MpodStatusParser.c
#mpodLv_SRCS += bonus_hv_watchdog.st

# Build the main IOC entry point where needed
mpodLv_SRCS_DEFAULT += mpodLvMain.cpp
mpodLv_SRCS_vxWorks += -nil-

# Finally link IOC to the EPICS Base libraries
mpodLv_LIBS += $(EPICS_BASE_IOC_LIBS)
mpodLv_LIBS += autosave
mpodLv_LIBS += devIocStats
mpodLv_LIBS += netsnmp devSnmp
mpodLv_LIBS += caPutLog
mpodLv_LIBS += calc
mpodLv_LIBS += seq
mpodLv_LIBS += waveformApp

netsnmp_DIR += $(NETSNMP)/lib

include $(TOP)/configure/RULES

