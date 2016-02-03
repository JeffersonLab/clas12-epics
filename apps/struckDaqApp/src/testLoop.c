#include <stddef.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdio.h>

#include "epicsExit.h"
#include "epicsThread.h"
#include "iocsh.h"
#include "time.h"

int testLoop() {
struct timespec currTime; 
 int startTime = 0;
 int stopTime = 0;
 int deltaTime =0;
 while (1) {
        clock_gettime(CLOCK_REALTIME, &currTime );
    	  stopTime = (1.0e+09 * currTime.tv_sec + currTime.tv_nsec); 
	  deltaTime = stopTime - startTime;

	printf( "Func: Seconds %d :: millisecond %d \n", 
		currTime.tv_sec, currTime.tv_nsec/1000000 );
	epicsThreadSleep(2.0);

  }
}
