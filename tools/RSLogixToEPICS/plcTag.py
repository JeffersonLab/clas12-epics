

import sys, string
import lxml.etree
import re

import plcData

from plcElement import  plcElementXML 
from plcElement import  UselessDataType


#===============================================================================
# Class to deal with the RSLogix500 tags in the XML files
# This class can be for Alias tags, but it will create a daughter alias tag of 
# plcAliasTag class to deal with aliases. This will deal directly with 
# Tag, InputTag, OutputTag, ConfigTag XML tags
#===============================================================================
class plcTag ( plcElementXML ):
    """Allen-Bradley PLC RSLogix5000 Tag"""
    nUnNamed = 0
                
    # Constructor of the tag from XML element
    def __init__(self, rootElement, parentObj=None, forcedName=None ):
        try:
            plcElementXML.__init__(self, rootElement, parentObj, forcedName )
        except UselessDataType as err:
            print err
            return
        
        self.structures = []
        self.arrayElements = []
        self.aliasTags = []
        self.daughters.append( self.structures )
        self.daughters.append( self.arrayElements )  
        self.daughters.append( self.aliasTags )   

        # For tags name contributes to the path    
        self.addNameToPath( self.name )          

        # If it is an alias create an alias tag and sotre it in the daughters and return
        # The alias tag will have no name, the daughter plcAliasTag itself will not contribute to path 
        if( "TagType" in self.root.attrib.keys() and self.root.attrib["TagType"] == "Alias" 
            and "AliasFor" in self.root.attrib.keys() ):
            aliasTag = plcAliasTag( self.root, self, "" )
            self.aliasTags.append( aliasTag )
            return

        # If we got  here then the tag is not an alias to another tag 
        # Refer to plcAliasTag class to what happens to the aliases 
        
        # Check if the tag is an array and set the flag for future use 
        self.isArray = False
        if( self.dimensions != None ):
            self.isArray = True

        self.createChildren()
        return 


    # In this method we generate the child objects of the tag 
    # this method is designed to be called from the contructor 
    def createChildren(self):
        if( ( self.dataType != "" ) and ( self.dataType in plcData.atomicTypes ) ): 
            # This tag is PLC atomic type, not sure yet if it is scalar or array 
            
            if( not self.isArray ):
                # This is a scalar number of atomic type. Define the scaler data 
                # and move on 
                dataValue = None
                dataRadix = ""
                if( "Radix" in self.root.attrib.keys() ):
                    dataRadix = self.root.attrib["Radix"]
                if( "Value" in self.root.attrib.keys()):
                    dataValue = self.root.attrib["Value"]
                self.scalar = plcData.plcScalar( self.path, self.dataType, dataValue, dataRadix )
            else:
            # This is an array if atomic elements. Create an array of atomic elemtss
                self.array = plcData.plcArray( self.path, self.dataType, self.dimensions )
        else:
            # This is not an atomic type tag, not sure yet scalar or array 
            if( not self.isArray ):
                # If the DataType is not a PLC type  then it has to be a structure                
                # Get all structure elements in the tag element. There should be only one!
                self.structElms = self.root.xpath("Data[@Format='Decorated']/Structure")
                if( len( self.structElms ) != 1 ):
                    print "Tag <{0}> does not contain data strcuture".format(self.name)
                    return                
                for structElm in self.structElms:   
#                    print "Data Structure: ", structElm.attrib                
                    # For tags that do not have name but the structure does we may want to use 
                    # the structure name in the path. Need to switch if decide to it that way
                    if( self.name == "" and "DataType" in structElm.attrib.keys() ):
#                        self.path += plcElementXML.elementSeparator + structElm.attrib["DataType"]
                        self.name = "UnNamedTag" + str(plcTag.nUnNamed)
                        self.addNameToPath( self.name )
