#!/usr/bin/python2.6

import sys, string
import lxml.etree
import re, math

import plcData
import plcController

import clfOptions

from plcElement import  plcElementXML 
from plcModule import plcModule
from plcTag import plcTag
from plcController import plcController 

#from clfOptions import clfOptions

import epicsRecords


# Function to return EPICS input record type for PLC atomic types
# At this point the type is  a string, in the future we will 
# probably need to define a class for the EPICS type
def PLCBasicTypes2InputEPICS( typeName ):
    if( typeName in plcData.atomicTypes or typeName == "BIT" ):
        if( typeName == "BOOL" or typeName == "BIT" ):
            return 'bi'
        elif ( typeName == "SINT" or typeName == "INT" or typeName == "DINT" or typeName == "REAL" ):
            return 'ai'
        elif ( typeName == "STRING" ):
#            return 'stringin'
            return None
        else:
            return None
    else:
        print "Bad PLC atomic Data Type <{0}> for input".format( typeName ) 
        return None

def PLCBasicTypes2OutputEPICS( typeName ):
    if( typeName in plcData.atomicTypes  or typeName == "BIT" ):
        if( typeName == "BOOL" or typeName == "BIT" ):
            return 'bo'
        elif ( typeName == "SINT" or typeName == "INT" or typeName == "DINT" or typeName == "REAL" ):
            return 'ao'
        elif ( typeName == "STRING" ):
            return None
        else:
            return None
    else:
        print "Bad PLC atomic Data Type for output <{0}>".format( typeName ) 
        return None

# Convert PLC tag name to valid EPICS name
def PLC_2_EPICS_Name( tagName ):
    epicsName = None
    if( tagName != None ):
        strippedName = tagName.rstrip(".")
        shortName = strippedName.replace( "Program:", ":")        
        epicsName = clfOptions.globOptions.getOption( "PrefixEPICS"  ) + shortName.replace( ".", "-" )
    return epicsName

# Check if the EPICS record name pattern matches name patterns to be excluded  
def ExcludedFromEPICS( recName ):
    # Loop through all patterns for ignoring EPICS records using their names
    # If there is a match return True (which means to be ignored) 
    for pattern in clfOptions.globOptions.getOption("IgnoreEPICS_Record"):
        regexPattern = re.compile( pattern )
        if( regexPattern.match( recName ) != None ): # There is a match
            return True
    return False


#===============================================================================
# This is the main execution block
#===============================================================================

#xmlFileName = '/group/halld/Online/controls/epics/R3-14-12-2/app/solenoidApp/Db/Hall_D_Version4.L5X'
#xmlFileName = '/group/halld/Online/controls/epics/R3-14-12-2/app/solenoidApp/Db/TagExportTest.L5X'
#xmlFileName = '/group/halld/Online/controls/epics/R3-14-12-2/app/solenoidApp/Db/cPID_vs_PIDE.L5X'
#xmlFileName = '/group/halld/Online/controls/epics/R3-14-12-2/app/solenoidApp/Db/Hall_D_Version4_withFakeAliases.L5X'

maxRecordNameLength4EPICS = 60   # This the maximum # of characters EPICS rcord name can have

# Get the global options from the clfOptions class
progOpts = clfOptions.globOptions

print "Starting to parse <{0}> L5X file".format( progOpts.getOption( "XMLFile" ))
# Parse the XML file specified in the command line options
tree = lxml.etree.parse( progOpts.getOption( "XMLFile" ) )
#root = tree.getroot()      

# Get the Controller XML tags
controllerElms = tree.xpath( "//Controller" )


if( len(controllerElms) != 1 ):
    print "There should be one Controller element in the XML file, found ", len(  controllerElms )
    print "Exiting..."
    sys.exit(-1)
    
# This is the main part where the L5X XML file from RSLogix5000 is being read
nIter = 0
newCtrler = plcController( controllerElms[0]  )
while( newCtrler.nFailedAliases > 0 ):
    # Will iterate until there are no unresolved aliases
    dummy = raw_input( "Iteration number {0} had {1} unresolved aliases, need anoter iteration. Hit return".format( nIter, newCtrler.nFailedAliases ) )
    oldCtrler = newCtrler
    newCtrler = plcController( controllerElms[0], oldCtrler )
    nIter += 1
    
