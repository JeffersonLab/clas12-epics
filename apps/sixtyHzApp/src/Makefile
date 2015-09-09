TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

LIBRARY_IOC_vxWorks += sixty_hzSupport

DBD += sixty_hzSupport.dbd

sixty_hzSupport_SRCS += fftmisc.c
sixty_hzSupport_SRCS += fourierf.c

sixty_hzSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================
# Build the IOC application

PROD_IOC_vxWorks = sixty_hz
# sixty_hz.dbd will be created and installed
DBD += sixty_hz.dbd

# sixty_hz.dbd will be made up from these files:
sixty_hz_DBD += base.dbd
sixty_hz_DBD += sixty_hzSupport.dbd

# sixty_hz_registerRecordDeviceDriver.cpp derives from sixty_hz.dbd
#sixty_hz_SRCS += sixty_hz_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
sixty_hz_SRCS_DEFAULT += sixty_hzMain.cpp
sixty_hz_SRCS_vxWorks += sixty_hz_registerRecordDeviceDriver.cpp

# Add support from base/src/vxWorks if needed
sixty_hz_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
sixty_hz_LIBS += sixty_hzSupport 
sixty_hz_LIBS += mca SIS38XX
sixty_hz_LIBS += sscan
sixty_hz_LIBS += autosave
#sixty_hz_LIBS += vme
sixty_hz_LIBS += std
sixty_hz_LIBS += asyn
sixty_hz_LIBS += SIS38XX

# NOTE: To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file
ifneq ($(SNCSEQ),)
      sixty_hzSupport_DBD += sixty_hzSNC.dbd
      sixty_hzSupport_SRCS += sixtyHz.st
      sixty_hz_SRCS += sixtyHz.st
      sixty_hzSupport_LIBS += seq pv
endif

# Finally link to the EPICS Base libraries
sixty_hz_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

