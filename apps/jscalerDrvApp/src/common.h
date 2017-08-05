#ifndef JSCALERS_COMMON_DOT_H
#define JSCALERS_COMMON_DOT_H

//#define SIMULATION

#define SCALERS_READ_INTERVAL 1

#define JLAB_SLOT_IS_EMPTY -1
//#define JLAB_BOARD_DISC2 0
//#define JLAB_BOARD_FADC250 1

#define SMI_STATE_UNDEFINED_2 -2
#define SMI_STATE_UNDEFINED -1
#define SMI_STATE_OFF 0
#define SMI_STATE_ON 1
#define SMI_STATE_ERROR 2

//#define NUMBEROFSCALERS_DISC2 16 
//#define NUMBEROFSCALERS_FADC250 16
//#define NUMBEROFSPECTRA_FADC250 5

#define NUMBER_OF_SCALER_THRESHOLDS 2
#define MODE_PARS_NUMBER 4

#define SCALER_NUMBER_OF_SUBGROUPS 4
#define NOT_PRESENT_VALUE -1
#define BOARD_NOT_PRESENT -2
#define CRATE_NOT_PRESENT -3

enum{
JLAB_SET_THRESHOLD,
JLAB_SET_READ_MODE,
JLAB_GET_NFIBERS,
};

enum{
ScalerThreshTrig_Gr1, ScalerThreshTDC_Gr1, ScalerThreshTrig_Gr2, ScalerThreshTDC_Gr2 
};

enum{SCALER_GROUP_1,SCALER_GROUP_2};

#define ScalerDsc2ClockFrequecy 125e+6

#define SCALERS_LSWAP(x) ((((x) & 0x000000ff) << 24) | \
                         (((x) & 0x0000ff00) <<  8) | \
                         (((x) & 0x00ff0000) >>  8) | \
                         (((x) & 0xff000000) >> 24))

#ifdef __cplusplus
extern "C" {
#endif
int IocGetValue(int crate, int slot, int channel, int command, double values[]);
int IocSetValue(int crate, int slot, int channel, int command, double values[]);
void IocReadWaveform(int crate, int slot, int channel, int len, double values[]);
int IocGetWaveformLength(int crate, int slot, int channel, int *len);
void IocReadWaveformSSPData(int crate, int slot, int channel, int len, double values[]);
int IocGetWaveformLengthSSPData(int crate, int slot, int channel, int *len);
void block_until_crate_read(int crate);

int ScalerBoardSmiMonitor( int is_init, char *epics_name,
unsigned int crate, unsigned int slot, unsigned int first_channel, unsigned int chs_number);

int ScalerBoardSmiControl
(char *smi_obj_name, unsigned int crate, unsigned int slot, 
unsigned int first_channel, unsigned int chs_number, unsigned int onoff);

int ScalerCrateSmiInit(char *smi_obj_name, unsigned int crate);

#ifdef __cplusplus
}
#endif

#endif



