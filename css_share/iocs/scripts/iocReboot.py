from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ConsoleUtil, FileUtil
import os,sys

# Reboot the IOC specified by the LABEL of the action menu widget
# This script will execute the script in EPICS $APP directory for 
# rebooting IOC using the macro ni the widget parent to specify the name of the IOC. 
# Therefore, the macro for the parent of the action button widget should match the name 
# of the IOC in the reboting script.  
appDirectory = os.getenv( "APP" )
rebootScript = appDirectory + "/scripts/IOC/iocReboot.py"

#command = rebootScript + " " + "'" + widget.getParent().getMacroValue( "ioc" ) + "'"
command = rebootScript + " " + widget.getParent().getMacroValue( "ioc" ) 

#ConsoleUtil.writeInfo( "Will execute " + "<" + command + ">" )
os.system( command )