#                        self.addNameToPath( structElm.attrib["DataType"] )                        
                        plcTag.nUnNamed += 1
                    elif( self.name == "" ):
                            self.name = "UnNamedTag" + str(plcTag.nUnNamed)
                            self.addNameToPath( self.name )
                            plcTag.nUnNamed += 1
            
                    # Create the new structure object and store it in the list of structures
                    newStruct = plcStructure( structElm, self )
                    self.structures.append( newStruct )
            else:
                # This is am arrasy of user-defined structures. Find all Elements define under it in the XML file 
                # and create correspondinf ArrayElement objects. 
                arrayElms = self.root.xpath("Data/Array[@DataType=$dt]/Element", dt = self.dataType )
                for arrElm in arrayElms:
                    newArrElm = plcArrayElement( arrElm, self )
                    self.arrayElements.append( newArrElm )                    
        return            
        

    def __repr__(self):
        retString = "<{0}>".format( self.name ) 
        if( self.scalar != None ): retString += "Has scalar tag <{0}>".format( self.path ) + "\n"
        if( self.array  != None ): retString += "Has array tag <{0}>".format( self.path )  + "\n"       
        return retString +  plcElementXML.__repr__(self)
    
    def __str__(self):
        retString = "<{0}>".format( self.name ) 
        if( self.scalar != None ): retString += "Has scalar tag <{0}>".format( self.path ) + "\n"
        if( self.array  != None ): retString += "Has array tag <{0}>".format( self.path )  + "\n"     
        return retString +  plcElementXML.__repr__(self)
        

#==============================================================================
# Class to handle DataValueMember elements in the RSLogix5000 XML file  
#==============================================================================
class plcDataValueMember( plcElementXML ):
    """Class to handle DataValueMember elements in the RSLogix5000 XML file """
    
    # Constructor 
    def __init__( self, rootElement, parentObj, forcedName=None ):
        try:
            plcElementXML.__init__(self, rootElement, parentObj, forcedName )
        except UselessDataType as err:
            print err
            return
        self.value = ""
        self.radix = "" 
#        self.scalar = None
                      
        # For tags name contributes to the path    
        self.addNameToPath( self.name )          

        # Data value member has to have a name
        if( self.name == "" ):
            print "No name specified for DataValueMemeber of tag <{0}>".format( self.parent.name )
            sys.exit(-1)
        # Data value member has to have a type 
        if( self.dataType == "" ):
            print "DataType is no specified for DataValueMember <{0}>".format( self.name )
            sys.exit(-1)
             
        # Get defualt value and "Radix"
        if( "Value" in rootElement.attrib.keys()):
            self.value = rootElement.attrib["Value"]
        if( "Radix" in rootElement.attrib.keys()):
            self.radix = rootElement.attrib["Radix"]
        
        # Create the scalar data object and store its reference in the objects attribute  
        self.scalar = plcData.plcScalar( self.path, self.dataType, self.value, self.radix )    
        
#        print "Finished constructing DataValueMemeber <{0}>".format( self.path )
        
        return
    
    def __repr__(self):
        return repr(self.scalar) + "\n"
    
    def __str__(self):
        return str(self.scalar) + "\n"
    
#===============================================================================
# Class to handle ArrayMember elements in the PLC XML file
# This class is only supposed to handle the atomic type arrays
#===============================================================================
class plcArrayMember( plcElementXML ):
    """ Class to handle ArrayMember structures in the PLC XML file """
    
    # Constructor 
    def __init__( self, rootElement, parentObj=None, forcedName=None ):
        # Inherit from plcTag since it does almost the same. 
        # Finds the structures or sees that is is an arrays for scaler tags 
        try:
            plcElementXML.__init__(self, rootElement, parentObj, forcedName )
        except UselessDataType as err:
            print err
            return

#        self.array = None
        self.arrayElements = []
        self.daughters.append(self.arrayElements)

        # For tags name contributes to the path    
        self.addNameToPath( self.name ) 
                 
        # Array has to have a type
        if( self.dataType == "" ):
            print "ArrayMember <{0}> does not have DataType".format( self.name )
            sys.exit(-1)

        # Array has to have dimensions
        if( self.dimensions == None or self.dimensions == "" ):
            print "ArrayMemeber <{0}> does not have dimensions".format( self.name )
            sys.exit(-1)

        # Create the correct object and store it
        if( self.dataType in plcData.atomicTypes ):
            # This is an array of atomic type
            self.array = plcData.plcArray( self.path, self.dataType, self.dimensions )
        else:
            # This is an array of user-specified structures
            # Loop through the elements and build the corresponding objects
            arrayElms = self.root.xpath("Element" )
            for arrElm in arrayElms:
                newArrElm = plcArrayElement( arrElm, self )
                self.arrayElements.append( newArrElm )
#        print "Completed Array member <{0}>".format(self.name) + str(self)        
        return



