TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC application

PROD_IOC_vxWorks = classc6

# classc6.dbd will be created and installed
DBD += classc6.dbd

# classc6.dbd will be made up from these files:
classc6_DBD += base.dbd
#classc6_DBD += btaSupport.dbd
#classc6_DBD += asSupport.dbd
classc6_DBD += devIocStats.dbd

# classc6_registerRecordDeviceDriver.cpp derives from classc6.dbd
#classc6_SRCS += classc6_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
classc6_SRCS_DEFAULT += classc6Main.cpp
classc6_SRCS_vxWorks += classc6_registerRecordDeviceDriver.cpp

# Add support from base/src/vxWorks if needed
classc6_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
#classc6_LIBS += btaSupport
classc6_LIBS += SIS38XX mca
classc6_LIBS += calc
classc6_LIBS += busy
classc6_LIBS += sscan
#classc6_LIBS += autosave
classc6_LIBS += std
classc6_LIBS += devIocStats
classc6_LIBS += vme
classc6_LIBS += asyn
classc6_LIBS += seq pv 

# Finally link to the EPICS Base libraries
classc6_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

