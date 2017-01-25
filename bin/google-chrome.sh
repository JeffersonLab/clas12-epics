#!/bin/sh

aa=`hostname`

exec /usr/bin/google-chrome --proxy-auto-detect --user-data-dir=$HOME/.config/google-chrome-$aa $@ &

