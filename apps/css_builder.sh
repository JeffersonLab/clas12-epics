#!/bin/bash
#
# Build CS-Studio Share
#   - copy synApps opi files
#   - link our opi files
#
# Author: Wesley Moore (wmoore@jlab.org)
# Date:   Aug 2015
#

top_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

css_share_path=$top_dir/../css_share/apps

cols=`tput cols`

printheader() {
    printf "=%.0s" $(seq 1 $cols)
    printf "\n %-30s%s\n" "Module" "Share Location"
    printf "=%.0s" $(seq 1 $cols)
    printf "\n"
}

# parse out synApps path
RELEASEFILE=$top_dir/configure/RELEASE
if [ -f "$RELEASEFILE" ]
then
    EPICS_BASE=`grep EPICS_BASE= $RELEASEFILE | uniq`
    EPICS_BASE=${EPICS_BASE#EPICS_BASE=}
    SYNAPPS=`grep SYNAPPS= $RELEASEFILE`
    SYNAPPS=${SYNAPPS#SYNAPPS=}
    SYNAPPS=${SYNAPPS//\$(EPICS_BASE)/$EPICS_BASE}
    if [ $SYNAPPS == "" ]; then
	printf "Error: could not parse synApps path from $RELEASEFILE\n"
	exit
    fi
else
    printf "Error: $RELEASEFILE not found\n"
    exit
fi

printf "\nSetting up new CSS Share\n\n"
if [ -d $SYNAPPS ]; then
    printf "Finding opi's in %s\n" $SYNAPPS
    apps=`find $SYNAPPS/ -name "opi" -type d`
    printheader
    printf "Installing:\n"
    for app in $apps
    do
        appname=${app#$SYNAPPS/}    # strip synapps path
        app_ver=${appname%%/*}      # get app-ver, strip sub dirs
        appname=${appname%%-*}      # get appname, strip version
        
        opi_dir="$css_share_path/synApps/$appname"
        rm -rf $opi_dir
        mkdir -p $opi_dir
        echo $app_ver >> $opi_dir/VERSION           # store version info
        
        printf " %-30s%s\n" $app_ver $opi_dir
        if [[ $app == *"asyn"* ]]
        then
            cp -r $app/boy/* $opi_dir/
        else
            cp -r $app/* $opi_dir/ 2>/dev/null      # hide warning about empty dir
        fi
    done

    printf "\nFixing synApps dir/file permissions\n"
    find $css_share_path/synApps -type f -print0 | xargs -0 chmod 664
    find $css_share_path/synApps -type d -print0 | xargs -0 chmod 755

    # synApps 5-7, 5-8
    printf "Fixing devIocStats color names (contains undefined rgb values)\n"
    cd $css_share_path/synApps/devIocStats
    sed -i 's/Gray_3\"/Gray_3\" red=\"200\" green=\"200\" blue=\"200\"/g' *
    sed -i 's/Gray_4\"/Gray_4\" red=\"187\" green=\"187\" blue=\"187\"/g' *
    sed -i 's/Gray_5\"/Gray_5\" red=\"174\" green=\"174\" blue=\"174\"/g' *
    sed -i 's/Gray_6\"/Gray_6\" red=\"158\" green=\"158\" blue=\"158\"/g' *
    sed -i 's/Gray_7\"/Gray_7\" red=\"145\" green=\"145\" blue=\"145\"/g' *
    sed -i 's/Gray_9\"/Gray_9\" red=\"120\" green=\"120\" blue=\"120\"/g' *
    sed -i 's/Gray_14\"/Gray_14\" red=\"0\" green=\"0\" blue=\"0\"/g' *
    cd $top_dir
fi

printf "\nFinding opi's in %s\n" $top_dir
apps=`find $top_dir/*App -name "opi" -type d`
printheader
printf "Linking:\n"
for app in $apps
do
    appname=${app#$top_dir/}            # strip dir path
    appname=${appname%%/*}              # strip sub dirs
    
    opi_dir="$css_share_path/$appname"
    rm -rf $opi_dir
    
    printf " %-30s%s\n" $appname $opi_dir
    ln -s $app $opi_dir
done

printf "\nSummary\n"
printf "=%.0s" $(seq 1 $cols)
printf "\nInstalled %10d opis\n" `find $css_share_path/synApps/ -name "*.opi" | wc -l`
printf "Linked    %10d opis\n" `find $css_share_path/*App/ -name "*.opi" | wc -l`


#link any scripts in any of the op/scripts direcrories
echo
echo "Linking scripts into ../css_share/common_scripts/"
ln -sf ${top_dir}/*/op/scripts/* ../css_share/common/scripts/
