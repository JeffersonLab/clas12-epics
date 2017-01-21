TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = dchvWaveform

# dchvWaveform.dbd will be created and installed
DBD += dchvWaveform.dbd
dchvWaveform_DBD += base.dbd
dchvWaveform_DBD += devIocStats.dbd
dchvWaveform_DBD += asSupport.dbd

# dchvWaveform_registerRecordDeviceDriver.cpp derives from dchvWaveform.dbd
dchvWaveform_SRCS += dchvWaveform_registerRecordDeviceDriver.cpp
dchvWaveform_SRCS += dchv_waveforms.st

# Build the main IOC entry point on workstation OSs.
dchvWaveform_SRCS_DEFAULT += dchvWaveformMain.cpp
dchvWaveform_SRCS_vxWorks += -nil-

dchvWaveform_LIBS += seq pv
dchvWaveform_LIBS += autosave
dchvWaveform_LIBS += devIocStats
dchvWaveform_LIBS += $(EPICS_BASE_IOC_LIBS)

# Finally link to the EPICS Base libraries
dchvWaveform_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

