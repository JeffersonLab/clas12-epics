#!/bin/sh

for workspace in /tmp/CSS-Workspaces/*
do
    if ! [ -e $workspace ] 
    then
        continue
    fi

    lockfile=$workspace/.metadata/.lock

    if ! [ -r $lockfile ] || ! [ -w $lockfile ]
    then
        echo Insufficient Permissions for $workspace
    elif ! [ -e $lockfile ]
    then
        # no lock file, safe to delete:
        rm -rf $workspace
    else
        # if can get the lock, delete the workspace:
        flock -E 99 -n -x $lockfile echo

        echo "$?"
        continue

        if ! [ "$?" -eq "99" ]
        then
            echo Unlocked $workspace
            #exec 3>&-
            echo B rm -rf $workspace
        else
            echo Cannot unlock $workspace
        fi
    fi
done

