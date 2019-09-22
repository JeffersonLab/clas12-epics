## 
## The following is needed if your board support package doesn't at boot time
## automatically cd to the directory containing its startup script
##
cd "$IOC_root_classc1"

############################################################################
< cdCommands
############################################################################
< ../network
############################################################################
cd topbin
ld < classc1.munch
cd top

## Register all support components
dbLoadDatabase("dbd/classc1.dbd")
classc1_registerRecordDeviceDriver(pdbbase)

epicsEnvSet( "EPICS_CA_ADDR_LIST", "129.57.255.4")

## Struck Scalers
#drvSIS3801Config("Port name",
#                  baseAddress,
#                  interruptVector,
#                  int interruptLevel,
#                  channels,
#                  signals)
#drvSIS3801Config("SIS38XX_0", 0x08000000, 220, 6, 16, 32)
#dbLoadRecords("$(STD)/stdApp/Db/scaler32.db", "P=bom_, S=sc, DTYP=Asyn Scaler, OUT=@asyn(SIS38XX_0), FREQ=25000000")
#dbLoadRecords("$(MCA)/db/SIS38XX.template", "P=bom_, SCALER=sc, PORT=SIS38XX_0")

#dbLoadRecords("db/bom_scaler.db", "scaler=bom_sc, FIFO=16, PORT=SIS38XX_0")
#dbLoadRecords("db/bom_stop_start.db",   "scaler=bom_sc")
#dbLoadRecords("db/bom_read_control.db", "scaler=bom_sc")
#dbLoadRecords("db/bom_sum.db",          "scaler=bom_sc")

## Joerger Scalers
# NOTE: this function is not defined in iocsh, only vxworks shell
VSCSetup(3, 0x0a000000, 200)
# scaler_c, d, e
dbLoadRecords("db/scaler_c.db")
dbLoadRecords("db/scaler_d.db")
dbLoadRecords("db/scaler_e.db")

## harp_generic
# OMS VME driver setup parameters: 
#     (1)cards, (2)base address(short, 16-byte boundary), 
#     (3)interrupt vector (0=disable or  64 - 255), (4)interrupt level (1 - 6),
#     (5)motor task polling rate (min=1Hz,max=60Hz)
omsSetup(2, 0x8000, 180, 5, 10)
dbLoadRecords("db/motor.db","motor_name=harp_2c21, card=0, slot=2, srev=2000, urev=2.54, direction=Neg, velo=5.0, accl=0.1")
dbLoadRecords("db/scan.db","motor_name=harp_2c21, start_at=25, end_at=55.0, start_speed=5.0, scan_speed=0.5, acq_time=0.1")
#
dbLoadRecords("db/motor.db","motor_name=harp_tagger, card=0, slot=1, srev=2000, urev=2.54, direction=Neg, velo=0.5, accl=0.01")
dbLoadRecords("db/scan.db","motor_name=harp_tagger, start_at=10, end_at=55.0, start_speed=5.0, scan_speed=0.5, acq_time=0.07")
dbLoadRecords("db/radiators.db")
#
dbLoadRecords("db/motor.db","motor_name=collimator,card=0,slot=3,srev=2000,urev=0.2,direction=Pos,velo=0.2,accl=0.5")
#dbLoadRecords("db/scan.db","motor_name=collimator,start_at=4.22,end_at=4.82,start_speed=0.2,scan_speed=0.02,acq_time=0.07")
dbLoadRecords("db/hallb_collimator.db")

#dbLoadRecords("db/motor.db","motor_name=harp_2H01, card=0, slot=0, srev=2000, urev=2.54, direction=Pos, velo=0.5, accl=0.01")
#dbLoadRecords("db/motor.db","motor_name=harp_2H01, card=0, slot=0, srev=10000, urev=2.54, direction=Pos, velo=0.5, accl=0.01")
dbLoadRecords("db/motor.db","motor_name=harp_2H01, card=0, slot=0, srev=2000, urev=0.508, direction=Pos, velo=0.5, accl=0.01")
dbLoadRecords("db/scan.db","motor_name=harp_2H01, start_at=3.0, end_at=10.5, start_speed=0.5, scan_speed=0.04, acq_time=0.1")

## IOC monitoring, etc
dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminVxWorks.db", "IOC=iocclassc1")
#dbLoadRecords("$(AUTOSAVE)/asApp/Db/save_restoreStatus.db", "P=iocclassc1:")

#KBB add Moller Motor 20160623
#dbLoadRecords("db/motor.db","motor_name=m_target, card=1, slot=0, srev=2000, urev=2.54, direction=Neg, velo=0.5, accl=0.01")
#dbLoadTemplate("db/moeller_target.substitutions")
dbLoadRecords("db/moeller_target.db")


# MOLLER QUADS:
#dbLoadRecords("db/dynabc.db")
#dbLoadRecords("db/dynabc_setvalues.db")

cd startup

## autosave setup
#< save_restore.cmd

iocInit "../resource.def"

## Handle autosave 'commands' contained in loaded databases.
#makeAutosaveFiles()
#create_monitor_set("info_positions.req", 5, "P=iocscalerTest:")
#create_monitor_set("info_settings.req", 30, "P=iocscalerTest:")

##
## Start any sequence programs
##

## Struck
#dbpf "bom_Dwell", "1.0"
#dbpf "bom_ReadAll.SCAN","Passive"
#seq &SIS38XX_SNL, "P=bom_, R=sc_, NUM_SIGNALS=32, FIELD=READ"

## Joerger
## removed for rafopar
#seq &scaler_c_restart
#seq &scaler_d_restart
#seq &scaler_e_restart

## Motors
seq &reset_motor, "name=up_2c21_reset, motor_name=harp_2c21"
seq &harp_scan_generic, "name=up_2c21_scan, motor_name=harp_2c21"

seq &reset_motor, "name=h_tagger_reset, motor_name=harp_tagger"
seq &harp_scan_generic, "name=h_tagger_scan, motor_name=harp_tagger"

seq &reset_motor, "name=h_2H01_reset, motor_name=harp_2H01"
seq &harp_scan_generic, "name=h_2H01_scan, motor_name=harp_2H01"

seq &reset_motor, "name=h_collimator_reset, motor_name=collimator"
#seq &harp_scan_generic, "name=h_collimator_scan, motor_name=collimator"

#seq &moeller_target

# for alarms:
dbpf "iocclassc1:FD_FREE.LOLO", "7"
dbpf "iocclassc1:FD_FREE.LOW", "9"

