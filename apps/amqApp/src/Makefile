TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC_linux-x86_64 = amq
PROD_IOC = $(PROD_IOC_$(T_A))
# amq.dbd will be created and installed
DBD += amq.dbd

# amq.dbd will be made up from these files:
amq_DBD += base.dbd

amq_DBD += amqdev.dbd

amq_DBD += devIocStats.dbd
amq_DBD += asSupport.dbd
amq_DBD += waveformApp.dbd

amqSupport_SRCS += amqSupport.cpp
LIBRARY_IOC_linux-x86_64 += amqSupport
LIBRARY_IOC = $(LIBRARY_IOC_$(T_A))

# amq_registerRecordDeviceDriver.cpp derives from amq.dbd
amq_SRCS += amq_registerRecordDeviceDriver.cpp
amq_SRCS += devamqAi.c devamqWaveform.c

# Build the main IOC entry point on workstation OSs.
amq_SRCS_DEFAULT += amqMain.cpp
#amq_SRCS_vxWorks += -nil-


USR_INCLUDES += -I./ -I$(IPC_HOME)/src/main -I/usr/include/apr-1 -I/usr/include/activemq-cpp-3.9.3

# Finally link to the EPICS Base libraries
amq_LIBS += $(EPICS_BASE_IOC_LIBS)
amq_LIBS += activemq-cpp json-c amqSupport
amq_LIBS += autosave
amq_LIBS += devIocStats
amq_LIBS += waveformApp

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
USR_CXXFLAGS +=  -std=c++11
USR_CXXFLAGS +=  -fpermissive -Wno-deprecated-declarations -Wno-unused-but-set-variable
USR_CFLAGS +=  -Wno-deprecated-declarations -Wno-implicit-function-declaration

