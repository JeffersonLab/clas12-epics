all: build install

# note the -r makes it runnable on other machines
build:
	shc -f network-port-reset.sh -o network-port-reset -r
	shc -f beam-viewer-reboot.sh -o beam-viewer-reboot -r

install:
	cp -f network-port-reset ../../bin/
	cp -f beam-viewer-reboot ../../bin/

clean:
	rm -f network-port-reset network-port-reset.sh.x.c ../../bin/network-port-reset
	rm -f beam-viewer-reboot beam-viewer-reboot.sh.x.c ../../bin/beam-viewer-reboot

