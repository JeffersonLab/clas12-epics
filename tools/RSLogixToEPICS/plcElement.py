import sys
import lxml.etree
import re

import clfOptions

class UselessDataType( Exception ):
    def __init__(self, value="Useless DataType"):
        self.val = value
        
    def __str__(self):
        return repr( self.val )


class plcElementXML:
    """ Base class for XML element for PLC program parsing"""
    #===========================================================================
    # Class for searching the object tree based on the path
    #===========================================================================
    class treeSeacrh:
        rootObject = None                   # This is the root object on the tree where the search sohuld start  
        nFailed = 0                         # Number of failed searches
        def search(self, searchPaths):       # This is the function that looks for the object with the path equal to "searchName" argument            
            # Go through over all children lists 
            returnList = []
            if( plcElementXML.treeSeacrh.rootObject != None ):
#                print "Searching for tag <{0}> in root object {1}".format( searchPaths, plcElementXML.treeSeacrh.rootObject.name )
                for childList in plcElementXML.treeSeacrh.rootObject.daughters:  
                    # Loop over all children  in the current list 
                    for elem in childList:
                        for path in searchPaths:
                            matchedElement = elem.matchPath( path ) 
                            if( matchedElement != None ):
#                                print "Found match <{0}> at <{1}>".format( matchedElement.name, matchedElement.path )
                                returnList.append( matchedElement )   # Add the matched element to the list to be returned                            
#                        if( elem.name == searchName ):
#                            returnList.append( elem )   # Add the matched element to the list to be returned
#                print returnList, " : ", len( returnList )
                if( len( returnList ) == 0 ):
                    plcElementXML.treeSeacrh.nFailed  += 1 
            return returnList
    
    # Define a static object for tree searches                   
    elementSearch = treeSeacrh()  
    
    # Thsi is the character that separates the elements of the structures in RSLogix5000
    elementSeparator = "."
    
    # DataType-s that are not needed in EPICS
    uselessDataTypes = []    
    if( clfOptions.globOptions.getOption( "IgnoreRSLogixDataType" ) != None ):
        uselessDataTypes.extend( clfOptions.globOptions.getOption( "IgnoreRSLogixDataType" ) ) # Get them from config file options   
#    uselessDataTypes = clfOptions.globOptions.getOption( "IgnoreRSLogixDataType" )
    
    # Patterns of DataTypes that are not needed in EPICS 
    uselessDataTypePatterns = []
    if( clfOptions.globOptions.getOption( "IgnoreRSLogixDataTypePattern" ) != None ):
        uselessDataTypePatterns.extend( clfOptions.globOptions.getOption( "IgnoreRSLogixDataTypePattern" ) )
#    uselessDataTypePatterns = [ "^FBD_.*$" ]
    
    # Constructor 
    def __init__(self, rootElement, parentObj=None, forcedName=None ) :
        self.root = rootElement                 # Root XML element for this data, that is where its xML tag is
        self.parent = parentObj                 # Parent object for this object (not in the XML tree)
        self.name = ""                          # Name of this instance
        self.path = ""                          # This is how the RSLogix5000 refers this tag 
        self.regex = "^$"                       # This is the regular expression which can be used when searching for targets in aliases
        self.daughters = []                     # Contains information who the daughter lists are (next level down)
        self.elementTag = self.root.tag         # The name of the XML tag that this object is created for
        self.dataType = ""                      # DataType of the XML element corresponding to this object 
        self.prefix = ""                        # Program prefix to specify the scope
        self.scalar = None
        self.array  = None 
        self.dimensions = None
        
        # For orphan elements the name and path starts from empty string and the parent 
        # for the orphans is himself. 
        if( parentObj == None ):
            self.name = ""
            self.path = ""
            self.parent = self            
        

        # If frocedName argument is defined in the call it overrides the name from XML 
        if( forcedName != None ):
            self.name = forcedName   
        # If the XML files specifies what the name should be, so be it
        elif( "Name" in self.root.attrib.keys() and forcedName != "" ):
            self.name = self.root.attrib["Name"]    
            
        if( "Dimensions"  in self.root.attrib.keys() ):
            self.dimensions = self.root.attrib["Dimensions"]           
            

        # By default the name does not contribute to the path
        # But the parent's path is inhereted 
        self.path = self.parent.path
        
        # Program prefix gets inherited from the parent object
        self.prefix = self.parent.prefix
        
        # Check to see if DataType is defined  and assign the class attribute                      
        if( "DataType" in self.root.attrib.keys() ):
            self.dataType = self.root.attrib["DataType"]      
    
