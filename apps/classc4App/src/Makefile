TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC_vxWorks = classc4

# classc4.dbd will be created and installed
DBD += classc4.dbd

# classc4.dbd will include these files:
classc4_DBD += base.dbd
classc4_DBD += asSupport.dbd
classc4_DBD += devIocStats.dbd
classc4_DBD += harp_genericSupport.dbd
classc4_DBD += scalerSupport.dbd
classc4_DBD += sixty_hzSupport.dbd

# classc4_registerRecordDeviceDriver.cpp derives from classc4.dbd
classc4_SRCS += classc4_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
classc4_SRCS_DEFAULT += classc4Main.cpp
classc4_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
classc4_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
classc4_LIBS += autosave
classc4_LIBS += devIocStats
classc4_LIBS += harp_genericSupport
classc4_LIBS += scalerSupport
classc4_LIBS += sixty_hzSupport
classc4_LIBS += mca SIS38XX
classc4_LIBS += busy calc sscan std vme
classc4_LIBS += oms
classc4_LIBS += motor
classc4_LIBS += asyn
classc4_LIBS += seq pv
classc4_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

