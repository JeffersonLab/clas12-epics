# csv2beast.py

Convert CSV to XML for BEAST configuration

Usage:
  csv2beast.py [FILE...] [DIR...]

  Excepts combinations of files and directories (default: ./).  Output file(s) will be the
  same as the input, only with xml extension.

Input format:
  Line 1: <config name>, <component 0>, <component 1>, <component N>, ...
  Line 2: column headers (Must start with pv)
  Line 3: data (Must start with pv name)

Input example:
  HallB, Torus, Vacuum
  pv, description, latching, annunciating, display title, display details
  B_TORUS:LC817A1, Torus Load Cell, true, true, Open Force GUI, /CLAS12_Share/blah-blah

Output example:
  <?xml version="1.0"?>
  <config name="HallB">
    <component name=" Torus">
    <component name=" Vacuum">
  		<pv name="B_TORUS:FOR:CCM_A:LC817A1">
  			<description>Torus Load Cell</description>
  			<latching>true</latching>
  			<annunciating>true</annunciating>
            <display>
                <title>Open Force GUI</title>
                <details</CLAS12_Share/blah-blah</details>
            </display>
		</pv>
    </component>
    </component>
  </config>

For use with EPICS build system:
  configure/CONFIG, add:
    FILE_TYPE += BEAST
    INSTALL_BEAST = $(INSTALL_LOCATION)/beast

  Db/Makefile, add:
    BEAST += myfile.xml

    ../%.xml: ../%.csv
        csv2beast.py $<

  This will generate and install the new xml file(s) when a csv is updated.

