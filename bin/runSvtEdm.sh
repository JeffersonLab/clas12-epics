#!/bin/sh
if ! [ "$USER" = "clasrun" ]
then
  echo Enter clasrun password:
  su clasrun -c 'ssh hbops@hlbl00 -t ssh svtl01 -t users/baltzell/svt/edmSvtRun'
else
  ssh hbops@hlbl00 -t ssh svtl01 -t users/baltzell/svt/edmSvtRun
fi

