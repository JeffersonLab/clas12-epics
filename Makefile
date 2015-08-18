#
# CLAS12 EPICS Makefile 
#

all: epics tools

clean: clean-epics clean-tools

distclean: distclean-epics

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

