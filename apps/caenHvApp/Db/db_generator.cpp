
/* db_generator.cpp */

#include <stdio.h>
#include <unistd.h>
#include <string>

using namespace std;



#include "../Driver/sy1527.h" /// my:
#include "command.h" /// my:

///----------------- CRATES/SLOTS CONFIGURATION ----------------------------

#define NCRATES 15
#define NSLOTS 16
enum {A1535, A1520};
int NCHANNELS[2] = {24, 12};

int slot_mask[NCRATES][NSLOTS] =
{
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},   // crate 0
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},   // crate 1
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},   // crate 2
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},   // crate 3
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},   // crate 4
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},   // crate 5
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},   // crate 6
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},   // crate 7
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},   // crate 8
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},   // crate 9
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},   // crate 10
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},   // crate 11
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},   // crate 12
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},   // crate 13
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}    // crate 14
};
int slot_types[NCRATES][NSLOTS] =
{
  {A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535 },  // crate 0
  {A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535 },  // crate 1
  {A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535 },  // crate 2
  {A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535 },  // crate 3
  {A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535 },  // crate 4
  {A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535 },  // crate 5
  {A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535 },  // crate 6
  {A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535 },  // crate 7
  {A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535 },  // crate 8
  {A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535 },  // crate 9
  {A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535 },  // crate 10
  {A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535 },  // crate 11
  {A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535 },  // crate 12
  {A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535 },  // crate 13
  {A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535, A1535 }   // crate 14
};

///-------------------------------------------------------------------------

///   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15     slot number


#define get_part \
"record(bigsub, \"%s_%d_%d\") { \n \
   field(PRIO,\"LOW\") \n \
   field(DESC,\"big subroutine record\") \n \
   field(INAM,\"InitChannel\") \n \
   field(INPA,\"%02d\") \n \
   field(INPB,\"%02d\") \n \
   field(HIGH,\"50\") \n \
   field(INPC,\"%02d\") \n \
   field(HSV,\"MAJOR\") \n \
   field(PREC,\"1\") \n \
   field(SNAM,\"ScanChannel\") \n \
   field(SCAN,\"2 second\") \n \
}\n "

//pwonoff
//HV/OFF
//HV/ON

/// for boards

#define put_part_board_bo \
"record(bo, \"%s_%d_P%d_BO\") {  \n \
   field(DTYP,\"CAEN_HV\") \n \
   field(DESC,\"smi\") \n \
   field(OUT,\"#C%d S%d\") \n \
   field(OMSL,\"supervisory\") \n \
   field(ZNAM,\"%s\") \n \
   field(ONAM,\"%s\") \n \
   field(SCAN,\"Passive\") \n \
}\n"

#define put_part_board_bi \
"record(bi, \"%s_%d_P%d\") {  \n \
   field(DTYP,\"CAEN_HV\") \n \
   field(OSV,\"MAJOR\") \n \
   field(DESC,\"smi\") \n \
   field(ZSV,\"NO_ALARM\") \n \
   field(INP,\"#C%d S%d\") \n \
   field(ZNAM,\"%s\") \n \
   field(ONAM,\"%s\") \n \
   field(SCAN,\"2 second\") \n \
}\n"


/// for channels

#define put_part_bo \
"record(bo, \"%s_%d_%d_%s\") {  \n \
   field(DTYP,\"CAEN_HV\") \n \
   field(DESC,\"binary output record\") \n \
   field(OUT,\"#C%d S%d\") \n \
   field(OMSL,\"supervisory\") \n \
   field(ZNAM,\"%s\") \n \
   field(ONAM,\"%s\") \n \
   field(SCAN,\"Passive\") \n \
}\n"

/// for channels

#define put_part_ao \
"record(ao, \"%s_%d_%d_%s\") {  \n \
   field(DTYP,\"CAEN_HV\") \n \
   field(DESC,\"analog output record\") \n \
   field(OUT,\"#C%d S%d\") \n \
   field(OMSL,\"supervisory\") \n \
   field(SCAN,\"Passive\") \n \
}\n"

/*
#define put_part \
"record(bo, \"%s_%d_%d_%s\") {  \n \
}\n"
*/

int main(int argc,char *argv[]){

//printf(\"%s\n\",set_part.c_str());

FILE *fp=fopen("hvprod.db","w+");

//fprintf(fp,"%s",crates.c_str());
//fprintf(fp,"%s",set_part.c_str());

char tmp[1000], tmp1[100];
/*
//printf(\"%d %d\n\", slot_mask[0][5], slot_mask[1][5]);

for(int i=0;i<NCRATES;i++){
  
  sprintf(tmp,CRATE_LABEL,i);
  scrate=string(tmp);
  replace();
  //if(!slot_mask[i][j])continue;
  // sprintf(tmp, get_carte_part, i,j,j10,i,j,j10);
   fprintf(fp,"%s",get_crate_part.c_str());
  

}
*/
//=======================================

char *pars[]={"pwonoff", "v0set","i0set", "trip", "rampup", "rampdn"};
char *znams[]={"HV/OFF","","","","",""};
char *onams[]={"HV/ON","","","","",""};
int commands[]= {S_CHHV, S_DV, S_TC, S_PRD, S_RUP, S_RDN};
int NSETPARS=sizeof(commands)/sizeof(commands[0]);

int input_c, input_s;


//printf("size%d\n", sizeof(commands));

// {card 0-7: chassis, 8-15: slot;  signal 0-7:channel, 8-15:command}.

int crossnumber;

 for(int ip=0;ip<NSETPARS;ip++){

crossnumber=0;
  for(int i=0;i<NCRATES;i++){
 
 sprintf(tmp1,CRATE_LABEL,i);
//printf("%s 0\n", tmp1);

  for(int j=0;j<NSLOTS;j++){
   if(!slot_mask[i][j])continue;
   input_c=i+(j<<8);




   for(int j10=0;j10<NCHANNELS[slot_types[i][j]];j10++){
//printf("%s 2\n", pars[ip]);
   input_s=j10+(commands[ip]<<8);
   if(commands[ip]==S_CHHV)
    sprintf(tmp, put_part_bo, tmp1,j,j10,pars[ip],input_c,input_s,znams[ip],onams[ip]);
   else 
    sprintf(tmp, put_part_ao, tmp1,j,j10,pars[ip],input_c,input_s);
//printf("%s 1\n", tmp);
    fprintf(fp,"%s",tmp);
   }
  }

 
  }
 }



//=======================================

for(int i=0;i<NCRATES;i++){

 sprintf(tmp1,CRATE_LABEL,i);

 for(int j=0;j<NSLOTS;j++){
  if(!slot_mask[i][j])continue;
  for(int j10=0;j10<NCHANNELS[slot_types[i][j]];j10++){
   sprintf(tmp, get_part, tmp1,j,j10,i,j,j10);
   fprintf(fp,"%s",tmp);
  }
 }
}
//printf(\"%s\n\",tmp);




//4000000000000000000
//printf(\"1\n\");
return 1;

}
