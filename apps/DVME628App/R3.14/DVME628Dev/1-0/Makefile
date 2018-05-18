#Makefile at top of application tree
TOP = .
include $(TOP)/configure/CONFIG
DIRS := $(DIRS) $(filter-out $(DIRS), configure)
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard *code*))
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard *Code*))
include $(TOP)/configure/RULES_TOP
