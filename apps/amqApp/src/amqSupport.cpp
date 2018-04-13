/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

//This is based on the SimpleAsyncConsumer.cpp from the active-cpp distribution eg:
//activemq-cpp-library-3.9.4/src/examples/consumers/SimpleAsyncConsumer.cpp
//Runs as a thread, initialised from the IOC support (see amqMain.cpp).



#include <decaf/lang/Thread.h>
#include <decaf/lang/Runnable.h>
#include <decaf/util/concurrent/CountDownLatch.h>
#include <activemq/core/ActiveMQConnectionFactory.h>
#include <activemq/core/ActiveMQConnection.h>
#include <activemq/transport/DefaultTransportListener.h>
#include <activemq/library/ActiveMQCPP.h>
#include <decaf/lang/Integer.h>
#include <activemq/util/Config.h>
#include <decaf/util/Date.h>
#include <cms/Connection.h>
#include <cms/Session.h>
#include <cms/TextMessage.h>
#include <cms/BytesMessage.h>
#include <cms/MapMessage.h>
#include <cms/ExceptionListener.h>
#include <cms/MessageListener.h>
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <stddef.h>
#include <string.h>
#include <aiRecord.h>
#include <biRecord.h>
#include <stringinRecord.h>
#include <waveformRecord.h>

#include <dbAccess.h>
#include <devSup.h>
#include <recGbl.h>
#include <alarm.h>
#include <recSup.h>
#include <epicsExport.h>
#include <json-c/json.h>


#include "amqSupport.h"
extern "C" void addPV(void * addr, int type, char *key);
void json_epics(json_object *jtop, int isdeep);
void json_read_array( json_object *jobj, int indx );
void json_read_value( json_object *jobj, int indx );

//void json_parse_array( json_object *jobj, char *key);
void print_json_value(json_object *jobj);


using namespace activemq;
using namespace activemq::core;
using namespace activemq::transport;
using namespace decaf::lang;
using namespace decaf::util;
using namespace decaf::util::concurrent;
using namespace cms;
using namespace std;

typedef long (*fptr)(void *precord); //needed to call process(precord)

Thread *consumerThread;        //The main thread

#define MAXPV 1000              //Maximum number of PVs

static waveformRecord* rawmessage = NULL; //if we want to store the raw mwssage in a char waveform
static char *jsonKeyFull[MAXPV];          //json keys for all full names
static char *jsonKeyParts[MAXPV][10];     //parts (delimited with _) XXX_YYY##3_ZZZ_KEY
static int   jsonKeyNparts[MAXPV];        //nparts
static int   jsonKeyIndices[MAXPV][10];   //incices for array parts
static void *pvstructs[MAXPV];            //pointers to the structs for all the PVs
static int pvtypes[MAXPV];                //
static int npv=0;                         //counter
static int startFlag=0;                   //
//static double rawval;

