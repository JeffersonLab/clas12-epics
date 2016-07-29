#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdint.h>

#include <dbDefs.h>
#include <registryFunction.h>
//#include <subRecord.h>
#include <aSubRecord.h>
#include <epicsExport.h>
#include <dbAddr.h>
#include <dbFldTypes.h>
#include <dbBase.h>
#include <dbCommon.h>
#include <dbAccessDefs.h>
#include <alarm.h>
#include <recGbl.h>

int MpodStatusParserDebug=0;

static long MpodStatusParserInit(aSubRecord *precord)
{
//	struct dbAddr *pAddr;
//	pAddr = (struct dbAddr*) calloc(2, sizeof(struct dbAddr));
//    precord->dpvt = pAddr;

    if (MpodStatusParserDebug) printf("Record %s called MpodStatusParserInit(%p)\n", precord->name, (void*) precord);

//    dbNameToAddr((char*)(precord->inpa).value.constantStr, pAddr);
//    if (MpodStatusParserDebug) printf("Record %s called MpodStatusParserInit(%p)\n", (char*)(precord->inpa).value.constantStr, (void*) pAddr);
//
//    ++pAddr; // access the nex element of array
//    dbNameToAddr((char*)(precord->inpb).value.constantStr, pAddr);
//    if (MpodStatusParserDebug) printf("Record %s called MpodStatusParserInit(%p)\n", (char*)(precord->inpb).value.constantStr, (void*) pAddr);

    return 0;
}
static long MpodStatusParserProcess(aSubRecord *precord)
{
    if (MpodStatusParserDebug) printf("Record %s called MpodStatusParserProcess(%p)\n", precord->name, (void*) precord);

    // stat_string like this "80 01 C0 outputOn(0) 15 16 17" means "8001c0" is the number with bits 0 15 16 17 risen.
    // So the algorith will be to count number of all fields (7 in this case). Then read first tokens as numbers and count the number of bits risen.
    // For example 80 has 1 bit 01 has another 1 and c0 has 2 bits. In total 4 + 3 tokens (80,01,c0) = 7 number of tokens
    // This last condition would be the consistency check for our parser.

    char* stat_string = (char *)precord->a;
    char ststr[40];
    char tmp[40];
    const int MAX_VOLTAGE_STATUSES = 32;
    strncpy(ststr,stat_string,40);

    // calculate number of tokens in the string
    int ntokens = 0;
    while (sscanf(stat_string, " %s ", &tmp[0])==1 && ntokens<MAX_VOLTAGE_STATUSES) {
    	stat_string += strlen(tmp)+1; // +1 to take into account the delimiting spaces
    	if (strlen(tmp)<2) break;
    	if (MpodStatusParserDebug) printf("1) ntokens = %d, stat_string = %s, tmp = %s\n", ntokens, stat_string, tmp);
    	ntokens++;
    }
    stat_string = (char *)precord->a; // reset the pointer to original place
    if (MpodStatusParserDebug) printf("1) ntokens = %d, %s\n", ntokens, stat_string);

    // get number of bits read and compare with number of tokens for consistency
    uint8_t st[MAX_VOLTAGE_STATUSES]; // number status read
    unsigned char bits[MAX_VOLTAGE_STATUSES]; // bits
    memset(bits, 0xff, sizeof(bits));
    int numbers=0, nbits=0;
    int j;
    uint32_t result = 0;
    if (sizeof(result)*8 != MAX_VOLTAGE_STATUSES)
    	printf("WARNING::"__FILE__"::%d number of bits in the result must be = %d. Otherwise results are not guaranteed.\n",__LINE__, MAX_VOLTAGE_STATUSES);
    while (sscanf(stat_string, "%02x ", (unsigned int *)&st[numbers])==1 && numbers<MAX_VOLTAGE_STATUSES) {
    	if (MpodStatusParserDebug) printf("2) stat_string = %s, st[%d] = 0x%x\n",stat_string, numbers, st[numbers]);
    	for(j=0; j<8; j++) { // loop over bits in the st[i]
    		if(st[numbers] & 1<<(7-j)) { // find the risen bits using the mask
    			bits[nbits] = numbers*8 + j; // decimal number of the bit counted from left to right
    			if (MpodStatusParserDebug) printf ("--- result = 0x%x %x %d\n",result, 1<<(numbers*8 + j), numbers*8 + j);
    			result |= 1<<(numbers*8 + j);
    			if (MpodStatusParserDebug) printf ("+++ result = 0x%x %x %d\n",result, 1<<(numbers*8 + j), numbers*8 + j);
    			nbits++; // number of risen bits found
    		}
    	}
    	numbers++;
    	if (numbers+nbits == ntokens) break; // The consistency condition is satisfied, no need to parse further.
    	stat_string += 3;
    }
    if (MpodStatusParserDebug) printf("ndigits = %d nbits = %d\n", numbers, nbits);

    // the final check, if fails report
    // note: since, the snmp messages could be longer than 40char limit of stringin record, that's why this part becomes pretty much meaningless
    if (ntokens != numbers + nbits) { // consistency check condition
	    printf("WARNING::Record %s called MpodStatusParserProcess."
	    		" Consistency check failed. Might be the snmp message got cut to fit into stringin record."
	    		" The stat_string parsed was = %s\n", precord->name, (char*)ststr);
//	    recGblSetSevr(precord, UDF_ALARM, INVALID_ALARM);
//		return -1;
	}

    if (MpodStatusParserDebug) {
    	for(j=0; j<MAX_VOLTAGE_STATUSES && bits[j]<0xff; j++) {
    		printf("bits[%d] = %d ", j, bits[j]);
    	}
    	puts("");
    	printf("Record %s called MpodStatusParserProcess(%s) with result = %d\n", precord->name, precord->inpa.value.constantStr, result);
    }

    precord->vala = &result; // mbbiDirect will keep the last 16 bits
    // output to bi record
    epicsEnum16 *outbi = (epicsEnum16*)precord->valb;
    if (	 (result &  1<<0) &&	// GOOD           outputOn (0),                           output channel is on
    		!(result &  1<<1) &&	// BAD            outputInhibit(1),                       external (hardware-)inhibit of the output channel
    		!(result &  1<<2) &&	// BAD            outputFailureMinSenseVoltage (2)        Supervision limit hurt: Sense voltage is too low
    		!(result &  1<<3) &&	// BAD            outputFailureMaxSenseVoltage (3),       Supervision limit hurt: Sense voltage is too high
    		!(result &  1<<4) &&	// BAD            outputFailureMaxTerminalVoltage (4),    Supervision limit hurt: Terminal voltage is too high
    		!(result &  1<<5) &&	// BAD            outputFailureMaxCurrent (5),            Supervision limit hurt: Current is too high
			!(result &  1<<6) &&	// BAD            outputFailureMaxTemperature (6),        Supervision limit hurt: Heat sink temperature is too high
    		!(result &  1<<7) &&	// BAD            outputFailureMaxPower (7),              Supervision limit hurt: Output power is too high
    		!(result &  1<<9) &&	// BAD            outputFailureTimeout (9),               Communication timeout between output channel and main control
    								// NORMAL         outputCurrentLimited (10),              Current limiting is active (constant current mode)
    								// NORMAL         outputRampUp (11),                      Output voltage is increasing (e.g. after switch on)
    								// NORMAL         outputRampDown (12),                    Output voltage is decreasing (e.g. after switch off)
    		!(result & 1<<13) &&	// BAD            outputEnableKill (13),                  EnableKill is active
    		!(result & 1<<14) &&	// BAD            outputEmergencyOff (14),                EmergencyOff event is active
    								// NORMAL         outputAdjusting (15),                   Fine adjustment is working
    								// NORMAL         outputConstantVoltage (16),             Voltage control (constant voltage mode)
    		!(result & 1<<17) &&  	// BAD            outputVoltageBoundsExceeded (17),       output Voltage out of bounds
    		!(result & 1<<18) &&  	// BAD            outputCurrentBoundsExceeded (18),       output Current out of bounds
    		!(result & 1<<19) ) 	// BAD            outputFailureCurrentLimit (19)          Hardware current limit (EHS) / trip (EDS, EBS) was exceeded
    {
    	outbi[0] = 1; // Good
    } else {
    	outbi[0] = 0; // Not good
    }

    if      (result&1<<19) precord->valc="ILimit";
    else if (result&1<<18) precord->valc="IOB";
    else if (result&1<<17) precord->valc="VOB";
    else if (result&1<<14) precord->valc="EmrgOff";
    else if (result&1<<13) precord->valc="KillEn";
    else if (result&1<<9)  precord->valc="TOut";
    else if (result&1<<7)  precord->valc="PMax";
    else if (result&1<<6)  precord->valc="TMax";
    else if (result&1<<5)  precord->valc="IMax";
    else if (result&1<<4)  precord->valc="TVMax";
    else if (result&1<<3)  precord->valc="SVMax";
    else if (result&1<<2)  precord->valc="SVMin";
    else if (result&1<<1)  precord->valc="ExtIn";
   
    else if (result&1<<12) precord->valc="RDN";
    else if (result&1<<11) precord->valc="RUP";
    else if (result&1<<15) precord->valc="ADJ";
    else if (result&1<<16) precord->valc="CV";
    else if (result&1<<10) precord->valc="CC";

    else if (result&1<<0) precord->valc="ON";
    else precord->valc="OFF";

    printf("Record %s called MpodStatusParserProcess(%s) before the end\n", precord->name, precord->inpa.value.constantStr);
    return 0;
}
// outputOn (0),                           output channel is on
// outputInhibit(1),                       external (hardware-)inhibit of the output channel
// outputFailureMinSenseVoltage (2)        Supervision limit hurt: Sense voltage is too low
// outputFailureMaxSenseVoltage (3),       Supervision limit hurt: Sense voltage is too high
// outputFailureMaxTerminalVoltage (4),    Supervision limit hurt: Terminal voltage is too high
// outputFailureMaxCurrent (5),            Supervision limit hurt: Current is too high
// outputFailureMaxTemperature (6),        Supervision limit hurt: Heat sink temperature is too high
// outputFailureMaxPower (7),              Supervision limit hurt: Output power is too high
// -- reserved
// outputFailureTimeout (9),               Communication timeout between output channel and main control
// outputCurrentLimited (10),              Current limiting is active (constant current mode)
// outputRampUp (11),                      Output voltage is increasing (e.g. after switch on)
// outputRampDown (12),                    Output voltage is decreasing (e.g. after switch off)
// outputEnableKill (13),                  EnableKill is aktive
// outputEmergencyOff (14),                EmergencyOff event is aktive
// outputAdjusting (15),                   Fine adjustment is working
// outputConstantVoltage (16),             Voltage control (constant voltage mode)
// outputVoltageBoundsExceeded (17),       output Voltage out of bounds
// outputCurrentBoundsExceeded (18),       output Current out of bounds
// outputFailureCurrentLimit (19)          Hardware current limit (EHS) / trip (EDS, EBS) was exceeded

epicsExportAddress(int, MpodStatusParserDebug);
epicsRegisterFunction(MpodStatusParserInit);
epicsRegisterFunction(MpodStatusParserProcess);
