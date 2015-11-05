
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <time.h>
#include <stdlib.h>
#include <TSystem.h>
#include <TRandom2.h>
#include <TROOT.h>

#include "Locations.H"
#include "ezcaRoot.h"

using namespace std;

enum EepicsType{                    EepicsBYTE, EepicsSTRING, EepicsSHORT, EepicsLONG, EepicsFLOAT, EepicsDOUBLE, EepicsNULL};
 const int   epicsTypeSize[]   = {            1,           32,           2,          8,           4,            8,          0};
const char *epicsTypeName[]   = {  "epicsBYTE","epicsSTRING","epicsSHORT","epicsLONG","epicsFLOAT","epicsDOUBLE",       NULL};

//gSystem->Load( "/home/mikef/ezcaRoot/lib/Linux64RH18/libRootEzca.so" );

void Test() {



}


void GenerateDatabase(){

  // This function generates the database from the outline file, as well as the xml file for creating the engine on the server.


  string line; 
  
  srand(time(NULL));
  
  
  // Database outline file
  ifstream outline;
  outline.open (OUTLINE);

  // Database file
  ofstream output;
  output.open(DATABASE);

  /* cout << "What is the name of the Archive Engine to be created?" << endl;
  string enginename;
  cin >> enginename;
  cout << "The engine is called " << enginename << endl;
  */
  
  // Archive Engine config file
  ofstream archive;
  archive.open(ARCHIVENAME".xml"); 

  // Alarm Server config file
  ofstream alarm;
  alarm.open(ALARMNAME".xml");

  // Create top of Archive config file
  archive << "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>" << endl;
  archive << "<engineconfig>" << endl;
 
  // Create top of Alarm config file
  alarm << "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>" << endl;
  alarm << "<config name=\""ALARMNAME"\">" << endl; 

  cout << "Reading outline file" << endl;

  // Read outline file
  if (outline.is_open())
    {
      while ( outline.good() )
	{
	  getline (outline, line);

	  // At this point want to check what the line is and 
	  // act on it appropriately

	  // If it starts with #, ie is a comment, ignore it
	  if (line.find("#") == 0) {continue;}

	  // If line is empty, ignore it
	  if (line.empty()){continue;}     


	  // Read the data into variables
	  istringstream ss(line); 	  
	  string PVname;
	  int noChan;
	  float min, max, smallAlarm, severeAlarm, deadband;
	  //              ^these are percentages^^^^^^^^^^^

	  ss >> PVname >> noChan >> max >> min >> smallAlarm >> severeAlarm >> deadband;
	  
	  cout << "Generating records for " << PVname << endl;

	  // Archive groups
	  archive << " <group>" << endl; 
	  archive << "    <name>"<<PVname<<"</name>" << endl;

	  //Alarm components
	  alarm << "  <component name=\"" << PVname << "\">" << endl;
	  alarm << "    <guidance> "<<endl;
	  alarm << "      <title>System Info</title>" << endl;
	  alarm << "      <details>This is info for this component</details>" << endl;
	  alarm << "    </guidance>"<<endl;


	 // Start generating records
	  for (int iii = 1; iii <= noChan; iii++)
	    {
	      // Really want to be checking what the data is and then be inserting it as appropriate...

	      // Insert the name of the channel
	      output << "record(ai, \"" << PVname << "_" << iii << "\"){" << endl;

	      // Starting value - random number between min and max
	      // Generate random floating point number between max and min value
	      float startVal = min + (float)rand()/((float)RAND_MAX/(max-min));
	      output << "\tfield(VAL, \""<< startVal << "\")" << endl;

	      //Raw VAl (used as 'initial' value to return to on reset)
	      output << "\tfield(EGUF, \""<< startVal << "\")" << endl;

	      // Small alarm
	      float smallrange = startVal / 100.0 * smallAlarm;
	      if (smallrange < 0) {smallrange=smallrange*-1;}

	      output << "\tfield(HIGH, \""<< startVal + smallrange << "\")" << endl;
	      output << "\tfield(HSV, \"MINOR\")" << endl;
	      output << "\tfield(LOW, \""<< startVal - smallrange << "\")" << endl;
	      output << "\tfield(LSV, \"MINOR\")" << endl;

	      // Severe alarm
	      float bigrange = startVal / 100.0 * severeAlarm;
	      if (bigrange < 0) {bigrange=bigrange*-1;}

	      output << "\tfield(HIHI, \""<< startVal + bigrange << "\")" << endl;
	      output << "\tfield(HHSV, \"MAJOR\")" << endl;
	      output << "\tfield(LOLO, \""<< startVal - bigrange << "\")" << endl;
	      output << "\tfield(LLSV, \"MAJOR\")" << endl;

	      // Operating Range
	      output << "\tfield(HOPR, \""<< startVal + ( startVal/100 * (severeAlarm * 1.5)) << "\")" << endl;
	      
	      output << "\tfield(LOPR, \""<< startVal - ( startVal/100 * (severeAlarm * 1.5)) << "\")" << endl;
	      
	      output << "\tfield(PREC, \"3\")"<<endl;

	      // Deadband
	      output << "\tfield(ADEL, \""<< startVal / 100.0 * deadband << "\")" <<endl;

	      // Disable fields
	      // If DISV==DISA record is disabled
	      output << "\tfield(DISV, \"0\")" << endl;
	      output <<  "\tfield(DISA, \"1\")" << endl;
	      // Close record
	      output << "}" << endl;


	      // Add channels to archive engine XML config file    
	      archive << "      <channel><name>" << PVname << "_" << iii << "</name><period>00:00:00.100</period><scan/></channel>" << endl;




	      // Add channels to Alarm config
	      
	      // these are to be split into groups of 20 so
	      if ((iii-1) % 20 == 0)
		{
		  if (iii!=1){alarm << "    </component>"<<endl;}
		  alarm << "    <component name=\""<<iii<<"-"<<iii+19<<"\">"<<endl;
		}
	      

	      alarm << "      <pv name=\""<<PVname<<"_"<<iii<<"\">"<<endl;
	      alarm << "        <description>channel "<<iii<< " of " << noChan << " for the " << PVname << " component</description>"<<endl;
	      alarm << "        <latching>true</latching> " << endl;
	      alarm << "        <annunciating>true</annunciating>" << endl;
	      alarm << "        <guidance>"<<endl;
	      alarm << "          <title>Help Info</title>"<<endl;
	      alarm << "          <details>Do something</details>"<<endl;
	      alarm << "        </guidance>"<<endl;
	      alarm << "      </pv>" << endl;

	    }
	  
	  archive << "  </group>"<<endl;

	  alarm << "    </component>"<<endl;
	  alarm << "  </component>"<<endl;


	  // Read next line

	}
     
      // Create record for the GUI 
      // Insert the name of the channel
      output << "record(ai, \"GUI\"){" << endl;
      output << "\tfield(DESC, \"blank\")" << endl;
      output << "\tfield(HOPR, \"0\")" << endl;
      output << "\tfield(LOPR, \"0\")" << endl;
      output << "\tfield(PREC, \"0\")"<<endl;
      output << "\tfield(DISA, \"1\")"<<endl;
      output << "}" << endl;

      // Place end of archive XML file
      //    archive << "  </group>" << endl;
      archive << "</engineconfig>"<<endl;

      // End of alarm xml file
      alarm << "</config>"<< endl;


      // After file has been completely read, close it and the output
      output.close();
      outline.close();
      archive.close();
      alarm.close();

      cout << "Database Created!" << endl;

      // Move XML files to appropriate folder
      gROOT->ProcessLine(".! mv " ARCHIVENAME ".xml " ARCHIVECONFIG);
      gROOT->ProcessLine(".! mv " ALARMNAME ".xml " ALARMCONFIG);

    }
  
  else cout << "unable to open file" << endl;
  
  return;
  
}


