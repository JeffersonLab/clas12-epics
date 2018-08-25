
// needs to go in records:
#define COLLIMATOR_POSITION 7.0837

// tolerances for magent currents:
#define QUAD_TOLERANCE 100
#define HELM_TOLERANCE 0.1
#define TAGGER_TOLERANCE 200

// values for automoller status:
#define NOT_CONFIGURED 0
#define CONFIGURING 1 
#define CONFIGURED 2
#define RUN_IN_PROGRESS 3
#define DC_ALARM 4
#define SVT_ALARM 5
#define MVT_ALARM 6
#define QUAD_ALARM 7
#define HELM_ALARM 8
#define TGT_ALARM 9
#define ACC_ALARM 10
#define COLLI_ALARM 11

// from moller_targetApp:
#define TGT_LEFT 11
#define TGT_EMPTY 12
#define TGT_RIGHT 13
#define TGT_ALUM 14

// from asymApp's moller_accumulate:
#define STARTDAQ 0
#define STOPDAQ 1

// from accelerator:
#define HWP_IN 0
#define HWP_OUT 1

#define _UNCONFIGURED 0x00
#define _CONFIGURED   0x01
#define _CONFIGURING  0x02
#define _RUNNING      0x03
#define _DC_ALARM     0x10
#define _SVT_ALARM    0x20
#define _MVT_ALARM    0x30
#define _QUAD_ALARM   0x40
#define _HELM_ALARM   0x50
#define _TGT_ALARM    0x60
#define _ACC_ALARM    0x70

