#
# File: .setup.sh
#
# EPICS Environment
#

export CLAS=/usr/clas12/release/pro
export EPICS=${CLAS}/epics
export ROOTSYS=/apps/root/5.34.21

## Overrides for RHEL5/6, only solves base (ex. caget, caput, etc)
REDHATFILE=/etc/redhat-release
EPICS_VER=R3.14.12.5
RHEL_VER=
if [ -e "$REDHATFILE" ]
then
  rhel_vers=`awk '{print substr($7,0,1)}' $REDHATFILE`
  cent_vers=`awk '{print substr($3,0,1)}' $REDHATFILE`
  if [ "$rhel_vers" == "5" ]
  then
    EPICS_VER=R3.14.12.3
    RHEL_VER="_RHEL5"
  elif [ "$cent_vers" == "5" ]
  then
    EPICS_VER=R3.14.12.3
    RHEL_VER="_RHEL5"
  elif [ "$rhel_vers" == "6" ]
  then
    EPICS_VER=R3.14.12.5
    RHEL_VER="_RHEL6"
  else
    EPICS_VER=R3.14.12.5
    RHEL_VER=""
  fi
fi

export EPICS_VER
export EPICS_BASE=/usr/clas12/${EPICS_VER}/base${RHEL_VER}
export EPICS_EXTENSIONS=/usr/clas12/${EPICS_VER}/extensions${RHEL_VER}

# set EPICS host architecture
export OSTYPE=`uname`
export MACHINE=`uname -m`
EPICS_HOST_ARCH=linux-x86_64
if [ "$OSTYPE" == "Linux" ]
then 
  if [ "$MACHINE" == "i686" ] || [ "$MACHINE" == "x86" ]
  then
    EPICS_HOST_ARCH=linux-x86
  fi
fi

if ! [ -d "$ROOTSYS" ]
then
  source /apps/root/5.34.21/bin/thisroot.sh
fi

export EPICS_HOST_ARCH
export EPICS_SCRIPTS=${EPICS}/apps/scripts
export EPICS_CA_AUTO_ADDR_LIST=no
export EPICS_CA_ADDR_LIST="129.57.255.12 129.57.163.255 129.57.231.255"

export PERL5LIB=${PERL5LIB}:/usr/clas12/third-party-libs/Pezca-1.3/lib/perl5/x86_64-linux-thread-multi

PYTHONPATH=${PYTHONPATH}:${EPICS_SCRIPTS}
PYTHONPATH=${PYTHONPATH}:${EPICS}/css_share/common/scripts
PYTHONPATH=${PYTHONPATH}:/usr/clas12/third-party-libs/pyepics-RHEL7
PYTHONPATH=${PYTHONPATH}:${ROOTSYS}/lib
export PYTHONPATH

LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${ROOTSYS}/lib
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/clas12/third-party-libs/net-snmp-5.8.dev/x86_64/lib
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${EPICS_BASE}/lib/${EPICS_HOST_ARCH}
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${EPICS_EXTENSIONS}/lib/${EPICS_HOST_ARCH}
export LD_LIBRARY_PATH

PATH=${PATH}:${ROOTSYS}/bin
PATH=${PATH}:${EPICS_BASE}/bin/${EPICS_HOST_ARCH}
PATH=${PATH}:${EPICS_EXTENSIONS}/bin/${EPICS_HOST_ARCH}
PATH=${PATH}:${EPICS_BIN}
PATH=${PATH}:/usr/clas12/css/pro/${EPICS_HOST_ARCH}/bin
PATH=${PATH}:/usr/csite/certified/bin
PATH=${PATH}:${EPICS_SCRIPTS}
export PATH


export MIBDIRS=/usr/clas12/R${EPICS_VER}/modules/snmp-nscl-1-0-RC9/mibs:/usr/share/snmp/mibs:/usr/local/share/snmp/mibs
export MIBS=ALL