void LoadDatabase(){

  // inserts the generated database into a softIoc - needs fixed

  gROOT->ProcessLine(".! echo \"Loading into softIoc.\" ");
  gROOT->ProcessLine(".! softIoc iocsetup.cmd & ");
  gROOT->ProcessLine(".! bg ");
  gROOT->ProcessLine(".! echo \"softIoc is now running.\" ");
}

void StopDatabase(){

 cout << "Stopping SoftIoc" << endl;
  gROOT->ProcessLine(".! kill `pgrep softIoc`");

}

void GenerateEngines(){

  // Create archive engine
  //  cout << "Loading Archive Engine" << endl;
  // Delete old version
  // gROOT->ProcessLine(".! "ARCHIVECONFIG"ArchiveConfigTool -engine "ARCHIVENAME" -delete_config -pluginCustomization archivesettings.ini");
  // Load 
  //gROOT->ProcessLine(".! "ARCHIVECONFIG"ArchiveConfigTool -engine "ARCHIVENAME" -config "ARCHIVECONFIG""ARCHIVENAME".xml -import -steal_channels -pluginCustomization archivesettings.ini");
  //cout << "Archive Engine Loaded" << endl;


  // Create alarm server

  cout << "Loading Alarm Server" << endl;
  gROOT->ProcessLine(".! "ALARMCONFIG"AlarmConfigTool -root "ALARMNAME" -import -file "ALARMCONFIG""ALARMNAME".xml -pluginCustomization alarmsettings.ini");
  cout << "Alarm Server Loaded" << endl;


  

}
 
