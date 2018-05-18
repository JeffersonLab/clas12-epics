#!/bin/sh
#
# Maps ./lists/ to http://clonsl3.jlab.org/cyber/
#
# This is hardcoded to eliminate confusion as to where this webserver is 
# supposed to be hosted.  Any changes to the URL need to be sent to the Cyber 
# Team (most likely chads@jlab.org).
#
# Changes to the lists do not require restarting the webserver.
#
# Author: Wesley Moore (wmoore@jlab.org)
# Date:   Feb 2018
#

if [[ $EUID -ne 0 ]]; then
    echo "Error: this script must be run as root"
    exit 1
fi

docker rm -f docker-cyberlists
docker pull httpd:latest
docker run -d \
    --name docker-cyberlists \
    --hostname=clonsl3.jlab.org \
    -p 80:80 \
    -v $PWD/lists/:/usr/local/apache2/htdocs/cyber \
    httpd:latest

