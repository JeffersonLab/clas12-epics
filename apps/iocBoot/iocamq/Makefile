TOP = ../..
include $(TOP)/configure/CONFIG
ARCH = linux-x86_64
TARGETS = envPaths
include $(TOP)/configure/RULES.ioc

datfiles = $(wildcard *.dat)

iocs : 
	awk -f  makeIocs.gk $(datfiles)
