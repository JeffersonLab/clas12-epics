
TOP=../../
include $(TOP)/configure/CONFIG

EPICS_BASE=/usr/clas12/R3.14.12.5/base_RHEL5
MODULES=$(EPICS_BASE)/../modules_RHEL5
SYNAPPS=$(EPICS_BASE)/../modules_RHEL5
EPICS_EXTENSIONS=$(EPICS_BASE)/../externsions_RHEL5
include $(MODULES)/configure/RELEASE
include $(SYNAPPS)/configure/RELEASE
COMMANDLINE_LIBRARY = READLINE_NCURSES

PROD += sy527_groups
PROD += sy527_test
PROD += v288_reset
PROD += v288_test

LIB_SRCS += sy1527.c
LIB_SRCS += sy1527epics2.c
LIB_SRCS += v288.o

sy527_groups_SRC += sy527_groups.c
sy527_test_SRC += sy527_test.c
v288_reset_SRC += v288_reset.c
v288_test_SRC += v288_test.c

PROD_LIBS += sy527epics2
LIBRARY += sy527epics2

INC += sy1527.h

PROD_LIBS += jvme
PROD_OBJS += $(CODA)/src/rol/Linux_i686_vme/obj/all_rocs.o

sy527_groups_OBJS += sy527_groups.o
sy527_test_OBJS += sy527_test.o
v288_reset_OBJS += v288_reset.o
v288_test_OBJS += v288_test.o

jvme_DIR += $(CODA)/src/rol/jvme

USR_CPPFLAGS += -DLinux_vme
USR_CXXFLAGS += -DLinux_vme
USR_CFLAGS += -DLinux_vme

USR_CFLAGS += -DUSE_CAEN527

USR_INCLUDES += -I$(CODA)/src/rol/jvme

include $(TOP)/configure/RULES


