##
## The following is needed if your board support package doesn't at boot time
## automatically cd to the directory containing its startup script
##
cd "/home/wmoore/workspaces/clas12-import-dev/apps/iocBoot/iocclassc4"

############################################################################
< cdCommands
############################################################################
< ../nfsCommands
############################################################################
cd topbin
ld < classc4.munch
cd startup

## Register all support components
dbLoadDatabase("$(TOP)/dbd/classc4.dbd")
classc4_registerRecordDeviceDriver(pdbbase)


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
# Note: this function is not defined in iocsh, only vxworks shell
VSCSetup(2, 0x0a000000, 200)
dbLoadTemplate("joerger_classc4.substitutions")

## FCUP
# from scalerApp
dbLoadRecords("$(TOP)/db/fcup_calc.db", "P=HB:,R=fcup,SCLR=scaler,CH=S2")
# from fcup_gainApp - DVME628, base address is hardcoded into the driver
dbLoadDatabase("$(TOP)/db/fcup_cal.db")

## harp_generic
# OMS VME driver setup parameters: 
#     (1)cards, (2)base address(short, 16-byte boundary), 
#     (3)interrupt vector (0=disable or  64 - 255), (4)interrupt level (1 - 6),
#     (5)motor task polling rate (min=1Hz,max=60Hz)
omsSetup(2, 0x8000, 180, 5, 10)
dbLoadRecords("$(TOP)/db/motor.db","M=harp_2H02A,card=0,slot=2,srev=2000,urev=2.54,direction=Pos,velo=0.5,accl=0.01")
dbLoadRecords("$(TOP)/db/scan.db","M=harp_2H02A,start_at=3.0,end_at=9.5,start_speed=0.5,scan_speed=0.04,acq_time=0.1")
#
dbLoadRecords("$(TOP)/db/motor.db", "M=viewer,card=0,slot=1,srev=2000,urev=2.54,direction=Neg,velo=0.03,accl=0.01")
dbLoadRecords("$(TOP)/db/viewer.db")
#
dbLoadRecords("$(TOP)/db/motor.db","M=hps_collimator,card=0,slot=3,srev=2000,urev=0.2,direction=Pos,velo=0.2,accl=0.5")
dbLoadRecords("$(TOP)/db/scan.db","M=hps_collimator,start_at=4.22,end_at=4.82,start_speed=0.2,scan_speed=0.02,acq_time=0.07")
dbLoadRecords("$(TOP)/db/hps_collimators.db")

## beam_stopper
dbLoadRecords("$(TOP)/db/motor.db","M=beam_stop, card=0, slot=0, srev=2000, urev=5.08, direction=Pos, velo=2.5, accl=0.1")
dbLoadRecords("$(TOP)/db/stopper.db")

## IOC monitoring, etc
dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminVxWorks.db", "IOC=iocclassc4")
dbLoadRecords("$(AUTOSAVE)/asApp/Db/save_restoreStatus.db", "P=iocclassc4:")

## autosave setup
< save_restore.cmd

iocInit "../resource.def"

## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=iocclassc4:")
create_monitor_set("info_settings.req", 30, "P=iocclassc4:")
create_monitor_set("joerger_classc4_settings.req", 60)
create_monitor_set("sixty_hz_settings.req", 30)

## Start any sequence programs
seq &sixtyHz

