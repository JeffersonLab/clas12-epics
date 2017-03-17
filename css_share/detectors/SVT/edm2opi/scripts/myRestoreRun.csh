#! /bin/csh  -f
source /cs/accadm/fiefdom/cshrc.ops
setenv EPICS_CA_ADDR_LIST "129.57.231.255"
#
#  run myRestore 
#  
echo "myRestore -ioc -R $1-t1h -D DEV "
myRestore -ioc -R $1 -t10m -D DEV
# hope this works!
