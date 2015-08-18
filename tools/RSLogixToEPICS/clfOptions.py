#!/usr/bin/env python

import sys, string, getopt, os
import lxml.etree

from optparse import OptionParser

#------------------------------------------------------------------------------ 
#
# This file is only to handle the options for exectuing the sctipt to convert 
# RSLogix5000 tags into EPICS DB. It contains a class that handles options 
# from both the command line and from the configuration file. Command line options 
# and configuration file options shold not overlap, but if they do the configuration 
# file will override the command line option.
# 
#------------------------------------------------------------------------------ 

#===============================================================================
# Class to handle command line and config file options
#===============================================================================
class clfOptions:
    """ Class to handle command line options and configuration file options """
        
    # Constructor
    def __init__( self, argList ):
        self.optionDict = {}
        # Command line
        try:
            # Get options from command line, may get overriden by config file
            self.parseCommandLine( argList )  
        except getopt.GetoptError as errMsg:
            print errMsg
            self.printHelpMessage()
            sys.exit(-1)
        # Config file, first check if it exists. If it is not defined or does not 
        # exist, then it will do nothing. Note, that there is a default config file. 
        if( "ConfigFile" in self.optionDict.keys() and 
            os.path.exists( self.optionDict["ConfigFile"] ) ):
            try:
                # Read options from the config. file
                self.readConfigFile(  self.optionDict["ConfigFile"] )  
            except IOError as errMsg:
                # If I/O exception reaches here simply print the message and exit
                print errMsg
                sys.exit(-1)                        
        return
    
    
    # Read configuration XML file and append the option list extracted from the file
    def readConfigFile( self, fileName ):
        print "Reading config file"
        tree = lxml.etree.parse( fileName ) # parse the XML tree
        rootElm = tree.getroot()            # get the root element of the tree 

        # First get the list of regular expressions to ignore based on EPICS record names 
        self.optionDict["IgnoreEPICS_Record"] = self.getIgnoreEPICSList( rootElm )
        
        # Get the list of the RSLogix DataTypes that will need to be ignored 
        self.optionDict["IgnoreRSLogixDataType"] = self.getIgnoreRSLogixTypeList( rootElm )
        
        self.optionDict["IgnoreRSLogixDataTypePattern"] = self.getIgnoreRSLogixTypePatternList(rootElm)
        return
    
    
    # Parse command file and append the option list extracted from the command file
    def parseCommandLine( self, argList ):
        print "Starting command line parsing:", argList
        # Here I am using optparse module which may be obsolete in future Python versions 
        # This part might need to be redone for it to work with Python 3.1
        # Python does not seem to be forward or backward compatable
        parser = OptionParser(usage = "usage: %prog [options] ")
        parser.add_option( "-i", "--idb", 
                           action="store", dest="idb", type="string", metavar="InputDBFile", 
                           default="Input4EPICS.db", help="Define file name for input database to be produced" )
        parser.add_option( "-o", "--odb", 
                           action="store", dest="odb", type="string", metavar="OutDBFile", 
                           default="Output4EPICS.db", help="Define file name for output database to be produced" )
        parser.add_option( "-a", "--adb", 
                           action="store", dest="adb", type="string", metavar="ArratyDBFile", 
                           default="Arrays4EPICS.db", help="Define file name for database of arrays to be produced" )
        
        parser.add_option( "-c", "--cfgfile", 
                           action="store", dest="cfgfile", type="string", metavar="ConfigFile", 
                           default="convert.cfg", help="Define configuration file name to read" )
        
        parser.add_option( "-x", "--xmlfile", 
                           action="store", dest="xmlfile", type="string", metavar="XMLFile", 
                           default="TagExportTest.L5X", help="Define L5X XML file name for input" )

        parser.add_option( "-s", "--asfile", 
                           action="store", dest="asfile", type="string", metavar="AutoSaveFile", 
                           default="AutoSave.req", help="Define AutoSave file name for output" )
      
        parser.add_option( "-p", "--prefix", 
                           action="store", dest="prefix", type="string", metavar="PrefixEPICS", 
                           default="$(IOC):", help="Prefix for all EPICS records" )
        
        (opts, args) = parser.parse_args( argList )
        
        # Assign the elements of the dictionary to the parsed option values
        self.optionDict["InputDBFile"]  = opts.idb
        self.optionDict["OutputDBFile"] = opts.odb
        self.optionDict["ArrayDBFile"]  = opts.adb
        self.optionDict["AutoSaveFile"] = opts.asfile
        self.optionDict["ConfigFile"]   = opts.cfgfile
        self.optionDict["XMLFile"]      = opts.xmlfile
        self.optionDict["PrefixEPICS"]  = opts.prefix
      
        return
        
        
    # Find the the list of patterns of EPICS record names that should not go into EPICS 
    def getIgnoreEPICSList(self, rootElm):
        ignoreList = []
        ignoreEPICSElms = rootElm.xpath( "//Ignore[@type='EPICS_Record']" )
        for ignoreEPICSElm in ignoreEPICSElms :
            if "pattern" in ignoreEPICSElm.attrib.keys():
                print "Adding ", ignoreEPICSElm.attrib["pattern"] , " to the ignoreEPICSList"
                ignoreList.extend( [ignoreEPICSElm.attrib["pattern"]] )
            else:
                print "Cannot find <pattern> attribute in <{0}> XML tag ".format( ignoreEPICSElm.tag )
        return ignoreList
        
        
    # Find the the list of RSLogix DataTypes that should nbe ignored when reading the L5X file 
    def getIgnoreRSLogixTypeList(self, rootElm):
        ignoreList = []
        # Find XML tags Ignore with attribute "name" and attribute "type"  equal to "RSLogixDataType"
        ignoreDataTypeElms = rootElm.xpath( "//Ignore[@type='RSLogixDataType' and @name]" )
        for ignoreDataTypeElm in ignoreDataTypeElms :
            if "name" in ignoreDataTypeElm.attrib.keys():
                print "Adding ", ignoreDataTypeElm.attrib["name"] , " to the ignoreRSLogixTypeList"
                ignoreList.extend( [ignoreDataTypeElm.attrib["name"]] )
            else:
                print "Cannot find <name> attribute in <{0}> XML tag ".format( ignoreDataTypeElm.tag )
        return ignoreList
       
    # Find the the list of RSLogix DataTypes name patterns that should nbe ignored when reading the L5X file 
    def getIgnoreRSLogixTypePatternList(self, rootElm):
        ignoreList = []
        # Find XML tags Ignore with attribute "pattern" and attribute "type"  equal to "RSLogixDataType"
        ignoreDataTypeElms = rootElm.xpath( "//Ignore[@type='RSLogixDataType' and @pattern]" )
        for ignoreDataTypeElm in ignoreDataTypeElms :
            if( "pattern" in ignoreDataTypeElm.attrib.keys() ) :
                print "Adding ", ignoreDataTypeElm.attrib["pattern"] , " to the ignoreRSLogixTypePatternList"
                ignoreList.extend( [ignoreDataTypeElm.attrib["pattern"]] )
            else:
                print "Cannot find <pattern> attribute in <{0}> XML tag ".format( ignoreDataTypeElm.tag )
        return ignoreList
       
    # Return option for key optKey if exists, otherwise return None
    def getOption(self, optKey):
        if optKey in self.optionDict:
            return self.optionDict[optKey]
        else :
            return None


    # Returns the disctionary of all options
    def getOptions(self):
        return self.optionDict
    
# Get the options, both from command line and the configuratio file specified in the command line. 
# Simply declare one global variable in this file, and use it everywhere instead of working out how 
# create a singleton in Python. 
globOptions = clfOptions( sys.argv[1:] )
    
        
# This gets executed if used as main         
if ( __name__ == "__main__" ):
    args = sys.argv[1:]
#    cfgFileName = "/group/halld/Online/controls/epics/R3-14-12-2/app/scripts/RSLogixToEPICS/convert.cfg"        
    testOptions = globOptions
#    testOptions = clfOptions( args  )
    print "\n ***************  This is the printout ***************** \n \n"
    for optKey in sorted( testOptions.getOptions() ):
        print "Option ", optKey, " : ", testOptions.getOption(optKey) , "\n"
    
    
    
