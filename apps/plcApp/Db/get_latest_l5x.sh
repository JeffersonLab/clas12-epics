#!/bin/bash

git clone https://github.com/jeffersonlab/clas12-plc
printf "=%.0s" $(seq 1 `tput cols`)
printf "Copying found L5X's...\n"
find clas12-plc -name "*L5X" -exec cp -v {} . \;
rm -rf clas12-plc

