#!/bin/bash
#
# testbuild.sh
# 
# Test build system for HPS EPICS.  On success, things will be fully compiled, 
# but no tools installed.
# 
# Options:
#   -e: test environmental variables only
# 
# Returns:
# 0=success
# 1=failure
# 
# Author: Wesley Moore (wmoore@jlab.org)
# Date:   Nov 2014
# 

RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
NORMAL=$(tput sgr0)
col=$(tput cols)

# $1 - 0=passed, 1=failed
# $2 - test name
passFail ()
{
  	len=${#2}
  	spc=$(expr $col - $len - 3)

	# Cleanup formatting if we are printing a long line.
	if [ $len -ge $(expr $col - 8) ] ; then
		CR="\n"
		spc=$(expr $col - 3)
	else
		CR=""
	fi

  	if [ $1 = 0 ]; then
		printf "%s${CR}%*s%s" "$2" $spc "$GREEN" "[passed]" "$NORMAL"
 	else
		printf "%s${CR}%*s%s" "$2" $spc "$RED" "[failed]" "$NORMAL"
  	fi
  	printf '\n'
  	return 0
}

printBreak ()
{
  	eval printf -- '-%.s' {1..$col} ; echo
}

printEnvErr ()
{
	printBreak
	echo "Use .setup-hps to setup the environmental variables (source .setup-hps)."
}

########################################
# MAIN
########################################
ENV_ONLY=0
ENV_ERR=0

while getopts "e" opt; do
  case $opt in
	e)
		ENV_ONLY=1
		;;
	*)
		echo "Invalid option: -$OPTARG" >&2
		;;
  esac
done

declare -a vars=("CLAS" "EPICS_BASE" "EPICS_HOST_ARCH" "EPICSB_DRIVERS")
printf "Testing environment variables:\n"
for var in "${vars[@]}"; do
  	if [ -n "${!var}" ]; then
  		passFail 0 "  $var=`printenv $var`"
  	else
  		passFail 1 "  $var not set"
  		ENV_ERR=1
  	fi
done

EPICS_LIBS="$EPICS_BASE/lib/$EPICS_HOST_ARCH"
if [ -n $LD_LIBRARY_PATH ]; then
	if [[ $LD_LIBRARY_PATH == *$EPICS_LIBS* ]]; then 
		passFail 0 "  LD_LIBRARY_PATH contains $EPICS_LIBS"
	else
		passFail 1 "  LD_LIBRARY_PATH does not contain $EPICS_LIBS"
		ENV_ERR=1
	fi
fi

if [ $ENV_ERR -eq 1 ]; then
	printEnvErr
  	exit 1
fi

if [ $ENV_ONLY -eq 1 ]; then # We're done
	exit 0
fi

# Since env is good, build all targets for testing.
declare -a targets=("make distclean" "make rebuild" "make clean-tools" "make tools")

printf "\nBuilding targets:\n"
for target in "${targets[@]}"; do
  	printf '%s\n' "  $target"
done

for target in "${targets[@]}"; do
  	printBreak
  	sleep 5
  	$target
	result=$? 
  	printBreak
  	if [ $result -eq 0 ]; then
		passFail 0 "$target"
  	else 
		passFail 1 "$target"
    	exit 1
  	fi
done

printBreak
printf "Run 'make install-tools' as needed\n"
printBreak

exit 0
