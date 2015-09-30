# Hall B iocLogServer

The Hall B iocLogServer is setup to run as a systemd service.

The iocLogServer is being used to provided caput logging.  The needed paths to the executable 
and the final log file are defined within the service definition.

## systemd Files
* iocLogServer.service - the systemd service, to be installed in /usr/lib/systemd/system/

