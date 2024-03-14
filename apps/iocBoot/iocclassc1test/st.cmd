## 
## The following is needed if your board support package doesn't at boot time
## automatically cd to the directory containing its startup script
##
cd "$IOC_root_classc1"

# 2023 NAB: When booting from clon00, vxWorks system time does not get initialized.
# The default is supposed to be from the ntp server on the boot host.  When I start
# clon00's ntpd daemon via systemctl and reboot, there's no effect.  Meanwhile, this
# makes it work via JLab's ntp server:
putenv "EPICS_TS_NTP_INET=129.57.90.1"

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