#===============================================================================
# Class to handle cases when an array is an array for non-atomic types. 
#===============================================================================
class plcArrayElement( plcElementXML ):
    """ Class to handle cases when an array is an array for non-atomic types """
    
    # Constructor 
    def __init__(self, rootElement, parentObj=None, forcedName=None ):
        try:
            plcElementXML.__init__(self, rootElement, parentObj, forcedName )
        except UselessDataType as err:
            print err
            return
        self.structures = []
        self.daughters.append( self.structures )        
        
        # ArrayElement (which corresponds to the Element XML tag) has to have Index attribute 
        if( "Index" not in self.root.attrib.keys() ):
            print "Structure in the array for tag <{0}> does not have Index. Exiting...".format(self.parent.name)
            sys.exit(-1)            
        self.index = self.root.attrib["Index"]
        # At this point we do not deal with the index, just keep it as it is
        # If it needs to be linearized, we will have to do at a later stage 
        self.name += self.index
        
        # REmove the dot from the end of the path and add the index piece to it
        self.removeLastDotFromPath()
        self.addNameToPath( self.index )
        
        # Find all daugher Structure XML elements and build the corresponding objects
        structElms = self.root.xpath( "Structure")        
        for structElm in structElms :
            newStruct = plcStructure( structElm, self )
            self.structures.append(newStruct)
        
        return
    
#===============================================================================
# Class to handle Alias Tags. It inherits from the regular plcElementXML class 
#===============================================================================
class plcAliasTag( plcElementXML ):
    """Class to handle RSLogix5000 PLC Aliases in XML file """
    
    # Constructor 
    def __init__( self, rootElement, parentObj=None, forcedName=None ):
        try:
            plcElementXML.__init__(self, rootElement, parentObj, forcedName )
        except UselessDataType as err:
            print err
            return
        self.targets = []
#        self.scalar = None
        self.daughters.append(self.targets)
        
        # Double check that this is an Alias tag in the XML file. If not then exit. 
        if( "AliasFor" not in self.root.attrib.keys() or 
            "TagType" not in self.root.attrib.keys() or 
            self.root.attrib["TagType"] != "Alias" ):
                print "Either AliasFor or TagType attributes missing for alias tag <{0}>. Exiting...".format( self.root.name )
                sys.exit(-1)
       
        # Find the target of this alias to get the datatype or the substructure for it
        self.tgtName = self.root.attrib["AliasFor"]   
        
        isArrayElement = self.checkPattern4ArrayElement( self.tgtName ) 
        isBitElement   = self.checkPattern4BitElement( self.tgtName )

        if( not isArrayElement and not isBitElement ):    
            # The alias target is neither an array element nor a bit of an integral type 
            # It is the most straightforward case when the alias is defined by actual target tag name 
            # Find the target element such that the path of the object is identical to the name 
            # given in the alias definition in the XML file. This is done so that the internal structure, 
            # if any can be traced
            tgtTag = self.findTargetElm( self.tgtName )        
            if ( tgtTag != None ):
                tgtElm = tgtTag.root            
                # Create names less plcTag or plcAliasTag objects and store them  
                if( "DataType" in tgtElm.attrib.keys() and tgtElm.attrib["DataType"] in plcData.atomicTypes ) :
                    # Target is not  an alias, the target will have empty name
                    newTag = plcTag( tgtElm, self, "" )
                    self.targets.append( newTag )
                else:
                    # The target will be an alias too, the target will have empty name 
#                    newAliasTag = plcAliasTag( tgtElm, self, "" )
                    newTag = plcTag( tgtElm, self, "" )
                    self.targets.append( newTag )
            else: 
                # Did not find the target by that name (path to be precise)
                print "No target found for Alias <{0}>".format(self.name)
        elif( isArrayElement ):
            # It is an element of an array. It cannot be an alias
#            print "Looking for array element for alias <{0}>".format( self.tgtName )            
            strippedName = self.stripAliasBrackets( self.tgtName )      # Strip the bracket part off from the right side
            tgtTag = self.findTargetElm( strippedName )                 # Find  the target that corresponds to the array name 
            # Keep stripping the last brackets until the tagret is not an array element
            while( tgtTag != None and self.checkPattern4ArrayElement( tgtTag.name ) ):
                strippedName = self.stripAliasBrackets( self.tgtName )      # Strip the bracket part off from the right side                
                tgtTag = self.findTargetElm( strippedName )
            # Once the target is not an array element we will be able to determine the type of the alias tag 
            if( tgtTag != None ):                                       # At least one target was found for the array
                # Get the structure of the array elemement based on the structure of the array found
                if( tgtTag.dataType in plcData.atomicTypes ):
                    # Atomic type. Add the bracket string to the path, create a scaler and keep the value in the scalar list
