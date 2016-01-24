# Hall B iocLogServer

The Hall B iocLogServer is setup to run as a systemd service.

The iocLogServer is being used to provided caput logging.  The needed paths to the executable 
and the final log file are defined within the service definition.

## systemd Files
* iocLogServer.service - the systemd service, to be installed in /etc/systemd/system/

## IOC Config Example
configure/RELEASE:
  CAPUTLOG=/usr/clas12/R3.14.12.5/modules/caPutLog-3-4

caenHvApp/src/Makefile:
  ioccaen_DBD  += caPutLog.dbd
  ioccaen_LIBS += caPutLog

caenhv.acf:
  ASG(DEFAULT) {
    RULE(1,READ)
    RULE(1,WRITE,TRAPWRITE)
  }

ioccaenhv/st.cmd:
  asSetFilename("caenhv.acf")
  iocInit()
  caPutLogInit("clonioc1:7011")

