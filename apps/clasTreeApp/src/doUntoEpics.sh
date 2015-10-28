#!/bin/sh

do_to_element(){
    pv="${element}v0set";
    caget -t $pv;
}

do_to_subnode(){
    pv="";
}



node=$1;
type=`echo $node | awk '{if($1~":")print "element";else print "subnode"}'`

if [ $type = "element" ]; then   #its an element
    element=$node;
    do_to_element;
else
    do_to_subnode;
fi

exit;
