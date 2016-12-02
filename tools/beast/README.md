## BEAST AlarmServer

There are four parts to running the AlarmServer.  They are:
- AlarmServer
- AlarmNotifier
- JMS2RDB
- ActiveMQ

All of these are handled with systemd services (see section below).  
Otherwise, you can interface with the AlarmServer and AlarmConfigTool directly.

## Usage

On the appropriate server, start/stop/restart the AlarmServer, AlarmNofitier, and JMS2RDB with systemctl.  Example:
```
sudo systemctl restart AlarmServer@HallB
sudo systemctl restart AlarmServer@HPS
```

## systemd Setup

Puppet will install systemd services and required packages to the appropriate 
server(s).  These services are fairly generic and call the scripts within this 
directory.  The aim was for them to be easily accessible to non-puppet admins.  
The services are:

- activemq.service       - JMS broker for clients (ex. cs-studio)

- AlarmServer@.service   - the alarm server itself
    - Ensures activemq.service is running
    - Runs AlarmServerConfig
    - Runs AlarmServerStart
    - Starts the other two services

- AlarmNotifier@.service - the Notifier for SMS/Email generation
    - Runs AlarmNotifierStart

- AlarmJMS2RDB@.service  - a tool that listens for JMS messages and writes them 
to a RDB
    - Runs AlarmJMS2RDBStart

## Scripts

- AlarmServerConfig  - deletes existing alarm database, builds new one, and 
exports it to *root*_tree.xml.
- AlarmServerStart   - starts AlarmServer
- AlarmNotifierStart - starts AlarmNotifier
- AlarmJMS2RDBStart  - start JMS2RDB

## Files

alarm_settings.ini      - config file for AlarmServer
jms2rdb_settings.ini    - config file for JMS2RDB
notifier_settings.ini   - config file for AlarmNotifier

*root* refers to the root of the alarm tree.

- *root*_root.xml     - defines the config name only, used to delete existing 
database and starts new one.
- *root*_includes.cfg - lists the XML files to use for building the alarm tree.
- *root*_tree.xml     - exported tree from AlarmServerConfig.

## Misc

To export current tree to file: 
```
AlarmConfigTool -root <root> -export -file <outfile> -data /dev/null
```

To delete an existing tree:
```
AlarmConfigTool -root <root> -delete / -data /dev/null
```

## Further Info

Contact Wesley Moore (wmoore@jlab.org)
