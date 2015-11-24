#!/bin/sh
template=/home/baltzell/.mozilla/firefox/0jaik1kf.default
dir=$HOME/.mozilla/firefox
list=$dir/profiles.ini

name=$1
profile=`mktemp -u XXXXXXXX.${name%%.*}`
if [ -e $dir/$profile ]
then
  profile=`mktemp -u XXXXXXXX.${name%%.*}`
  if [ -e $dir/$profile ]
  then
    profile=`mktemp -u XXXXXXXX.${name%%.*}`
    if [ -e $dir/$profile ]
    then
      echo ERROR:  COULD NOT GENERATE A PROFILE
      exit
    fi
  fi
fi

nprofiles=`grep \[Profile[0-9]*\] $list | tail -1`
nprofiles=`echo $nprofiles | sed 's/^.*Profile\([0-9]*\)]/\1/'`
let nprofiles=nprofiles+1

cp -r $template $dir/$profile
rm -rf $dir/$profile/sessionstore*
rm -rf $dir/$profile/datareporting
rm -rf $dir/$profile/healthreport

echo >> $list
echo [Profile$nprofiles] >> $list
echo Name=$name >> $list
echo IsRelative=1 >> $list
echo Path=$profile >> $list
echo Default=0 >> $list
echo >> $list


