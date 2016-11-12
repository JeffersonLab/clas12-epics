#!/bin/bash

host=$1
cd /usr/clas12/DATA/cameras

# setup the symlink:
# (cs-studio needs to toggle between jpgs to force screen refreshes, so we use a symlink)
rm -f ${host}_link.jpg
ln -s ${host}.jpg ${host}_link.jpg

while [ 1 ]
do
  # wget is slower than mv, and cs-studio doesn't like a partial file,
  # so wget to a temporary file, then mv
  wget -O ${host}_tmp.jpg http://${host}/axis-cgi/jpg/image.cgi
  mv -f ${host}_tmp.jpg ${host}.jpg
  sleep 1
done

