importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var istatus;
try { istatus = PVUtil.getDouble(pvs[0]) | 0; }
catch (ee) {}

var type = widget.getMacroValue("TYPE");

// copied this logic from hv_control Qt GUI code.

//java.lang.System.out.println("set_status.js");


if (type == "527")
{
	
	var statuses=["ON","RUP",  "RDN",  "OVC",  "UNV",  "OVV",  "ExTrip","MAXV", "    ", "Kill", "InTrip"];
	var bgcolors=["On","Minor","Minor","Major","Major","Major","Major", "Major","Major","Off","Major"];
	
	var theStatus=-1;
	var j10=-1
	
	var sstatus="OFF";
	
	for (var ii=15; ii>=5; ii--)
	{
	  j10++;
	  if (ii==7 || ii==6) continue;
	  if ((1<<ii) & istatus) 
	  {  
	    theStatus = ii;
	    sstatus = statuses[j10];
	  }
	}

//  if (pvs[0].getName()=="B_DET_DC_HV_SEC6_R2_SL3_S01-08.L")
//  {
//    java.lang.System.err.println("-- "+pvs[0].getName()+" = "+istatus);
//  }

	//java.lang.System.out.println("----- "+istatus+" "+theStatus+" "+sstatus);
	
	if ( ((1<<6)  & istatus)) { sstatus="Kill"; }
	if ( ((1<<13) & istatus)) { sstatus="RDN"; }
	if (!((1<<0)  & istatus)) { sstatus="COMMS"; }
	
//	widget.setPropertyValue("text",sstatus);
		
	if (sstatus == "OFF") { 
	  widget.setPropertyValue("background_color","Off");
	  widget.setPropertyValue("foreground_color","Header_Foreground");
    }
    else if (sstatus=="COMMS")
    {
        //widget.setPropertyValue("background_color","MEDM_COLOR_38");
        widget.setPropertyValue("background_color","Attention");
        widget.setPropertyValue("foreground_color","Header_Foreground");
    }
    else if (sstatus=="Kill")
    {
        widget.setPropertyValue("background_color","MEDM_COLOR_24");
        widget.setPropertyValue("foreground_color","Header_Foreground");
    }
    else if (sstatus=="RUP" || sstatus=="RDN")
    {
        widget.setPropertyValue("background_color","Minor");
        widget.setPropertyValue("foreground_color","Header_Foreground");
    }
    else
    {
        widget.setPropertyValue("foreground_color","Text_Foreground");
        if (sstatus == "ON") {
            widget.setPropertyValue("background_color","On");
        }
        else {
            widget.setPropertyValue("background_color","Major");
            if (theStatus>=0 && theStatus<bgcolors.size)
                widget.setPropertyValue("background_color",bgcolors[theStatus]);
        }
    }
}


else if (type == "1527" || type == "4527")
{	
	var istatus2;
	try { istatus2 = PVUtil.getDouble(pvs[1]); }
	catch (ee) {}
		
	if (istatus2==0 && istatus>=0)
	{
		var statuses=["ON","RUP",  "RDN",  "OVC",  "OVV",  "UNV",  "ExTrip","MAXV", "ExDis",       "InTrip","CalEr","ChUn"];
		var bgcolors=["On","Minor","Minor","Major","Major","Major","Major", "Major","Disconnected","Major","Major","Disconnected"];
		
		var theStatus=-1;
		
		for (var ii=0; ii<12; ii++)
		{
		  if ((1<<ii) & istatus)
		  {
		    theStatus=ii;
		  } 
		}
		if (istatus == 0) { 
		  widget.setPropertyValue("background_color","Off");
		  widget.setPropertyValue("foreground_color","Header_Foreground");
		}
		else
		{
		  widget.setPropertyValue("foreground_color","Text_Foreground");
		  widget.setPropertyValue("background_color",bgcolors[theStatus]);		  
		}
     }
     else
     {
//       widget.setPropertyValue("text","COMMS");
       widget.setPropertyValue("background_color","Major");
       widget.setPropertyValue("foreground_color","Text_Foreground");   
     }

}

