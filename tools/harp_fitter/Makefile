all: clean dict exe

clean:
	rm -f harp_fitter FitterDict.cxx FitterDict.h 

exe:	FitterDict.cxx	Fitter.cxx
		g++ `root-config --cflags --glibs` -lSpectrum -o harp_fitter Fitter.cxx FitterDict.cxx

dict:	Fitter.h FitterLinkDef.h
		rootcint -f FitterDict.cxx -c Fitter.h FitterLinkDef.h

