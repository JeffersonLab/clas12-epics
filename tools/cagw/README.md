# Hall B CA Gateways

The Hall B CA Gateways are setup to run as a systemd service and managed by 
Puppet.  However, the config files in this directory can be modified without 
any required Puppet updates.  Just restart the gateway service on the 
associated host.  

##Gateways in use
* clondb3 - read-only access
    * Allowed access from WebOPI webserver that sits outside the firewall. 
    * Used by the AlarmServer/Notifier to provide a clean interface to all 
    channels it needs.
* clonioc1 - r/w access
    * Provides the gateway for to all other controls subnets (ex. 
    Solenoid/Torus controls, detector test areas, etc).
    * Provides a way to archive PVs on dev subnets.

## systemd Files
* gateway.service - systemd service, to be installed in 
/etc/systemd/system/
    * NOTE: the '-server' option is not used when the run within systemd.
* gateway - service config file, to be installed in /etc/sysconfig/

## CA Gateway Files
* gateway_<hostname>.access - defines access security rules
* gateway_<hostname>.pvlist - defines allowed PVs
* cagwStats.opi - opi for displaying gateway stats
  * found in apps/cagwApp/op/opi
  * fd, quitFlag, and quitServerFlag are not shown

## Usage Examples
```
sudo systemctl start gateway
sudo systemctl stop gateway
sudo systemctl restart gateway
```
