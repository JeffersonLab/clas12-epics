importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var status = PVUtil.getString(pvs[0]);

java.lang.System.err.println("mpodstatus:  "+pvs[0]+"   a"+status+"a");

if (status == "00 ") {
    widget.setPropertyValue("text","OFF");
}
else {
    widget.setPropertyValue("text",status);
}

