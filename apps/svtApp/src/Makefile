TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC_vxWorks = svt

# svt.dbd will be created and installed
DBD += svt.dbd

# svt.dbd will include these files:
svt_DBD += base.dbd
svt_DBD += devIocStats.dbd
svt_DBD += V450.dbd 
svt_DBD += translateAlm.dbd
svt_DBD += bigsubRecord.dbd
svt_DBD += asSupport.dbd

# svt_registerRecordDeviceDriver.cpp derives from svt.dbd
svt_SRCS += svt_registerRecordDeviceDriver.cpp
svt_SRCS += translateAlm.c
svt_SRCS += bigsubRecord.c

# Build the main IOC entry point where needed
svt_SRCS_DEFAULT += svtMain.cpp
svt_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#svt_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
svt_LIBS += devIocStats
svt_LIBS += V450
svt_LIBS += autosave
svt_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

