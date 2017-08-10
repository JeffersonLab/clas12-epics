
// 1st hexdigit:  threshold/counts type
//                1 = fadc OR tdc threshold
//                2 = trg threshold
//                3 = fadc OR tdc-gated counts
//                4 = trg-gated counts
//                5 = tdc counts
//                6 = trg counts
//            (subtracting 1 gives threshold index: 0,1)
//            (subtracting 3 gives counts index: 0,1,2,3)
//
// 2nd hexdigit:  board type 
//                0=fadc
//                1=disc
//                2=ssp


#define FADCTET 0x01
#define FADCCNT 0x03

#define TDCTET  0x11
#define TRGTET  0x12
#define GTRGCNT 0x13
#define GTDCCNT 0x14
#define TRGCNT  0x15
#define TDCCNT  0x16

#define SSPSCAL 0x21
#define SSPDATA 0x22

#define SSPNSFIB 0x23
#define SSPNDFIB 0x24

#define SSPTEMP1 0x25
#define SSPTEMP2 0x26
#define SSPTEMP3 0x27
#define SSPVOLT1 0x28
#define SSPVOLT2 0x29
#define SSPVOLT3 0x2A
#define SSPVOLT4 0x2B
#define SSPVOLT5 0x2C
#define SSPVOLT6 0x2D

