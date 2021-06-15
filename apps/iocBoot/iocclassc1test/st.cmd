## 
## The following is needed if your board support package doesn't at boot time
## automatically cd to the directory containing its startup script
##
cd "$IOC_root_classc1"

############################################################################
< cdCommands
############################################################################
< ../network-86
############################################################################
cd topbin
ld < classctest.munch
cd top

## Register all support components
dbLoadDatabase("dbd/classctest.dbd")
classctest_registerRecordDeviceDriver(pdbbase)

#drvSIS3820Config("STRKHEL", 0x8000000, 220, 6, 16, 32, 0, 0)

## IOC monitoring, etc
dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminVxWorks.db", "IOC=iocclassc1test")

cd startup

iocInit "../resource.def"


#dbLoadRecords("db/raster2021.db")

#seq &uitfraster
#seq &frxscale,"R=ITFRA"

#dbpf "ITFRA_WOFF.ASG","ITFRASTER"
#dbpf "ITFRA_WGO.ASG","ITFRASTER"
#dbpf "ITFRA_FSDRESET.ASG","ITFRASTER"
#dbpf "ITFRA_VSCALE.ASG","ITFRASTER"
#dbpf "ITFRA_XIMIN.ASG","ITFRASTER"
#dbpf "ITFRA_YIMIN.ASG","ITFRASTER"
#dbpf "ITFRA_XIMAX.ASG","ITFRASTER"
#dbpf "ITFRA_YIMAX.ASG","ITFRASTER"
