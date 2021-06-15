TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC_vxWorks = classctest

# classctest.dbd will be created and installed
DBD += classctest.dbd

# classctest.dbd will include these files:
classctest_DBD += base.dbd
#classctest_DBD += bomSupport.dbd
classctest_DBD += devIocStats.dbd
#classctest_DBD += harp_genericSupport.dbd
#classctest_DBD += scaler_cSupport.dbd
#classctest_DBD += scaler_dSupport.dbd
#classctest_DBD += scaler_eSupport.dbd
##classctest_DBD += XY240Support.dbd

# classctest_registerRecordDeviceDriver.cpp derives from classctest.dbd
classctest_SRCS += classctest_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
classctest_SRCS_DEFAULT += classctestMain.cpp
classctest_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
classctest_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
#classctest_LIBS += bomSupport
#classctest_LIBS += harp_genericSupport
#classctest_LIBS += scaler_cSupport
#classctest_LIBS += scaler_dSupport
#classctest_LIBS += scaler_eSupport 
#classctest_LIBS += SIS38XX
##classctest_LIBS += XY240Support
classctest_LIBS += mca
classctest_LIBS += calc
classctest_LIBS += busy
classctest_LIBS += sscan
classctest_LIBS += oms
classctest_LIBS += motor
classctest_LIBS += vme
classctest_LIBS += brm13
classctest_LIBS += devIocStats
classctest_LIBS += std
classctest_LIBS += asyn
classctest_LIBS += seq pv
classctest_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

