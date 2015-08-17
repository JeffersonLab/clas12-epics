import sys, string
import re
#import lxml.etree


atomicTypes = ["BOOL", "SINT", "INT", "DINT", "REAL", "STRING"]

#----------------------------------------------------------------------------- #
# Class to keep information on the deconvoluted tag
# such as name, type, initial value etc
#----------------------------------------------------------------------------- #
class plcBasicData:
        """Class to handle basic data types in RSLogix5000"""
        
        # Constructor
        def __init__(self, dName=None, dType=None ):
            self.name = dName       # Name of the data (probably PLC tag name
            self.type = dType       # PLC data type
            
             
        def __repr__(self):
#            print "Reping Basic"
            return "{0} # {1} ".format( self.name, self.type )
           
        def __str__(self):
#            print "Stringing Basic"
            return "{0} # {1} ".format( self.name, self.type )

        def tagName(self):
            return self.name.rstrip( "." )

#===============================================================================
# Class ro handle scaler PLC data, what is BOOL, SINT, INT, DINT, STRING, REAL 
#===============================================================================
class plcScalar( plcBasicData ):
    """ Class to handle intrinsic scaler data of RSLogix 5000 """ 
    def __init__( self, dName=None, dType=None, dVal=None, dRadix="Decimal" ):
        plcBasicData.__init__( self, dName, dType )
        self.val = dVal        # Initial value for this data
        self.radix = dRadix
        # Take care if the value is represented in binary format
        # PLC XML file has  a weird way of presenting binary
        # First two characters of binary literals are "2#"
        if(self.radix == "Binary" and self.val != None and string.find(self.val, "2#") == 0):
            self.val = string.replace(self.val, "2#", "")
            self.val = string.replace(self.val, "_" , "")
            self.val = int(self.val, 2)
            
    def __repr__(self):
#        print "Reping scalar"
        return plcBasicData.__repr__(self) + " @ {0}".format( self.val )
           
    def __str__(self):
#        print "Stringing scalar"
        return plcBasicData.__str__(self) + " @ {0}".format( self.val )



#===============================================================================
# Class to handle array data
#===============================================================================
class plcArray( plcBasicData ):
    """ Class to handle arrays of RSLogix 5000 """ 
    def __init__( self, aName=None, aType=None, aDim=None ):
        plcBasicData.__init__( self, aName, aType )
        self.dimensions = aDim                              # Dimensions of the array
        self.numberOfElements = self.getNumberOfElements()  # Calculate the number of elements

#        print "Array <{0}> has <{1}> elements, dimensions are <{2}>".format( self.name, self.numberOfElements, self.dimensions )
        return
        
    def __repr__(self):
        return plcBasicData.__repr__(self) + " {0} long".format( self.dimensions )
           
    def __str__(self):
        return plcBasicData.__str__(self) + " {0} long".format( self.dimensions )

    # Method that finds the number of elements in the RSLogix5000 array based on the dimensions part 
    # of the array specification in the XML file, i.e "[3,4,23,3]"
    def getNumberOfElements(self):
        self.numberOfElements = int(1)        
        # Check that the dimensions are of reasonable pattern
#        pattern = "^\[(\d*\,){0,5}\d*\]$"
        pattern = "^(\d*\s){0,5}\d*$"
        regexPattern = re.compile( pattern )
        if( regexPattern.match( self.dimensions ) != None ):            # Found a match
            # this is a good dimensions pattern, start splitting and parsing
            #First strip the brackets
            tmpString = self.dimensions
#            tmpString = tmpString.replace( "\[", "")
#            tmpString = tmpString.replace( "\]", "")
            # Split into string using coma as the separator
            dimStrings = tmpString.split(" ")
            # Multiply the numbers
            for dim in dimStrings:
                self.numberOfElements *= int(dim) 
        return self.numberOfElements
    