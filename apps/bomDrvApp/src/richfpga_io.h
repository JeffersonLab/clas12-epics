#ifndef RICHFPGA_IO_H
#define RICHFPGA_IO_H

typedef struct
{
	union
	{
		unsigned int val;
		struct
		{
			unsigned int cmd_fsu			: 1;
			unsigned int cmd_ss			: 1;
			unsigned int cmd_fsb			: 1;
			unsigned int swb_buf_250f	: 1;
			unsigned int swb_buf_500f	: 1;
			unsigned int swb_buf_1p		: 1;
			unsigned int swb_buf_2p		: 1;
			unsigned int ONOFF_ss		: 1;
			unsigned int sw_ss_300f		: 1;
			unsigned int sw_ss_600f		: 1;
			unsigned int sw_ss_1200f	: 1;
			unsigned int EN_ADC			: 1;
			unsigned int H1H2_choice	: 1;
			unsigned int sw_fsu_20f		: 1;
			unsigned int sw_fsu_40f		: 1;
			unsigned int sw_fsu_25k		: 1;
			unsigned int sw_fsu_50k		: 1;
			unsigned int sw_fsu_100k	: 1;
			unsigned int sw_fsb1_50k	: 1;
			unsigned int sw_fsb1_100k	: 1;
			unsigned int sw_fsb1_100f	: 1;
			unsigned int sw_fsb1_50f	: 1;
			unsigned int cmd_fsb_fsu	: 1;
			unsigned int valid_dc_fs	: 1;
			unsigned int sw_fsb2_50k	: 1;
			unsigned int sw_fsb2_100k	: 1;
			unsigned int sw_fsb2_100f	: 1;
			unsigned int sw_fsb2_50f	: 1;
			unsigned int valid_dc_fsb2	: 1;
			unsigned int ENb_tristate	: 1;
			unsigned int polar_discri	: 1;
			unsigned int inv_discriADC	: 1;
		} bits;
	} Global0;

	union
	{
		unsigned int val;
		struct
		{
			unsigned int d1_d2					: 1;
			unsigned int cmd_CK_mux				: 1;
			unsigned int ONOFF_otabg			: 1;
			unsigned int ONOFF_dac				: 1;
			unsigned int small_dac				: 1;
			unsigned int enb_outADC				: 1;
			unsigned int inv_startCmptGray	: 1;
			unsigned int ramp_8bit				: 1;
			unsigned int ramp_10bit				: 1;
			unsigned int Reserved0				: 23;
		} bits;
	} Global1;

	union
	{
		unsigned int val;
		struct
		{
			unsigned int DAC0				: 10;
			unsigned int Reserved0		: 6;
			unsigned int DAC1				: 10;
			unsigned int Reserved1		: 6;
		} bits;
	} DAC;

	unsigned int Reserved0;

	union
	{
		unsigned int val;
		struct
		{
			unsigned int Gain0			: 8;
			unsigned int Sum0				: 1;
			unsigned int CTest0			: 1;
			unsigned int MaskOr0			: 2;
			unsigned int Reserved0		: 4;
			unsigned int Gain1			: 8;
			unsigned int Sum1				: 1;
			unsigned int CTest1			: 1;
			unsigned int MaskOr1			: 2;
			unsigned int Reserved1		: 4;
		} bits;
	} CH[32];
	
} MAROC_Regs;

typedef struct
{
	unsigned int Ch0_31_Hold1;
	unsigned int Ch32_63_Hold1;
	unsigned int Ch0_31_Hold2;
	unsigned int Ch32_63_Hold2;
} MAROC_DyRegs;

typedef struct
{
/* 0x0000-0x0003 */ unsigned int		Ctrl;
/* 0x0004-0x0007 */ unsigned int		Reserved0[(0x0008-0x0004)/4];
/* 0x0008-0x000B */ unsigned int		SpiCtrl;
/* 0x000C-0x000F */ unsigned int		SpiStatus;
/* 0x0010-0x00FF */ unsigned int		Reserved1[(0x0100-0x0010)/4];
} RICH_clk;

typedef struct
{
/* 0x0000-0x0003 */ unsigned int		SerCtrl;
/* 0x0004-0x0007 */ unsigned int		SerStatus;
/* 0x0008-0x000B */ unsigned int		DACAmplitude;
/* 0x000C-0x000F */ unsigned int		Reserved0[(0x0010-0x000C)/4];
/* 0x0010-0x009F */ MAROC_Regs		Regs;
/* 0x00A0-0x00AF */ MAROC_DyRegs		DyRegs_WrAll;
/* 0x00B0-0x00DF */ MAROC_DyRegs		DyRegs_Rd[3];
/* 0x00E0-0x00FF */ unsigned int		Reserved1[(0x0100-0x00E0)/4];
} RICH_MAROC_Cfg;

