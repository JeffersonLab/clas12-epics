TOOLDIRS := ${shell find . -maxdepth 1 ! -path . -type d -print}

# remove nonconformant tools:
TOOLDIRS := $(filter-out cyber, $(TOOLDIRS))


.PHONY: all clean distclean install uninstall 

all:
	-@for dir in $(TOOLDIRS); do cd $$dir && make all ; cd .. ; done

install: all
	-@for dir in $(TOOLDIRS); do cd $$dir && make install ; cd .. ; done

clean:
	-@for dir in $(TOOLDIRS); do cd $$dir && make clean ; cd .. ; done

uninstall:
	-@for dir in $(TOOLDIRS); do cd $$dir && make uninstall ; cd .. ; done
