{
#include <RVersion.h>
  char amqlib[200];
  char amqdict[200];
  char newmacropath[500];
  char newincpath[500];
  
  //append the ROOTAMQ dir to the macropath
  sprintf(amqlib,"%s/libRootMQ.so",gSystem->Getenv("ROOTAMQ"));
  sprintf(amqdict,"%s/AutoDict_RootMQ_cxx.so",gSystem->Getenv("ROOTAMQ"));

  sprintf(newmacropath,"%s:%s",gROOT->GetMacroPath(),gSystem->Getenv("ROOTAMQ"));
  gROOT->SetMacroPath(newmacropath);
  sprintf(newincpath,"%s %s -I%s",gSystem->GetIncludePath(),"-I/usr/include/activemq-cpp-3.9.3 -I/usr/include/apr-1 -I/usr/include/json-c", 
  	  gSystem->Getenv("ROOTAMQ"));
  gSystem->SetIncludePath(newincpath);
  
  gSystem->Load("/usr/lib64/libactivemq-cpp.so");
  gSystem->Load("/usr/lib64/libjson-c.so");
  gSystem->Load(amqlib);
  
 //if root 5, generate and load dict to allow macros to do RootMQ things 
#if ROOT_VERSION_CODE < ROOT_VERSION(6,0,0)
  gInterpreter->GenerateDictionary("RootMQ","RootMQ.h");
  gSystem->Load(amqdict);
#endif
 
}