print "Parsing complete"
   
longTagDataList = []                            # List of tags whos EPICS name was longer than maximum allowed
scalarsList = newCtrler.getScalarsList4EPICS()  # Get all scalars for the newCtrlr

inRecordFile    = open( progOpts.getOption( "InputDBFile"  ), 'w' )          # Open the file for writing
outRecordFile   = open( progOpts.getOption( "OutputDBFile" ), 'w' )          # Open the file for writing
arrayRecordFile = open( progOpts.getOption( "ArrayDBFile"  ), 'w' )          # Open the file for writing
autoSaveFile    = open( progOpts.getOption( "AutoSaveFile" ), 'w' )          # Open the file for alarm request file


# Write dummy record into the files so that there is at least one recordd in each EPICS DB file
# This solves the problem with errors when loading an empty file using dbLoadRecord
dummyInRecord  = epicsRecords.epicsRecord( "bi",       PLC_2_EPICS_Name( "dummyNonExistantTag") )
dummyInRecord.writeFile( inRecordFile )
dummyOutRecord = epicsRecords.epicsRecord( "bo",       PLC_2_EPICS_Name( "dummyNonExistantTag") )
dummyOutRecord.writeFile( outRecordFile )
dummyArrRecord = epicsRecords.epicsRecord( "waveform", PLC_2_EPICS_Name( "dummyNonExistantTag") )
dummyArrRecord.writeFile( arrayRecordFile )

for scalar in scalarsList:
    if( scalar != None ):
#        print scalar
        tagName = scalar.name.rstrip( "." )
        recordName = PLC_2_EPICS_Name( tagName )
#        print "The length of <{0}> is {1} \n".format( recordName, len( recordName ) )
        if( len( recordName ) <= maxRecordNameLength4EPICS ):
            # EPICS has a maximum for record name length (I think 60 characters)
            
            # Create the input EPICS DB file
            epicsTypeName = PLCBasicTypes2InputEPICS( scalar.type )
            if( epicsTypeName != None and recordName != None and not ExcludedFromEPICS( recordName ) ):
                if( epicsTypeName == "bi" ):
                    epicsRec = epicsRecords.biRecord( recordName, scalar )
                elif( epicsTypeName == "ai" ):
                    epicsRec = epicsRecords.aiRecord( recordName, scalar )               
                elif( epicsTypeName == "stringin" ):
                    epicsRec = epicsRecords.siRecord( recordName, scalar )                             
                else:   
                    print( "Do not know what to do with EPICS record ", recordName, "of type ", epicsTypeName )
                    sys.exit(-1)
#                print "  EPICS name is ", recordName, " , EPICS  type is ", epicsTypeName
                epicsRec.writeFile( inRecordFile )   
                epicsRec.writeAutoSaveFields( autoSaveFile )       # Write the fields into the autosave request file
#                print tagName
            
            # Create the output EPICS DB file
            epicsTypeName = PLCBasicTypes2OutputEPICS( scalar.type )
            if( epicsTypeName != None and recordName != None and not ExcludedFromEPICS( recordName ) ):
                if( epicsTypeName == "bo" ):
                    epicsRec = epicsRecords.boRecord( recordName, scalar )
                elif( epicsTypeName == "ao" ):
                    epicsRec = epicsRecords.aoRecord( recordName, scalar )               
                else:   
                    print( "Do not know what to do with EPICS record ", recordName, "of type ", epicsTypeName )
                    sys.exit(-1)                    
#                print "  EPICS name is ", recordName, " , EPICS  type is ", epicsTypeName
                epicsRec.writeFile( outRecordFile )   
                                  
        else: 
            # If the name is too long do not generate the corresponding record, save it in the list and 
            # print out the failed record names at the end. 
            longTagDataList.extend( [scalar] ) 
            
            
# Once finished with scalars, do the arrays (only input can be done with  waveforms)            
arraysList = newCtrler.getArraysList4EPICS()            # Get all arrays for the newCtrlr
for array in arraysList:
    if( array != None ):
