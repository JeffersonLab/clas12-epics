TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC_vxWorks += classc8

# classc8.dbd will be created and installed
DBD += classc8.dbd

# classc8.dbd will include these files:
classc8_DBD += base.dbd
classc8_DBD += struckDaqSupport.dbd
#classc8_DBD += asSupport.dbd
classc8_DBD += devIocStats.dbd

# classc8_registerRecordDeviceDriver.cpp derives from classc8.dbd
classc8_SRCS += classc8_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
classc8_SRCS_DEFAULT += classc8Main.cpp
classc8_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
classc8_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
classc8_LIBS += struckDaqSupport
classc8_LIBS += SIS38XX mca
classc8_LIBS += busy calc sscan std
#classc8_LIBS += autosave
classc8_LIBS += devIocStats
classc8_LIBS += asyn
classc8_LIBS += seq pv

# Finally link IOC to the EPICS Base libraries
classc8_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

