1. Introduction

These scripts for converting the L5X file from RSLogix5000 were originally 
created for interfacing the Hall D solenoid magnet controls in PLC to Hall D
EPICS-based control system. Because the L5X is a complex file which can contain 
all the information about the  RSLogix5000 project, and since the documentation 
on the tags and attributes in the L5X file is far from being complete, these 
scripts will not be able to generate all the tags from all L5X files. In some cases 
more coding may need to be done to add extra functionality. This README file 
attempts to describe what has been implemented in the current version of the 
conversion scripts. 


2. How it works 

The purpose of these Python scripts with to build an EPICS database for interfacing 
a Allen-Bradley RSLogix 5000 project exported into an L5X file. L5X file is an XML 
file that can contain all the necessary information to create an ACD file file. 
The conversion process can be broken up into two consecutive stages: XML file parsing and 
EPICS database construction. 

a) XML parsing
In the first stage the XML file is parsed to find certain types of tags with 
the final objective of identifying all the tags in the RSLogix that can be (or need to be) 
present in EPICS database. Each L5X file contains at least one "Controller" tag, 
which in turn contains  "Modules" and "Programs" tags. It also can "Tags" tag, 
which will contain all the controller-scoped PLC tags. Each of the "Modules" and 
"Programs" nodes contain definitions of all the modules and programs in that 
RSLogix5000 project, which eventually contain the definition of program-scoped 
tags and the tags associated with each instance of the hardware modules. 

Sometimes generating all possible EPICS records that can match the PLC tags 
is not necessary. In fact, if the number of independent EPICS 32-bit variables 
obtain from a single PLC is larger than ten thousand then the update rate of 
EPICS records via "eter_ip" EPICS driver can be on the order of ten seconds, which 
often might be unacceptable. For such cases the scripts allow for a possibility to 
ignore some RSLogix data types based on their exact name or regular expressions. 
One can also prevent some of the resulting EPICS variables from being written 
into the DB-files by using regular expressions. Note, that there is a difference 
between the two way of reducing the number of the resulting EPICS records. If one chooses 
to reject based on PLC data-type, then any tag of the specified data-type is completely 
ignored and is not read from the XML file. Therefore, it will not be used when 
trying to resolve the aliases. When excluding EPICS records based on their name 
only the EPICS records matching the particular pattern specified by the regular 
expressions will be dropped. 
  
b) EPICS database construction
Once the XML file has been parsed and the lists of all atomic tags are compiled 
the script starts generating the EPICS database files. The EPICS records are 
defined such that they will work with "ether_ip" driver. A version of the  manual 
of the "ether_ip" should come with the rest of the scripts file and this file. 
The features of the driver define what types of EPICS records can be created and 
what kind of Allen-Bradley tags they should correspond to. 

In this application we try to preserve the name of the PLC tags in the EPICS 
database so that it was possible to uniquely identify what PLC tag each EPICS 
record correspond to without maintaining any translation tables. Since "." is 
reserved in EPICS record names to separate different field of the record, we 
translate "." character in RSLogix tag name to "-" character in EPICS. Also 
we drop "Program" prefix from the name of the program-scoped tags since this 
does not carry any information. 
o Each controller-scoped PLC tag corresponds to an EPICS record with the same 
name, but prepended with an "$(IOC):" prefix. This prefix can be changed from the 
command line. 
o Each program-scoped tag corresponds to an EPICS record with the same name, 
but prepended with "$(IOC)::" prefix, followed by the program name and the rest 
of the PLC tag name. Basically, two consecutive semicolumns indicate that this is 
a program scoped tag. 

The script will generate "bi", "bo", "mbbiDirect", "mbboDirect", "ai", "ao" and "waveform" 
EPICS records. The "waveform" type is used to read into EPICS RSLogix arrays of DINT and REAL types. 
These types of arrays in PLC cannot be written from EPICS waveforms, the communication for the waveforms 
is unidirectional.  But  "bi", "bo" records are used for bi-directional communication with RSLogix "BOOL" 
types and aliases to "BIT" elements of PLC arrays. "ai" and "ao" records are used for communicating 
with "SINT", "INT", "DINT" and "REAL" tags in PLC. The arrays of bits from the PLC programs 
are matched to "mbbiDirect" and "mbboDirect" records. Since the number of bits for 
"mbbiDirect" and "mbboDirect" is limited to 16, the script splits the bit arrays longer than 
sixteen elements into multiple EPICS records with the same name but with a suffix indicating 
the number of the 16-bit EPICS record. The suffix is separate from the rest of the EPICS 
record name by ";" character. 


3. Usage instructions

In order to be able run these scripts one needs to install Python 2.6, including "lxml" 
package. There are many Python script files, but the main file is "convertRSLogix2EPICS.py" 
which contains the main execution block. Below is the syntax for running the conversion 
script


Usage: convertRSLogix2EPICS.py [options] 

Options:
  -h, --help            show this help message and exit
  -i InputDBFile, --idb=InputDBFile
                        Define file name for input database to be produced
  -o OutDBFile, --odb=OutDBFile
                        Define file name for output database to be produced
  -a ArratyDBFile, --adb=ArratyDBFile
                        Define file name for database of arrays to be produced
  -c ConfigFile, --cfgfile=ConfigFile
                        Define configuration file name to read
  -x XMLFile, --xmlfile=XMLFile
                        Define L5X XML file name for input
  -p PrefixEPICS, --prefix=PrefixEPICS
                        Prefix for all EPICS records

Here, "InputDBFile" is the name of the file that contains the "scalar" EPICS records 
for input to EPICS.   "OutDBFile" corresponds to the DB-file containing the scaler 
EPICS records for input into PLC. ArratyDBFile indicates the filename for the 
DB-file with waveform records for input into EPICS. "ConfigFile" is the name of 
the configuration file to be read, and "XMLFile" is the name of the L5X file  
containing the exported RSLogix 5000 project. "PrefixEPICS" is the desired prefix to use 
for all EPICS records when constructing EPICS database and it needs to be a macro, like 
$(PREFIX). 

While running, the program may need to to multiple passes over the XML tree in order 
to resolve all the alias tags in RSLogix project. If after a pass there are unresolved 
aliases, the script will print the number of the unresolved aliases and wait for 
the user to hit "Return" button, after which it will do another pass. After each 
iteration the number of unresolved aliases should decrease. If it stays constant, 
then there must be a problem either with the L5X file (not all of the project has been 
exported), or there is a bug in the script. When all alias target have been identified 
the program will print the tag name which were skipped due to unacceptably long 
EPICS variable names that were skipped and will stop. 
    
The script will generate three files: one for input type records, one for the output 
type records, and another one for arrays. The record name in the files do not contain any 
inforamtion about if they are for input ot ouput, so if one loads both the input files and 
the output files with the same value for the prefix macro then the input and out records 
name will be identical and this wil result in IIC initialization failure. Therefore, one 
needs to assign different values to prefix macro for the input an output record files, for 
instance the commands in the IOC script can look like this:
 
...
dbLoadRecords ( "Input4EPICS.db" ,  "IOC="gluon01:i",PLCID=hallden2t1" )
dbLoadRecords ( "Output4EPICS.db",  "IOC="gluon01:o",PLCID=hallden2t1" )
dbLoadRecords ( "Arrays4EPICS.db",  "IOC="gluon01:i",PLCID=hallden2t1" )
...

4. Still to be implemented 

o Ignore RSlogix data types that have names identical to any of the add-on instruction 
definition names.
o Add a class to handle DataTypes XML tags in the L5X file inorder to be able to handle 
PLC tags that do not have their description within their nodes. 

