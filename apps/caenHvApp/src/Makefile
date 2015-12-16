TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC_Linux = ioccaen
# ecalHV.dbd will be created and installed
DBD += ioccaen.dbd

# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
ioccaen_SRCS += ioccaen_registerRecordDeviceDriver.cpp
ioccaen_SRCS += bigsub.c
ioccaen_SRCS += devCAEN.c
ioccaen_SRCS_DEFAULT += ioccaenMain.cpp
ioccaen_SRCS_vxWorks += -nil-

# CAEN_HV/include
USR_INCLUDES += -I$(TOP)/include

ioccaen_LIBS += sy1527epics1
ioccaen_LIBS += caenhvwrapper 
ioccaen_LIBS += hscaenet 
ioccaen_LIBS += devIocStats
ioccaen_LIBS += caPutLog
ioccaen_LIBS += $(EPICS_BASE_IOC_LIBS)

sy1527epics1_DIR  += $(TOP)/lib/$(T_A)
caenhvwrapper_DIR += $(CAENHVWRAPPER_LIB)
hscaenet_DIR      += $(HSCAENET_LIB)

#===========================

ioccaen_LIBS += smi
ioccaen_LIBS += smiui
ioccaen_LIBS += dim

smi_DIR   += $(SMIXX_LIB)
smiui_DIR += $(SMIXX_LIB)
dim_DIR   += $(DIM_LIB)

USR_INCLUDES += $(SMIXX_INCLUDE)
USR_INCLUDES += $(DIM_INCLUDE)

#===========================
include $(TOP)/configure/RULES

#----------------------------------------
#  ADD RULES AFTER THIS LINE

GENERATOR = mkHVEpics

gen:	$(GENERATOR)

$(GENERATOR): $(GENERATOR).C
	g++ -o $(GENERATOR) $(GENERATOR).C

gen_clean:
	/bin/rm -r $(GENERATOR)

iocs:    $(GENERATOR)	
	./$(GENERATOR) all
	./$(GENERATOR) crates
	./$(GENERATOR) groups
	chmod +x ../../iocBoot/ioccaenhv/st.cmd*

ioc_clean:
	/bin/rm -f ../../iocBoot/ioccaenhv_*
	/bin/rm -f ../../iocBoot/ioccaenhv/st.cmd*
	/bin/rm -r ../Db/HV*.substitutions
