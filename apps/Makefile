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
classc1App_DEPEND_DIRS += bomApp harp_genericApp kepcoApp scalerApp	# vme crate
classc4App_DEPEND_DIRS += harp_genericApp scalerApp sixtyHzApp 	# vme crate
kepcoApp_DEPEND_DIRS   += DVME628App
dynabcApp_DEPEND_DIRS  += XY240App
taggerTempApp_DEPEND_DIRS += XY560App

include $(TOP)/configure/RULES_TOP

.PHONY: css cssclean scripts
css:
	@./css_builder.sh

cssclean:
	$(RMDIR) ./css_share

scripts:
	cd scripts;ln -sf ../*/op/scripts/* ./
