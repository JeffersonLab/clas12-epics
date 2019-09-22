## iocclassc6 vxWorks startup file

cd "$IOC_root_classc6"

< cdCommands
#< ../nfsCommands
< ../network
#< ../users

cd topbin

ld 0,0, "classc6.munch"
#ld < classc6.munch

cd top

dbLoadDatabase "dbd/classc6.dbd"
classc6_registerRecordDeviceDriver pdbbase

putenv("EPICS_CA_AUTO_ADDR_LIST = NO")
putenv("EPICS_CA_ADDR_LIST = 129.57.163.255")

## Load IOC status records
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminVxWorks.db","IOC=iocclassc6")

# Hovanes's addresses increment by 0x01000000
# Current Struck addresses in classc6, December 2017:
# 0x8000000 is SIS3820, 64 MB - the new board for clas12
# 0x9000000 is SIS3801 - the last board used for asym in clas6
# 0xA000000 is SIS3801 - marked as previously used for asym in clas6
# Old CLAS6 FIFO is 32768
# This is a reasonable test value: 32768

#drvSIS3820Config("STRKHEL", 0x08000000, 220, 6, 16, 32, 0, 0)
#drvSIS3801Config("STRKHEL", 0x09000000, 220, 6, 32768, 32)
drvSIS3801Config("STRKHEL", 0x0A000000, 220, 6, 32768, 32)

dbLoadRecords("$(STD)/stdApp/Db/scaler32.db", "P=asym_, S=sc, DTYP=Asyn Scaler, OUT=@asyn(STRKHEL), FREQ=25000000")
dbLoadRecords("$(MCA)/db/SIS38XX.template", "P=asym_, SCALER=asym_sc, PORT=STRKHEL")

dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=0,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=3,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=5,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=6,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=7,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=8,PORT=STRKHEL")

#dbLoadRecords("db/asym_scaler_macro-swap.db","FIFO=32768,CHAN=3,PORT=STRKHEL,CHAN2=8")
#dbLoadRecords("db/asym_scaler_macro-swap.db","FIFO=32768,CHAN=6,PORT=STRKHEL,CHAN2=7")
#dbLoadRecords("db/asym_scaler_macro-swap.db","FIFO=32768,CHAN=7,PORT=STRKHEL,CHAN2=6")
#dbLoadRecords("db/asym_scaler_macro-swap.db","FIFO=32768,CHAN=8,PORT=STRKHEL,CHAN2=3")

dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=9,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=10,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=11,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=16,PORT=STRKHEL")

dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=20,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=24,PORT=STRKHEL")

dbLoadRecords("db/asym_scaler_macro_sums.db","FIFO=32768,CHAN=0,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro_sums.db","FIFO=32768,CHAN=7,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro_sums.db","FIFO=32768,CHAN=8,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro_sums.db","FIFO=32768,CHAN=9,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro_sums.db","FIFO=32768,CHAN=10,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro_sums.db","FIFO=32768,CHAN=11,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro_sums.db","FIFO=32768,CHAN=16,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro_sums.db","FIFO=32768,CHAN=20,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro_sums.db","FIFO=32768,CHAN=24,PORT=STRKHEL")

# fill in the unused channels:
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=1,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=2,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=4,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=12,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=13,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=14,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=15,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=17,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=18,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=19,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=21,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=22,PORT=STRKHEL")
dbLoadRecords("db/asym_scaler_macro.db","FIFO=32768,CHAN=23,PORT=STRKHEL")

dbLoadRecords("db/moller_setup.db")
dbLoadRecords("db/asym_scaler_common.db")
dbLoadRecords("db/asym_fdbk.db")
dbLoadRecords("db/polarization.db")
dbLoadRecords("db/asym_file.db")

dbLoadRecords("db/moeller_coincaccid_ratio.db")

cd startup
iocInit

# alarm limits on SLM beam charge asymmetry:
dbpf "q_asym_3.HIGH","0.2"
dbpf "q_asym_3.HIHI","0.4"
dbpf "q_asym_3.HSV","MINOR"
dbpf "q_asym_3.HHSV","MAJOR"

# Struck setup for asym,
# * with external channel advance and user inputs (Mode 0)
# * if prescale!=0 it doesn't advance
dbpf "asym_ReadAll.SCAN","Passive"
dbpf "asym_InputMode","Mode 0"
dbpf "asym_ChannelAdvance","External"
dbpf "asym_Prescale","0"

seq &SIS38XX_SNL_asym, "P=asym_, R=, NUM_SIGNALS=25, FIELD=READ"

seq &asym

epicsThreadSleep(1)
dbpf "moller_accumulate","0"

## update these after 2017 engineering run:
#seq &kepco_seq
#seq &quad_current
#seq &moller_setup

