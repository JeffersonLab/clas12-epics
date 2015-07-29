INSTALL_BIN := /usr/local/bin
PROGFILES   += procServMgr
PROGFILES   += softioc_console

LOGROTATE_D := /etc/logrotate.d
LOGCONFIG   += hps_softiocs

.PHONY: all clean install uninstall


install:
	@for file in $(PROGFILES); do \
		echo "Installing $(INSTALL_BIN)/$$file" ; \
		install -m 0755 $$file $(INSTALL_BIN) ; \
	done
	
	@echo "Installing $(LOGROTATE_D)/$(LOGCONFIG)" ; \
	install -m 0644 $(LOGCONFIG) $(LOGROTATE_D) ;

uninstall:
	@for file in $(PROGFILES); do $(RM) $(INSTALL_BIN)/$$file; done
