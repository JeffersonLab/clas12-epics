TARGET = tordaq
DICT = exDict
CC = g++
LDFLAGS = $(shell root-config --libs) $(shell root-config --glibs)
CFLAGS = -std=c++11 $(shell root-config --cflags)

all: tordaqDict tordaqGui tordaqConverter

tordaqDict:
	rootcint -f $(DICT).cxx -c $(TARGET)Gui.hh exLinkDef.h

tordaqGui:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $(TARGET)Gui $(TARGET)Gui.cxx $(DICT).cxx

tordaqConverter:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $(TARGET)Converter $(TARGET)Converter.c

