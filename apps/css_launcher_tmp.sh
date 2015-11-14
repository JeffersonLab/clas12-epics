#!/bin/sh

# run css with an on-the-fly generated workspace
#   - to avoid duplicate conflicting workspaces
#   - to guarantee standard startup user interface

css_share_path=`pwd`/../css_share
plugin_profile=$css_share_path/common/prefs/plugin_customization.ini
workspace=$css_share_path/common/prefs/workspace

# generate a temporary css workspace:
tmp=`mktemp -d -p /tmp/CSS-Workspaces`
cp -rf $workspace/*    $tmp
cp -rf $workspace/.*   $tmp
cp -rf $plugin_profile $tmp

# we want to run *everything* from the tmp workspace:
css -nosplash \
    -data $tmp \
    -pluginCustomization $tmp/plugin_customization.ini \
    -share_link $css_share_path=/CLAS12_Share

# delete the tmp workspace:
rm -rf $tmp

