#!/bin/sh

# force java version
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-oracle
export PATH=$JAVA_HOME/bin:$PATH

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
css_share_path=$DIR/../css_share
cfg=plugin_customization.ini

if [ ! -z $1 ]
then
  if [ ! -d "$1" ]
  then
    echo $1 is not a directory, so assuming it is a config suffix
    cfg=plugin_customization-$1.ini
  else
    echo $1 is a directory, so assuming it is the share
    css_share_path=$1
  fi
  if [ ! -z $2 ]
  then
    if [ ! -d "$2" ]
    then
      echo $2 is not a directory, so assuming it is a config suffix
      cfg=plugin_customization-$2.ini
    else
      echo $2 is a directory, so assuming it is the share
      css_share_path=$2
    fi
  fi
fi

css=`which css 2> /dev/null`
if ! [ -e "$css" ]
then
    echo 'No css found in $PATH'
    exit
fi

echo Running css ...
css \
  -pluginCustomization $css_share_path/common/prefs/$cfg \
	-share_link $css_share_path=/CLAS12_Share &