////////////////////////////////////////////////////////////////////////////////
class SimpleAsyncConsumer : public ExceptionListener,
                            public MessageListener,
			    public Runnable,
                            public DefaultTransportListener {
private:
  
  Connection* connection;
  Session* session;
  Destination* destination;
  MessageConsumer* consumer;
  bool useTopic;
  std::string brokerURI;
  std::string destURI;
  bool clientAck;
  json_object *jobj;
  
private:
  
  SimpleAsyncConsumer(const SimpleAsyncConsumer&);
  SimpleAsyncConsumer& operator=(const SimpleAsyncConsumer&);
  StreamMessage *smessage;

public:
  
  SimpleAsyncConsumer(const std::string& brokerURI,
		      const std::string& destURI,
		      bool useTopic = false,
		      bool clientAck = false) :
    connection(NULL),
    session(NULL),
    destination(NULL),
    consumer(NULL),
    useTopic(useTopic),
    brokerURI(brokerURI),
    destURI(destURI),
    clientAck(clientAck),
    jobj(NULL){
  }
  
  virtual ~SimpleAsyncConsumer() {
    this->cleanup();
  }
  
  void close() {
    this->cleanup();
  }
  
  virtual void run() {
    
    try {
      
      std::cout << "Running it" << std::endl;
      
      // Create a ConnectionFactory
      ActiveMQConnectionFactory* connectionFactory = new ActiveMQConnectionFactory(brokerURI);
      
      // Create a Connection
      connection = connectionFactory->createConnection();
      delete connectionFactory;
      
      ActiveMQConnection* amqConnection = dynamic_cast<ActiveMQConnection*>(connection);
      if (amqConnection != NULL) {
	amqConnection->addTransportListener(this);
      }
      
      connection->start();
      
      connection->setExceptionListener(this);
      
      // Create a Session
      if (clientAck) {
	session = connection->createSession(Session::CLIENT_ACKNOWLEDGE);
      } else {
	session = connection->createSession(Session::AUTO_ACKNOWLEDGE);
      }
      
      // Create the destination (Topic or Queue)
      if (useTopic) {
	destination = session->createTopic(destURI);
      } else {
	destination = session->createQueue(destURI);
      }
      
      // Create a MessageConsumer from the Session to the Topic or Queue
      consumer = session->createConsumer(destination);
      consumer->setMessageListener(this);
      std::cout << "Listening" << std::endl;
      
    } catch (CMSException& e) {
      e.printStackTrace();
    }
  }
  
  // Called from the consumer since this class is a registered MessageListener.
  virtual void onMessage(const Message* message) {
    
    if(!startFlag) return;
    //if(strcmp(message->getCMSType().c_str(),"json")==0){
    //  fprintf(stderr,"Message Type = %s\n", message->getCMSType().c_str());
    // }
    smessage = (StreamMessage*)message;  
    static int count = 0;
    rset* prset;
    uint copy=0;
    int isdeep=0;
    try {
      count++;
      const TextMessage* textMessage = dynamic_cast<const TextMessage*>(message);
      string text = "";
      
      if (textMessage != NULL) {
	text = textMessage->getText();
      }
      else{
	text = smessage->readString();
      }
      if(strlen(text.c_str())>6){
	//std::cout << "Full Message = " << text.c_str() << endl;
	if(rawmessage){                 //if theres a RAWMSG record copy up to NELM of the message to the waveform
	  copy=strlen(text.c_str());    //try to copy the whole thing
	  if(copy>rawmessage->nelm){    //but chop if not enough space in the waveform
	    copy=rawmessage->nelm;
	  }
	  dbScanLock((dbCommon*)rawmessage);
	  strncpy((char *)(rawmessage->bptr),text.c_str(),copy);
	  rawmessage->nord = copy;
	  prset=(rset*)rawmessage->rset;
	  ((fptr)(prset->process))((dbCommon*)rawmessage);
	  dbScanUnlock((dbCommon*)rawmessage);
	}
	if(npv){
	  //text.insert (0, 1, '{');
	  //text.append(1, '}');
	  jobj = json_tokener_parse(text.c_str());
	  if(jobj!=NULL){
	    if(strchr(text.c_str()+1,'{')){  //if there's another "{" after the start, it has some nesting.
	      isdeep=1;
	    }
	    json_epics(jobj,isdeep);
	  }
	    else{ 
	      //	  std::cout << "Not a json thing. Here's the raw text" << std::endl;
	      //	  std::cout << "Full Message = " << text.c_str() << endl;
	    }
	}
      }
      
      if (clientAck) {
	message->acknowledge();
      }
      
    } catch (CMSException& e) {
      e.printStackTrace();
    }
  }
  
  // If something bad happens you see it here as this class is also been
  // registered as an ExceptionListener with the connection.
  virtual void onException(const CMSException& ex AMQCPP_UNUSED) {
    printf("CMS Exception occurred.  Shutting down client.\n");
    exit(1);
  }
  
  virtual void onException(const decaf::lang::Exception& ex) {
    printf("Transport Exception occurred: %s \n", ex.getMessage().c_str());
  }
  
  virtual void transportInterrupted() {
    std::cout << "The Connection's Transport has been Interrupted." << std::endl;
  }
  
  virtual void transportResumed() {
    std::cout << "The Connection's Transport has been Restored." << std::endl;
  }
  
private:
  
  void cleanup(){
    
    //*************************************************
    // Always close destination, consumers and producers before
    // you destroy their sessions and connection.
    //*************************************************
    
    // Destroy resources.
    try{
      if( destination != NULL ) delete destination;
    }catch (CMSException& e) {}
    destination = NULL;
    
    try{
      if( consumer != NULL ) delete consumer;
    }catch (CMSException& e) {}
    consumer = NULL;
    
    // Close open resources.
    try{
      if( session != NULL ) session->close();
      if( connection != NULL ) connection->close();
    }catch (CMSException& e) {}
    
    // Now Destroy them
    try{
      if( session != NULL ) delete session;
    }catch (CMSException& e) {}
    session = NULL;
    
    try{
      if( connection != NULL ) delete connection;
    }catch (CMSException& e) {}
    connection = NULL;
  }
};

