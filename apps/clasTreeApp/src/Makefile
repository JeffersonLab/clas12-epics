TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC application

PROD_IOC = clasTree
# clasTree.dbd will be created and installed
DBD += clasTree.dbd

# clasTree.dbd will be made up from these files:
clasTree_DBD += base.dbd

# clasTree_registerRecordDeviceDriver.cpp derives from clasTree.dbd
clasTree_SRCS += clasTree_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
clasTree_SRCS_DEFAULT += clasTreeMain.cpp
clasTree_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#clasTree_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
clasTree_LIBS += $(EPICS_BASE_IOC_LIBS)


# make the ioc db substitutions and init files for the tree
IOCDIR = ../../iocBoot/iocclasTree

#define variables to make extra targets
OUTNAME = clas12
SCRIPTDIR = ../../op/scripts
DICTFILE=$(SCRIPTDIR)/$(OUTNAME)NodesDict.py
RECDUMP = ./sub2dump.sh
PARSER = ./parseEpicsRecordDump

TARGETS += $(DICTFILE)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

DICTDEPS =  ../sub2dump.sh ../parseEpicsRecordDump 
DICTDEPS += $(EPICS)/apps/caenHvApp/src/HV_allnames.txt

# need deps from other apps whos .sub or .db files are to be parsed.
$(DICTFILE):	$(DICTDEPS)
		cd ../; ln -sf ../../db ../; $(RECDUMP) | $(PARSER) -v outname=$(OUTNAME)
		cd $(SCRIPTDIR); ln -sf $(OUTNAME)NodesDict.py NodesDict.py

