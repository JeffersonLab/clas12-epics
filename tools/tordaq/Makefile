TARGET = tordaq
CC = g++
LDFLAGS = $(shell root-config --libs) $(shell root-config --glibs)
CFLAGS = -std=c++11 $(shell root-config --cflags)

all:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $(TARGET) $(TARGET).c

