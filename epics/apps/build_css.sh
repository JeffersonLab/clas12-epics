#!/bin/bash
#
# Build CSS opi tree
#   - copy synApps opi files
#   - link our opi files
#
# Author: Wesley Moore (wmoore@jlab.org)
# Date:   Aug 2015
#

synapps=/usr/clas12/devel/R3.14.12.5/support
css_tree=./css

echo "[Setting up new CSS tree]"
rm -rf $css_tree

echo "Finding opi's in $synapps ..."
for app in `find $synapps/ -name "opi" -type d`
do
    appname=${app#$synapps/}    # strip synapps path
    app_ver=${appname%%/*}      # get app-ver, strip sub dirs
    appname=${appname%%-*}      # get appname, strip version
    
    opi_dir="$css_tree/synApps/$appname"
    rm -rf $opi_dir
    mkdir -p $opi_dir
    echo $app_ver >> $opi_dir/VERSION   # store version info
    
    echo "  $app_ver > $opi_dir"
    if [[ $app == *"asyn"* ]]
    then
        cp -r $app/boy/* $opi_dir/
    else
        cp -r $app/* $opi_dir/
    fi
done

# Fix devIocStats opi color names (synApps 5-7, 5-8)
echo "Fixing devIocStats color names (undefined rgb values)..."
cd $css_tree/synApps/devIocStats
sed -i 's/Gray_3\"/Gray_3\" red=\"200\" green=\"200\" blue=\"200\"/g' *
sed -i 's/Gray_4\"/Gray_4\" red=\"187\" green=\"187\" blue=\"187\"/g' *
sed -i 's/Gray_5\"/Gray_5\" red=\"174\" green=\"174\" blue=\"174\"/g' *
sed -i 's/Gray_6\"/Gray_6\" red=\"158\" green=\"158\" blue=\"158\"/g' *
sed -i 's/Gray_7\"/Gray_7\" red=\"145\" green=\"145\" blue=\"145\"/g' *
sed -i 's/Gray_9\"/Gray_9\" red=\"120\" green=\"120\" blue=\"120\"/g' *
sed -i 's/Gray_14\"/Gray_14\" red=\"0\" green=\"0\" blue=\"0\"/g' *
cd ../../../

cwd=`pwd`
echo "Finding opi's in $cwd ..."
for app in `find $cwd -name "opi" -type d`
do
    appname=${app#$cwd/}          # strip synapps path
    app_ver=${appname%%/*}        # get app-ver, strip sub dirs
    appname=${appname%%App*}      # get appname, strip version
    
    opi_dir="$css_tree/$appname"
    rm -rf $opi_dir
    mkdir -p $opi_dir
    
    echo "  $app_ver > $opi_dir"
    ln -s $app/* $opi_dir/        # link files not dirs for easier navigation
done

