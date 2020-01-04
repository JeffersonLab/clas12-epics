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
classc6_DBD += calc.dbd
#classc6_DBD += bomSupport.dbd
classc6_DBD += stdSupport.dbd
classc6_DBD += mcaSupport.dbd
classc6_DBD += SIS38XXSupport.dbd
classc6_DBD += sscanSupport.dbd
classc6_DBD += busySupport.dbd
classc6_DBD += asyn.dbd
classc6_DBD += vmeVXSupport.dbd

classc6_DBD += bomSupport.dbd
classc6_DBD += asym.dbd
classc6_DBD += mollerSetup.dbd

classc6_DBD += asSupport.dbd
classc6_DBD += devIocStats.dbd

# Build the main IOC entry point on workstation OSs.
classc6_SRCS_DEFAULT += classc6Main.cpp
classc6_SRCS_vxWorks += classc6_registerRecordDeviceDriver.cpp

# Add support from base/src/vxWorks if needed
classc6_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
#classc6_LIBS += bomSupport
classc6_LIBS += mca SIS38XX
classc6_LIBS += calc
classc6_LIBS += busy
classc6_LIBS += sscan
classc6_LIBS += vme std
classc6_LIBS += asyn
classc6_LIBS += seq pv

classc6_LIBS += bomSupport
classc6_LIBS += asymSupport
classc6_LIBS += mollerSetupSupport

classc6_LIBS += devIocStats
classc6_LIBS += autosave

# Finally link to the EPICS Base libraries
classc6_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

