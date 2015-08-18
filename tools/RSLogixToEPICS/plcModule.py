#!/usr/bin/env python

import lxml.etree
import string
import sys

import plcData
from plcElement import plcElementXML
import plcTag


#===============================================================================
# Class to handle PLC ports for modules in RSLogix5000
#===============================================================================
class plcPort( plcElementXML ):
        """Class to handle PLC ports in RSLogix5000"""

        # Port types that are considered to be controlled from upstream
        # This is used for tag naming for module tags
#        controlledTypes = [ "ICP", "PointIO", "Compact" ]
        controlledTypes = [ "ICP", "PointIO", "Compact" ]

        # Constructor 
        def __init__( self, rootElement, parentObj ) :
            plcElementXML.__init__(self, rootElement, parentObj )            
            self.id = rootElement.attrib["Id"]
            self.address = ""
            self.type = ""
            self.upstream = ""
            
            if( "Id" in self.root.attrib.keys() ):
                self.Id = rootElement.attrib["Id"]
            else :
                print "Port in module <{0}> does not have Id. Exiting...".format(self.parentObj)
                sys.exit(-1)

            # Get the port attributes and return                
            if( "Address" in self.root.attrib.keys() ):
                self.address = rootElement.attrib["Address"]
            if( "Type" in self.root.attrib.keys() ):
                self.type = rootElement.attrib["Type"]               
            if( "Upstream" in self.root.attrib.keys() ):
                self.upstream = rootElement.attrib["Upstream"]                             
            return 
    
    
        def __repr__(self):
            return "ID - {0}, Address -  {1}, Type - {2}, Upstream - {3}".format( 
                                            self.id, self.address, self.type, self.upstream)
           
        def __str__(self):
            return "ID - {0}, Address -  {1}, Type - {2}, Upstream - {3}".format( 
                                            self.id, self.address, self.type, self.upstream)



#===============================================================================
# Clas to deal with the A-B PLC modules in XML
#===============================================================================
class plcModule( plcElementXML ):
    """Allen-Bradley PLC Module Class"""
    nUnNamed = 0
        
    # Constructor. Takes the root element and find all that is needed for this module
    def __init__(self, rootElement, parentObj=None ):
        plcElementXML.__init__(self, rootElement, parentObj )            
        self.confTags = []
        self.inTags = []
        self.outTags = []
        self.ports = []

        self.daughters.append(self.inTags)
        self.daughters.append(self.outTags)
        self.daughters.append(self.confTags)
        
        if( self.name == "" ):
            self.name = "UnNamedModule" + str(plcModule.nUnNamed)
            plcModule.nUnNamed += 1                         

        if( "ParentModule" not in self.root.attrib.keys() ):
            print "Module <{0}> does not have ParentModule XML attribute".format( self.name )
            sys.exit(-1)
        self.parentModuleName = self.root.attrib["ParentModule"]
        
        if( "ParentModPortId" not in self.root.attrib.keys() ):
            print "Module <{0}> does not have ParentModPortId XML attribute".format( self.name )
            sys.exit(-1)
        self.parentModulePortID = self.root.attrib["ParentModPortId"]
           
#        print "Creating Module named ", self.name, " type ", self.root.attrib["CatalogNumber"]
 
        # Get all the ports that have PointIO, Ethernet and ICP interfaces              
        self.portElms = self.root.xpath("Ports/Port[@Type='PointIO' or @Type='ICP' or @Type='Ethernet' or @Type='Compact']")
        for portElm in self.portElms:
#            print "Port: ", portElm.attrib
            newPort = plcPort( portElm, self )
            self.ports.append( newPort )
                
        subTagName = None                
#        if( self.parentModuleName != "Local" ):
        if( True ):
            moduleIsControlled = False
            # Loopo over all the ports to see if the module tags will be called by its name or parents name
            # At this point we will go only one lever up, that is the module tags cannot be named after their grandparents. 
            # It is either their name with address 0 or the parents name with the address of the corresponding port. 
            portAddress = None
            for port in self.ports: 
                if( port.upstream == "true" and port.type in plcPort.controlledTypes ):
                    # Apparently this means that this module is controlled from upstream
                    # Declare the module to be controlled by the parent and break out of the loop    
                    moduleIsControlled = True
                    portAddress = port.address
                    break
            if( moduleIsControlled ):                         
#                subTagName = self.parentModuleName + ":" + self.parentModulePortID + ":"
                subTagName = self.parentModuleName + ":" + portAddress + ":"
            else :
#                subTagName = self.name + ":0:"                       
                subTagName = self.name + ":"                       
        else :
            subTagName = self.name+ ":0:"               
                
#        print "SubTageName is ", subTagName
                        
        # Get all configuration tags for the module    
        self.confTagElms = self.root.xpath("Communications/ConfigTag[@ExternalAccess='Read/Write']")
        for tagElm in self.confTagElms :
#            print "Tag: ", tagElm.attrib 
            newTag = plcTag.plcTag(tagElm, self, subTagName+"C" )
            self.confTags.append(newTag)  
                    
        # Get all input tags for the module    
        self.inTagElms = self.root.xpath("Communications/Connections/Connection/InputTag[@ExternalAccess='Read/Write']")
        for tagElm in self.inTagElms :
#            print "Tag: ", tagElm.attrib 
            newTag = plcTag.plcTag(tagElm, self, subTagName+"I" )
            self.inTags.append(newTag)  

        # Get all output tags for the module    
        self.outTagElms = self.root.xpath("Communications/Connections/Connection/OutputTag[@ExternalAccess='Read/Write']")
        for tagElm in self.outTagElms :
#            print "Tag: ", tagElm.attrib 
            newTag = plcTag.plcTag(tagElm, self, subTagName+"O" )
            self.outTags.append(newTag)  
        return
    

    def __repr__(self):            
        retString = self.name + "\n"
        for port in self.ports:
            retString += "    Port: " + repr(port) + "\n"
        for tag in self.confTags:
            retString += "    Conf Tag: " + repr(tag) + "\n"
        for tag in self.inTags:
            retString += "    Input Tag: " + repr(tag) + "\n"
        for tag in self.outTags:
            retString += "    Output Tag: " + repr(tag) + "\n"                
        return retString
                            
    def __str__(self):
        retString = self.name + "\n"
        for port in self.ports:
            retString += "    Port: " + str(port) + "\n"
        for tag in self.confTags:
            retString += "    Conf Tag: " + str(tag) + "\n"
        for tag in self.inTags:
            retString += "    Input Tag: " + str(tag) + "\n"             
        for tag in self.outTags:
            retString += "    Output Tag: " + str(tag) + "\n"                             
        return  retString
            
        

