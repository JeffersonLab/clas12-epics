## 
## The following is needed if your board support package doesn't at boot time
## automatically cd to the directory containing its startup script
##
cd "$IOC_root_classc1"

putenv "EPICS_TS_NTP_INET=129.57.90.1"

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

epicsEnvSet( "EPICS_CA_ADDR_LIST", "129.57.235.12")

## Joerger Scalers
# NOTE: this function is not defined in iocsh, only vxworks shell
VSCSetup(3, 0x0a000000, 200)
# scaler_c, d, e
dbLoadRecords("db/scaler_c.db")
dbLoadRecords("db/scaler_d.db")
dbLoadRecords("db/scaler_e.db")

# OMS VME driver setup parameters: 
#     (1)cards, (2)base address(short, 16-byte boundary), 
#     (3)interrupt vector (0=disable or  64 - 255), (4)interrupt level (1 - 6),
#     (5)motor task polling rate (min=1Hz,max=60Hz)
omsSetup(3, 0x8000, 180, 5, 10)

# First Card:
dbLoadRecords("db/motor.db","motor_name=harp_2H01, card=0, slot=0, srev=2000, urev=0.508, direction=Pos, velo=0.5, accl=0.01")
dbLoadRecords("db/scan.db","motor_name=harp_2H01, start_at=3.0, end_at=10.5, start_speed=0.5, scan_speed=0.04, acq_time=0.1")
dbLoadRecords("db/motor.db","motor_name=harp_tagger, card=0, slot=1, srev=2000, urev=2.54, direction=Neg, velo=0.5, accl=0.01")
dbLoadRecords("db/scan.db","motor_name=harp_tagger, start_at=10, end_at=55.0, start_speed=5.0, scan_speed=0.5, acq_time=0.07")
dbLoadRecords("db/motor.db","motor_name=harp_2c21, card=0, slot=2, srev=2000, urev=2.54, direction=Neg, velo=5.0, accl=0.1")
dbLoadRecords("db/scan.db","motor_name=harp_2c21, start_at=25, end_at=55.0, start_speed=5.0, scan_speed=0.5, acq_time=0.1")
dbLoadRecords("db/motor.db","motor_name=collimator,card=0,slot=3,srev=2000,urev=0.2,direction=Pos,velo=0.2,accl=0.5")
dbLoadRecords("db/hallb_collimator.db")

# Second Card:
#dbLoadRecords("db/motor.db","motor_name=m_target, card=1, slot=0, srev=2000, urev=2.54, direction=Neg, velo=0.5, accl=0.01")
#dbLoadTemplate("db/moeller_target.substitutions")
dbLoadRecords("db/moeller_target.db")
dbLoadRecords("db/motor.db","motor_name=harp_2H00A, card=1, slot=3, srev=2000, urev=0.1016, direction=Neg, velo=0.4,accl=0.01")
dbLoadRecords("db/scan.db","motor_name=harp_2H00A, start_at=3.0, end_at=10.5, start_speed=0.5, scan_speed=0.04, acq_time=0.1")

# PRAD Collimator and Radiator:
dbLoadRecords("db/motor.db", "motor_name=prad:colli,card=1,slot=1,srev=2000,urev=0.1016,direction=Pos,velo=0.25,accl=0.01")

# PRAD Vetoes:
dbLoadRecords("db/motor.db", "motor_name=prad:veto1, card=2, slot=0, srev=2000, urev=2.54, direction=Neg, velo=6, accl=0.01")
dbLoadRecords("db/motor.db", "motor_name=prad:veto2, card=2, slot=1, srev=2000, urev=2.54, direction=Neg, velo=6, accl=0.01")
dbLoadRecords("db/motor.db", "motor_name=prad:veto3, card=2, slot=2, srev=2000, urev=2.54, direction=Neg, velo=6, accl=0.01")
dbLoadRecords("db/motor.db", "motor_name=prad:veto4, card=2, slot=3, srev=2000, urev=2.54, direction=Neg, velo=6, accl=0.01")

# PRAD/X17 motor positions:
dbLoadRecords("db/pradcolli.db","P=prad:colli:,MOTOR=prad:colli")
dbLoadRecords("db/x17-harp-positions.db","P=x17:target:,MOTOR=harp_2H00A")

## IOC monitoring, etc
dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminVxWorks.db", "IOC=iocclassc1")
#dbLoadRecords("$(AUTOSAVE)/asApp/Db/save_restoreStatus.db", "P=iocclassc1:")

cd startup

## autosave setup
#< save_restore.cmd

iocInit "../resource.def"

## Handle autosave 'commands' contained in loaded databases.
#makeAutosaveFiles()
#create_monitor_set("info_positions.req", 5, "P=iocscalerTest:")
#create_monitor_set("info_settings.req", 30, "P=iocscalerTest:")

## Added these three line. to start counting after restarting IOC
dbpf "scaler_c.CNT","1"
dbpf "scaler_c_mode.VAL","1"
dbpf "scaler_d.CNT","1"
dbpf "scaler_d_mode.VAL","1"
dbpf "display_c_mode.VAL","Hertz"
dbpf "display_d_mode.VAL","Hertz"

##
## Start any sequence programs
##

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

seq &reset_motor, "name=h_2H00A_reset, motor_name=harp_2H00A"
seq &harp_scan_generic, "name=h_2H00A_scan, motor_name=harp_2H00A"

seq &reset_motor, "name=h_collimator_reset, motor_name=collimator"

seq &reset_motor, "name=prad:colli:reset, motor_name=prad:colli"
seq &reset_motor, "name=prad:veto1:reset, motor_name=prad:veto1"
seq &reset_motor, "name=prad:veto2:reset, motor_name=prad:veto2"
seq &reset_motor, "name=prad:veto3:reset, motor_name=prad:veto3"
seq &reset_motor, "name=prad:veto4:reset, motor_name=prad:veto4"

#seq &moeller_target

# for alarms:
dbpf "iocclassc1:FD_FREE.LOLO", "7"
dbpf "iocclassc1:FD_FREE.LOW", "9"

