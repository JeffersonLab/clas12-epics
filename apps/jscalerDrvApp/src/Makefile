TOP=../..

include $(TOP)/configure/CONFIG

STATIC_BUILD=YES

LIB_SRCS += jscalers.cpp

#PROD_LIBS += jscalers

LIBRARY_Linux += jscalers

INC += common.h
INC += jscalers.h

#===========================
PROD_LIBS    += rol
rol_DIR      += $(CODA_LIB)
rol_DIR      += $(ROL_LIB)
USR_INCLUDES += $(ROL_INCLUDE)

$(info $$USR_INCLUDES is [${USR_INCLUDES}])
$(info $$TOP is [${TOP}])

#===========================
include $(TOP)/configure/RULES

