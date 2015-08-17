#!/usr/bin/python2.6

import sys, string
import lxml.etree

import plcData

from plcElement import  plcElementXML 
from plcModule import plcModule
from plcTag import plcTag

#===============================================================================
# Class to handle PLC Controller XML Element in RSLogix5000 XML file
# This will be the top oblect that will doughter the rest of the objects.
#===============================================================================
class plcController( plcElementXML ):
    """Class to handle Controller CML elements from RSLogix5000 XML file"""

    # Constructor    
    def __init__( self, rootElement, searchRoot=None ):
        plcElementXML.__init__( self, rootElement )
        self.tags = []
        self.modules = []
        self.programs = []
        self.daughters.append( self.tags )
        self.daughters.append( self.modules )
        self.daughters.append( self.programs )
        self.processorType = ""
        self.nFailedAliases = 0
            
        # This static variable should not change while the controller tree is being built            
        plcElementXML.treeSeacrh.rootObject = self      # Set the static variable

        if( searchRoot != None ) :
            # If searching tree is specified, then set it to what was sepcified
            plcElementXML.treeSeacrh.rootObject = searchRoot
            
        plcElementXML.treeSeacrh.nFailed = 0                    # Number of failed searches is zero now 
       
        # Get the processor type attribute
        if( "ProcessorType" in self.root.attrib.keys() ):
            self.processorType = self.root.attrib["ProcessorType"]
        
        # Get all the modules
        moduleElements = self.root.xpath("Modules/Module")
        for moduleElm in moduleElements:
            newModule = plcModule( moduleElm, self )
            self.modules.append( newModule )

        # Get all the programs
        programElements = self.root.xpath("Programs/Program")        
        for programElm in programElements:
            newProgram = plcProgram( programElm, self  )
            self.programs.append( newProgram )
            
        # Get all controller scoped tags
        tagElms = self.root.xpath( "Tags/Tag")        
        for tagElm in tagElms:
            newTag = plcTag( tagElm, self  )
            self.tags.append( newTag )

        self.nFailedAliases = plcElementXML.treeSeacrh.nFailed
        print "Number of failed searches is ", plcElementXML.treeSeacrh.nFailed

        return
    
    # Recursively return scalar elements in a single list 
    def getScalarsList4EPICS(self):
        retList = []
        # Add its own scalar if exists
        if( self.scalar != None ):
            retList.extend( [self.scalar] )      # Append in form of single list elelemnt 
        # Go down the tree and add scalars of the daughter elements
        for daughter in self.tags, self.programs:
            for elem in daughter:
                if( elem != None ):
                    retList.extend( elem.getScalarsList() ) 
        return retList
                    
    # Recursively return array elements in a single list 
    def getArraysList4EPICS(self):
        retList = []
        # Add its own array if exists
        if( self.array != None ):
            retList.extend( [self.array] )      # Append in form of single list elelemnt 
        # Go down the tree and add arrays of the daughter elements
        for daughter in self.tags, self.programs:
            for elem in daughter:
                if( elem != None ):
                    retList.extend( elem.getArraysList() ) 
        return retList
    

    def __repr__(self):            
        retString = self.name + ", Processor " + self.processorType + "\n"
        for module in self.modules:
            retString += "Module: " + repr(module) + "\n"
        for program in self.programs:
            retString += "Program: " + repr(program) + "\n"           
        for tag in self.tags:
            retString += "Program: " + repr(tag) + "\n"        
        return retString
                            
    def __str__(self):
        retString = self.name + ", Processor " + self.processorType + "\n"
        for module in self.modules:
            retString += "Module: " + str(module) + "\n"
        for program in self.programs:
            retString += "Program: " + str(program) + "\n"   
        retString += "Controller Scope: \n"     
        for tag in self.tags:
            retString += str(tag) + "\n"        
           
        return  retString


