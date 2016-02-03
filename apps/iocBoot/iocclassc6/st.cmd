## iocclassc6 vxWorks startup file

## The following is needed if your board support package doesn't at boot time
## automatically cd to the directory containing its startup script
cd "$IOC_root_classc6"

< cdCommands
#< ../nfsCommands
< ../network
#< ../users

cd topbin

## You may have to change classc6 to something else
## everywhere it appears in this file
ld 0,0, "classc6.munch"

## Register all support components
cd top
dbLoadDatabase "dbd/classc6.dbd"
classc6_registerRecordDeviceDriver pdbbase

## Load record instances
dbLoadRecords("db/bta_suppl.db","hall=B,ioc=classc6")

## Load IOC status records
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminVxWorks.db","IOC=iocclassc6")

cd startup
iocInit

## Start any sequence programs
#seq &bta, "hall=B,ioc=classc6" 

