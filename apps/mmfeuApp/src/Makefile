TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

#=============================
# Build the IOC application

PROD_IOC = mmfeu
# mmfeu.dbd will be created and installed
DBD += mmfeu.dbd

# mmfeu.dbd will be made up from these files:
mmfeu_DBD += base.dbd
mmfeu_DBD += devIocStats.dbd
mmfeu_DBD += asyn.dbd
mmfeu_DBD += calc.dbd
mmfeu_DBD += drvAsynIPPort.dbd
mmfeu_DBD += stream.dbd
mmfeu_DBD += system.dbd

# Include dbd files from all support applications:
#mmfeu_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#mmfeu_LIBS += xxx

# mmfeu_registerRecordDeviceDriver.cpp derives from mmfeu.dbd
mmfeu_SRCS += mmfeu_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
mmfeu_SRCS_DEFAULT += mmfeuMain.cpp
mmfeu_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#mmfeu_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
mmfeu_LIBS += devIocStats
mmfeu_LIBS += stream
mmfeu_LIBS += asyn
mmfeu_LIBS += calc

# Finally link IOC to the EPICS Base libraries
mmfeu_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