#        print array
        tagName = array.name.rstrip( "." )
        nELM = array.numberOfElements
        recordName = PLC_2_EPICS_Name( tagName )
        if( len( recordName ) <= maxRecordNameLength4EPICS ):
            if( not ExcludedFromEPICS( recordName ) ):            
                epicsTypeName = "waveform"
                if( array.type == "REAL" or array.type == "DINT" ):
                    # Only REAL and DINT are converted to arrays, make an EPICS array 
                    # Note that only input into EPICS is support for the arrays, and according 
                    # to the ether_ip manual it is only supported for DINT and REAL arrays. 
                    epicsRec = epicsRecords.wfRecord( recordName, nELM, array )
                    epicsRec.writeFile( arrayRecordFile )   
#                    print tagName                    
                elif( array.type == "BOOL" ) :
#                    print tagName

                    # BOOL arrays are split into multiple mbbiDirect/mbboDirect records 
                    # vecause these records can handle 16 bits at most. Whoever makes the 
                    # screens should combine these records to get the right sequnce of bits.
                    # Both read and write will thus be supported since ether_ip supports both 
                    # mbbiDirect and mbboDirect.  
                    # Make a series of mbbiDirect and mbboDirect records
                    # First make mbbiDirect records
                    if( nELM <= epicsRecords.mbbiDirectRecord.maxSize ):  
                        # Make a single mbbiDirect record
                        epicsRec = epicsRecords.mbbiDirectRecord( recordName, array, nELM )
                        epicsRec.writeFile( inRecordFile )   
                    else :
                        # Split into multiple mbbiDirect records
                        nRecs = int( math.ceil( float(nELM) / epicsRecords.mbbiDirectRecord.maxSize ) )   # Number of records
                        nBits4Last = nELM % epicsRecords.mbbiDirectRecord.maxSize                   # Number of bits in the last record
                        for iRec in range(nRecs):
                            iPos = iRec * epicsRecords.mbbiDirectRecord.maxSize                     # Position to start from
                            nBits = epicsRecords.mbbiDirectRecord.maxSize
                            if( iRec == nRecs ): nBits = nBits4Last                            
                            newName = recordName + ";" + str(iRec)                                  # Append the record name to the name                       
                            epicsRec = epicsRecords.mbbiDirectRecord( newName, array, nBits, iPos )
                            epicsRec.writeFile( inRecordFile )                               
                    # Also make mbboDirect records
                    if( nELM <= epicsRecords.mbboDirectRecord.maxSize ):
                        epicsRec = epicsRecords.mbboDirectRecord( recordName, array, nELM )
                        epicsRec.writeFile( outRecordFile )   
                    else :
                        # Split into multiple mbboDirect records
                        nRecs = int( math.ceil( float(nELM) / epicsRecords.mbboDirectRecord.maxSize ) )  # Number of records
                        nBits4Last = nELM % epicsRecords.mbboDirectRecord.maxSize                   # Number of bits in the last record
                        for iRec in range(nRecs):
                            iPos = iRec * epicsRecords.mbboDirectRecord.maxSize                     # Position to start from
                            nBits = epicsRecords.mbboDirectRecord.maxSize
                            if( iRec == nRecs ): nBits = nBits4Last  
                            newName = recordName + ";" + str(iRec)                                  # Append the record name to the name                         
                            epicsRec = epicsRecords.mbboDirectRecord( newName, array, nBits, iPos )
                            epicsRec.writeFile( outRecordFile )                           
        else: 
            # If the name is too long do not generate the corresponding record, save it in the list and 
            # print out the failed record names at the end. 
            longTagDataList.extend( [array] ) 

inRecordFile.close()            # Close the file for input records 
outRecordFile.close()           # Close the file for the output records
arrayRecordFile.close()         # Close the array record file 
autoSaveFile.close()            # Close the auto save request file for fields
                
# Print out which tags did not generate EPICS records because of  the EPICS record length
print "Skipped the following PLC tags because of length (>{0} chars)".format( maxRecordNameLength4EPICS )
for scalarData in longTagDataList:
    print scalarData.name 
    
exit(0)
    
#print "Printing arrays"    
#arraysList = newCtrler.getArraysList4EPICS()
#for array in arraysList:
#    print array
     
