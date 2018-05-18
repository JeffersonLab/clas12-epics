STUB = tordaq
DICT = exDict
CC = g++
LDFLAGS = $(shell root-config --libs) $(shell root-config --glibs)
CFLAGS = -std=c++11 $(shell root-config --cflags)

all: clean $(STUB)Dict $(STUB)Gui $(STUB)Converter

$(STUB)Dict:
	rootcint -f $(DICT).cxx -c $(STUB)Gui.hh exLinkDef.h

$(STUB)Gui:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $(STUB)Gui $(STUB)Gui.cxx $(STUB)GuiUtil.cxx $(DICT).cxx

$(STUB)Converter:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $(STUB)Converter $(STUB)Converter.c

clean:
	rm -f $(STUB)Converter $(STUB)Gui $(STUB)Data_hh.so $(STUB)Data_hh.d $(DICT).cxx $(DICT).h $(DICT)_rdict.pcm 

