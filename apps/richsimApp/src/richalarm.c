
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <dbDefs.h>
//#include <subRecord.h>
//#include <mcaRecord.h>
#include <dbCommon.h>
#include <dbAccess.h>
#include <registryFunction.h>
#include <subRecord.h>
#include <aSubRecord.h>
#include <epicsExport.h>
#include <stringinRecord.h>
#include <longinRecord.h>


int richinit(pvsub)
	struct subRecord* pvsub;
{
	//printf("richinit was called \n");
	return(0);
}


int richproc(pvsub)
	struct subRecord* pvsub;
{
	int a = (int) pvsub->a;  //:stat
	int c = (int) pvsub->c;  //comms
	int vtol = 0;
	//b = vmon
	//e = vset
	//f = 0.01
	//g = .STAT
	//printf("%d \n",a);
	
	if(pvsub->b > (pvsub->e + pvsub->e * pvsub->f))//if vmon is greater than
							//vset by some factor f
		vtol=1;
	else if(pvsub->b < (pvsub->e - pvsub->e * pvsub->f))//if vmon is less 
							//than vset by factor f
		vtol=2;
	else{
		vtol=0;
	}
	//initialization to no alarm state
	pvsub->val = 15;
	
	if( c & 1)//check communications
		 pvsub->val=0;
	else if(pvsub->c ==0 && !(a&1)) //if there is comm but channel is off
		pvsub->val=1;
	else if((a&1)){
		int theStatus=-1;
		int status[]={2,3,4,5,6,7,8,9,10,11,12};//vals come from the
							//mbbi record in 
							//richhv_sim.db
		int i=1;
		for(i=1;i<12;i=i+1){
			if((1<<i) & a){
				theStatus=i;
			}
		}
		if(theStatus != -1){ 
			pvsub->val=status[theStatus-1];
		}
		else if(pvsub->c ==0 && pvsub->a==1 && vtol ==1)//check vhigh
				pvsub->val=13;
		else if (pvsub->c ==0 && pvsub->a==1 && vtol ==2)//check vlow
				pvsub->val=14;
	}

	return(0);

}
//method that allows you to see which bits are set with a byte monitor.  shifts
// the :stat bits left 3,comms bit left 2,nothing to vtol 
int richSetBits(pvsub)
      struct subRecord* pvsub;
{
        int a = (int) pvsub->a;  //:stat
        int c = (int) pvsub->c;  //comms
        int string = 0;
	int vtol = 0;
        //printf("%f \n",pvsub->g);
        //b vmon
        //e vset
        //f = 0.01
        //g = .STAT

        if(pvsub->b > (pvsub->e + pvsub->e * pvsub->f))
             vtol=1;
        else if(pvsub->b < (pvsub->e - pvsub->e * pvsub->f))
             vtol=2;
        else
             vtol=0;
                 
          //d = a|(c<<12)|(vtol<<13);
           string = (a<<3)|(c<<2)|vtol;
        //pvsub->d = (epicsFloat64) d;
        //printf("%d, %f \n",d,pvsub->d);
        //printf("%f \n",pvsub->d);
        pvsub->val = string;
       return(0); 
}


epicsRegisterFunction(richinit);
epicsRegisterFunction(richproc);
epicsRegisterFunction(richSetBits);