#                    self.addNameToPath( self.name )
                    self.scalar = plcData.plcScalar( self.path, tgtTag.dataType, None, None )
                else:                                                   
                    # Target is a user-defined tructure
                    parentTag = plcTag( tgtTag.root, self, "" )              # Array tag will be target, no name
                    self.targets.append( parentTag )                
            else:            
                # Did not find the target by that name (path to be precise)
                print "No target found for Alias <{0}>, was looking for array <{1}>".format( self.name, strippedName )                               
        elif( isBitElement ):
            # Since we know it is a bit, we do not care what the target is and we simply create a BIT scalar object
            self.scalar = plcData.plcScalar( self.path, "BIT", None, "Binary" )                
            
#        print "Finished dealing with alias", str(self) + "\n"
        return
#
##        tgtElms = self.root.xpath( "//Tag[@Name=$tgt]", tgt = self.tgtName )
#        #tgtElms = self.root.xpath("//Tag[re:test(@AliasFor, $tgt)]", namespaces={'re':'http://exslt.org/regular-expressions'}, tgt=self.tgtName )
#        tgtElms = self.root.xpath("//Tag[re:match(@AliasFor, $tgt)]", namespaces={'re':'http://exslt.org/regular-expressions'}, tgt=self.tgtName )
# 
# 
#        
#        # First find tags whos name exactly matches the target name 
#        exactTargets =  self.root.xpath("//Tag[re:match(@AliasFor, ^$tgt$)]", namespaces={'re':'http://exslt.org/regular-expressions'}, tgt=self.tgtName )
#        if( len( exactTargets) > 0 ):
#            #There are exact matches
#            if( len( tgtElms ) > 1 ):
#                print "Number of targets for alias to <{0}> is {1}, should be only one target".format( self.tgtName, len( tgtElms ) )
#                #sys.exit(-1)
#                return
#            tgtElm = exactTargets[0]
#        else: 
#            # If we are here there were no exact maches for the taget name 
#            # Firt look for array element targets
#            arrayElmTargets = self.root.xpath("//Tag[re:match(@AliasFor, ^$tgt[.*]$)]", 
#                                              namespaces={'re':'http://exslt.org/regular-expressions'}, tgt=self.tgtName )
    
    # Returns True if aliasName matches the patern of an array element based on brackets at the end 
    def checkPattern4ArrayElement( self, aliasName ):
        # Pattern that array elements have, multipdimensioanl is allowed, spaces not allowed. the lasst piece should be like [14,12] etc
        arrElmPattern = re.compile( "^([\w:\.]*)\[(\d{1,5}\,){0,6}\d{1,5}\]$" )
        return  ( arrElmPattern.match( aliasName ) != None )  

    # Returns True if aliasName matches patern of an bit set element based the dot followed by a number
    def checkPattern4BitElement(self, aliasName ):
        # Pattern that bit members have, the last peice should be like ".15"  
        bitPattern   = re.compile( "^([\w:\.\[\]]*)\.(\d{1,5})$" )
        return( bitPattern.match( self.tgtName ) != None ) 
    
    
    # Strips the bracket part of the path by finding the rightmost "[" and returning substring before it
    def stripAliasBrackets(self, inString):
        lastBracketPosition = inString.rfind( "[" )     # Find the right most right square bracket
        if( lastBracketPosition > 0 ):            
            return inString[0:lastBracketPosition]          # Return the substring before the right bracket
        else:
            return None
        
    # Strips the part after last dot, including the dot, and returns the part on the left side of the dot 
    def stripAliasDotNumber( self, inString ):
        lastDotPosition = inString.rfind( "." )
        if( lastDotPosition > 0 ):
            return inString[0:lastDotPosition]               # Return the substring before the last dot
        else :
            return None
        
    # Method to find the target tag for the alias 
    def findTargetElm( self, tgtName ):
#        print "Need to find target <{0}>".format( tgtName ) 
            
        # Search for elements whos path matches the name with a dot added to the end 
        # since we never remove the last dot from the path of the tag obejects    
        # Look for match for both global and program scopes
        scopedTgtName = self.prefix + plcElementXML.elementSeparator + tgtName
        matchedTags = plcElementXML.elementSearch.search( ( tgtName + ".", scopedTgtName + "." ) )  

        # Will return None if not match is found for that target name
        if( len( matchedTags ) != 1 ):
            print "Number of alias Matches for <{0}> name is {1}".format( tgtName, len( matchedTags ))
            return None
        
        return matchedTags[0]
    
    
    def __repr__(self):
        retString = "<{0}> ".format( self.name )         
        if( self.scalar != None ): retString += "Has scalar tag <{0}> of type {1}".format( self.path, self.scalar.type) + "\n"
        return retString +  plcElementXML.__repr__(self)
    
    def __str__(self):
        retString = "<{0}> ".format( self.name )                 
        if( self.scalar != None ): retString += "Has scalar tag <{0}> of type {1}".format( self.path, self.scalar.type) + "\n"
        return retString +  plcElementXML.__repr__(self)
    