class plcProgram( plcElementXML ):
    """ Class to handle Program elements in the RSLogix5000 XML file """
    
    # This is the character that separates the program name from the tag-names within the program
    programSeparator = "."
    
    def __init__(self, rootElement, parentObject=None, forcedName=None ):
        plcElementXML.__init__( self, rootElement, parentObject, forcedName )
        self.disabled = "true"
        self.mainRoutineName = ""
        self.tags = []
        self.daughters.append(self.tags)
        
        # The prefix that gets added to program-scoped PLC tags in RSLogix5000 is "Program:" 
        self.prefix = "Program:" + self.name
        self.addNameToPath( self.prefix )
        
        # Check if this program is claimed to be disabled in the XML file, and skip its tags if it is
        if ( "Disabled" in self.root.attrib.keys() ):
            self.disabled = self.root.attrib["Disabled"]
            if( self.disabled == "true" ):
                print "Program <{0}> is disabled, skipping its tags".format( self.name )
        
        if( "MainRoutineName" in self.root.attrib.keys() ):
            self.mainRoutineName  =   self.root.attrib["MainRoutineName"]
        
        # Find all the Tag XML elements in the XML file and build the corresponding objects for them
        tagElms = self.root.xpath( "Tags/Tag")        
        for tagElm in tagElms:
            newTag = plcTag( tagElm, self  )
            self.tags.append( newTag )
        
        return
    
    # Override the path appending method of the plcElementXLM method 
    # since the program separator is a column
    def addNameToPath( self, newName ):
        self.path += newName + self.programSeparator
        return
    
    
    def __repr__(self):            
        retString = self.name + ", MainRoutineName " + self.mainRoutineName + "\n"
        for tag in self.tags:
            retString += "    Tag: " + repr(tag) 
        return retString
                            
    def __str__(self):
        retString = self.name + ", MainRoutineName " + self.mainRoutineName + "\n"
        for tag in self.tags:
            retString += "    Tag: " + str(tag) 
        return  retString
    
    
##===============================================================================
## This is the main execution block
##===============================================================================
#
##xmlFileName = '/group/halld/Online/controls/epics/R3-14-12-2/app/solenoidApp/Db/Hall_D_Version4.L5X'
#xmlFileName = '/group/halld/Online/controls/epics/R3-14-12-2/app/solenoidApp/Db/TagExportTest.L5X'
##xmlFileName = '/group/halld/Online/controls/epics/R3-14-12-2/app/solenoidApp/Db/cPID_vs_PIDE.L5X'
##xmlFileName = '/group/halld/Online/controls/epics/R3-14-12-2/app/solenoidApp/Db/Hall_D_Version4_withFakeAliases.L5X'
#
#
#tree = lxml.etree.parse(xmlFileName)
#root = tree.getroot()      
#
#print "Starting to pars"
#
#controllerElms = tree.xpath( "//Controller" )
#
#print "Parsing complete"
#
#if( len(controllerElms) != 1 ):
#    print "There should be one Controller element in the XML file, found ", len(  controllerElms )
#    print "Exiting..."
#    sys.exit(-1)
#    
#print controllerElms[0].attrib
#print controllerElms[0].tag
#
#nIter = 0
#newCtrler = plcController( controllerElms[0]  )
##plcElementXML.treeSeacrh.rootObject = newCtrler
##matches = plcElementXML.elementSearch.search( "FakeUDT_1.FakeyBOOL." )
##print "Here are matches: ", matches 
#while( newCtrler.nFailedAliases > 0 ):
#    dummy = raw_input( "Iteration number {0} had {1} unresolved aliases, need anoter iteration. Hit return".format( nIter, newCtrler.nFailedAliases ) )
#    oldCtrler = newCtrler
#    newCtrler = plcController( controllerElms[0], oldCtrler )
#    nIter += 1
#   
#     
##print "Catalog complete. Printing..."
##print "Controller: " + str( newCtrler )

        