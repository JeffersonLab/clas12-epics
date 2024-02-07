
// 1st hexdigit:  threshold/counts/sspdata type
//                1 = fadc OR tdc threshold
//                2 = trg threshold
//                3 = fadc OR tdc-gated counts
//                4 = trg-gated counts
//                5 = tdc counts
//                6 = trg counts
//            (subtracting 1 gives threshold index: 0,1)
//            (subtracting 3 gives counts index: 0,1,2,3)
//            (subtracting 3 gives ssp fiber count)
//            (subtracting 5 gives ssp data index)
//
// 2nd hexdigit:  board type 
//                0=fadc
//                1=disc
//                2=ssp


#define FADCTET 0x01
#define FADCCNT 0x03
#define FADCCNTRAW 0x23

#define TDCTET  0x11
#define TRGTET  0x12
#define GTRGCNT 0x13
#define GTDCCNT 0x14
#define TRGCNT  0x15
#define TDCCNT  0x16
#define GTRGCNTRAW 0x23
#define GTDCCNTRAW 0x24
#define TRGCNTRAW  0x25
#define TDCCNTRAW  0x26

#define SSPSCAL 0x31
#define SSPDATA 0x32

#define SSPNSFIB 0x33
#define SSPNDFIB 0x34

#define SSPTEMP1 0x35
#define SSPTEMP2 0x36
#define SSPTEMP3 0x37
#define SSPVOLT1 0x38
#define SSPVOLT2 0x39
#define SSPVOLT3 0x3A
#define SSPVOLT4 0x3B
#define SSPVOLT5 0x3C
#define SSPVOLT6 0x3D

#define SSPUPTIME 0x3E
#define SSPSEUCNT 0x3F
#define SSPSTAT   0x40
