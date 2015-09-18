
/*  moller system commands */

#define DO_NOTHING  0
#define CONFIGURE_LEFT_NEG  10
#define CONFIGURE_LEFT_POS  11
#define CONFIGURE_RIGHT_NEG  12
#define CONFIGURE_RIGHT_POS  13
#define CHANGE_HELM_NEG      14
#define CHANGE_HELM_POS      15
#define CHANGE_TARGET_LEFT   16
#define CHANGE_TARGET_RIGHT  17
#define CHANGE_TARGET_EMPTY  18
#define CHANGE_TARGET_ALUM   19
#define BACKOUT    20


/* moller system status */
#define STATE_INIT              1
#define WAITING                 3
#define CONFIGURED_NEG_LEFT    10
#define CONFIGURED_POS_LEFT    20
#define CONFIGURED_NEG_RIGHT   30
#define CONFIGURED_POS_RIGHT   40
#define UNDEFINED             666

/* helmholtz coils */

#define NEGATIVE   -1 
#define OFF         0
#define POSITIVE    1
#define OK          1

/* target commands */

#define LEFT        11
#define EMPTY       12
#define RIGHT       13
#define CALIBRATE    1

#define CALIBRATED   1

#define DONE         0

/* quad commands */

#define ON       1
#define OFF      0

/* daq commands  */

#define DISABLED  1
#define ENABLED   0
#define RESET     1
