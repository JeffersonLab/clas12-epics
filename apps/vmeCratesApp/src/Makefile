TOP=../..

include $(TOP)/configure/CONFIG

# Build the IOC application
PROD_IOC_Linux = vmeCrates

# vmeCrates.dbd will be created and installed
DBD += vmeCrates.dbd

# vmeCrates.dbd will include these files:
vmeCrates_DBD += snmp.dbd
vmeCrates_DBD += devSnmp.dbd
vmeCrates_DBD += devIocStats.dbd
vmeCrates_DBD += asSupport.dbd
vmeCrates_DBD += caPutLog.dbd

# vmeCrates_registerRecordDeviceDriver.cpp derives from mpodLv.dbd
vmeCrates_SRCS += vmeCrates_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
vmeCrates_SRCS_DEFAULT += vmeCratesMain.cpp
vmeCrates_SRCS_vxWorks += -nil-

# Finally link IOC to the EPICS Base libraries
vmeCrates_LIBS += $(EPICS_BASE_IOC_LIBS)
vmeCrates_LIBS += devSnmp
vmeCrates_LIBS += autosave
vmeCrates_LIBS += devIocStats
vmeCrates_LIBS += caPutLog

include $(TOP)/configure/RULES

