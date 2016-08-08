importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

iocName=widget.getMacroValue("ioc");

response=GUIUtil.openConfirmDialog("Really Reboot "+iocName+" ?");

if (response==1)
{
  xtermTitle="IOC-REBOOT___________"+iocName
  cmd = "xterm -bg red -fg white -g 72x15 -T \'"+xtermTitle+"\'";
  cmd += " -e softioc_console -R "+iocName;
  
  ScriptUtil.executeSystemCommand(cmd,0);
}
