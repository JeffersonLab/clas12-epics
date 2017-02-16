#!/bin/sh

query='use ALARM; SELECT NAME FROM ALARM_TREE, PV WHERE (ALARM_TREE.COMPONENT_ID = PV.COMPONENT_ID) and (PV.STATUS_ID = 12);'

#list=`mysql -h clondb3 -u alarm -p'$alarm' -e "$query"`

#list=`echo $list | sed 's/ /\r/'`
#echo $list

#date && echo $list | logentry -l HBCONTROLS -t 'Disabled Alarm List' -b -

mysql -h clondb3 -u alarm -p\$alarm -e "$query"
  
