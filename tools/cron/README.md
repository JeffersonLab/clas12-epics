name                | purpose                       | puppet | user     | host      | notes  
------------------- | ----------------------------- | ------ | -------- | --------- | -----------------------------------
`procServ.crontab`  | automatically start soft IOCs | yes    | wmoore   | clonioc\* | requires filesystem permissions (1)
`webopi.crontab`    | copy OPI files to web server  | yes    | wmoore   | clonsl3   | requires filesystem permissions (2)
`torsol.crontab`    | copy FastDAQ data to tape     | no     | clascron | clonsl3   | requires scicomp certificate (3)
`logs.crontab`      | manage IOC log files          | yes    | root     | clonsl3   | requires filesystem permissions (3)
`harp2pos.crontab`  | copy harp scan data for MCC   | no     | n/a      | n/a       | unused since 2020

(1) - `/usr/clas12/DATA/logs`, `/usr/clas12/DATA/autosave`, and `$EPICS/apps/iocBoot/ioc*/pv.list`
(2) - `/group/hallb/www/hallbopi/html/opis`
(3) - shared with the the Hall B DAQ
(4) - `/usr/clas12/DATA/logs`

Note, there's also a log rotator running on `/usr/clas12/DATA/logs`, probably via a systemd service.

