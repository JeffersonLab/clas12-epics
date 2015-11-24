#!/bin/sh

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
#echo $BASH_SOURCE
#echo $DIR

css_share_path=$DIR/../css_share

echo Running css ...

css \
    -pluginCustomization $css_share_path/common/prefs/plugin_customization.ini \
	-share_link $css_share_path=/CLAS12_Share \
	-nosplash &

