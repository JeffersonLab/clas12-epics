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


#include <linux/limits.h>
#include <decaf/lang/Thread.h>
#include <decaf/lang/Runnable.h>
#include <decaf/util/concurrent/CountDownLatch.h>
#include <decaf/lang/Long.h>
#include <decaf/util/Date.h>
#include <activemq/core/ActiveMQConnectionFactory.h>
#include <activemq/util/Config.h>
#include <activemq/library/ActiveMQCPP.h>
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
#include <memory>
#include <RootMQ.h>

using namespace activemq;
using namespace activemq::core;
using namespace decaf;
using namespace decaf::lang;
using namespace decaf::util;
using namespace decaf::util::concurrent;
using namespace cms;
using namespace std;

////////////////////////////////////////////////////////////////////////////////
class SimpleProducer{
  //class SimpleProducer : public Runnable {
private:

  Connection* connection;
  Session* session;
  Destination* destination;
  MessageProducer* producer;
  std::string brokerURI;
  bool isConnected;

private:

    SimpleProducer( const SimpleProducer& );
    SimpleProducer& operator= ( const SimpleProducer& );

public:

  SimpleProducer( const std::string& brokerURI ) :
    connection(NULL),
    session(NULL),
    destination(NULL),
    producer(NULL),
    brokerURI(brokerURI){
    
    isConnected=0;
    
    activemq::library::ActiveMQCPP::initializeLibrary();

    try{
      // Create a ConnectionFactory
      auto_ptr<ActiveMQConnectionFactory> connectionFactory( new ActiveMQConnectionFactory( brokerURI ) );
      
      // Create a Connection
      connection = connectionFactory->createConnection();
      
      connection->start();
      // Create a Session
      session = connection->createSession( Session::AUTO_ACKNOWLEDGE );
    }catch (CMSException& e) {           
      printf( "Warning - Failed to connect to AMQ Message Broker at \"%s\"\n",brokerURI.c_str());
      printf( "No messages will be sent to ActiveMQ\n");
      //e.printStackTrace();
      isConnected=0;
      return;
    } 
    
    isConnected = 1;
  }
  

  int SendMessage(const char *topic, char *msg){
    // Create the destination 
    destination = session->createTopic( topic );
    
    // Create a MessageProducer from the Session to the Topic or Queue
    producer = session->createProducer( destination );
    producer->setDeliveryMode( DeliveryMode::NON_PERSISTENT );
    
    // Create the Thread Id String
    string threadIdStr = Long::toString( Thread::currentThread()->getId() );
    
    // Create a messages
    string text = msg;
    
    TextMessage* message = session->createTextMessage( text );
    
    printf( "Sent message: \"%s\"\n", text.c_str() );
    producer->send( message );
    
    delete message;
    return 0;
  }
  bool GetConnectionStatus(){return isConnected;};
  
  virtual ~SimpleProducer(){
  }
    
  
private:

};

//This is a simple wrapper to allow ROOT to interact simply using a CLASS that doesn't require any c++-11 extensions
//for backward compatibility with ROOT 5.

static SimpleProducer *producer;

RootMQ::RootMQ(const char *broker_host){
  std::string brokerURI = broker_host;

  // Create the producer
  producer = new SimpleProducer( brokerURI);
  isConnected = producer->GetConnectionStatus();
  return;
}  

int RootMQ::SendMessage(const char *topic, char *msg){
  return producer->SendMessage(topic, msg);
}

//We could pull in a library for this json stuff or use ROOT: TBufferJSON
//But let's keep it simple for now with some good old fashioned c code.

void RootMQ::jStart(char *jstring){
  sprintf(jstring,"{");
}
void RootMQ::jEnd(char *jstring){
  strcat(jstring,"}");
}

void RootMQ::jAddInt(char *jstring, const char *name, int data, const char *format){
  if(strlen(jstring)>2) strcat(jstring,", ");
  sprintf(jstring+strlen(jstring),"\"%s\":",name);
  sprintf(jstring+strlen(jstring),format,data);
}
void RootMQ::jAddDouble(char *jstring, const char *name, double data, const char *format){
  if(strlen(jstring)>2) strcat(jstring,",");
  sprintf(jstring+strlen(jstring),"\"%s\":",name);
  sprintf(jstring+strlen(jstring),format,data);
  
}

void RootMQ::jAddString(char *jstring, const char *name, char *data){
  if(strlen(jstring)>2) strcat(jstring,",");
  sprintf(jstring+strlen(jstring),"\"%s\":\"%s\"",name,data);
}
void RootMQ::jAddJson(char *jstring, const char *name, char *data){
  if(strlen(jstring)>2) strcat(jstring,",");
  sprintf(jstring+strlen(jstring),"\"%s\":%s",name,data);
}

void RootMQ::jAddIntArray(char *jstring, const char *name, int *data, int len, const char *format){
  if(strlen(jstring)>2) strcat(jstring,", ");
  sprintf(jstring+strlen(jstring),"\"%s\":[",name);
  for(int n = 0; n<len;n++){
    sprintf(jstring+strlen(jstring),format,data[n]);
    if(n<len-1) strcat(jstring,",");
  }
  strcat(jstring,"]");
}

void RootMQ::jAddDoubleArray(char *jstring, const char *name, double *data, int len, const char *format){
  if(strlen(jstring)>2) strcat(jstring,", ");
  sprintf(jstring+strlen(jstring),"\"%s\":[",name);
  for(int n = 0; n<len;n++){
    sprintf(jstring+strlen(jstring),format,data[n]);
    if(n<len-1) strcat(jstring,",");
  }
  strcat(jstring,"]");
}

void RootMQ::jAddStringArray(char *jstring, const char *name, char **data, int len){
  if(strlen(jstring)>2) strcat(jstring,", ");
  sprintf(jstring+strlen(jstring),"\"%s\":[",name);
  for(int n = 0; n<len;n++){
    sprintf(jstring+strlen(jstring),"%s",data[n]);
    if(n<len-1) strcat(jstring,",");
  }
  strcat(jstring,"]");
}
  
  