#===============================================================================
# Class to handle Structure elements in the RSLogix5000 XML file
#===============================================================================
class plcStructure( plcElementXML ):
    """Allen-Bradley PLC RSLogix5000 Tag structures"""
            
    # Constructor of the tag from XML element
    def __init__( self, rootElement, parentObj = None, forcedName=None ):
        try:
            plcElementXML.__init__(self, rootElement, parentObj, forcedName )
        except UselessDataType as err:
            print err
            return

        self.dataValueMembers = []
        self.arrayMembers = []
        self.structureMembers = []

        self.daughters.append( self.dataValueMembers )                 
        self.daughters.append( self.arrayMembers )
        self.daughters.append( self.structureMembers )

        # Check to see if DataType is defined                        
        if( self.dataType == "" ):
            print "Structure {0} does not know its DataType".format( self.name )
            sys.exit(-1)
            
        # Get all DataValueMembers. Here it is pretty straightforward
        dvElms = self.root.xpath( "DataValueMember" )
        for dvElm in dvElms:
            newDataValue = plcDataValueMember( dvElm, self )
            self.dataValueMembers.append( newDataValue )
                
        # Get all ArrayMembers inside this tag
        amElms = self.root.xpath( "ArrayMember" )
        for amElm in amElms:   
            newArray = plcArrayMember( amElm, self )
            self.arrayMembers.append(newArray)
                
        # Get all StructureMEmbers inside this tag                
        smElms = self.root.xpath( "StructureMember" )
        for smElm in smElms:
            newStruct = plcStructureMember(smElm, self)
            self.structureMembers.append( newStruct )   
        
        return 
        
            
    
#===============================================================================
# Class to handle StructureMember elements in the RSLogix5000 XML file
# Pretty much identical to plcStructure class, except the name should contribute 
# to the path (that is the PLC tag name
#===============================================================================
class plcStructureMember( plcElementXML ):
    """Class to handle StructureMember elements in the PLC XML file """    

    # Constructor of the tag from XML element
    def __init__( self, rootElement, parentObj = None, forcedName=None ):
        try:
            plcElementXML.__init__(self, rootElement, parentObj, forcedName )
        except UselessDataType as err:
            print err
            return

        self.dataValueMembers = []
        self.arrayMembers = []
        self.structureMembers = []

        self.daughters.append( self.dataValueMembers )                 
        self.daughters.append( self.arrayMembers )
        self.daughters.append( self.structureMembers )

        if( self.name == "" ):
            print "StrucureMember of <{0}> does not have a name. Exiting...".format( self.parent.name )

        # The name can contribute to the path
        self.addNameToPath( self.name )

        # Check to see if DataType is defined                        
        if( self.dataType == "" ):
            print "Structure {0} does not know its DataType".format( self.name )
            sys.exit(-1)


        if( self.dataType in plcData.atomicTypes ): 
            # This tag is PLC atomic type, it seems like it can only be scalar            
            # Assume that this is a scalar number of atomic type. Define the scaler data 
            # and move on 
            dataValue = None
            dataRadix = ""
            if( "Radix" in self.root.attrib.keys() ):
                dataRadix = self.root.attrib["Radix"]
            if( "Value" in self.root.attrib.keys()):
                dataValue = self.root.attrib["Value"]
            self.scalar = plcData.plcScalar( self.path, self.dataType, dataValue, dataRadix )
            return

            
        # Get all DataValueMembers. Here it is pretty straightforward
        dvElms = self.root.xpath( "DataValueMember" )
        for dvElm in dvElms:
            newDataValue = plcDataValueMember( dvElm, self )
            self.dataValueMembers.append( newDataValue )
                
        # Get all ArrayMembers inside this tag
        amElms = self.root.xpath( "ArrayMember" )
        for amElm in amElms:   
            newArray = plcArrayMember( amElm, self ) 
            self.arrayMembers.append(newArray)
                
        # Get all StructureMEmbers inside this tag                
        smElms = self.root.xpath( "StructureMember" )
        for smElm in smElms:
            newStruct = plcStructureMember(smElm, self)
            self.structureMembers.append( newStruct )                                                

        return 




    