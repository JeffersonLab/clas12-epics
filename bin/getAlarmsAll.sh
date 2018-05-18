#!/bin/sh
mysql -h clondb3 -u alarm -e \
"use ALARM; SELECT * from PV;" \
-p\$alarm

