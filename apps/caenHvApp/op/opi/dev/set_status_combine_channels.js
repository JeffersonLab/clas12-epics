importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var type = widget.getMacroValue("TYPE");

//java.lang.System.out.println(String(type));

var p = new Array(24);
for (var ii=0; ii<24; ii++)
{
    p[ii] = PVUtil.getDouble(pvs[0]) | 0;
}


var color="OK";

if (type == "1527" || type == "4527")
{
    for (ii=0; ii<24; ii++)
    {
        if (p[ii] == 1)
        {
          color = "STOP";
          break;
        }
        else if (p[ii] == 2)
        {
          color = "Attention";
          break;
        }
        else if (p[ii] == 3)
        {
          color == "Off";
          break;
        }
    }

    widget.setPropertyValue("off_color",color);

}
