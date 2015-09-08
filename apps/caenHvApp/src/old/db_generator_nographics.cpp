#include <stdio.h>
#include <unistd.h>
#include <string>

using namespace std;

#define NCRATES 2
#define NSLOTS 16
#define NCHANNELS 24

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

#define get_part \
"record(bigsub, \"B/HV/%02d/%02d/%02d\") { \n \
   field(PRIO,\"LOW\") \n \
   field(DESC,\"big subroutine record\") \n \
   field(INAM,\"InitChannel\") \n \
   field(INPA,\"%02d\") \n \
   field(INPB,\"%02d\") \n \
   field(HIGH,\"10\") \n \
   field(INPC,\"%02d\") \n \
   field(HSV,\"MAJOR\") \n \
   field(PREC,\"3\") \n \
   field(SNAM,\"ScanChannel\") \n \
   field(SCAN,\"2 second\") \n \
}\n "

int main(int argc,char *argv[]){

//printf("%s\n",set_part.c_str());

FILE *fp=fopen("hvprod.db","w+");

fprintf(fp,"%s",crates.c_str());
fprintf(fp,"%s",set_part.c_str());

char tmp[1000];

//printf("%d %d\n", slot_mask[0][5], slot_mask[1][5]);

for(int i=0;i<NCRATES;i++){
 for(int j=0;j<NSLOTS;j++){
  if(!slot_mask[i][j])continue;
  for(int j10=0;j10<NCHANNELS;j10++){
   sprintf(tmp, get_part, i,j,j10,i,j,j10);
   fprintf(fp,"%s",tmp);
  }
 }
}
//printf("%s\n",tmp);




//4000000000000000000
//printf("1\n");
return 1;

}
