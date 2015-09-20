## Example vxWorks startup file

## The following is needed if your board support package doesn't at boot time
## automatically cd to the directory containing its startup script
cd "/home/wmoore/workspaces/clas12-import-dev/apps/iocBoot/iocscalerTest"

############################################################################
< cdCommands
############################################################################
< ../nfsCommands
############################################################################
cd topbin
ld < scaler.munch
cd startup

## Register all support components
dbLoadDatabase("$(TOP)/dbd/scaler.dbd")
scaler_registerRecordDeviceDriver(pdbbase)

## Struck Scalers
#drvSIS3801Config("Port name",
#                  baseAddress,
#                  interruptVector,
#                  int interruptLevel,
#                  channels,
#                  signals)
drvSIS3801Config("SIS38XX_1", 0x08000000, 221, 6, 4096, 32)

dbLoadRecords("$(TOP)/db/sixty_hz_debug.db")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=0, INP=@asyn(SIS38XX_1 0)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=1, INP=@asyn(SIS38XX_1 1)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=2, INP=@asyn(SIS38XX_1 2)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=3, INP=@asyn(SIS38XX_1 3)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=4, INP=@asyn(SIS38XX_1 4)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=5, INP=@asyn(SIS38XX_1 5)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=6, INP=@asyn(SIS38XX_1 6)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=7, INP=@asyn(SIS38XX_1 7)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=8, INP=@asyn(SIS38XX_1 8)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=9, INP=@asyn(SIS38XX_1 9)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=10, INP=@asyn(SIS38XX_1 10)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=11, INP=@asyn(SIS38XX_1 11)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=12, INP=@asyn(SIS38XX_1 12)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=13, INP=@asyn(SIS38XX_1 13)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=14, INP=@asyn(SIS38XX_1 14)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=15, INP=@asyn(SIS38XX_1 15)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=16, INP=@asyn(SIS38XX_1 16)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=17, INP=@asyn(SIS38XX_1 17)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=18, INP=@asyn(SIS38XX_1 18)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=19, INP=@asyn(SIS38XX_1 19)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=20, INP=@asyn(SIS38XX_1 20)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=21, INP=@asyn(SIS38XX_1 21)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=22, INP=@asyn(SIS38XX_1 22)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=23, INP=@asyn(SIS38XX_1 23)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=24, INP=@asyn(SIS38XX_1 24)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=25, INP=@asyn(SIS38XX_1 25)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=26, INP=@asyn(SIS38XX_1 26)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=27, INP=@asyn(SIS38XX_1 27)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=28, INP=@asyn(SIS38XX_1 28)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=29, INP=@asyn(SIS38XX_1 29)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=30, INP=@asyn(SIS38XX_1 30)")
dbLoadRecords("$(TOP)/db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=31, INP=@asyn(SIS38XX_1 31)")

## Joerger Scalers
dbLoadRecords("$(STD)/stdApp/Db/scaler16m.db","P=HB:,S=SCLR,OUT=#C1 S0 @,DTYP=Joerger VSC8/16,FREQ=10000000")
dbLoadRecords("$(TOP)/db/scaler16m_norm.db", "P=HB:,S=SCLR")
# NOTE: this function is not defined in iocsh, only vxworks shell
VSCSetup(2, 0x0a000000, 200)

## FCUP
dbLoadRecords("$(TOP)/db/fcup_calc.db", "SCLR=HB:SCLR,CH=S2")

## IOC monitoring, etc
dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminVxWorks.db", "IOC=iocscalerTest")
dbLoadRecords("$(AUTOSAVE)/asApp/Db/save_restoreStatus.db", "P=iocscalerTest:")

## autosave setup
< save_restore.cmd

iocInit "../resource.def"

## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=iocscalerTest:")
create_monitor_set("info_settings.req", 30, "P=iocscalerTest:")
create_monitor_set("scaler16m_settings.req", 30, "P=HB:,S=SCLR")
create_monitor_set("sixty_hz_settings.req", 30)

## Start any sequence programs
seq &sixtyHz

