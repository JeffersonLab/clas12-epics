#!/bin/bash

# B.Morris - 09/04/2019
# network@jlab.org
#

hostname="${@: -1}"

if ! [ $1 == "-a" ]; then
  if [ `whoami` == "clasrun" ]; then
    echo "Invalid User."
    exit
  fi
fi

if [[ ! $hostname =~ ^[-_\.[:alnum:]]+$ ]]; then
    echo "Usage: $0 <hostname>";
    echo "       <hostname>            DNS hostname of the device that needs to be reset";
    echo;
    echo "This script will locate the given hostname on the network and perform a hard reset of the switch port";
    echo "if it is authorized to do so.";
    echo;
    exit 1;
fi

curl -k https://jnet.jlab.org/remote/port_reset.php?hostname=$hostname
echo

