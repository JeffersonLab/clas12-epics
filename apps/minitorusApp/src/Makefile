TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Install minitorusSupport.dbd into <top>/dbd
DBD += minitorusSupport.dbd

minitorusSupport_DBD += minitorusSNC.dbd

# Build an IOC support library
LIBRARY_IOC_vxWorks += minitorusSupport

# Compile and add the code to the support library
minitorusSupport_SRCS += dynaPowerLib.c
minitorusSupport_SRCS += minitorus.st

minitorusSupport_LIBS += seq pv
minitorusSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

# Build the IOC application
PROD_IOC_vxWorks = minitorus

# minitorus.dbd will be created and installed
DBD += minitorus.dbd

# minitorus.dbd will include these files:
minitorus_DBD += base.dbd
minitorus_DBD += minitorusSupport.dbd

# minitorus_registerRecordDeviceDriver.cpp derives from minitorus.dbd
minitorus_SRCS += minitorus_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
minitorus_SRCS_DEFAULT += minitorusMain.cpp
minitorus_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
minitorus_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
minitorus_LIBS += minitorusSupport
minitorus_LIBS += seq pv
minitorus_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

