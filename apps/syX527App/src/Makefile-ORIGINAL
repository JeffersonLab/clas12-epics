#
# NOTE:
#   In configure/CONFIG_SITE, CROSS_COMPILER_TARGET_ARCHS is empty.  So only 
#   linux target is built.
#

TOP=../..
include $(TOP)/configure/CONFIG

LIB_SRCS += sy1527.c 
LIB_SRCS += sy1527epics1.c
PROD_SRC += sy1527_test.c

PROD_LIBS += sy1527epics1

PROD_LIBS += caenhvwrapper 
PROD_LIBS += hscaenet 
PROD_LIBS += pthread
hscaenet_DIR += $(HSCAENET_LIB)
caenhvwrapper_DIR += $(CAENHVWRAPPER_LIB)
pthread_DIR += $(PTHREAD_LIB)

LIBRARY_Linux += sy1527epics1
PROD_Linux += sy1527_test

INC += sy1527.h
INC += sy1527epics1.h

#===========================

PROD_LIBS += smi
PROD_LIBS += smiui
PROD_LIBS += dim

smi_DIR += $(SMIXX_LIB)
smiui_DIR += $(SMIXX_LIB)
dim_DIR += $(DIM_LIB)

USR_INCLUDES += $(SMIXX_INCLUDE)
USR_INCLUDES += $(DIM_INCLUDE)

#===========================
include $(TOP)/configure/RULES

