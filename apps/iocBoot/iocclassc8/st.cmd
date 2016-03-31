## classc8 vxWorks startup file

## The following is needed if your board support package doesn't at boot time
## automatically cd to the directory containing its startup script
cd "$IOC_root_classc8"

############################################################################
< cdCommands
############################################################################
< ../network
############################################################################
cd topbin
ld < classc8.munch
cd top

## Register all support components
dbLoadDatabase("dbd/classc8.dbd")
classc8_registerRecordDeviceDriver(pdbbase)

epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES", "10000000")

## Struck Scalers
#drvSIS3801Config("Port name",
#                  baseAddress,
#                  interruptVector,
#                  int interruptLevel,
#                  channels,
#                  signals)
drvSIS3801Config("SIS38XX_0", 0x08000000, 220, 6, 60000, 5)
dbLoadRecords("$(STD)/stdApp/Db/scaler32.db", "P=struck, S=Daq, DTYP=Asyn Scaler, OUT=@asyn(SIS38XX_0), FREQ=25000000")
dbLoadRecords("$(MCA)/db/SIS38XX.template", "P=struck, SCALER=Daq, PORT=SIS38XX_0")

dbLoadRecords("db/struckDaqCommon.db")
dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=0, PORT=SIS38XX_0")
dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=1, PORT=SIS38XX_0")
dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=2, PORT=SIS38XX_0")
dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=3, PORT=SIS38XX_0")
dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=4, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=5, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=6, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=7, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=8, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=9, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=10, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=11, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=12, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=13, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=14, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=15, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=16, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=17, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=18, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=19, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=20, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=21, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=22, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=23, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=24, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=25, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=26, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=27, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=28, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=29, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=30, PORT=SIS38XX_0")
#dbLoadRecords("db/struckDaq.db", "FIFO=60000, CHAN=31, PORT=SIS38XX_0")

# Load IOC status records
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminVxWorks.db","IOC=iocclassc8")

cd startup
iocInit "../resource.def"

## Struck
dbpf "struckDwell", "0.000015"
dbpf "struckReadAll.SCAN","Passive"
seq &SIS38XX_SNL, "P=struck, R=Daq_, NUM_SIGNALS=5, FIELD=READ"

## Start any sequence programs
seq &struckDaq
#testLoop()

