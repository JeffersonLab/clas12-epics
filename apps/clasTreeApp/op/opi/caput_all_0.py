from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil

nodefull = PVUtil.getString(pvArray[0])      #Full name of the node Eg. B_SYS_HV_ECAL_SEC1
bgcol    = widget.getMacroValue("BGCOL")     #BG color for button

#Write this command as the tooltip, to make it available as a macro for the action (a fudge suggested in the CSS/Boy forum)
widget.setPropertyValue("tooltip",nodefull)
widget.setPropertyValue("background_color",bgcol)
