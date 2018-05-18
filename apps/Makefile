#Makefile at top of application tree
TOP = .
include $(TOP)/configure/CONFIG
DIRS := $(DIRS) $(filter-out $(DIRS), configure)
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard *App))
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard iocBoot))

# these are currently built by hand on RHEL5:
DIRS := $(filter-out caenHv527App, $(DIRS))
DIRS := $(filter-out sy527App, $(DIRS))

define DIR_template
 $(1)_DEPEND_DIRS = configure
endef
$(foreach dir, $(filter-out configure,$(DIRS)),$(eval $(call DIR_template,$(dir))))

iocBoot_DEPEND_DIRS    += $(filter %App,$(DIRS))

#
# Set app dependencies
#
clasTreeApp_DEPEND_DIRS  += caenHvApp
svtApp_DEPEND_DIRS += highlandV450App
caenHvApp_DEPEND_DIRS  += syX527App
classc1App_DEPEND_DIRS += harp_genericApp kepcoApp scalerApp	# vme crate
classc4App_DEPEND_DIRS += harp_genericApp scalerApp sixtyHzApp 	# vme crate
classc6App_DEPEND_DIRS += btaApp
classc8App_DEPEND_DIRS += struckDaqApp
classc3App_DEPEND_DIRS += XY560App
jscalerApp_DEPEND_DIRS += jscalerDrvApp
kepcoApp_DEPEND_DIRS   += DVME628App
dynabcApp_DEPEND_DIRS  += XY240App
taggerTempApp_DEPEND_DIRS += XY560App
testApp_DEPEND_DIRS += waveformApp
svtCtrlApp_DEPEND_DIRS += waveformApp
jscalerApp_DEPEND_DIRS += waveformApp

include $(TOP)/configure/RULES_TOP

.PHONY: css cssclean scripts
css:
	@./css_builder.sh

cssclean:
	$(RMDIR) ./css_share

scripts:
	cd scripts;ln -sf ../*/op/scripts/* ./
