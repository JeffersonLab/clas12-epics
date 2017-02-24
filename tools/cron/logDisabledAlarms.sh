#!/bin/sh

query='use ALARM; SELECT NAME FROM ALARM_TREE, PV WHERE (ALARM_TREE.COMPONENT_ID = PV.COMPONENT_ID) and (PV.STATUS_ID = 12);'

result=`mysql -h clondb3 -u alarm -p'$alarm' -e "$query" | grep -v NAME`

if [ -z $1 ]
then
  echo "$result"
else
  echo "$result" | logentry -l HBCONTROLS -t 'Disabled Alarm List' -b -
fi

