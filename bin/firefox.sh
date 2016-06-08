#!/bin/sh

aa=`hostname`

exec /usr/bin/firefox -P ${aa%%.*} $@

