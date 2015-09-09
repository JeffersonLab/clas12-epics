TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build an IOC support library
LIBRARY_IOC_vxWorks += rasterSupport

rasterSupport_SRCS += rastLib.c

rasterSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

# Build the IOC application
PROD_IOC_vxWorks = raster

# raster.dbd will be created and installed
DBD += raster.dbd

# raster.dbd will include these files:
raster_DBD += base.dbd

# raster_registerRecordDeviceDriver.cpp derives from raster.dbd
raster_SRCS += raster_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
raster_SRCS_DEFAULT += rasterMain.cpp
raster_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#raster_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
raster_LIBS += rasterSupport

# To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file
ifneq ($(SNCSEQ),)
    raster_DBD += rasterSNC.dbd
    rasterSupport_SRCS += raster.st
    rasterSupport_LIBS += seq pv
    raster_LIBS += seq pv
endif

# Finally link IOC to the EPICS Base libraries
raster_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

