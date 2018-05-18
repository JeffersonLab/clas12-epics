# Author Ken Livingston 1st June 2017

# This script if for the csh like shells, see thisreeper.sh for bash like shells.

# source this script to set up reeper eg.
# source "${EPICS_EXTENSIONS}/reeper/thisreeper.sh"
 
# Or set the env variable and path yourself- Eg.
# setenv REEPER "${EPICS_EXTENSIONS}/reeper"
# setenv PATH "${REEPER}:${PATH}"

# donot use lsof, it hangs sometimes, probably in part because it prints
# every damn open file (53K lines on clonsl1 at the moment), which is a
# pretty damn ridiculous way to find the path of one file.  We certainly
# can't have this sourced from .setup, as it breaks ssh logins sometimes,
# which results in operations problems and pages at 3 in the morning.
#
#set LSOF=`env PATH=/usr/sbin:${PATH} which lsof`
#set thisfile="`${LSOF} -w +p $$ | grep -oE '/.*thisreeper.csh'  `"
#setenv REEPER `dirname $thisfile`
#setenv PATH "${REEPER}:${PATH}"
