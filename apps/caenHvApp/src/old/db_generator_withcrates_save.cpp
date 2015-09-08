#include <stdio.h>
#include <unistd.h>
#include <string>

using namespace std;

#define NCRATES 2
#define NSLOTS 16
#define NCHANNELS 24

#include "../Driver/sy1527.h" /// my:
#include "command.h" /// my:

//int mask[NCRATES][NSLOTS];

//int mask[0][16]={1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1};

int slot_mask[NCRATES][NSLOTS]=
    {{1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},   // crate 0
     {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}};  // crate 1

///   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15     slot number

string crates=string(
"record( mbbi, \"crates\") { \n \
        field(DESC, \"List of crates\") \n \
	field(DTYP, \"CAEN x527 generic HV Mainframe\") \n \
	field( INP,  \"crateList\") \n \
#	field( VAL,  \"0\") \n \
	field( ZRVL, \"0\") \n \
	field( ONVL, \"1\") \n \
	field( TWVL, \"2\") \n \
	field( THVL, \"3\") \n \
	field( FRVL, \"4\") \n \
	field( FVVL, \"5\") \n \
	field( SXVL, \"6\") \n \
	field( SVVL, \"7\") \n \
	field( EIVL, \"8\") \n \
	field( NIVL, \"9\") \n \
	field( TEVL, \"10\") \n \
	field( ELVL, \"11\") \n \
	field( TTVL, \"13\") \n \
	field( FTVL, \"14\") \n \
	field( FFVL, \"15\") \n \
	field( PINI, \"YES\") \n \
} \n ");

string set_part=string(
"record(ao, \"B/HV/ALL_SET_VALUES\") { \n \
   field(DTYP,\"CAEN_HV\") \n \
   field(PRIO,\"LOW\") \n \
   field(DESC,\"all set values\") \n \
   field(OUT,\"#C0 S0\") \n \
   field(OMSL,\"supervisory\") \n \
   field(SCAN,\"Passive\") \n \
} \n ");



string scrate;
string get_crate_part;