typedef struct
{
/* 0x0000-0x000F */ unsigned int		DisableCh[4];
/* 0x0010-0x0013 */ unsigned int		HitOrMask0;
/* 0x0014-0x0017 */ unsigned int		HitOrMask1;
/* 0x0018-0x00FF */ unsigned int		Reserved0[(0x0100-0x0018)/4];
/* 0x0100-0x01FF */ unsigned int		Scalers[64];
} RICH_Maroc_Proc;

typedef struct
{
/* 0x0000-0x0003 */ unsigned int		AdcCtrl;
/* 0x0004-0x0007 */ unsigned int		Reserved0[(0x0008-0x0004)/4];
/* 0x0008-0x000B */ unsigned int		Hold1Delay;
/* 0x000C-0x000F */ unsigned int		Hold2Delay;
/* 0x0010-0x00FF */ unsigned int		Reserved1[(0x0100-0x0010)/4];
} RICH_MAROC_Adc;

typedef struct
{
/* 0x0000-0x0003 */ unsigned int		Lookback;
/* 0x0004-0x0007 */ unsigned int		WindowWidth;
/* 0x0008-0x000B */ unsigned int		BlockCfg;
/* 0x000C-0x000F */ unsigned int		Reserved0[(0x0010-0x000C)/4];
/* 0x0010-0x0013 */ unsigned int		DeviceID;
/* 0x0014-0x0017 */ unsigned int		TrigDelay;
/* 0x0018-0x0023 */ unsigned int		Reserved1[(0x0024-0x0018)/4];
/* 0x0024-0x0027 */ unsigned int		FifoWordCnt;
/* 0x0028-0x002B */ unsigned int		FifoEventCnt;
/* 0x002C-0x007F */ unsigned int		Reserved2[(0x0080-0x002C)/4];
/* 0x0080-0x0083 */ unsigned int		FifoData;
/* 0x0084-0x00FF */ unsigned int		Reserved3[(0x0100-0x0084)/4];
} RICH_EvtBuilder;

typedef struct
{
/* 0x0000-0x0003 */ unsigned int		ErrCtrl;
/* 0x0004-0x0007 */ unsigned int		ErrAddrL;
/* 0x0008-0x000B */ unsigned int		ErrAddrH;
/* 0x000C-0x000F */ unsigned int		Reserved0[(0x0010-0x000C)/4];
/* 0x0010-0x0013 */ unsigned int		HeartBeatCnt;
/* 0x0014-0x0017 */ unsigned int		InitializationCnt;
/* 0x0018-0x001B */ unsigned int		ObservationCnt;
/* 0x001C-0x001F */ unsigned int		CorrectionCnt;
/* 0x0020-0x0023 */ unsigned int		ClassifactionCnt;
/* 0x0024-0x0027 */ unsigned int		InjectionCnt;
/* 0x0028-0x002B */ unsigned int		EssentialCnt;
/* 0x002C-0x002F */ unsigned int		UncorrectableCnt;
/* 0x0030-0x0033 */ unsigned int		RamAddr;
/* 0x0034-0x0037 */ unsigned int		RamWrData;
/* 0x0038-0x003B */ unsigned int		RamRdData;
/* 0x003C-0x003F */ unsigned int		Reserved1[(0x0040-0x003C)/4];
/* 0x0040-0x0043 */ unsigned int		RegData;
/* 0x0044-0x0047 */ unsigned int		RegCtrl;
/* 0x0048-0x004F */ unsigned int		Reserved2[(0x0050-0x0048)/4];
/* 0x0050-0x0053 */ unsigned int		MonRd;
/* 0x0054-0x0057 */ unsigned int		MonWr;
/* 0x0058-0x005B */ unsigned int		MonStatus;
/* 0x005C-0x005F */ unsigned int		Reserved3[(0x0060-0x005C)/4];
/* 0x0060-0x0063 */ unsigned int		XAdcCtrl;
/* 0x0064-0x0067 */ unsigned int		XAdcStatus;
/* 0x0068-0x006F */ unsigned int		Reserved4[(0x0070-0x0068)/4]; 
/* 0x0070-0x0073 */ unsigned int		FiberCtrl;
/* 0x0074-0x0077 */ unsigned int		FiberStatus;
/* 0x0078-0x00FF */ unsigned int		Reserved5[(0x0100-0x0078)/4];
} RICH_Testing;

