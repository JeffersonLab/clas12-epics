CC = gcc
all: clean caenhvReset install
caenhvReset:
	$(CC) -o caenhvReset caenhvReset.c
install:
	cp -f caenhvReset.py ../../bin/
clean:
	rm -f caenhvReset ../../bin/caenhvReset.py

