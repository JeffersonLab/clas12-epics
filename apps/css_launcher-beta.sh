#!/bin/sh

# force java version
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-oracle
export PATH=$JAVA_HOME/bin:$PATH

if [ ! -z $1 ]
then
    css_share_path=$1
else
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    css_share_path=$DIR/../css_share
fi


css=`which css 2> /dev/null`

if ! [ -e "$css" ]
then
    echo 'No css found in $PATH'
    exit
fi

echo Running css ...
/usr/clas12/css/dev/linux-x86_64/cs-studio/cs-studio \
    -pluginCustomization $css_share_path/common/prefs/plugin_customization.ini \
	-share_link $css_share_path=/CLAS12_Share &
