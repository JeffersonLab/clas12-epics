Fitter.exe:	FitterDict.cxx	Fitter.cxx
		g++ `root-config --cflags --glibs` -lSpectrum -o Fitter.exe Fitter.cxx FitterDict.cxx

FitterDict.cxx:	Fitter.h FitterLinkDef.h
		rootcint -f FitterDict.cxx -c Fitter.h FitterLinkDef.h