/*
void VaryDatabaseBG(){
  // This function will call the VaryDatabaseTerm function, but suppress its output to the background. APPARENTLY THIS CANT BE DONE SADFACE
  
  gROOT->ProcessLine(".! openvt root");
  // gROOT->SetBatch(kFALSE);
  }*/

void StartArchiveEngine() {

  cout << "Initiating Archive Engine" << endl;
  // Start
  gROOT->ProcessLine(".! "ARCHIVEEXE"ArchiveEngine -engine "ARCHIVENAME" -pluginCustomization archivesettings.ini &");
    // note there is an error if the engine is already running
  //  gSystem->Sleep(2000);
  cout << "Archive Engine is now running." << endl;

}

void StopArchiveEngine(){
 cout << "Killing Archive Engine" << endl;
  gROOT->ProcessLine(".! kill `pgrep ArchiveEngine`");

}


void StopArchiveEngineFF() {
  
  // This stops the engine, regardless of whether or not it was opened in the current shell, at the price of opening a firefox tab.
  gROOT->ProcessLine(".! firefox localhost:4812/stop &");
  
}

void StartAlarmServer(){

  cout << "Initiating Alarm Server" << endl;

  // start JMS server
  gROOT->ProcessLine(".! "ACTIVEMQ" start");

  gROOT->ProcessLine(".! "ALARMEXE"AlarmServer -root "ALARMNAME" -pluginCustomization alarmsettings.ini &");



}

void StopAlarmServer(){

  cout << "Killing Alarm Server" << endl;
  gROOT->ProcessLine(".! kill `pgrep AlarmServer`");

}

  void VaryDatabase(){
    // This function will vary a selection of the PV's every second, in the terminal.

    cout << "Randomising variables" << endl;

  // Get the initial value of the PV from the .db file

  ifstream database;
  database.open(DATABASE);

  string line;
  int size=0,iii=0;

// read database to calculate size of required array
  while ( database.good() )
    {
      getline (database, line);
      
      if (line.find("record")!=string::npos) {size++;}
    }

  database.close();

  // dynamic allocation of arrays
  string* name = new string[size];
  float* value = new float[size];
  
  //reopen database to populate arrays
  database.open(DATABASE);

  while(database.good())
    {

      getline (database, line);

      // Get the name of each PV
      if (line.find("record")!=string::npos)
	{
	  int end = line.rfind("{");
	  name[iii] = line.substr(12, end-14);
	  //	  cout << "name = " << name[iii] << endl;
	}

      // does "Line" contain "(EGUF"? If yes, collect value;
      size_t found = line.find("EGUF");
      size_t endofline = line.rfind("\"");
      if (found != string::npos)
	{
	  string val = line.substr(found+7, (endofline-found-7)); // String value
	  value[iii] = atof(val.c_str()); // Convert to float
	  iii++;
	}
      
    }

  database.close();
  iii = 0;

  // Now you have an array with each initial value contained in it.
TRandom2 r(0);

 



  //Randomise a random channel from 1-5
  while(1==1)
    {  
      // Randomise around that value
      
      iii = r.Uniform(0,5) ;
 
       int plus = r.Uniform(0,2);
       iii=iii+(200*plus);//include first 5 tof channels
      
      // cout << r << endl;

      double random = r.Gaus(value[iii], 10.0);
      //                    ^start val^ ^sigma^

      // Put the new value in the PV
      epicsPut((Char_t *)name[iii].data(), EepicsDOUBLE, 1, &random);
 
      cout << name[iii] << " starts at  " << value[iii] <<  " and is randomised to " << random << endl;
      
      
      gSystem->Sleep(500);
    }

  // Delete dynamic arrays
  delete[] name;
  delete[] value;

}



void DisplayCSS(){

  cout << "Opening CSS GUI" << endl;

  //This function opens the CSS GUI 
  gROOT->ProcessLine(".! "CSS" -data "CSSFILES" homepage.opi &");
  //gROOT->ProcessLine(".! "CSS" -data /home/bryanm/CSS-Workspaces/Default/CSS/homepage.opi&");

}

