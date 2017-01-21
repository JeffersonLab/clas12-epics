#!/bin/sh
root=$1
inputFile=$2
/usr/clas12/css/dev/linux-x86_64/bin/AlarmConfigTool \
  -root $root -alh \
  -file $inputFile \
  -data /dev/null