SimpleAsyncConsumer *consumer;  //global prt to allow to be started as thread (see below)

// 
////////////////////////////////////////////////////////////////////////////////
void initConsumer(const char *broker_host, const char *topic) {

  activemq::library::ActiveMQCPP::initializeLibrary();
  std::string brokerURI = broker_host;
  std::string destURI = topic;
  bool useTopics = true;
  bool clientAck = false;

  // Create the consumer
  consumer = new SimpleAsyncConsumer( brokerURI, destURI, useTopics, clientAck );
  
  // Start the consumer thread.
  consumerThread = new Thread(consumer);
  consumerThread->start();
  consumerThread->join();
  
  // Wait for the consumer to indicate that its ready to go.
  //consumer.waitUntilReady();
  
  return;
}

  void closeConsumer(){
  
  // All CMS resources should be closed before the library is shutdown.
  consumer->close();  
  activemq::library::ActiveMQCPP::shutdownLibrary();
}

//called fron IOC after all records loaded
void startConsumer(){
  startFlag=1;
}

//called from init_record to save addr of record, type and related json key 
void addPV(void *addr, int type, char* key){
  char *lastu;
  char *thisu;
  std::cerr << "Adding key" << key <<  std::endl;

  if((type==EWaveform)&&strstr(key,"RAWMSG")){  //If waveform with RAWMSG in key, 
    rawmessage = (waveformRecord*)addr;         //save as special
    std::cerr << "Raw messages will go into " << rawmessage->name << std::endl;
    return;
  }    

  pvstructs[npv] = addr;                           //save address as a void
  
  jsonKeyFull[npv] = new char[strlen(key)+1];      //save the full name
  strcpy(jsonKeyFull[npv],key);
  
  //The key will be specified like this  AAA_BBB_CCC##3_DDD_THING (hopeully simpler)
  //                                     obj obj arr[3] obj item

  jsonKeyNparts[npv]=0;
  lastu=key;
  while((thisu=strchr(lastu,'_'))){                                      //find underscore
    jsonKeyParts[npv][jsonKeyNparts[npv]] = new char[(thisu-lastu)+1];   //make string for it
    strncpy(jsonKeyParts[npv][jsonKeyNparts[npv]],lastu,(thisu-lastu));  //copy to it
    strcpy(jsonKeyParts[npv][jsonKeyNparts[npv]]+(thisu-lastu),"");      //terminate
    lastu=thisu+1;                                                       //move past the "_"
    jsonKeyNparts[npv]++;                                                //increment the counter
  }
  
  jsonKeyParts[npv][jsonKeyNparts[npv]] = new char[strlen(lastu)];       //so copy full key
  strcpy(jsonKeyParts[npv][jsonKeyNparts[npv]],lastu);

  jsonKeyNparts[npv]++;                                                  //increment the counter



  pvtypes[npv]   = type;                                                  //save type
  std::cerr << "PV "<< npv << "parts: ";

  for(int n=0;n<jsonKeyNparts[npv];n++){                                  //see if this is an element in an array
    jsonKeyIndices[npv][n]=-1;                                            //delimited by ##.
    if((lastu=strstr(jsonKeyParts[npv][n],"##"))){                        //if so, save the index
      sscanf(lastu+2,"%d",&jsonKeyIndices[npv][n]);
      strcpy(lastu,"");                                                   //strip off the ##N part
      std::cerr << jsonKeyParts[npv][n] << "[" << jsonKeyIndices[npv][n] << "] ";
    }
    else{
      std::cerr << jsonKeyParts[npv][n] << " ";
    }
  }
  std::cerr << std::endl;
  
  npv++;
}


