#
# CLAS12 EPICS Makefile 
#
.PHONY: epics tools

all: epics tools

clean: clean-epics clean-tools

distclean: distclean-epics

rebuild: rebuild-epics

install: epics install-tools

uninstall: uninstall-tools

#
# EPICS
#
epics:
	(cd apps; make)

clean-epics:
	(cd apps; make clean)

distclean-epics:
	(cd apps; make distclean)

rebuild-epics:
	(cd apps; make rebuild)

#
# tools 
#
tools:
	(cd tools; make)

clean-tools:
	(cd tools; make clean)

install-tools:
	(cd tools; make install)

uninstall-tools:
	(cd tools; make uninstall)

