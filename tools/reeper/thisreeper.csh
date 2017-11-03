# Author Ken Livingston 1st June 2017

# This script if for the csh like shells, see thisreeper.sh for bash like shells.

# source this script to set up reeper eg.
# source "${EPICS_EXTENSIONS}/reeper/thisreeper.sh"
 
# Or set the env variable and path yourself- Eg.
# setenv REEPER "${EPICS_EXTENSIONS}/reeper"
# setenv PATH "${REEPER}:${PATH}"


set LSOF=`env PATH=/usr/sbin:${PATH} which lsof`
set thisfile="`${LSOF} -w +p $$ | grep -oE '/.*thisreeper.csh'  `"
setenv REEPER `dirname $thisfile`
setenv PATH "${REEPER}:${PATH}"
