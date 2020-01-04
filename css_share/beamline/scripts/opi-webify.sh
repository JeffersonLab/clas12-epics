#!/bin/bash
for x in $@
do
  sed -i 's/<fontdata fontName.*\/>/<opifont.name fontName="Sans" height="8" style="0">Fine Print<\/opifont.name>/' $x
  sed -i 's/<opifont\.name.*opifont\.name>/<opifont.name fontName="Sans" height="8" style="0">Fine Print<\/opifont.name>/' $x
done

