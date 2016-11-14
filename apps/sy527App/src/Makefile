
TOP=../../
include $(TOP)/configure/CONFIG

EPICS_BASE=/usr/clas12/R3.14.12.5/base_RHEL5
MODULES=$(EPICS_BASE)/../modules_RHEL5
SYNAPPS=$(EPICS_BASE)/../modules_RHEL5
EPICS_EXTENSIONS=$(EPICS_BASE)/../externsions_RHEL5
include $(MODULES)/configure/RELEASE
include $(SYNAPPS)/configure/RELEASE
COMMANDLINE_LIBRARY = READLINE_NCURSES

PROD += v288_test
PROD += sy527_test

LIB_SRCS += sy1527.c
LIB_SRCS += sy1527epics2.c
LIB_SRCS += v288.o

v288_test_SRC += v288_test.c
sy527_test_SRC += sy527_test.c

PROD_LIBS += sy527epics2
LIBRARY += sy527epics2

PROD_LIBS += jvme
PROD_OBJS += $(CODA)/src/rol/Linux_i686_vme/obj/all_rocs.o

v288_test_OBJS += v288_test.o
sy527_test_OBJS += sy527_test.o

jvme_DIR += $(CODA)/src/rol/jvme

USR_CPPFLAGS += -DLinux_vme
USR_CXXFLAGS += -DLinux_vme
USR_CFLAGS += -DLinux_vme

USR_CFLAGS += -DUSE_CAEN527

USR_INCLUDES += -I$(CODA)/src/rol/jvme

include $(TOP)/configure/RULES


