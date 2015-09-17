#Makefile at top of application tree
TOP = .
include $(TOP)/configure/CONFIG
DIRS := $(DIRS) $(filter-out $(DIRS), configure)
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard *App))
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard iocBoot))
# Build out CSS opi links
#DIRS := $(DIRS) $(filter-out $(DIRS), css)

define DIR_template
 $(1)_DEPEND_DIRS = configure
endef
$(foreach dir, $(filter-out configure,$(DIRS)),$(eval $(call DIR_template,$(dir))))

iocBoot_DEPEND_DIRS    += $(filter %App,$(DIRS))

#
# Set app dependencies
#
caenHvApp_DEPEND_DIRS  += syX527App
scalerApp_DEPEND_DIRS  += sixtyHzApp				# to be rm'd later
classc1App_DEPEND_DIRS += bomApp  	                # vme crate
classc4App_DEPEND_DIRS += scalerApp sixtyHzApp  	# vme crate


include $(TOP)/configure/RULES_TOP

.PHONY: css cssclean
css:
	@./build_css.sh

cssclean:
	$(RMDIR) ./css

