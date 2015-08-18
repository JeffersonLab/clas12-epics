import sys
from plcData import plcBasicData

class epicsRecord:
    """Generic EPICS record which is the base class for other EPICS records"""
    
    recScanField = 'Passive'            # By default no scanning, passive records
    recSyncFrequ = '1'                  # Frequency at which the records w/o SCAN field are synced  with PLC
    recPrecField = '2'                  # Precision for displaying
    recDtypField = "EtherIP"            # Device support type
   
   
    def  __init__( self, rType = "bo", rName = "testRecord", tagData=None ):
        self.recType = rType            # EPICS record type 
        self.recName = rName            # EPICS record name  
        self.recTag = tagData           # PLC tag data object
        
#        if( tagData != None ):
#            self.recTag  = tagData.name     # PLC Tag name for i/O fields
                    
        self.recField = {}
        self.recField["SCAN"] = epicsRecord.recScanField
        self.recField["DESC"] = ""
        self.recField["VAL" ] = ""
        self.recField["PINI"] = "" 
        if( tagData != None ) :     # Use Soft Channel if there is no tagData
            self.recField["DTYP"] = epicsRecord.recDtypField  # Device support name (needs to be EitherIP for A-B)
       
        return
   
    # Method that writes the EPICS record to a file
    def writeFile( self, fileHandle ):
        outString = " \n"
        if( self.recTag != None ):
            outString += "# record for PLC tag <{0}> of type <{1}>\n".format( self.recTag.tagName(), self.recTag.type )
        outString += 'record( {0}, "{1}" ) \n'.format( self.recType, self.recName )
        outString += "{ \n"
        for field in self.recField:
            if ( field != "" and self.recField[field] != "" ):
                outString += '  field({0}, "{1}" ) \n'.format( field, self.recField[field] )
        outString += "} \n"
        outString += " \n"
        fileHandle.write( outString )
        return
    
    def writeAutoSaveFields(self, fileHandle ):
        '''Write the alarm fields for this record'''
        outString = ""
        if( self.recTag != None ):
            outString += "# record for PLC tag <{0}> of type <{1}>\n".format( self.recTag.tagName(), self.recTag.type )
        for fieldName in self.recAutoSaveFields:
            outString += '{0}.{1} \n'.format( self.recName, fieldName )
        fileHandle.write( outString )
        return

    # Method to return fields of the record        
    def setField( self, fieldName, value ):
        self.recField[fieldName] = value
        return self.recField[fieldName]
    
    # Method to retun value of the record fields
    def getField( self, fieldName ):
        if ( fieldName in self.recField.keys() ):
            return self.recField[fieldName]
        else:
            return ""
    # Methods to set and get the record type and name
    def setName( self, rName ):
        self.recName = rName
        return self.recName
    
    def getName( self ):
        return self.recName
    
    def setType( self, rType ):
        self.recType = rType
        return self.recType
    
    def getType( self ):
        return self.recType

# Binary input (bi) class definition
class biRecord( epicsRecord ):
    """Binary input record bi class"""
    recScanField = '1 second'   # Scanning frequency for input type

    def __init__( self, rName = "testRecord", tagData=None ):
        epicsRecord.__init__( self, "bi", rName, tagData )
        self.recAutoSaveFields = ( "ZSV", "OSV", "COSV" )
        self.recField["INP"] = "@$(PLCID) {0}".format( self.recTag.tagName() )
        self.recField["ONAM"] = ""
        self.recField["ZNAM"] = ""
        self.recField["SCAN"] = biRecord.recScanField   #  Need to scan for input records
        return

# Binary output (bo) class definition
class boRecord( epicsRecord ):
    """Binary outupt record bo class"""
    def __init__( self, rName = "testRecord", tagData=None  ):
        epicsRecord.__init__( self, "bo", rName, tagData )
        self.recAutoSaveFields = ( "ZSV", "OSV", "COSV" )
        self.recField["OUT"] = "@$(PLCID) {0} S {1}".format( self.recTag.tagName(), boRecord.recSyncFrequ )
        self.recField["ONAM"] = ""
        self.recField["ZNAM"] = ""
        return