void DisplayMEDM(){

  //This functionality may be abandoned in future versions 


  //Show the MEDM GUI
  gROOT->ProcessLine(".! /home/epics/epics/extensions/bin/linux-x86_64/medm /home/mikef/epics/medmhomepage.adl &");
}


  void VaryDatabaseWander(){
    // This function will vary a selection of the PV's every second, in the terminal.


  // Get the initial value of the PV from the .db file

  ifstream database;
  database.open(DATABASE);

  string line;
  int size=0,iii=0;
  
  // read database to calculate size of required array
  while ( database.good() )
    {
      getline (database, line);
      
      if (line.find("record")!=string::npos) {size++;}
    }

  database.close();

  // dynamic allocation of arrays
  string* name = new string[size];
  float* value = new float[size];
  
  //reopen database to populate arrays
  database.open(DATABASE);

  while(database.good())
    {

      getline (database, line);

      // Get the name of each PV
      if (line.find("record")!=string::npos)
	{
	  int end = line.rfind("{");
	  name[iii] = line.substr(12, end-14);
	  	  cout << "name = " << name[iii] << endl;
	}

      // does "Line" contain "(EGUF,"? If yes, collect value;
      size_t found = line.find("EGUF");
      size_t endofline = line.rfind("\"");
      if (found != string::npos)
	{
	  string val = line.substr(found+7, (endofline-found-7)); // String value
	  value[iii] = atof(val.c_str()); // Convert to float
	  iii++;
	}
      
    }

  database.close();
  iii = 0;

  // Now you have an array with each initial value contained in it.
TRandom2 r(0);



  //Randomise a random channel from 1-5
 while(1)
    {  
      // Randomise around that value
      
      iii = r.Uniform(0,2) ;
 
      // int plus = r.Uniform(0,2);
      //  iii=iii+(200*plus);//include first 5 tof channels
      
      // cout << r << endl;


      double random = r.Gaus(value[iii], 10.0);
      //                    ^start val^ ^sigma^

      // Put the new value in the PV
      epicsPut((Char_t *)name[iii].data(), EepicsDOUBLE, 1, &random);
 
      cout << name[iii] << " starts at  " << value[iii] <<  " and is randomised to " << random << endl;

      //the line below ensure the value is randomised from the most recent value, not the initial value.
      value[iii]=random;

      gSystem->Sleep(500);
    }

 // Delete dynamic arrays!
 delete[] name;
 delete[] value;

}


void Help(){

  gROOT->ProcessLine(".! more "HELPFILE);

}


 void VaryDatabaseWhole(){
    // This function will vary a selection of the PV's every second, in the terminal.

   

   // Get the initial value of the PV from the .db file

   ifstream database;
   database.open(DATABASE);
   
   string line;
   int size=0,iii=0;
   
   // read database to calculate size of required array
   while ( database.good() )
     {
       getline (database, line);
       
       if (line.find("record")!=string::npos) {size++;}
     }
   database.close();
   
   // dynamic allocation of arrays
   string* name = new string[size];
   float* value = new float[size];
   
   //reopen database to populate arrays
   database.open(DATABASE);
   
   while(database.good())
     {
       
       getline (database, line);
       
       // Get the name of each PV
       if (line.find("record")!=string::npos)
	 {
	   int end = line.rfind("{");
	   name[iii] = line.substr(12, end-14);
	   
	 }
       
       // does "Line" contain "(EGUF"? If yes, collect value;
       size_t found = line.find("EGUF");
       size_t endofline = line.rfind("\"");
       if (found != string::npos)
	 {
	   string val = line.substr(found+7, (endofline-found-7)); // String value
	   value[iii] = atof(val.c_str()); // Convert to float
	   
	   iii++;
	 }
       
     }
   
   database.close();
   iii = 0;
   
   // Now you have an array with each initial value contained in it.
   TRandom2 r(0);

   cout << "Initialising..." << endl;
   // refresh each value to get rid of the "invalid" alarms
   for (int jjj=0; jjj < size; jjj++)
     {
       double tmp = value[jjj];
       epicsPut((Char_t *)name[jjj].data(), EepicsDOUBLE, 1, &tmp);

     }
   cout << "Randomising variables" << endl;
   
   while(1==1)
     {  
       // select random PV
       iii = r.Uniform(0,size) ;
       
       
       float sigma = 1.0;
       if (sigma < 0) 
	 sigma = sigma * -1;
       
       double random = r.Gaus(value[iii], sigma);
       //                    ^start val^ ^variation^
       
       // Put the new value in the PV
       epicsPut((Char_t *)name[iii].data(), EepicsDOUBLE, 1, &random);
       cout << name[iii] << "starts at " << value[iii] << "and becomes " << random << endl;
       
     }
   
   // Delete dynamic arrays
   delete[] name;
   delete[] value;
   
 }



void Start(){

  // Execute each function in sequence to create, load and execute a simulation.

  GenerateDatabase();
  //StopDatabase();
  //LoadDatabase();
  GenerateEngines();
  StopArchiveEngineFF();
  StartArchiveEngine();
  StopAlarmServer();
  StartAlarmServer();
  DisplayCSS();
  VaryDatabaseWhole();


}

