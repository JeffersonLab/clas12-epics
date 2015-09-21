# Hall B CA Gateway

The Hall B CA Gateway is setup to run as a systemd service.

Th CA Gateway is being used to provide read-only access outside the firewall.  The 
main intention is to support our webopi webserver.  Note that the '-server' option 
is not used when the run within systemd.

## systemd Files
* gateway.service - the systemd service, to be installed in /usr/lib/systemd/system/
* gateway - the service environment variable file, to be installed in /etc/sysconfig/

## CA Gateway Files
* gateway.access - defines access security rules used by the gateway
* gateway.pvlist - defines allowed PVs

