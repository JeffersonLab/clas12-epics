from java.lang import Thread, Runnable
from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ConsoleUtil, FileUtil
import os,sys

# Connect to the console of the IOC specified by the LABEL of the action menu widget
# This script will execute the script in EPICS $APP directory for 
# connecting to the IOC using the macro in the widget parent to specify the name of the IOC. 
# Therefore, the macro for the parent of the action button widget should match the name 
# of the IOC in the reboting script.  

class consoleTask(Runnable):
    def __init__(self, wid ) :
	self.widget = wid
	return

    def run(self):
        try:
            appDirectory = os.getenv( "APP" )
            consoleScript = appDirectory + "/scripts/IOC/iocConsole.py"

            command = consoleScript + " " + self.widget.getParent().getMacroValue( "ioc" ) 

#ConsoleUtil.writeInfo( "Will execute " + "<" + command + ">" )
            os.system( command )
        except Exception, e:
            ConsoleUtil.writeInfo( "There was a problem : " + str(e) )
            raise e    
        return

consoleTask = consoleTask( widget )
thread = Thread( consoleTask )
thread.start()