// Mux signal selection for SD->*Src registers
#define SD_SRC_SEL_0					0
#define SD_SRC_SEL_1					1
#define SD_SRC_SEL_MAROC_OR		2
#define SD_SRC_SEL_INPUT_1			5
#define SD_SRC_SEL_INPUT_2			6
#define SD_SRC_SEL_INPUT_3			7
#define SD_SRC_SEL_MAROC_OR1_0	10
#define SD_SRC_SEL_MAROC_OR1_1	11
#define SD_SRC_SEL_MAROC_OR2_0	12
#define SD_SRC_SEL_MAROC_OR2_1	13
#define SD_SRC_SEL_MAROC_OR3_0	14
#define SD_SRC_SEL_MAROC_OR3_1	15
#define SD_SRC_SEL_PULSER_DLY0	18
#define SD_SRC_SEL_PULSER_DLY1	19
#define SD_SRC_SEL_PULSER_DLY2	20
#define SD_SRC_SEL_PULSER_DLY0_N	21
#define SD_SRC_SEL_PULSER_DLY1_N	22
#define SD_SRC_SEL_PULSER_DLY2_N	23
#define SD_SRC_SEL_BUSY				24

typedef struct
{
/* 0x0000-0x0007 */ unsigned int		OutSrc[2];
/* 0x000C-0x0037 */ unsigned int		Reserved0[(0x0038-0x0008)/4];
/* 0x0038-0x003B */ unsigned int		CTestSrc;
/* 0x003C-0x003F */ unsigned int		TrigSrc;
/* 0x0040-0x0043 */ unsigned int		SyncSrc;
/* 0x0044-0x007F */ unsigned int		Reserved1[(0x0080-0x0044)/4];
/* 0x0080-0x0083 */ unsigned int		PulserPeriod;
/* 0x0084-0x0087 */ unsigned int		PulserLowCycles;
/* 0x0088-0x008B */ unsigned int		PulserNCycles;
/* 0x008C-0x008F */ unsigned int		PulserStart;
/* 0x0090-0x0093 */ unsigned int		PulserStatus;
/* 0x0094-0x0097 */ unsigned int		PulserDelay;
/* 0x0098-0x00FF */ unsigned int		Reserved2[(0x0100-0x0098)/4];
/* 0x0100-0x0103 */ unsigned int		ScalerLatch;
/* 0x0104-0x0107 */ unsigned int		Reserved3[(0x0108-0x0104)/4];
/* 0x0108-0x010B */ unsigned int		Scaler_GClk125;
/* 0x010C-0x010F */ unsigned int		Scaler_Sync;
/* 0x0110-0x0113 */ unsigned int		Scaler_Trig;
/* 0x0114-0x011B */ unsigned int		Scaler_Input[2];
/* 0x011C-0x011F */ unsigned int		Reserved4[(0x0120-0x011C)/4];
/* 0x0120-0x0127 */ unsigned int		Scaler_Output[2];
/* 0x0128-0x012B */ unsigned int		Reserved5[(0x012C-0x0128)/4];
/* 0x012C-0x0137 */ unsigned int		Scaler_Or0[3];
/* 0x0138-0x0143 */ unsigned int		Scaler_Or1[3];
/* 0x0144-0x0147 */ unsigned int		Scaler_Busy;
/* 0x0148-0x014B */ unsigned int		Scaler_BusyCycles;
/* 0x014C-0x01FF */ unsigned int		Reserved6[(0x0200-0x014C)/4];
} RICH_sd;

typedef struct
{
/* 0x0000-0x00FF */ RICH_clk			Clk;
/* 0x0100-0x01FF */ RICH_MAROC_Cfg	MAROC_Cfg;
/* 0x0200-0x03FF */ RICH_sd			Sd;
/* 0x0400-0x04FF */ RICH_MAROC_Adc	MAROC_Adc;
/* 0x0500-0x0FFF */ unsigned int		Reserved0[(0x1000-0x0500)/4];
/* 0x1000-0x15FF */ RICH_Maroc_Proc	MAROC_Proc[3];
/* 0x1600-0x1FFF */ unsigned int		Reserved1[(0x2000-0x1600)/4];
/* 0x2000-0x20FF */ RICH_EvtBuilder	EvtBuilder;
/* 0x2100-0x2FFF */ unsigned int		Reserved2[(0x3000-0x2100)/4];
/* 0x3000-0x30FF */ RICH_Testing		Testing;
} RICH_regs;

#define OK								0
#define ERROR							-1

#define FLASH_CMD_WRPAGE			0x12
#define FLASH_CMD_RD					0x13
#define FLASH_CMD_GETSTATUS		0x05
#define FLASH_CMD_WREN				0x06
#define FLASH_CMD_GETID				0x9F
#define FLASH_CMD_ERASE64K			0xDC

#define FLASH_BYTE_LENGTH			32*1024*1024
#define FLASH_MFG_MICRON			0x20
#define FLASH_DEVID_N25Q256A		0xBB19

void rich_write32(void *addr, int val);
unsigned int rich_read32(void *addr);

void rich_read32_n(int n, void *addr, unsigned int *buf);
void rich_TransferSpi_n(int n, unsigned char *tx, unsigned char *rx);

#endif