/*printing the value corresponding to boolean, double, integer and strings*/
void print_json_value(json_object *jobj){
  //enum json_type type;
  //printf("type: ",type);
  int type = json_object_get_type(jobj); /*Getting the type of the json object*/
  switch (type) {
    case json_type_boolean: printf("json_type_boolean\n");
                         printf("value: %sn", json_object_get_boolean(jobj)? "true": "false");
                         break;
    case json_type_double: printf("json_type_doublen");
                        printf("          value: %lf\n", json_object_get_double(jobj));
                         break;
    case json_type_int: printf("json_type_intn");
                        printf("          value: %d\n", json_object_get_int(jobj));
                         break;
    case json_type_string: printf("json_type_stringn");
                         printf("          value: %sn", json_object_get_string(jobj));
                         break;
  }
}

/*printing the value corresponding to boolean, double, integer and strings*/
void json_read_value(json_object *jobj, int indx ){
  void *prec = pvstructs[indx];
  char *key = ((dbCommon*)(prec))->name;
  int pvtype= pvtypes[indx];
  rset* prset;
  
  enum json_type type = json_object_get_type(jobj); /*Getting the type of the json object*/
  double aival=0.0;

  //printf("Trying to write %s %d %d %d %d\n",key,type, json_type_boolean,json_type_double, json_type_int );

  switch (type) {
  case json_type_boolean:
    //printf("Trying to Bool write %s \n",key);
    if((pvtype!= EAi)&&(pvtype != EBi)){         //bool can go to Ai or Bi record
      printf("Warning: key=%s is Json boolean - needs to go to EPICS Ai or Bi record\n",key);
      return;
    }
    if(json_object_get_boolean(jobj)) aival=1.0;
    
    dbScanLock((dbCommon*)prec);
    if(pvtype==EAi)((aiRecord*)(prec))->val = aival;
    else ((biRecord*)(prec))->val = (int)aival;
    ((dbCommon*)prec)->udf = FALSE;

    prset=(rset*)((dbCommon*)prec)->rset;
    ((fptr)(prset->process))((dbCommon*)prec);
    dbScanUnlock((dbCommon*)prec);
    
    break;
    
  case json_type_double:
    //printf("Trying to Double write %s \n",key);
    if(pvtype != EAi){         //Double must go to Ai record
      printf("Warning: key=%s is Json double - needs to go to EPICS Ai record\n",key);
      return;
    }
    dbScanLock((dbCommon*)prec);
    ((aiRecord*)(prec))->val = json_object_get_double(jobj);
    ((dbCommon*)prec)->udf = FALSE;
    prset=(rset*)((dbCommon*)prec)->rset;
    ((fptr)(prset->process))((dbCommon*)prec);
    dbScanUnlock((dbCommon*)prec);
    
    break;
    
  case json_type_int:
    //printf("Trying to Int write %s \n",key);
    if(pvtype != EAi){         //Int must go to Ai record
      printf("Warning: key=%s is Json int - needs to go to EPICS Ai record\n",key);
      return;
    }
    dbScanLock((dbCommon*)prec);
    ((aiRecord*)(prec))->val = (double)json_object_get_int(jobj);
    ((dbCommon*)prec)->udf = FALSE;
    prset=(rset*)((dbCommon*)prec)->rset;
    ((fptr)(prset->process))((dbCommon*)prec);
    dbScanUnlock((dbCommon*)prec);
    
    break;
    
  case json_type_string: 
    //printf("Trying to string write %s \n",key);
    if((pvtype != EString)&&(pvtype != EWaveform)){  // string must go into must go to stringin or waveform
      printf("Warning: key=%s is Json string - needs to go to EPICS stringin or waveform record\n",key);
      return;
    }
    dbScanLock((dbCommon*)prec);
    if(pvtype == EString){
      strncpy(((stringinRecord*)(prec))->val,json_object_get_string(jobj),40);
    }
    else{
      strncpy((char *)((waveformRecord*)(prec))->bptr,json_object_get_string(jobj),(int)(((waveformRecord*)(prec))->nelm));
      if(strlen(json_object_get_string(jobj))>(((waveformRecord*)(prec))->nelm)) ((waveformRecord*)(prec))->nord = ((waveformRecord*)(prec))->nelm;
      else ((waveformRecord*)(prec))->nord = strlen(json_object_get_string(jobj));
    }
    ((dbCommon*)prec)->udf = FALSE;
    prset=(rset*)((dbCommon*)prec)->rset;
    ((fptr)(prset->process))((dbCommon*)prec);
    dbScanUnlock((dbCommon*)prec);
    break;

  default:
    printf("BREAK - Key type %s %d\n",key,type);
    break;
  }
}


