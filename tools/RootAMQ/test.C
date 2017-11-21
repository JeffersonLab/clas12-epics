//Example of how to send ROOT data to activeMQ in json format.
//Run like this:
// in .cshrc / .bashrc set the env variable AMQROOT to this directory

//For this demo.
//root $AMQROOT/mqLoad.C $AMQROOT/test.C
//.. or your own code
//root $AMQROOT/mqLoad.C  myRootCode.C


#include <stdlib.h>
#include <stdio.h>
#include <TRandom.h>
#include <TSystem.h>
#include "RootMQ.h"

RootMQ *mq;     //RootMQ class
char js[500];   //the json string
TRandom *r;     //random generator

void test(){
  
  //create some variables to test
  int EventRate;
  double LiveTime;
  int TestScalers[20];
  double TestVals[20];

  r = new TRandom();  //and a randomizer for them
  

  mq=new RootMQ("tcp://clondb1:61616");  //create mq and try to connect
  //  mq=new RootMQ("tcp://junk:61616");  //create mq and try to connect

  if(mq->GetConnectionStatus()==1){
    printf( "Successfully connected to ActiveMQ\n");    //if not is will print it's own warnings
  }
  else return;
  
  
  while(1){
    
    //fill the variables then make the json string, then send to mq
    EventRate = r->Integer(100);
    LiveTime  = r->Gaus(2000,5000);
    for(int n=0;n<20;n++){
      TestScalers[n] = (int)r->Integer(8000) - (int)r->Integer(10000);
      TestVals[n]    = r->Gaus(1.0,2.0);
    }
    
    mq->jStart(js);                                   //start the json string
    mq->jAddInt(js,"EventRate",EventRate);            //Add the data
    mq->jAddDouble(js,"LiveTime",LiveTime);
    mq->jAddIntArray(js,"TestScalers",TestScalers,20);
    mq->jAddDoubleArray(js,"TestVals",TestVals,20);
    mq->jEnd(js);                                     //end the string
  
    mq->SendMessage("clasrun.clasprod.daq.HallB_DAQ",js);                 //send the message
    gSystem->Sleep(2000);
  }
}
