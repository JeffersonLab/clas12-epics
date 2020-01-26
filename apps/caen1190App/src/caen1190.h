#ifndef CAEN1190_H
#define CAEN1190_H

#include <stddef.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdio.h>
#include <time.h>
#include <unistd.h>

#include "jvme.h"
#include "tdc1190.h"

#define NCHANS 4
#define MAXHITSPERCHAN 0x80000

int caen1190_init();
int caen1190_read(unsigned int *,unsigned int *,unsigned int);

#endif

