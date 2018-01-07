TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC_vxWorks = classc1

# classc1.dbd will be created and installed
DBD += classc1.dbd

# classc1.dbd will include these files:
classc1_DBD += base.dbd
classc1_DBD += asSupport.dbd
classc1_DBD += devIocStats.dbd
classc1_DBD += harp_genericSupport.dbd
classc1_DBD += scalerSupport.dbd

# classc1_registerRecordDeviceDriver.cpp derives from classc1.dbd
classc1_SRCS += classc1_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
classc1_SRCS_DEFAULT += classc1Main.cpp
classc1_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
classc1_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
classc1_LIBS += harp_genericSupport
classc1_LIBS += scalerSupport
classc1_LIBS += SIS38XX
classc1_LIBS += mca
classc1_LIBS += calc
classc1_LIBS += busy
classc1_LIBS += sscan
classc1_LIBS += std
classc1_LIBS += oms
classc1_LIBS += motor
classc1_LIBS += vme
classc1_LIBS += autosave
classc1_LIBS += devIocStats
classc1_LIBS += asyn
classc1_LIBS += seq pv
classc1_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

