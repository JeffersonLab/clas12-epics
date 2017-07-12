#!./URLDriverApp

< envPaths-AD

errlogInit(20000)

# NAB: this is important:
#epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES","100000000")
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES","1000000000")

dbLoadDatabase("$(TOP)/dbd/URLDriverApp.dbd")
URLDriverApp_registerRecordDeviceDriver(pdbbase) 

epicsEnvSet("PREFIX", "cctv6:")
epicsEnvSet("PORT",   "cctv6")

epicsEnvSet("QSIZE",  "20")
epicsEnvSet("XSIZE",  "640")
epicsEnvSet("YSIZE",  "480")
#epicsEnvSet("XSIZE",  "1280")
#epicsEnvSet("YSIZE",  "960")
epicsEnvSet("NCHANS", "2048")

# NAB: record files use includes, so go to directory instead of modifying many files:
cd ${ADCORE}/db

# Create a URL driver
# URLDriverConfig(const char *portName, int maxBuffers, size_t maxMemory, int priority, int stackSize)
URLDriverConfig("$(PORT)", 0, 0)
asynSetTraceIOMask("$(PORT)",0,2)
#asynSetTraceMask("$(PORT)",0,255)

dbLoadRecords("$(ADCORE)/db/ADBase.template",     "P=$(PREFIX),R=cam1:,PORT=$(PORT),ADDR=0,TIMEOUT=1")

dbLoadRecords("$(ADURL)/db/URLDriver.template","P=$(PREFIX),R=cam1:,PORT=$(PORT),ADDR=0,TIMEOUT=1")

# Create a standard arrays plugin.
NDStdArraysConfigure("Image1", 3, 0, "$(PORT)", 0)
dbLoadRecords("$(ADCORE)/db/NDPluginBase.template","P=$(PREFIX),R=image1:,PORT=Image1,ADDR=0,TIMEOUT=1,NDARRAY_PORT=$(PORT),NDARRAY_ADDR=0")
#dbLoadRecords("$(ADCORE)/db/NDStdArrays.template", "P=$(PREFIX),R=image1:,PORT=Image1,ADDR=0,TIMEOUT=1,TYPE=Int16,FTVL=SHORT,NELEMENTS=921600,NDARRAY_PORT=$(PORT)")
# 640x480:
#dbLoadRecords( "$(ADCORE)/db/NDStdArrays.template", "P=$(PREFIX),R=image1:,PORT=Image1,ADDR=0,TIMEOUT=1,TYPE=Int8, FTVL=CHAR, NELEMENTS=921600,NDARRAY_PORT=$(PORT)")
# 2592x1944: 
dbLoadRecords( "$(ADCORE)/db/NDStdArrays.template", "P=$(PREFIX),R=image1:,PORT=Image1,ADDR=0,TIMEOUT=1,TYPE=Int8, FTVL=CHAR, NELEMENTS=15116544,NDARRAY_PORT=$(PORT)")


# Load all other plugins using commonPlugins.cmd
< ${IOCTOP}/commonPlugins.cmd

########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################

#dbLoadRecords("$(ADCORE)/db/NDPluginBase.template","P=ROI1,R=image2:,PORT=Image2,ADDR=0,TIMEOUT=1,NDARRAY_PORT=ROI1,NDARRAY_ADDR=0")
#dbLoadRecords("$(ADCORE)/db/NDPluginBase.template","P=PROC1,R=image3:,PORT=Image3,ADDR=0,TIMEOUT=1,NDARRAY_PORT=PROC1,NDARRAY_ADDR=0")
#dbLoadRecords("$(ADCORE)/db/NDPluginBase.template","P=CC1,R=image4:,PORT=Image4,ADDR=0,TIMEOUT=1,NDARRAY_PORT=CC1,NDARRAY_ADDR=0")

NDStdArraysConfigure("Image2", 3, 0, "ROI1", 0)
dbLoadRecords("NDStdArrays.template", "P=$(PREFIX),R=image2:,  PORT=Image2,ADDR=0,TIMEOUT=1,NDARRAY_PORT=ROI1,TYPE=Int8,FTVL=CHAR,NELEMENTS=15116544")
NDStdArraysConfigure("Image3", 3, 0, "PROC1", 0)
dbLoadRecords("NDStdArrays.template", "P=$(PREFIX),R=image3:,  PORT=Image3,ADDR=0,TIMEOUT=1,NDARRAY_PORT=PROC1,TYPE=Int8,FTVL=CHAR,NELEMENTS=15116544")
NDStdArraysConfigure("Image4", 3, 0, "CC1", 0)
dbLoadRecords("NDStdArrays.template", "P=$(PREFIX),R=image4:,  PORT=Image4,ADDR=0,TIMEOUT=1,NDARRAY_PORT=CC1,TYPE=Int8,FTVL=CHAR,NELEMENTS=15116544")
NDStdArraysConfigure("Image5", 3, 0, "OVER1", 0)
dbLoadRecords("NDStdArrays.template", "P=$(PREFIX),R=image5:,  PORT=Image5,ADDR=0,TIMEOUT=1,NDARRAY_PORT=OVER1,TYPE=Int8,FTVL=CHAR,NELEMENTS=15116544")


########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################

# NAB: after loading records, get back to ioc directory:
cd ${IOCTOP}

dbLoadRecords("profiles.db","P=$(PREFIX),R=image1:,XSIZE=$(XSIZE),YSIZE=$(YSIZE)")

iocInit()

dbpf "cctv6:cam1:URL4" "http://mvtgas.jlab.org/axis-cgi/jpg/image.cgi"
dbpf "cctv6:cam1:URL3" "http://hallbcam07.jlab.org/axis-cgi/jpg/image.cgi?user=user&pwd=user"
dbpf "cctv6:cam1:URL2" "http://hallbcam02.jlab.org/axis-cgi/jpg/image.cgi"
dbpf "cctv6:cam1:URL1" "http://cctv6.jlab.org/axis-cgi/jpg/image.cgi"

dbpf "cctv6:cam1:AcquirePeriod" "1.0"
dbpf "cctv6:cam1:NumImages" "10"
dbpf "cctv6:cam1:ImageMode" "Continuous"

# looks like this propogates down the chain of plugins/images
dbpf "cctv6:cam1:ArrayCallbacks" "Enable"

#dbpf "cctv6:image1:ArrayCallbacks" "Enable"

dbpf "cctv6:image1:EnableCallbacks" "Enable"
dbpf "cctv6:image2:EnableCallbacks" "1"
dbpf "cctv6:image3:EnableCallbacks" "1"
dbpf "cctv6:image4:EnableCallbacks" "1"
dbpf "cctv6:image5:EnableCallbacks" "1"
dbpf "cctv6:ROI1:EnableCallbacks" "1"
dbpf "cctv6:Proc1:EnableCallbacks" "1"
dbpf "cctv6:CC1:EnableCallbacks" "1"
dbpf "cctv6:Over1:EnableCallbacks" "1"

dbpf "cctv6:cam1:Acquire" "1"

dbl > pv.list