#        print "Created base element ",  plcElementXML.__repr__(self)

        # Do not process any tags that are of DataType-s which do not need to go to EPICS
        # TO accomplish that we raise an exception
        if( self.dataTypeIsUseless() ) : 
            raise UselessDataType( "Useless DataType <{0}>".format( self.dataType ) )
        
        return

    def __repr__(self):
        retString = self.elementTag + " ^^^^ " + self.name + " *** " + self.dataType + " !!!! " + self.path + "\n" 
        for daughter in self.daughters:
            for elem in daughter:
                retString += repr( elem ) 
        return retString 
    
    def __str__(self):
        retString = self.elementTag + " ^^^^ " + self.name + " *** " + self.dataType + " !!!! " + self.path + "\n"
        for daughter in self.daughters:
            for elem in daughter:
                retString += str( elem ) 
        return retString  
  
    
    # Adds the newName to the path, including the element separator at the end
    def addNameToPath( self, newName ):
        if( newName != "" ):
            self.path += newName + self.elementSeparator 
        return
    
    # Strips the last dot from the path
    def removeLastDotFromPath(self):
        self.path = self.path.rstrip(".")
        return
    
    # Adds the newName to the regualr expression, including the element separator at the end 
    def appendRegEx(self, newName ):
        if( newName != "" ):
            self.regex += newName + self.elementSeparator
    
    # Strips the last dot from the regular expression for the alias recognition
    def removeLastDotFromRegEx(self):
        self.regex = self.regex.rstrip(".")
        return

    def matchPath( self, checkPath ):
        if( self.path == checkPath ):
            return self
        else :
            for elmList in self.daughters:
                for elem in elmList:
                    matchedElement = elem.matchPath( checkPath )
                    if ( matchedElement != None ):
                        return matchedElement
        return None 
    
    # Recursively return scalar elements in a single list 
    def getScalarsList(self):
        retList = []
        # Add its own scalar if exists
        if( self.scalar != None ):
            retList.extend( [self.scalar] )      # Append in form of single list elelemnt 
        # Go down the tree and add scalars of the daughter elements
        for daughter in self.daughters:
            for elem in daughter:
                if( elem != None ):
                    retList.extend( elem.getScalarsList() ) 
        return retList
                    
    # Recursively return array elements in a single list 
    def getArraysList(self):
        retList = []
        # Add its own array if exists
        if( self.array != None ):
            retList.extend( [self.array] )      # Append in form of single list elelemnt 
        # Go down the tree and add arrays of the daughter elements
        for daughter in self.daughters:
            for elem in daughter:
                if( elem != None ):
                    retList.extend( elem.getArraysList() ) 
        return retList
                   
    # Return True if the dataType of this object is not needed in EPICS, otherwise return False
    def dataTypeIsUseless(self):        
        # If dataTyoe is not defined it will not be declared useless
        if( self.dataType == None or self.dataType == "" ):
            return False           
        # Check if this DataType is explicitly specified as useless in EPICS
        if( self.dataType in plcElementXML.uselessDataTypes ):
            return True
        # Check if this DataType matches one of the patterns for types that are nto needed in EPICS. 
        for pattern in plcElementXML.uselessDataTypePatterns:
            regexPattern = re.compile( pattern )
            if( regexPattern.match( self.dataType ) != None ):
                return True
        return False # If we got here then this DataType might be uselful in EPICS
                   
        
        