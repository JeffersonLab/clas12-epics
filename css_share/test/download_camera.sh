#!/bin/bash

host=$1
cd /usr/clas12/DATA/cameras

# setup the symlink:
rm -f ${host}_link.jpg
ln -s ${host}.jpg ${host}_link.jpg

while [ 1 ]
do
  # wget is slower than mv, and cs-studio doesn't like a partial file,
  # so wget to a temporary file, then mv
  wget -O ${host}_tmp.jpg http://cctv6/axis-cgi/jpg/image.cgi
  mv -f ${host}_tmp.jpg ${host}.jpg
  sleep 1
done

