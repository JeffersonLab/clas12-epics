importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

switch (PVUtil.getDouble(pvs[0])) {
    case 0:
	    widget.setPropertyValue("background_color","Off");
	    widget.setPropertyValue("background_color","Off");
        break;
    case 1:
	    widget.setPropertyValue("background_color","On");
	    widget.setPropertyValue("background_color","On");
        break;
    case 2:
    case 3:
        widget.setPropertyValue("background_color","Minor");
        widget.setPropertyValue("foreground_color","Minor");
        break;
    case 4:
    case 5:
    case 6:
    case 7:
    case 8:
    case 9:
    case 10:
	  	widget.setPropertyValue("background_color","Major");
  	  	widget.setPropertyValue("background_color","Major");
        break;
    default:
        widget.setPropertyValue("background_color","Warning");
        widget.setPropertyValue("foreground_color","Warning");
        break;
}

