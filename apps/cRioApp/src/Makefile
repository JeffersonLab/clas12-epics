TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Install cRioSupport.dbd into <top>/dbd
#DBD += cRioSupport.dbd

# Build an IOC support library
#LIBRARY_IOC += cRioSupport

#cRioSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

# Build the IOC application
PROD_IOC_Linux = cRio

# cRio.dbd will be created and installed
DBD += cRio.dbd

# cRio.dbd will include these files:
cRio_DBD += base.dbd
cRio_DBD += asSupport.dbd
cRio_DBD += devIocStats.dbd

# cRio_registerRecordDeviceDriver.cpp derives from cRio.dbd
cRio_SRCS += cRio_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
cRio_SRCS_DEFAULT += cRioMain.cpp
cRio_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#cRio_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
cRio_LIBS += autosave
cRio_LIBS += devIocStats

# Finally link IOC to the EPICS Base libraries
cRio_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

