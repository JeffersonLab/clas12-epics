#!/bin/sh

aa=`hostname`

exec firefox -P ${aa%%.*} $@

