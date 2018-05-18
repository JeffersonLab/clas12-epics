#!/bin/sh
mysql -h clondb3 -u alarm -e \
"use log ; 
select datum,value 
from message,message_content 
where message.datum > '2017-05-18 00:00:00' 
and message.type = 'log' 
and message.name = 'send' 
and message.id=message_content.message_id 
and message_content.msg_property_type_id = 4;" \
-p\$alarm

