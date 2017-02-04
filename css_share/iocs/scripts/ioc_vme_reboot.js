importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

iocName=widget.getMacroValue("ioc");

// get rid of the "ioc" prefix, if it exists:
host=iocName
if (host.startsWith("ioc")) host=iocName.slice(3)

if (GUIUtil.openConfirmDialog("Really Reboot "+iocName+" ?"))
{
  cmd = "ssh clasrun@clon10 remote_reboot.tcl "+host;
  ScriptUtil.executeSystemCommand(cmd,0);
}

