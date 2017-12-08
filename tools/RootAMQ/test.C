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
char js[1000];   //the json string
TRandom *r;     //random generator
char hist1[200];
char hist2[200];

void test(int sleep=2000){
  
  //create some variables to test
  int EventRate;
  double LiveTime;
  int TestScalers[20];
  double TestVals[20];


  r = new TRandom();  //and a randomizer for them
  

  mq=new RootMQ("tcp://clon00:61616");               //create mq and try to connect

  if(mq->GetConnectionStatus()==1){
    printf( "Successfully connected to ActiveMQ\n");    //if not is will print it's own warnings
  }
  else return;
  
  
  while(1){
    
    //fill the variables randomly 
    EventRate = r->Integer(100);
    LiveTime  = r->Gaus(2000,5000);
    for(int n=0;n<20;n++){
      TestScalers[n] = (int)r->Integer(8000) - (int)r->Integer(10000);
      TestVals[n]    = r->Gaus(1.0,2.0);
    }

    make_json_hist_int(hist1,20,TestScalers,20,50);
    make_json_hist_int(hist2,20,TestScalers+20,20,60);
      
    //make the json string from the variable
    mq->jStart(js);                                   //start the json string
    mq->jAddInt(js,"EventRate",EventRate);            //Add the data
    mq->jAddDouble(js,"LiveTime",LiveTime);
    mq->jAddIntArray(js,"TestScalers",TestScalers,20);
    mq->jAddDoubleArray(js,"TestVals",TestVals,10);
    mq->jAddJson(js,"TestHist",hist1);
    mq->jAddJson(js,"TestHist2",hist2);

    mq->jEnd(js);                                     //end the string
  
    //send the message
    mq->SendMessage("clasrun.clasprod.daq.HallB_DAQ",js);
    gSystem->Sleep(sleep);
  }
}

void make_json_hist_int(char *jhist, int npoints, int *data, float xmin=1, float xmax=0){
  char *end;
  sprintf(jhist,"{ \"NBINSX\":%d",npoints);
  if(xmin<xmax){
    sprintf(jhist,"%s,\"XMIN\":%e,\"XMAX\":%e",jhist,xmin,xmax);
  }
  sprintf(jhist, "%s,\"DATA\":[%d",jhist,data[0]);
  for(int n=1;n<npoints;n++){
    end=jhist+strlen(jhist);
    sprintf(end,",%d",data[n]);
  }
  strcat(jhist,"]");
  //others here

  strcat(jhist,"}");
}
