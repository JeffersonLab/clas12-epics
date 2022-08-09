
// needs to go in records:
#define COLLIMATOR_POSITION 7.0837

// tolerances for magent currents:
#define QUAD_TOLERANCE 200
#define HELM_TOLERANCE 0.1
#define TAGGER_TOLERANCE 200

// values for automoller.db status:
#define NOT_CONFIGURED 0
#define CONFIGURING 1 
#define CONFIGURED 2
#define RUN_IN_PROGRESS 3
#define ACCID_ALARM 4
#define QASY_ALARM 5
#define DC_ALARM 6
#define SVT_ALARM 7
#define MVT_ALARM 8
#define QUAD_ALARM 9
#define HELM_ALARM 10
#define TGT_ALARM 11
#define COLLI_ALARM 12

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

