#!/bin/bash

while [ 1 ]
do
  wget -O aaxis.jpg http://cctv6/axis-cgi/jpg/image.cgi
  # wget is slower than mv, and cs-studio doesn't like a partial file
  mv -f aaxis.jpg axis.jpg
  sleep 1
done