int replace(){

get_crate_part = string(
"record( ao, \""+scrate+":scanPeriod\")  \n \
{   \n \
	field( DESC, \"Base scan period\")  \n \
	field( VAL, \"0.2\") \n \
	field( PINI, \"YES\") \n \
} \n \
record( ai, \""+scrate+":connected\") \n \
{ \n \
	field( DESC, \"Crate connection status\") \n \
} \n \
record( bo, \""+scrate+":pwonoff\") \n \
{ \n \
        field( DESC, \"Power on/off, all Ch.\") \n \
} \n \
record( stringin, \""+scrate+":crateIP\") \n \
{ \n \
        field(DESC, \"Name of Slot0 Board\") \n \
	field(DTYP, \"CAEN x527 generic HV Mainframe\") \n \
	field(SCAN, \"1 second\") \n \
	field(INP,  \"@"+scrate+" -1\") \n \
	field(FLNK, \""+scrate+":boardName0\") \n \
} \n \
record( stringin, \""+scrate+":boardName0\") \n \
{ \n \
        field(DESC, \"Name of Slot0 Board\") \n \
	field(DTYP, \"CAEN x527 generic HV Mainframe\") \n \
	field(SCAN, \"Passive\") \n \
	field(INP,  \"@"+scrate+" 0\") \n \
	field(FLNK, \""+scrate+":boardName1\") \n \
} \n \
record( stringin, \""+scrate+":boardName1\") \n \
{ \n \
        field(DESC, \"Name of Slot1 Board\") \n \
	field(DTYP, \"CAEN x527 generic HV Mainframe\") \n \
	field(SCAN, \"Passive\") \n \
	field(INP,  \"@"+scrate+" 1\") \n \
	field(FLNK, \""+scrate+":boardName2\") \n \
} \n \
record( stringin, \""+scrate+":boardName2\") \n \
{ \n \
        field(DESC, \"Name of Slot2 Board\") \n \
	field(DTYP, \"CAEN x527 generic HV Mainframe\") \n \
	field(SCAN, \"Passive\") \n \
	field(INP,  \"@"+scrate+" 2\") \n \
	field(FLNK, \""+scrate+":boardName3\") \n \
} \n \
record( stringin, \""+scrate+":boardName3\") \n \
{ \n \
        field(DESC, \"Name of Slot3 Board\") \n \
	field(DTYP, \"CAEN x527 generic HV Mainframe\") \n \
	field(SCAN, \"Passive\") \n \
	field(INP,  \"@"+scrate+" 3\") \n \
	field(FLNK, \""+scrate+":boardName4\") \n \
} \n \
record( stringin, \""+scrate+":boardName4\") \n \
{ \n \
        field(DESC, \"Name of Slot4 Board\") \n \
	field(DTYP, \"CAEN x527 generic HV Mainframe\") \n \
	field(SCAN, \"Passive\") \n \
	field(INP,  \"@"+scrate+" 4\") \n \
	field(FLNK, \""+scrate+":boardName5\") \n \
} \n \
record( stringin, \""+scrate+":boardName5\") \n \
{ \n \
        field(DESC, \"Name of Slot5 Board\") \n \
	field(DTYP, \"CAEN x527 generic HV Mainframe\") \n \
	field(SCAN, \"Passive\") \n \
	field(INP,  \"@"+scrate+" 5\") \n \
	field(FLNK, \""+scrate+":boardName6\") \n \
} \n \
record( stringin, \""+scrate+":boardName6\") \n \
{ \n \
        field(DESC, \"Name of Slot6 Board\") \n \
	field(DTYP, \"CAEN x527 generic HV Mainframe\") \n \
	field(SCAN, \"Passive\") \n \
	field(INP,  \"@"+scrate+" 6\") \n \
	field(FLNK, \""+scrate+":boardName7\") \n \
} \n \
record( stringin, \""+scrate+":boardName7\") \n \
{ \n \
        field(DESC, \"Name of Slot7 Board\") \n \
	field(DTYP, \"CAEN x527 generic HV Mainframe\") \n \
	field(SCAN, \"Passive\") \n \
	field(INP,  \"@"+scrate+" 7\") \n \
	field(FLNK, \""+scrate+":boardName8\") \n \
} \n \
record( stringin, \""+scrate+":boardName8\") \n \
{ \n \
        field(DESC, \"Name of Slot8 Board\") \n \
	field(DTYP, \"CAEN x527 generic HV Mainframe\") \n \
	field(SCAN, \"Passive\") \n \
	field(INP,  \"@"+scrate+" 8\") \n \
	field(FLNK, \""+scrate+":boardName9\") \n \
} \n \
record( stringin, \""+scrate+":boardName9\") \n \
{ \n \
        field(DESC, \"Name of Slot9 Board\") \n \
	field(DTYP, \"CAEN x527 generic HV Mainframe\") \n \
	field(SCAN, \"Passive\") \n \
	field(INP,  \"@"+scrate+" 9\") \n \
	field(FLNK, \""+scrate+":boardName10\") \n \
} \n \
record( stringin, \""+scrate+":boardName10\") \n \
{ \n \
        field(DESC, \"Name of Slot10 Board\") \n \
	field(DTYP, \"CAEN x527 generic HV Mainframe\") \n \
	field(SCAN, \"Passive\") \n \
	field(INP,  \"@"+scrate+" 10\") \n \
	field(FLNK, \""+scrate+":boardName11\") \n \
} \n \
record( stringin, \""+scrate+":boardName11\") \n \
{ \n \
        field(DESC, \"Name of Slot11 Board\") \n \
	field(DTYP, \"CAEN x527 generic HV Mainframe\") \n \
	field(SCAN, \"Passive\") \n \
	field(INP,  \"@"+scrate+" 11\") \n \
	field(FLNK, \""+scrate+":boardName12\") \n \
} \n \
record( stringin, \""+scrate+":boardName12\") \n \
{ \n \
        field(DESC, \"Name of Slot12 Board\") \n \
	field(DTYP, \"CAEN x527 generic HV Mainframe\") \n \
	field(SCAN, \"Passive\") \n \
	field(INP,  \"@"+scrate+" 12\") \n \
	field(FLNK, \""+scrate+":boardName13\") \n \
} \n \
record( stringin, \""+scrate+":boardName13\") \n \
{ \n \
        field(DESC, \"Name of Slot13 Board\") \n \
	field(DTYP, \"CAEN x527 generic HV Mainframe\") \n \
	field(SCAN, \"Passive\") \n \
	field(INP,  \"@"+scrate+" 13\") \n \
	field(FLNK, \""+scrate+":boardName14\") \n \
} \n \
record( stringin, \""+scrate+":boardName14\") \n \
{ \n \
        field(DESC, \"Name of Slot14 Board\") \n \
	field(DTYP, \"CAEN x527 generic HV Mainframe\") \n \
	field(SCAN, \"Passive\") \n \
	field(INP,  \"@"+scrate+" 14\") \n \
	field(FLNK, \""+scrate+":boardName15\") \n \
} \n \
record( stringin, \""+scrate+":boardName15\") \n \
{ \n \
        field(DESC, \"Name of Slot1 Board\") \n \
	field(DTYP, \"CAEN x527 generic HV Mainframe\") \n \
	field(SCAN, \"Passive\") \n \
	field(INP,  \"@"+scrate+" 15\") \n \
} \n ");

return 0;

}

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