# Multibit input (mbbiDirect) class definition
class mbbiDirectRecord( epicsRecord ):
    maxSize = 16                # There can only be 16 bits read out
    """mbbiDirect input record  class"""
    recScanField = '1 second'   # Scanning frequency for input type
    recAutoSaveFields = ( )

    def __init__( self, rName = "testRecord", tagData=None, numberOfBits=16, firstBit=0 ):
        epicsRecord.__init__( self, "mbbiDirect", rName, tagData )
        self.recAutoSaveFields = ()
        self.recField["INP"] = "@$(PLCID) {0}[{1}]".format( self.recTag.tagName(), firstBit )
        self.recField["SCAN"] = mbbiDirectRecord.recScanField   #  Need to scan for input records
        self.recField["NOBT"] = numberOfBits
        return
    
# Multibit output (mbboDirect) class definition
class mbboDirectRecord( epicsRecord ):
    maxSize = 16               # There can only be 16 bits read out
    """mbbiDirect output record  class"""
    def __init__( self, rName = "testRecord", tagData=None, numberOfBits=16, firstBit=0 ):
        epicsRecord.__init__( self, "mbboDirect", rName, tagData )
        self.recAutoSaveFields = ()
        self.recField["OUT"] = "@$(PLCID) {0}[{1}] S {2}".format( self.recTag.tagName(), firstBit, mbboDirectRecord.recSyncFrequ )
        self.recField["NOBT"] = numberOfBits
        return

# Analog input (ai) class definition
class aiRecord( epicsRecord ):
    """Analog input record ai class"""
    recScanField = '1 second'   # Scanning frequency for input type

    def __init__( self, rName = "testRecord", tagData=None ):
        epicsRecord.__init__( self, "ai", rName, tagData )
        self.recAutoSaveFields = ( "LOLO", "LOW", "HIGH", "HIHI", "LLSV", "LSV", "HSV", "HHSV", "HYST" )
        self.recField["INP"] = "@$(PLCID) {0}".format( self.recTag.tagName() )
        self.recField["SCAN"] = aiRecord.recScanField   #  Need to scan for input records
        self.recField["PREC"] = aiRecord.recPrecField   #  Should specify the precision
        return

# Analog output (ao) class definition
class aoRecord( epicsRecord ):
    """Analog output record ao class"""
    def __init__( self, rName = "testRecord", tagData=None ):
        epicsRecord.__init__( self, "ao", rName, tagData )
        self.recAutoSaveFields = ( "LOLO", "LOW", "HIGH", "HIHI", "LLSV", "LSV", "HSV", "HHSV", "HYST" )
        self.recField["OUT"] = "@$(PLCID) {0} S {1}".format( self.recTag.tagName(), aoRecord.recSyncFrequ )
        self.recField["PREC"] = aoRecord.recPrecField   #  Should specify the precision
        return

# String input (stringin) class definition
class siRecord( epicsRecord ):
    """Analog input record stringin class"""
    recScanField = '1 second'                           # Scanning frequency for input type
    def __init__( self, rName = "testRecord", tagData=None ):
        epicsRecord.__init__( self, "stringin", rName, tagData )
        self.recAutoSaveFields = ()

        self.recField["INP"] = "@$(PLCID) {0}".format( self.recTag.tagName() )
        self.recField["SCAN"] = siRecord.recScanField   #  Need to scan for input records
        return

class wfRecord( epicsRecord ):
    """ Wafeform record class for input """
    recScanField = "1 second"
    def __init__( self, rName = "testRecord", nELM=1, tagData=None ):
        epicsRecord.__init__( self, "waveform", rName, tagData )        
        self.recAutoSaveFields = ()
        
        self.recField["INP"]  = "@$(PLCID) {0}".format( self.recTag.tagName() )
        self.recField["SCAN"] = wfRecord.recScanField   #  Need to scan for input records
        self.recField["NELM"] = nELM                        # Number of elements to read
        
        # Dtermine the proper FTVL and PREC fields
        if( tagData.type == "REAL"):
            self.recField["FTVL"] = "DOUBLE"                # Type of the waveform elements 
            self.recField["PREC"] = aoRecord.recPrecField   # Should specify the precision
        elif( tagData.type == "DINT" ):
            self.recField["FTVL"] = "LONG"                  # Type of the waveform elements 
        else:
            print( "Bad tag type <{0}> for the waveform <{1}>. Exiting... ".format( tagData, rName ) )
            sys.exit(-1)
            
        return
   


