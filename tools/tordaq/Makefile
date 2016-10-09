STUB = tordaq
DICT = exDict
CC = g++
LDFLAGS = $(shell root-config --libs) $(shell root-config --glibs)
CFLAGS = -std=c++11 $(shell root-config --cflags)

all: clean $(STUB)Dict $(STUB)Gui $(STUB)Converter

$(STUB)Dict:
	rootcint -f $(DICT).cxx -c $(STUB)Gui.hh exLinkDef.h
$(STUB)Gui:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $(STUB)Gui $(STUB)Gui.cxx $(DICT).cxx
$(STUB)Converter:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $(STUB)Converter $(STUB)Converter.c

clean:
	rm -f tordaqConverter tordaqGui tordaqData_hh.so tordaqData_hh.d exDict.cxx exDict.h