fprintf(fp,"%s",crates.c_str());
fprintf(fp,"%s",set_part.c_str());

char tmp[1000], tmp1[100];

//printf(\"%d %d\n\", slot_mask[0][5], slot_mask[1][5]);

for(int i=0;i<NCRATES;i++){
  
  sprintf(tmp,CRATE_LABEL,i);
  scrate=string(tmp);
  replace();
  //if(!slot_mask[i][j])continue;
  // sprintf(tmp, get_carte_part, i,j,j10,i,j,j10);
   fprintf(fp,"%s",get_crate_part.c_str());
  

}

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

   if(commands[ip]==S_CHHV){
    
/// see MAX_BOARD_PARTS that is 4 at the moment !!!!!!!!!

///    input_s=0+(S_BDHV<<8);

    if((crossnumber%2)==0){
     input_s=0 + (24 << 8); // simulate part of the chamber (type 0) 
     sprintf(tmp, put_part_board_bo, tmp1,j,0,input_c,input_s,znams[ip],onams[ip]);
     fprintf(fp,"%s",tmp);
     input_s=0 + (24 << 8); // simulate part of the chamber (type 0) 
     sprintf(tmp, put_part_board_bi, tmp1,j,0,input_c,input_s,znams[ip],onams[ip]);
     fprintf(fp,"%s",tmp);
    }
    else if((crossnumber%2)==1){
     input_s=0 + (12 << 8); // simulate part of the chamber (type 1) 
     sprintf(tmp, put_part_board_bo, tmp1,j,1,input_c,input_s,znams[ip],onams[ip]);
     fprintf(fp,"%s",tmp);
     input_s=0 + (12 << 8); // simulate part of the chamber (type 1) 
     sprintf(tmp, put_part_board_bi, tmp1,j,1,input_c,input_s,znams[ip],onams[ip]);
     fprintf(fp,"%s",tmp);
     input_s=12 + (24 << 8); // simulate part of the chamber (type 2) 
     sprintf(tmp, put_part_board_bo, tmp1,j,2,input_c,input_s,znams[ip],onams[ip]);
     fprintf(fp,"%s",tmp);
     input_s=12 + (24 << 8); // simulate part of the chamber (type 2) 
     sprintf(tmp, put_part_board_bi, tmp1,j,2,input_c,input_s,znams[ip],onams[ip]);
     fprintf(fp,"%s",tmp);
    }

   crossnumber++;
   }
/*
///    input_s=0+(S_BDHV<<8);
    input_s=0 + (12 << 8); // simulate first part of the board 
    sprintf(tmp, put_part_board_bo, tmp1,j,0,input_c,input_s,znams[ip],onams[ip]);
    fprintf(fp,"%s",tmp);
    input_s=12 + (24 << 8);  // simulate the second part of the board
    sprintf(tmp, put_part_board_bo, tmp1,j,1,input_c,input_s,znams[ip],onams[ip]);
    fprintf(fp,"%s",tmp);
    input_s=0 + (12 << 8); // simulate first part of the board 
    sprintf(tmp, put_part_board_bi, tmp1,j,0,input_c,input_s,znams[ip],onams[ip]);
    fprintf(fp,"%s",tmp);
    input_s=12 + (24 << 8);  // simulate the second part of the board
    sprintf(tmp, put_part_board_bi, tmp1,j,1,input_c,input_s,znams[ip],onams[ip]);
    fprintf(fp,"%s",tmp);
   }
*/



   for(int j10=0;j10<NCHANNELS;j10++){
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
  for(int j10=0;j10<NCHANNELS;j10++){
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
