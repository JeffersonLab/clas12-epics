#!/bin/bash

host=$1
cd /usr/clas12/DATA/cameras

ip=`host $host | awk '{print$4}'`

echo $ip

# setup the symlink:
# (cs-studio needs to toggle between jpgs to force screen refreshes, so we use a symlink)
rm -f ${host}_link.jpg
ln -s ${host}.jpg ${host}_link.jpg

ii=0
while [ 1 ]
do
  # wget is slower than mv, and cs-studio doesn't like a partial file,
  # so wget to a temporary file, then mv
  
  wget -q -O ${host}_tmp.jpg http://${ip}/axis-cgi/jpg/image.cgi
  
  # convert image to exact size (and correct aspect ratio) for display on css screens:
  # (NOTE:  the "display" command requires an X-server, "convert" does not)
  #convert -resize 397x391! ${host}_tmp.jpg ${host}_tmp2.jpg 
  convert -resize 282x286! ${host}_tmp.jpg ${host}_tmp2.jpg 
  
  mv -f ${host}_tmp2.jpg ${host}.jpg
  
  sleep 0.5
  
  let ii=ii+1
  jj=`echo "scale=0;$ii%2" | bc`
  kk=`echo "scale=0;$ii/2" | bc`
  if [ "$jj" = "0" ]
  then
    caput -t B_HW_CAMS_cctv6:HEARTBEAT $kk &
  fi

done

