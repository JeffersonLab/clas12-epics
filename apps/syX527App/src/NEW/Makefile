#
# to compile vxWorks version, create 'O.vxWorks-ppc604_long' directory
# and type:
#
# gmake -C O.vxWorks-ppc604_long -f ../Makefile TOP=../../../.. T_A=vxWorks-ppc604_long clean
# gmake -C O.vxWorks-ppc604_long -f ../Makefile TOP=../../../.. T_A=vxWorks-ppc604_long
#


#======================================================

# my: comment out +++++++++++ so far I do not undertand why it is needed for 
EPICS_BASE_HOST_BIN = $(EPICS_BASE)/bin/linux-x86/

TOP=../..
include $(TOP)/configure/CONFIG

PROD += v288_test
PROD += sy527_test

LIB_SRCS += sy1527.c 
LIB_SRCS += sy1527epics1.c
LIB_SRCS += v288.o

v288_test_SRC += v288_test.c
sy527_test_SRC += sy527_test.c


PROD_LIBS += sy527epics1
LIBRARY += sy527epics1


INSTALL_LIB = $(EPICSB_DRIVERS)/lib/$(T_A)
INSTALL_LOCATION_LIB = $(EPICSB_DRIVERS)/lib
INSTALL_BIN = $(EPICSB_DRIVERS)/bin/$(T_A)

#===========================

PROD_LIBS += jvme
PROD_OBJS += $(CODA)/src/rol/Linux_i686_vme/obj/all_rocs.o

v288_test_OBJS += v288_test.o
sy527_test_OBJS += sy527_test.o


#PROD_LIBS += smi
#PROD_LIBS += smiui
#PROD_LIBS += dim

jvme_DIR += $(CODA)/src/rol/jvme
#smi_DIR += $(SMIDIR)/$(ODIR)
#smiui_DIR += $(SMIDIR)/$(ODIR)
#dim_DIR += $(DIMDIR)/$(ODIR)

USR_CPPFLAGS += -DLinux_vme
USR_CXXFLAGS += -DLinux_vme
USR_CFLAGS += -DLinux_vme


# sy527 flag
USR_CFLAGS += -DUSE_CAEN527

# smi flag
#USR_CFLAGS += -DUSE_SMI



USR_INCLUDES += -I$(CODA)/src/rol/jvme
#USR_INCLUDES += -I $(SMIDIR)/smixx
#USR_INCLUDES += -I $(DIMDIR)/dim

#===========================
include $(TOP)/configure/RULES


