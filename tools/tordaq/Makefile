TARGET = tordaq
DICT = exDict
CC = g++
LDFLAGS = $(shell root-config --libs) $(shell root-config --glibs)
CFLAGS = -std=c++11 $(shell root-config --cflags)

all: tordaq tordaqdict tordaqgui

tordaq:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $(TARGET) $(TARGET).c

tordaqdict:
	rootcint -f $(DICT).cxx -c $(TARGET)Gui.h exLinkDef.h

tordaqgui:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $(TARGET)Gui $(TARGET)Gui.cxx $(DICT).cxx

