## Example vxWorks startup file

## The following is needed if your board support package doesn't at boot time
## automatically cd to the directory containing its startup script
cd "/home/wmoore/workspaces/clas12-import-dev/apps/iocBoot/iocscalerTest"

############################################################################
< cdCommands
############################################################################
< ../nfsCommands
############################################################################
cd topbin
ld < scaler.munch
cd startup

iocsh "st.cmd.iocsh"

