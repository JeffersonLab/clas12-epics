# Author Ken Livingston 1st June 2017

# This script if for the sh like shells, see thisreeper.csh for csh like shells.

# source this script to set up reeper eg.
# source "${EPICS_EXTENSIONS}/reeper/thisreeper.sh"
 
# Or set the env variable and path yourself- Eg.
# export REEPER "${EPICS_EXTENSIONS}/reeper"
# export PATH "${REEPER}:${PATH}"

thisdir=`dirname ${BASH_SOURCE[0]}`
export REEPER="$thisdir"
export PATH="${REEPER}:${PATH}"
