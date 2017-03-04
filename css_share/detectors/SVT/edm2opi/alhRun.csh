#! /bin/csh  -f
source /cs/accadm/fiefdom/cshrc.ops
alias ccd 'set ccdTool_appname=\!$ ; source $HBASE/bin/ccdSource'
#setenv EPICS_CA_ADDR_LIST "129.57.41.33 129.57.41.25 129.57.41.27 129.57.228.100"
setenv EPICS_CA_ADDR_LIST "129.57.231.255"
req csuedvl
ccd HallBSVTAlarms
cd dvl/output
#
#  start up a passive alh if a master is already running or you're not on svtl01
#  
# Note that this is a specal version of alh that is compiled against 3.14 
# so that it can handle long signal names.
#
set masterAlh=`ps -ef | grep SVT.alhC | grep -v "\-S" | wc -l`
#if( $masterAlh <= 1 && `hostname` == "svtl01") /cs/dvlhome/bin/alh -T SVT.alhConfig >&  /dev/null &
#if( $masterAlh > 1 || `hostname` != "svtl01" ) /cs/dvlhome/bin/alh -S SVT.alhConfig >&  /dev/null &
if( $masterAlh <= 1 && `hostname` == "svtl01") /cs/prohome/apps/a/alhEpics/1-2-34/bin/rhel-6-ia32/alh -T SVT.alhConfig >&  /dev/null &
if( $masterAlh > 1 || `hostname` != "svtl01" ) /cs/prohome/apps/a/alhEpics/1-2-34/bin/rhel-6-ia32/alh -S SVT.alhConfig >&  /dev/null &
# hope this works!
