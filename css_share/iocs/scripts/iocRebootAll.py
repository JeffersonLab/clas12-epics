from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ConsoleUtil, FileUtil
import os,sys
import subprocess
from java.lang import Thread, Runnable

# Reboot all IOC-es
# This script will execute the script in EPICS $APP directory for 
# rebooting IOC using the macro in the widget parent to specify the name of the IOC. 
# Therefore, the macro for the parent of the action button widget should match the name 
# of the IOC in the reboting script.  
class MyTask_iocRebootAction(Runnable):
	def run(self):

            appDirectory = os.getenv( "APP" )
            rebootScript = appDirectory + "/scripts/IOC/iocReboot.py"
            command = rebootScript + " all" #+ widget.getParent().getMacroValue( "ioc" ) 
#	    print "xxx ",command
            #ConsoleUtil.writeInfo( sys.argv[0] + "Will execute: " + command)
            process = subprocess.Popen([command, ], stdout=subprocess.PIPE, shell=True)
            (out, err) = process.communicate()
            #widget.setPropertyValue("text", out)

thread = Thread(MyTask_iocRebootAction())
thread.start()
