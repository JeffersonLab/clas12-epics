TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build an IOC support library
LIBRARY_IOC_vxWorks += rasterSupport

DBD += rasterSupport.dbd
rasterSupport_DBD += base.dbd

rasterSupport_SRCS += rastLib.c

ifneq ($(SNCSEQ),)
    rasterSupport_DBD += rasterSNC.dbd
    rasterSupport_SRCS += raster.st
    rasterSupport_LIBS += seq pv
endif

rasterSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

# Build the IOC application
PROD_IOC_vxWorks = raster

# raster.dbd will be created and installed
DBD += raster.dbd

raster_DBD += rasterSupport.dbd

# raster_registerRecordDeviceDriver.cpp derives from raster.dbd
raster_SRCS += raster_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
raster_SRCS_DEFAULT += rasterMain.cpp
raster_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#raster_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
raster_LIBS += rasterSupport

ifneq ($(SNCSEQ),)
    raster_LIBS += seq pv
endif

raster_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