void json_read_array( json_object *jobj, int indx) {   //got here because it's a json array who key matches that of an epics PV in the list
  enum json_type type;
  json_object * jvalue;
  rset* prset;

  int pvtype= pvtypes[indx];                           //find the type of the PV
  void *prec = pvstructs[indx];                        //get the record for the PV
  char *key = ((dbCommon*)(prec))->name;
  char *pvname = ((dbCommon*)prec)->name;              //find name of PV

  if(pvtype != EWaveform){
    printf("Warning PV %s is not a waveform, but needs to be to read json array object %s \n", pvname, key);
    return;
  }
  
  int arraylen = json_object_array_length(jobj);       //Getting the length of the array
  int ncopy = arraylen;                                //default to copying full arrray

  waveformRecord * wrec = (waveformRecord*)(prec);     //cast to waveform
  double *bptr_d = (double *)(wrec->bptr);             //cast the waveform buffer as int and double
  float *bptr_f = (float *)(wrec->bptr);               //cast the waveform buffer as int and double
  int *bptr_i = (int *)(wrec->bptr);
  int wavelen = wrec->nelm;                            //find no of elements in waveform

  if(arraylen>wavelen){                                //check that the waveform is big enough
    ncopy=wavelen;
    printf("Warning PV %s.NELM = %d, but json array %s has %d elements. Cutting off the end! \n", pvname, wavelen,key,arraylen);
  }
  
  //we'll assume all values are the same as the 1st int the array.
  jvalue = json_object_array_get_idx(jobj, 0); 
  type = json_object_get_type(jvalue);

  if((type==json_type_double)||(type==json_type_int)){ //only int and double
    switch (type){
    case json_type_double:
      if((wrec->ftvl != DBR_DOUBLE)&&(wrec->ftvl != DBR_FLOAT)){
	printf("Warning PV %s.FTVL needs to be DOUBLE or FLOAT for json array %s. Not filling waveform!\n",pvname,key );
	break;
      }
      dbScanLock((dbCommon*)prec);
      if(wrec->ftvl==DBR_DOUBLE){
	for (int i=0; i<ncopy; i++){
	  jvalue = json_object_array_get_idx(jobj, i);
	  bptr_d[i]=json_object_get_double(jvalue);      //fill the buffer with doubles
	}
      }
      else if(wrec->ftvl==DBR_FLOAT){
	for (int i=0; i<ncopy; i++){
	  jvalue = json_object_array_get_idx(jobj, i);
	  bptr_f[i]=(float)json_object_get_double(jvalue);      //fill the buffer with floats
	}
      }
      wrec->nord=ncopy;
      prset=(rset*)((dbCommon*)prec)->rset;
      ((fptr)(prset->process))((dbCommon*)prec);
      dbScanUnlock((dbCommon*)prec);

      break;
    case json_type_int:
      if(wrec->ftvl==DBR_DOUBLE){
	dbScanLock((dbCommon*)prec);
	for (int i=0; i<ncopy; i++){
	  jvalue = json_object_array_get_idx(jobj, i);
	  bptr_d[i]=(double)json_object_get_int(jvalue);
	}
      }
      else if(wrec->ftvl==DBR_FLOAT){
	dbScanLock((dbCommon*)prec);
	for (int i=0; i<ncopy; i++){
	  jvalue = json_object_array_get_idx(jobj, i);
	  bptr_f[i]=(float)json_object_get_int(jvalue);
	}
      }
      else if(wrec->ftvl==DBR_LONG){
	dbScanLock((dbCommon*)prec);
	for (int i=0; i<ncopy; i++){
	  jvalue = json_object_array_get_idx(jobj, i);
	  bptr_i[i]=json_object_get_int(jvalue);
	}
      }
      else{
      	printf("Warning PV %s.FTVL needs to be LONG, FLOAT or DOUBLE for json array %s. Not filling waveform!\n",pvname,key );
      	break;
      }

      wrec->nord=ncopy;
      prset=(rset*)((dbCommon*)prec)->rset;
      ((fptr)(prset->process))((dbCommon*)prec);
      dbScanUnlock((dbCommon*)prec);
      break;
      
    default:
      break;
    }
  }
}


