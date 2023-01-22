name                | purpose                       | puppet | user     | host       | notes  
------------------- | ----------------------------- | ------ | -------- | ---------- | --------------------------------
`procServ.crontab`  | automatically start soft IOCs | yes    | wmoore   | clonioc`*` | requires filesystem permissions
`webopi.crontab`    | copy OPI files to web server  | yes    | wmoore   | clonsl3    | requires filesystem permissions
`torsol.crontab`    | copy FastDAQ data to tape     | no     | clascron | clonsl3    | requires scicomp certificate
`logs.crontab`      | manage IOC log files          | yes    | root     | clonsl3    | requires filesystem permissions
`harp2pos.crontab`  | copy harp scan data for MCC   | no     | n/a      | n/a        | unused since 2020

