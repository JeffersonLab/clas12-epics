##
## The following is needed if your board support package doesn't at boot time
## automatically cd to the directory containing its startup script
##
cd "$IOC_root_classc4"

############################################################################
< cdCommands
############################################################################
< ../network
############################################################################
cd topbin
ld < classc4.munch
cd top

## Register all support components
dbLoadDatabase("dbd/classc4.dbd")
classc4_registerRecordDeviceDriver(pdbbase)

epicsEnvSet( "EPICS_CA_ADDR_LIST", "129.57.255.4")

## Struck Scalers
#drvSIS3801Config("Port name",
#                  baseAddress,
#                  interruptVector,
#                  int interruptLevel,
#                  channels,
#                  signals)
drvSIS3801Config("SIS38XX_0", 0x08000000, 221, 6, 4096, 32)

dbLoadRecords("db/sixty_hz_common.db")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=0, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=1, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=2, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=3, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=4, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=5, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=6, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=7, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=8, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=9, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=10, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=11, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=12, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=13, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=14, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=15, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=16, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=17, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=18, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=19, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=20, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=21, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=22, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=23, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=24, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=25, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=26, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=27, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=28, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=29, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=30, PORT=SIS38XX_0")
dbLoadRecords("db/sixty_hz_macro.db", "FIFO=4096, HALF_FIFO=2048, CHAN=31, PORT=SIS38XX_0")

## Joerger Scalers
# Note: this function is not defined in iocsh, only vxworks shell
VSCSetup(2, 0x0a000000, 200)
dbLoadRecords("db/scaler.db")
dbLoadRecords("db/frwd_scaler.db")

## harp_generic
# OMS VME driver setup parameters: 
#     (1)cards, (2)base address(short, 16-byte boundary), 
#     (3)interrupt vector (0=disable or  64 - 255), (4)interrupt level (1 - 6),
#     (5)motor task polling rate (min=1Hz,max=60Hz)
omsSetup(2, 0x8000, 180, 5, 10)
dbLoadRecords("db/motor.db","motor_name=harp_2H02A,card=0,slot=2,srev=2000,urev=2.54,direction=Pos,velo=0.5,accl=0.01")
#dbLoadRecords("db/scan.db","motor_name=harp_2H02A,start_at=4.2,end_at=8.4,start_speed=0.5,scan_speed=0.04,acq_time=0.1")
dbLoadRecords("db/scan.db","motor_name=harp_2H02A,start_at=37.5,end_at=85.0,start_speed=1.5,scan_speed=0.4,acq_time=0.07")

dbLoadRecords("db/motor.db", "motor_name=viewer,card=0,slot=1,srev=2000,urev=2.54,direction=Neg,velo=0.03,accl=0.01")
dbLoadRecords("db/viewer.db")
#
dbLoadRecords("db/motor.db","motor_name=hps_collimator,card=0,slot=3,srev=2000,urev=0.2,direction=Pos,velo=0.2,accl=0.5")
dbLoadRecords("db/scan.db","motor_name=hps_collimator,start_at=4.22,end_at=4.82,start_speed=0.2,scan_speed=0.02,acq_time=0.07")
dbLoadRecords("db/hps_collimators.db")

## beam_stopper
dbLoadRecords("db/motor.db","motor_name=beam_stop, card=0, slot=0, srev=2000, urev=5.08, direction=Pos, velo=2.5, accl=0.1")
dbLoadRecords("db/stopper.db")

## IOC monitoring, etc
dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminVxWorks.db", "IOC=iocclassc4")
#dbLoadRecords("$(AUTOSAVE)/asApp/Db/save_restoreStatus.db", "P=iocclassc4:")

# currently running in softioc for testing:
dbLoadTemplate("db/scaler-ped.substitutions")
#dbLoadRecords("db/scaler-ped.db","OUT=fcup_offset,P=fcup_offset,RAW=scalerS2b, REF=IPM2C21A,REFMAX=0.1,RAWMAX=9999,N=5")
#dbLoadRecords("db/scaler-ped.db","OUT=slm_offset, P=slm_offset, RAW=scalerS16b,REF=IPM2C21A,REFMAX=0.1,RAWMAX=800,N=5")
dbLoadRecords("db/scaler_calc1b.db")


cd startup

## autosave setup
#< save_restore.cmd

iocInit "../resource.def"

## hard-coded fcup calibration, used to calculate scaler_calc1

dbpf "fcup_offset","199.9"
dbpf "fcup_slope","906.2"

dbpf "slm_offset","-1301.0"
dbpf "slm_slope","4298"

## Added these three line. to start counting after restarting IOC
dbpf "scaler.CNT","1"
dbpf "scaler_mode.VAL","1"
dbpf "display_mode.VAL","Hertz"

## Handle autosave 'commands' contained in loaded databases.
#makeAutosaveFiles()
#create_monitor_set("info_positions.req", 5, "P=iocclassc4:")
#create_monitor_set("info_settings.req", 30, "P=iocclassc4:")

## Added these three line. to start counting after restarting IOC
dbpf "scaler_c.CNT","1"
dbpf "scaler_c_mode.VAL","1"
dbpf "display_c_mode.VAL","Hertz"


## 
## Start any sequence programs
## 

seq &sixtyHz

## removed for rafopar
#seq &scaler_restart
#seq &frwd_scaler_restart

## Motors
seq &reset_motor, "name=beam_stop_reset, motor_name=beam_stop"

seq &reset_motor, "name=harp_2H02A_reset, motor_name=harp_2H02A"
seq &harp_scan_generic, "name=harp_2H02A_scan, motor_name=harp_2H02A"

seq &reset_motor, "name=viewer_reset, motor_name=viewer"
#seq &reset_motor, "name=hps_target_reset, motor_name=hps_target"

seq &reset_motor, "name=hps_collimator_reset, motor_name=hps_collimator"
seq &harp_scan_generic, "name=hps_collimator_scan, motor_name=hps_collimator"

