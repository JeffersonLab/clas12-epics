TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#PROD_LIBS += sy1527epics

LIBRARY_IOC  += sy1527epics

LIB_SRCS += sy1527.c 
LIB_SRCS += sy1527epics.c

LIB_LIBS += caenhvwrapper 
LIB_LIBS += hscaenet 
LIB_LIBS += pthread
LIB_LIBS += smi
LIB_LIBS += smiui
LIB_LIBS += dim
LIB_LIBS += $(EPICS_BASE_IOC_LIBS)

hscaenet_DIR      += $(HSCAENET_LIB)
caenhvwrapper_DIR += $(CAENHVWRAPPER_LIB)
pthread_DIR       += $(PTHREAD_LIB)
smi_DIR   += $(SMIXX_LIB)
smiui_DIR += $(SMIXX_LIB)
dim_DIR   += $(DIM_LIB)

INC += sy1527.h
INC += sy1527epics.h

USR_INCLUDES += $(SMIXX_INCLUDE)
USR_INCLUDES += $(DIM_INCLUDE)

#=============================
# Build test IOC

PROD_IOC += sy1527_test

sy1527_test_SRCS += sy1527_test.c

sy1527_test_LIBS += sy1527epics
sy1527_test_LIBS += $(EPICS_BASE_IOC_LIBS)


include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
