#!/bin/sh

aa=`hostname`

exec /usr/bin/google-chrome --user-data-dir=$HOME/.config/google-chrome-$aa $@ &