void json_epics(json_object *jtop, int isdeep){ 

        
  //Need to decode something like this: AAA_BBB_CCC##3_DDD_THING
  //                                    obj obj arr[3] obj item
  //
  enum json_type type = json_type_null;
  json_object *value;
  json_object *jobj;
  
  
  for(int n=0;n<npv;n++){                  //check all the keys which are for EPICS PVs

    if(isdeep==0){                         //no nesting all at top level in json string
      if(json_object_object_get_ex(jtop,jsonKeyFull[n],&value)){ //So look for full key
	type = json_object_get_type(value);
	switch (type){
	case json_type_boolean:
	case json_type_double:
	case json_type_int:
	case json_type_string:
	  json_read_value(value,n);
	  break;
	case json_type_array:
	  json_read_array(value,n);
	  break;
	default:
	  break;
	}
      }
    }

    else{                                    //some depth - so interpret the nesting from the name       
      jobj=jtop;                             //point to the top level jobj
      for(int p=0;p<jsonKeyNparts[n];p++){   //go over all the parts
	//printf("looking for %s\n",jsonKeyParts[n][p]);
	if(!json_object_object_get_ex(jobj,jsonKeyParts[n][p],&value)) break;  //break if key not found
	//printf("found %s\n",jsonKeyParts[n][p]);
	type = json_object_get_type(value);
	if(p<jsonKeyNparts[n]-1){             //must be a jobj or array#index, since before the _THING part
	  if(type == json_type_object){
	    jobj=value;
	    continue;                         //make this the jobs for the next item
	  }
	  else if((type == json_type_array)&&(jsonKeyIndices[n][p]>-1)){    //array with index
	    value = json_object_array_get_idx(value, jsonKeyIndices[n][p]);
	    type = json_object_get_type(value);
	    if(type != json_type_object)break;
	    jobj=value;
	    continue;                         //make this the jobs for the next item
	  }
	  else break;                         //not found, break
	}
	
	else{                                 // at the _THING part - its an actual value
	
	  if(jsonKeyIndices[n][p]>-1){
	    value = json_object_array_get_idx(value, jsonKeyIndices[n][p]);
	    type = json_object_get_type(value);
	  }
	  switch (type){
	  case json_type_boolean:
	  case json_type_double:
	  case json_type_int:
	  case json_type_string:
	    json_read_value(value,n);
	    break;
	  case json_type_array:
	    json_read_array(value,n);
	    break;
	  default:
	    break;
	  }
	}
      }
    }
  }
  json_object_put(jtop);
}
  
// void json_parse_array( json_object *jobj, char *key) {
//   enum json_type type;
//   json_object *jarray = jobj; /*Simply get the array*/
  
//   int arraylen = json_object_array_length(jarray); /*Getting the length of the array*/
//   //printf("Array Length: %dn",arraylen);
//   int i;
//   json_object * jvalue;
  
//   for (i=0; i< arraylen; i++){
//     jvalue = json_object_array_get_idx(jarray, i); /*Getting the array element at position i*/
//     type = json_object_get_type(jvalue);
//     if (type == json_type_array) {
//       json_parse_array(jvalue,key);
//     }
//     if (type == json_type_object) {
//       json_epics(jvalue);
//     }
//   }
// }
