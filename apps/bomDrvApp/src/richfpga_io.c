#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <arpa/inet.h> 
#include "richfpga_io.h"

//double bomScalers[16];
//pthread_mutex_t bomScalersMutex;

RICH_regs *pRICH_regs = (RICH_regs *)0x0;

int sockfd_reg = 0;

typedef struct
{
	int len;
	int type;
	int wrcnt;
	int addr;
	int flags;
	int vals[1];
} write_struct;

typedef struct
{
	int len;
	int type;
	int rdcnt;
	int addr;
	int flags;
} read_struct;

typedef struct
{
	int len;
	int type;
	int rdcnt;
	int data[1];
} read_rsp_struct;

void rich_write32(void *addr, int val)
{
	write_struct ws;

	ws.len = 16;
	ws.type = 4;
	ws.wrcnt = 1;
	ws.addr = (int)((long)addr);
	ws.flags = 0;
	ws.vals[0] = val;
	write(sockfd_reg, &ws, sizeof(ws));
}

unsigned int rich_read32(void *addr)
{
	read_struct rs;
	read_rsp_struct rs_rsp;
	int len;
	
	rs.len = 12;
	rs.type = 3;
	rs.rdcnt = 1;
	rs.addr = (int)((long)addr);
	rs.flags = 0;
	write(sockfd_reg, &rs, sizeof(rs));
	
	len = read(sockfd_reg, &rs_rsp, sizeof(rs_rsp));
	if(len != sizeof(rs_rsp))
		printf("Error in %s: socket read failed...\n", __FUNCTION__);
	
	return rs_rsp.data[0];
}

void rich_read32_n(int n, void *addr, unsigned int *buf)
{
	read_struct rs;
	read_rsp_struct rs_rsp;
	int len, i;
	
	for(i = 0; i < n; i++)
	{
		rs.len = 12;
		rs.type = 3;
		rs.rdcnt = 1;
		rs.addr = (int)((long)addr);
		rs.flags = 0;
		write(sockfd_reg, &rs, sizeof(rs));
	}
	
	for(i = 0; i < n; i++)
	{
		len = read(sockfd_reg, &rs_rsp, sizeof(rs_rsp));
		if(len != sizeof(rs_rsp))
			printf("Error in %s: socket read failed...\n", __FUNCTION__);
		
		buf[i] = rs_rsp.data[0];
	}
}

/*****************************************************************/
/*          RICH Static Register Configuration Interface         */
/*****************************************************************/

void rich_clear_regs()
{
	int val;

	/* set rst_sc low */
	val = rich_read32(&pRICH_regs->MAROC_Cfg.SerCtrl);
	val &= 0xFFFFFFFE;
	rich_write32(&pRICH_regs->MAROC_Cfg.SerCtrl, val);

	/* set rst_sc high */
	val |= 0x00000001;
	rich_write32(&pRICH_regs->MAROC_Cfg.SerCtrl, val);
}

MAROC_Regs rich_shift_regs(MAROC_Regs regs)
{
	MAROC_Regs result;
	int i, val;
	
	/* write settings to FPGA shift register */
	rich_write32(&pRICH_regs->MAROC_Cfg.Regs.Global0.val, regs.Global0.val);
	rich_write32(&pRICH_regs->MAROC_Cfg.Regs.Global1.val, regs.Global1.val);
	rich_write32(&pRICH_regs->MAROC_Cfg.Regs.DAC.val, regs.DAC.val);
	
	for(i = 0; i < 32; i++)
		rich_write32(&pRICH_regs->MAROC_Cfg.Regs.CH[i].val, regs.CH[i].val);
	
	/* do shift register transfer */
	val = rich_read32(&pRICH_regs->MAROC_Cfg.SerCtrl);
	val |= 0x00000002;
	rich_write32(&pRICH_regs->MAROC_Cfg.SerCtrl, val);
	
	/* check for shift register transfer completion */
	for(i = 10; i > 0; i--)
	{
		val = rich_read32(&pRICH_regs->MAROC_Cfg.SerStatus);
		if(!(val & 0x00000001))
			break;
		
		if(!i)
			printf("Error in %s: timeout on serial transfer...\n", __FUNCTION__);

		usleep(100);
	}

	/* read back settings from FPGA shift register */
	result.Global0.val = rich_read32(&pRICH_regs->MAROC_Cfg.Regs.Global0.val);
	result.Global1.val = rich_read32(&pRICH_regs->MAROC_Cfg.Regs.Global1.val);
	result.DAC.val = rich_read32(&pRICH_regs->MAROC_Cfg.Regs.DAC.val);
	
	for(i = 0; i < 32; i++)
		result.CH[i].val = rich_read32(&pRICH_regs->MAROC_Cfg.Regs.CH[i].val);
	
	return result;
}

void rich_print_regs(MAROC_Regs regs)
{
	int i;
	
	printf("Global0 = 0x%08X\n", regs.Global0.val);
	printf("   cmd_fsu           = %d\n", regs.Global0.bits.cmd_fsu);
	printf("   cmd_ss            = %d\n", regs.Global0.bits.cmd_ss);
	printf("   cmd_fsb           = %d\n", regs.Global0.bits.cmd_fsb);
	printf("   swb_buf_250f      = %d\n", regs.Global0.bits.swb_buf_250f);
	printf("   swb_buf_500f      = %d\n", regs.Global0.bits.swb_buf_500f);
	printf("   swb_buf_1p        = %d\n", regs.Global0.bits.swb_buf_1p);
	printf("   swb_buf_2p        = %d\n", regs.Global0.bits.swb_buf_2p);
	printf("   ONOFF_ss          = %d\n", regs.Global0.bits.ONOFF_ss);
	printf("   sw_ss_300f        = %d\n", regs.Global0.bits.sw_ss_300f);
	printf("   sw_ss_600f        = %d\n", regs.Global0.bits.sw_ss_600f);
	printf("   sw_ss_1200f       = %d\n", regs.Global0.bits.sw_ss_1200f);
	printf("   EN_ADC            = %d\n", regs.Global0.bits.EN_ADC);
	printf("   H1H2_choice       = %d\n", regs.Global0.bits.H1H2_choice);
	printf("   sw_fsu_20f        = %d\n", regs.Global0.bits.sw_fsu_20f);
	printf("   sw_fsu_40f        = %d\n", regs.Global0.bits.sw_fsu_40f);
	printf("   sw_fsu_25k        = %d\n", regs.Global0.bits.sw_fsu_25k);
	printf("   sw_fsu_50k        = %d\n", regs.Global0.bits.sw_fsu_50k);
	printf("   sw_fsu_100k       = %d\n", regs.Global0.bits.sw_fsu_100k);
	printf("   sw_fsb1_50k       = %d\n", regs.Global0.bits.sw_fsb1_50k);
	printf("   sw_fsb1_100k      = %d\n", regs.Global0.bits.sw_fsb1_100k);
	printf("   sw_fsb1_100f      = %d\n", regs.Global0.bits.sw_fsb1_100f);
	printf("   sw_fsb1_50f       = %d\n", regs.Global0.bits.sw_fsb1_50f);
	printf("   cmd_fsb_fsu       = %d\n", regs.Global0.bits.cmd_fsb_fsu);
	printf("   valid_dc_fs       = %d\n", regs.Global0.bits.valid_dc_fs);
	printf("   sw_fsb2_50k       = %d\n", regs.Global0.bits.sw_fsb2_50k);
	printf("   sw_fsb2_100k      = %d\n", regs.Global0.bits.sw_fsb2_100k);
	printf("   sw_fsb2_100f      = %d\n", regs.Global0.bits.sw_fsb2_100f);
	printf("   sw_fsb2_50f       = %d\n", regs.Global0.bits.sw_fsb2_50f);
	printf("   valid_dc_fsb2     = %d\n", regs.Global0.bits.valid_dc_fsb2);
	printf("   ENb_tristate      = %d\n", regs.Global0.bits.ENb_tristate);
	printf("   polar_discri      = %d\n", regs.Global0.bits.polar_discri);
	printf("   inv_discriADC     = %d\n", regs.Global0.bits.inv_discriADC);

	printf("Global1 = 0x%08X\n", regs.Global1.val);
	printf("   d1_d2             = %d\n", regs.Global1.bits.d1_d2);
	printf("   cmd_CK_mux        = %d\n", regs.Global1.bits.cmd_CK_mux);
	printf("   ONOFF_otabg       = %d\n", regs.Global1.bits.ONOFF_otabg);
	printf("   ONOFF_dac         = %d\n", regs.Global1.bits.ONOFF_dac);
	printf("   small_dac         = %d\n", regs.Global1.bits.small_dac);
	printf("   enb_outADC        = %d\n", regs.Global1.bits.enb_outADC);
	printf("   inv_startCmptGray = %d\n", regs.Global1.bits.inv_startCmptGray);
	printf("   ramp_8bit         = %d\n", regs.Global1.bits.ramp_8bit);
	printf("   ramp_10bit        = %d\n", regs.Global1.bits.ramp_10bit);

	printf("DAC = 0x%08X\n", regs.DAC.val);
	printf("   DAC0              = %d\n", regs.DAC.bits.DAC0);
	printf("   DAC1              = %d\n", regs.DAC.bits.DAC1);

	printf("Channels:\n");
	printf("%7s%7s%7s%7s%7s\n", "CH", "Gain", "Sum", "CTest", "MaskOr");
	for(i = 0; i < 64; i++)
	{
		if(i & 0x1)
			printf("%7d%7d%7d%7d%7d\n", i,
					 regs.CH[i>>1].bits.Gain0, regs.CH[i>>1].bits.Sum0,
					 regs.CH[i>>1].bits.CTest0, regs.CH[i>>1].bits.MaskOr0);
		else
			printf("%7d%7d%7d%7d%7d\n", i,
					 regs.CH[i>>1].bits.Gain1, regs.CH[i>>1].bits.Sum1,
					 regs.CH[i>>1].bits.CTest1, regs.CH[i>>1].bits.MaskOr1);
	}
	printf("\n");
}


void rich_init_regs(MAROC_Regs *regs, int thr)
{
	int i;

	memset(regs, 0, sizeof(MAROC_Regs));

	regs->Global0.bits.cmd_fsu = 1;
	regs->Global0.bits.cmd_ss = 1;
	regs->Global0.bits.cmd_fsb = 1;
	regs->Global0.bits.swb_buf_250f = 0;
	regs->Global0.bits.swb_buf_500f = 0;
	regs->Global0.bits.swb_buf_1p = 0;
	regs->Global0.bits.swb_buf_2p = 0;
	regs->Global0.bits.ONOFF_ss = 1;
	regs->Global0.bits.sw_ss_300f = 1;
	regs->Global0.bits.sw_ss_600f = 1;
	regs->Global0.bits.sw_ss_1200f = 0;
	regs->Global0.bits.EN_ADC = 1;	// enable ADC
//regs->Global0.bits.EN_ADC = 0;	// disable ADC
	regs->Global0.bits.H1H2_choice = 0;
	regs->Global0.bits.sw_fsu_20f = 1;
	regs->Global0.bits.sw_fsu_40f = 1;
	regs->Global0.bits.sw_fsu_25k = 0;
	regs->Global0.bits.sw_fsu_50k = 0;
	regs->Global0.bits.sw_fsu_100k = 0;
	regs->Global0.bits.sw_fsb1_50k = 0;
	regs->Global0.bits.sw_fsb1_100k = 0;
	regs->Global0.bits.sw_fsb1_100f = 1;
	regs->Global0.bits.sw_fsb1_50f = 1;
	regs->Global0.bits.cmd_fsb_fsu = 0;
	regs->Global0.bits.valid_dc_fs = 1;
	regs->Global0.bits.sw_fsb2_50k = 0;
	regs->Global0.bits.sw_fsb2_100k = 0;
	regs->Global0.bits.sw_fsb2_100f = 0;
	regs->Global0.bits.sw_fsb2_50f = 1;
	regs->Global0.bits.valid_dc_fsb2 = 0;
	regs->Global0.bits.ENb_tristate = 1;
	regs->Global0.bits.polar_discri = 0;
	regs->Global0.bits.inv_discriADC = 0;
	regs->Global1.bits.d1_d2 = 0;
	regs->Global1.bits.cmd_CK_mux = 0;
	regs->Global1.bits.ONOFF_otabg = 0;
	regs->Global1.bits.ONOFF_dac = 0;
	regs->Global1.bits.small_dac = 0; /* 0=2.3mV/DAC LSB, 1=1.1mV/DAC LSB */
	regs->Global1.bits.enb_outADC = 0;
//	regs->Global1.bits.enb_outADC = 1;
	regs->Global1.bits.inv_startCmptGray = 0;
	regs->Global1.bits.ramp_8bit = 0;
	regs->Global1.bits.ramp_10bit = 0;
//	regs->DAC.bits.DAC0 = 300; /* with small_dac = 0,  pedestal < ~200, signal ~200 to ~500, 500fC/pulse injected */
	regs->DAC.bits.DAC0 = thr; /* with small_dac = 0,  pedestal < ~200, signal ~200 to ~500, 500fC/pulse injected */
	regs->DAC.bits.DAC1 = 0;


	for(i = 0; i < 64; i++)
	{
		int ctest;
		
		if(i == 0) ctest = 0;
		else ctest = 0;
		
		if(!(i & 0x1))
		{
			regs->CH[i>>1].bits.Gain0 = 64; /* Gain 64 = unity */
			regs->CH[i>>1].bits.Sum0 = 0;
			regs->CH[i>>1].bits.CTest0 = ctest;
			regs->CH[i>>1].bits.MaskOr0 = 0;
		}
		else
		{
			regs->CH[i>>1].bits.Gain1 = 64; /* Gain 64 = unity */
			regs->CH[i>>1].bits.Sum1 = 0;
			regs->CH[i>>1].bits.CTest1 = ctest;
			regs->CH[i>>1].bits.MaskOr1 = 0;
		}
/*
if(i == 0)
{
	regs->CH[i>>1].bits.MaskOr0 = 0;
}
else
{
	if(i != 1)
		regs->CH[i>>1].bits.Gain0 = 0;
	regs->CH[i>>1].bits.Gain1 = 0;
}
*/
	}
}
/*****************************************************************/
/*****************************************************************/
/*****************************************************************/

/*****************************************************************/
/*          RICH Dynamic Register Configuration Interface        */
/*****************************************************************/

void rich_clear_dynregs()
{
	int val;

	/* set rst_r low */
	val = rich_read32(&pRICH_regs->MAROC_Cfg.SerCtrl);
	val &= 0xFFFFFFFB;
	rich_write32(&pRICH_regs->MAROC_Cfg.SerCtrl, val);

	/* set rst_r high */
	val |= 0x00000004;
	rich_write32(&pRICH_regs->MAROC_Cfg.SerCtrl, val);
}

void rich_shift_dynregs(MAROC_DyRegs wr, MAROC_DyRegs *rd1, MAROC_DyRegs *rd2, MAROC_DyRegs *rd3)
{
	int i, val;
	
	/* write settings to FPGA shift register */
	rich_write32(&pRICH_regs->MAROC_Cfg.DyRegs_WrAll.Ch0_31_Hold1, wr.Ch0_31_Hold1);
	rich_write32(&pRICH_regs->MAROC_Cfg.DyRegs_WrAll.Ch32_63_Hold1, wr.Ch32_63_Hold1);
	rich_write32(&pRICH_regs->MAROC_Cfg.DyRegs_WrAll.Ch0_31_Hold2, wr.Ch0_31_Hold2);
	rich_write32(&pRICH_regs->MAROC_Cfg.DyRegs_WrAll.Ch32_63_Hold2, wr.Ch32_63_Hold2);

	/* do shift register transfer */
	val = rich_read32(&pRICH_regs->MAROC_Cfg.SerCtrl);
	val |= 0x00000008;
	rich_write32(&pRICH_regs->MAROC_Cfg.SerCtrl, val);
	
	/* check for shift register transfer completion */
	for(i = 10; i > 0; i--)
	{
		val = rich_read32(&pRICH_regs->MAROC_Cfg.SerStatus);
		if(!(val & 0x00000002))
			break;
		
		if(!i)
			printf("Error in %s: timeout on serial transfer...\n", __FUNCTION__);

		usleep(100);
	}

	/* read back settings from FPGA shift register */
	if(rd1)
	{
		rd1->Ch0_31_Hold1 = rich_read32(&pRICH_regs->MAROC_Cfg.DyRegs_Rd[0].Ch0_31_Hold1);
		rd1->Ch32_63_Hold1 = rich_read32(&pRICH_regs->MAROC_Cfg.DyRegs_Rd[0].Ch32_63_Hold1);
		rd1->Ch0_31_Hold2 = rich_read32(&pRICH_regs->MAROC_Cfg.DyRegs_Rd[0].Ch0_31_Hold2);
		rd1->Ch32_63_Hold2 = rich_read32(&pRICH_regs->MAROC_Cfg.DyRegs_Rd[0].Ch32_63_Hold2);
	}

	if(rd2)
	{
		rd2->Ch0_31_Hold1 = rich_read32(&pRICH_regs->MAROC_Cfg.DyRegs_Rd[1].Ch0_31_Hold1);
		rd2->Ch32_63_Hold1 = rich_read32(&pRICH_regs->MAROC_Cfg.DyRegs_Rd[1].Ch32_63_Hold1);
		rd2->Ch0_31_Hold2 = rich_read32(&pRICH_regs->MAROC_Cfg.DyRegs_Rd[1].Ch0_31_Hold2);
		rd2->Ch32_63_Hold2 = rich_read32(&pRICH_regs->MAROC_Cfg.DyRegs_Rd[1].Ch32_63_Hold2);
	}

	if(rd3)
	{
		rd3->Ch0_31_Hold1 = rich_read32(&pRICH_regs->MAROC_Cfg.DyRegs_Rd[2].Ch0_31_Hold1);
		rd3->Ch32_63_Hold1 = rich_read32(&pRICH_regs->MAROC_Cfg.DyRegs_Rd[2].Ch32_63_Hold1);
		rd3->Ch0_31_Hold2 = rich_read32(&pRICH_regs->MAROC_Cfg.DyRegs_Rd[2].Ch0_31_Hold2);
		rd3->Ch32_63_Hold2 = rich_read32(&pRICH_regs->MAROC_Cfg.DyRegs_Rd[2].Ch32_63_Hold2);
	}
}


void rich_print_dynregs(MAROC_DyRegs regs)
{
	int i;
	
	printf("Channels:\n");
	printf("%7s%7s%7s\n", "CH", "Hold1", "Hold2");
	for(i = 0; i < 64; i++)
	{
		if(i < 32)
			printf("%7d%7d%7d\n", i,
				(regs.Ch0_31_Hold1>>i) & 0x1,
				(regs.Ch0_31_Hold2>>i) & 0x1);
		else
			printf("%7d%7d%7d\n", i,
				(regs.Ch32_63_Hold1>>(i-32)) & 0x1,
				(regs.Ch32_63_Hold2>>(i-32)) & 0x1);
	}
	printf("\n");
}


void rich_init_dynregs(MAROC_DyRegs *regs)
{
	//int i;

	memset(regs, 0, sizeof(MAROC_DyRegs));

	regs->Ch0_31_Hold1 = 0x00000001;
	regs->Ch32_63_Hold1 = 0x00000000;
	regs->Ch0_31_Hold2 = 0x00000000;
	regs->Ch32_63_Hold2 = 0x00000000;
}

float rich_print_scaler(char *name, unsigned int scaler, float ref)
{
  float rate = (float)scaler / ref;
	printf("%-10s %9u %9fHz\n", name, scaler, rate);
  return rate;
}

void rich_dump_scalers(double scalers[16])
{
	float ref, fval;
	unsigned int val;
	int i, j;
	//char buf[100];

	/* halt scaler counting */
	rich_write32(&pRICH_regs->Sd.ScalerLatch, 0x1);

	/* read reference time */
	val = rich_read32(&pRICH_regs->Sd.Scaler_GClk125);
	if(!val)
	{
		printf("Error in %s: referenec time invalid - scaler normalization incorrect\n", __FUNCTION__);
		val = 1;
	}
	ref = (float)val / 125.0E6;

	/* read scalers */
  /*
	rich_print_scaler("GClk125", rich_read32(&pRICH_regs->Sd.Scaler_GClk125), ref);
	rich_print_scaler("Sync", rich_read32(&pRICH_regs->Sd.Scaler_Sync), ref);
	rich_print_scaler("Trig", rich_read32(&pRICH_regs->Sd.Scaler_Trig), ref);
	rich_print_scaler("Input0", rich_read32(&pRICH_regs->Sd.Scaler_Input[0]), ref);
	rich_print_scaler("Input1", rich_read32(&pRICH_regs->Sd.Scaler_Input[1]), ref);
	rich_print_scaler("Input2", rich_read32(&pRICH_regs->Sd.Scaler_Input[2]), ref);
	rich_print_scaler("Output0", rich_read32(&pRICH_regs->Sd.Scaler_Output[0]), ref);
	rich_print_scaler("Output1", rich_read32(&pRICH_regs->Sd.Scaler_Output[1]), ref);
	rich_print_scaler("Output2", rich_read32(&pRICH_regs->Sd.Scaler_Output[2]), ref);
	rich_print_scaler("Or0_1", rich_read32(&pRICH_regs->Sd.Scaler_Or0[0]), ref);
	rich_print_scaler("Or0_2", rich_read32(&pRICH_regs->Sd.Scaler_Or0[1]), ref);
	rich_print_scaler("Or0_3", rich_read32(&pRICH_regs->Sd.Scaler_Or0[2]), ref);
	rich_print_scaler("Or1_1", rich_read32(&pRICH_regs->Sd.Scaler_Or1[0]), ref);
	rich_print_scaler("Or1_2", rich_read32(&pRICH_regs->Sd.Scaler_Or1[1]), ref);
	rich_print_scaler("Or1_3", rich_read32(&pRICH_regs->Sd.Scaler_Or1[2]), ref);
	rich_print_scaler("Busy", rich_read32(&pRICH_regs->Sd.Scaler_Busy), ref);
	rich_print_scaler("BusyCycles", rich_read32(&pRICH_regs->Sd.Scaler_BusyCycles), ref);
*/

  static const int bom_pmt2fpga_map[] = {31,33,27,37,23,41,19,45,15,49,11,53,7,57,3,61,35};
/*
  for(j = 0; j < 64; j++)
	{
		printf("CH%2d", j);

		for(i = 2; i < 3; i++)
		{
			val = rich_read32(&pRICH_regs->MAROC_Proc[i].Scalers[j]);
			fval = (float)val / ref;
			printf(" [%10u,%13.3fHz]", val, fval);
		}
		printf("\n");
	}
*/

    for (int ii=0; ii<16; ii++) {
        int k = bom_pmt2fpga_map[ii];
		val = rich_read32(&pRICH_regs->MAROC_Proc[2].Scalers[k]);
        fval = (float)val / ref;
        scalers[ii] = fval;
        printf("%8.1f ", scalers[ii]);
    }
    printf("\n");

	/* resets scalers */
	rich_write32(&pRICH_regs->Sd.ScalerLatch, 0x2);

	/* enable scaler counting */
	rich_write32(&pRICH_regs->Sd.ScalerLatch, 0x0);
}

void rich_set_pulser(float freq, float duty, int count)
{
	if(freq <= 0.0)
	{
		printf("Error in %s: freq invalid, setting to 1Hz", __FUNCTION__);
		freq = 1.0;
	}

	if((duty <= 0.0) || (duty >= 1.0))
	{
		printf("Error in %s: duty invalid, setting to 50%", __FUNCTION__);
		duty = 0.5;
	}

	rich_write32(&pRICH_regs->Sd.PulserStart, 0);
	
	freq = 125000000 / freq;
	rich_write32(&pRICH_regs->Sd.PulserPeriod, (int)freq);

	duty = freq * (1.0 - duty);
	rich_write32(&pRICH_regs->Sd.PulserLowCycles, (int)duty);

	rich_write32(&pRICH_regs->Sd.PulserNCycles, count);
	rich_write32(&pRICH_regs->Sd.PulserStart, 1);
}

void rich_enable_all_tdc_channels()
{
	int i;
	
	for(i = 0; i < 3; i++)
	{
		rich_write32(&pRICH_regs->MAROC_Proc[i].DisableCh[0], 0x00000000);
		rich_write32(&pRICH_regs->MAROC_Proc[i].DisableCh[1], 0x00000000);
		rich_write32(&pRICH_regs->MAROC_Proc[i].DisableCh[2], 0x00000000);
		rich_write32(&pRICH_regs->MAROC_Proc[i].DisableCh[3], 0x00000000);
	}
}

void rich_disable_all_tdc_channels()
{
	int i;
	
	for(i = 0; i < 3; i++)
	{
		rich_write32(&pRICH_regs->MAROC_Proc[i].DisableCh[0], 0xFFFFFFFF);
		rich_write32(&pRICH_regs->MAROC_Proc[i].DisableCh[1], 0xFFFFFFFF);
		rich_write32(&pRICH_regs->MAROC_Proc[i].DisableCh[2], 0xFFFFFFFF);
		rich_write32(&pRICH_regs->MAROC_Proc[i].DisableCh[3], 0xFFFFFFFF);
	}
}

void rich_enable_tdc_channel(int ch)
{
	//int i;
	int proc_idx, proc_reg, proc_bit;
	int val;
	
	if((ch < 0) || (ch > 191))
	{
		printf("Error in %s: invalid channel %d\n", __FUNCTION__, ch);
		return;
	}

	proc_idx = ch / 64;
	proc_reg = (ch % 64) / 16;
	proc_bit = (ch % 16);

	val = rich_read32(&pRICH_regs->MAROC_Proc[proc_idx].DisableCh[proc_reg]);
	val = val & ~(0x00010001<<proc_bit);
	rich_write32(&pRICH_regs->MAROC_Proc[proc_idx].DisableCh[proc_reg], val);
}

void rich_disable_tdc_channel(int ch)
{
	//int i;
	int proc_idx, proc_reg, proc_bit;
	int val;
	
	if((ch < 0) || (ch > 191))
	{
		printf("Error in %s: invalid channel %d\n", __FUNCTION__, ch);
		return;
	}

	proc_idx = ch / 64;
	proc_reg = (ch % 64) / 16;
	proc_bit = (ch % 16);

	val = rich_read32(&pRICH_regs->MAROC_Proc[proc_idx].DisableCh[proc_reg]);
	val = val | (0x00010001<<proc_bit);
	rich_write32(&pRICH_regs->MAROC_Proc[proc_idx].DisableCh[proc_reg], val);
}

void rich_setup_readout(int lookback, int window)
{
	rich_write32(&pRICH_regs->EvtBuilder.Lookback, lookback);		/* lookback*8ns from trigger time */
	rich_write32(&pRICH_regs->EvtBuilder.WindowWidth, window);	/* capture window*8ns hits after lookback time */
	rich_write32(&pRICH_regs->EvtBuilder.BlockCfg, 1);				/* 1 event per block */
	rich_write32(&pRICH_regs->EvtBuilder.DeviceID, 0x01);			/* setup a dummy device ID (5bit) written in each event for module id - needs to be expanded */
}

void rich_fifo_reset()
{
	rich_write32(&pRICH_regs->Clk.Ctrl, 0x01);						/* assert soft reset */
	rich_write32(&pRICH_regs->Clk.Ctrl, 0x00);						/* deassert soft reset */
}

void rich_fifo_status()
{
	int wordCnt, eventCnt;
	
	wordCnt = rich_read32(&pRICH_regs->EvtBuilder.FifoWordCnt);
	eventCnt = rich_read32(&pRICH_regs->EvtBuilder.FifoEventCnt);
	
	printf("FIFO Event Status: WCNT=%9d ECNT=%9d\n", wordCnt, eventCnt);
}

int rich_fifo_nwords()
{
	return rich_read32(&pRICH_regs->EvtBuilder.FifoWordCnt);
}

void rich_fifo_read(int *buf, int nwords)
{
	while(nwords--)
		*buf++ = rich_read32(&pRICH_regs->EvtBuilder.FifoData);
}

void rich_process_buf(int *buf, int nwords, FILE *f, int print)
{
	static int tag = 15;
	static int tag_idx = 0;
	int word;
	
	while(nwords--)
	{
		word = *buf++;
		
		if(f) fprintf(f, "0x%08X", word);
		if(print) printf("0x%08X", word);
		
		if(word & 0x80000000)
		{
			tag = (word>>27) & 0xF;
			tag_idx = 0;
		}
		else
			tag_idx++;
		
		switch(tag)
		{
			case 0:	// block header
				if(f) fprintf(f, " [BLOCKHEADER] SLOT=%d, BLOCKNUM=%d, BLOCKSIZE=%d\n", (word>>22)&0x1F, (word>>8)&0x3FF, (word>>0)&0xFF);
				if(print) printf(" [BLOCKHEADER] SLOT=%d, BLOCKNUM=%d, BLOCKSIZE=%d\n", (word>>22)&0x1F, (word>>8)&0x3FF, (word>>0)&0xFF);
				break;
				
			case 1:	// block trailer
				if(f) fprintf(f, " [BLOCKTRAILER] SLOT=%d, WORDCNT=%d\n", (word>>22)&0x1F, (word>>0)&0x3FFFFF);
				if(print) printf(" [BLOCKTRAILER] SLOT=%d, WORDCNT=%d\n", (word>>22)&0x1F, (word>>0)&0x3FFFFF);
				break;

			case 2:	// event header
				if(f) fprintf(f, " [EVENTHEADER] TRIGGERNUM=%d, DEVID=%d\n", (word>>0)&0x3FFFFF, (word>>22)&0x1F);
				if(print) printf(" [EVENTHEADER] TRIGGERNUM=%d, DEVID=%d\n", (word>>0)&0x3FFFFF, (word>>22)&0x1F);
				break;
				
			case 3:	// trigger time
				if(tag_idx == 0)
				{
					if(f) fprintf(f, " [TIMESTAMP 0] TIME=%d\n", (word>>0)&0xFFFFFF);
					if(print) printf(" [TIMESTAMP 0] TIME=%d\n", (word>>0)&0xFFFFFF);
				}
				else if(tag_idx == 1)
				{
					if(f) fprintf(f, " [TIMESTAMP 1] TIME=%d\n", (word>>0)&0xFFFFFF);
					if(print) printf(" [TIMESTAMP 1] TIME=%d\n", (word>>0)&0xFFFFFF);
				}
				break;

			case 8:	// TDC hit
				if(f) fprintf(f, " [TDC HIT] EDGE=%d, CH=%d, TIME=%d\n", (word>>26)&0x1,(word>>16)&0xFF, (word>>0)&0xFFFF);
				if(print) printf(" [TDC HIT] EDGE=%d, CH=%d, TIME=%d\n", (word>>26)&0x1,(word>>16)&0xFF, (word>>0)&0xFFFF);
				break;

			case 14:	// data not valid
				if(f) fprintf(f, " [DNV]\n");
				if(print) printf(" [DNV]\n");
				break;
				
			case 15:	// filler word
				if(f) fprintf(f, " [FILLER]\n");
				if(print) printf(" [FILLER]\n");
				break;
				
			default:	// unknown
				if(f) fprintf(f, " [UNKNOWN]\n");
				if(print) printf(" [UNKNOWN]\n");
				break;
		}
	}
}

void rich_setmask_fpga_or(int m0_0, int m0_1, int m1_0, int m1_1, int m2_0, int m2_1)
{
	rich_write32(&pRICH_regs->MAROC_Proc[0].HitOrMask0, m0_0);
	rich_write32(&pRICH_regs->MAROC_Proc[0].HitOrMask1, m0_1);
	rich_write32(&pRICH_regs->MAROC_Proc[1].HitOrMask0, m1_0);
	rich_write32(&pRICH_regs->MAROC_Proc[1].HitOrMask1, m1_1);
	rich_write32(&pRICH_regs->MAROC_Proc[2].HitOrMask0, m2_0);
	rich_write32(&pRICH_regs->MAROC_Proc[2].HitOrMask1, m2_1);
}

/*****************************************************************/
/*****************************************************************/
/*****************************************************************/

#define MAROC_NUM		2

void rich_test_regs(int thr)
{
	int i;
	
	MAROC_Regs wr_regs[MAROC_NUM];
	MAROC_Regs rd_regs[MAROC_NUM];
	MAROC_DyRegs wr_dyn_regs;
	MAROC_DyRegs rd_dyn_regs[MAROC_NUM];
	
	for(i = 0; i < MAROC_NUM; i++)
		rich_init_regs(&wr_regs[i], thr);

	rich_clear_regs();
	for(i = MAROC_NUM-1; i >= 0; i--)
		rich_shift_regs(wr_regs[i]);
	
	for(i = 0; i < MAROC_NUM; i++)
	{
		rd_regs[i] = rich_shift_regs(wr_regs[i]);
	
//		printf("MAROC ID %d READ BACK REG DUMP:\n", i);
//		rich_print_regs(rd_regs[i]);
	}

	/* Initialize dynamic registers */
	rich_init_dynregs(&wr_dyn_regs);

	rich_clear_dynregs();
	rich_shift_dynregs(wr_dyn_regs, NULL, NULL, NULL);
	if(MAROC_NUM == 2)
		rich_shift_dynregs(wr_dyn_regs, &rd_dyn_regs[0], NULL, &rd_dyn_regs[1]);
	else if(MAROC_NUM == 3)
		rich_shift_dynregs(wr_dyn_regs, &rd_dyn_regs[0], &rd_dyn_regs[1], &rd_dyn_regs[2]);

	for(i = 0; i < MAROC_NUM; i++)
	{
//		printf("MAROC ID %d READ BACK DYN REG DUMP:\n", i);
//		rich_print_dynregs(rd_dyn_regs[i]);
	}
}

int open_socket(int port)
{
	struct sockaddr_in serv_addr;
	int sockfd = 0;
	
	if((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
	{
		printf("\n Error : Could not create socket \n");
		exit(1);
	}
	memset(&serv_addr, '0', sizeof(serv_addr)); 

	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(port);

	if(inet_pton(AF_INET, "129.57.160.211", &serv_addr.sin_addr)<=0)
	{
		printf("\n inet_pton error occured\n");
		exit(1);
	} 

	if( connect(sockfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
	{
		printf("\n Error : Connect Failed \n");
		exit(1);
	}
	return sockfd;
}

void open_register_socket()
{
	int n, val;
	
	sockfd_reg = open_socket(6102);

	/* Send endian test header */
	val = 0x12345678;
	write(sockfd_reg, &val, 4);
	
	val = 0;
	n = read(sockfd_reg, &val, 4);
	printf("n = %d, val = 0x%08X\n", n, val);
}

unsigned int gBuf[100000];

#define MAROC_ADC_RESOLUTION_12b		11
#define MAROC_ADC_RESOLUTION_10b		9
#define MAROC_ADC_RESOLUTION_8b		7

#define MAROC_MASK_DISABLE				0x0
#define MAROC_MASK_2ASIC				0x5
#define MAROC_MASK_3ASIC				0x7

void SetupMAROC_ADC(unsigned char h1, unsigned char h2, int resolution, int maroc_mask)
{
	rich_write32(&pRICH_regs->MAROC_Adc.Hold1Delay, h1);
	rich_write32(&pRICH_regs->MAROC_Adc.Hold2Delay, h2);
	rich_write32(&pRICH_regs->MAROC_Adc.AdcCtrl, (resolution<<4) | (maroc_mask<<1) | 0x1);
	rich_write32(&pRICH_regs->MAROC_Adc.AdcCtrl, (resolution<<4) | (maroc_mask<<1));
}

int main2(int argc, char *argv[])
{
	//int n, val = 0;
	//long long nevents, nbytes, dbytes;

	open_register_socket();

	rich_test_regs(400);
	rich_set_pulser(10000000.0, 0.5, 0xFFFFFFFF);					// freq, dutycycle, repetition (0= disable,0xffffffff = infinite)
	rich_write32(&pRICH_regs->MAROC_Cfg.DACAmplitude, 1000);

	// Setup FPGA version of MAROC OR (note: this OR is formed in the FPGA from the MAROC hits and does not use the MAROC_OR signal)
	rich_setmask_fpga_or(0x00000001, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000);

	rich_write32(&pRICH_regs->Sd.OutSrc[0], SD_SRC_SEL_PULSER_DLY0);			// output pulser to TTL outputs for probing/scope trigger
	rich_write32(&pRICH_regs->Sd.OutSrc[1], SD_SRC_SEL_PULSER_DLY1);
	rich_write32(&pRICH_regs->Sd.CTestSrc, 0);//SD_SRC_SEL_PULSER_DLY1_N);	// internal pulser fires test charge injection
	rich_write32(&pRICH_regs->Sd.PulserDelay, (0<<16) | (0<<8) | (0<<0));
	
	/* Set trig source to disabled */
	rich_write32(&pRICH_regs->Sd.TrigSrc, 0);
	rich_write32(&pRICH_regs->EvtBuilder.TrigDelay, 128);				//128*8ns = 1024ns trigger delay
	
	int hold_dly = 5;
//	SetupMAROC_ADC(20, 20, MAROC_ADC_RESOLUTION_12b, MAROC_MASK_DISABLE);
	SetupMAROC_ADC(hold_dly, hold_dly, MAROC_ADC_RESOLUTION_12b, MAROC_MASK_3ASIC);

	/* Soft pulse sync */
	rich_write32(&pRICH_regs->Sd.SyncSrc, 1);
	rich_write32(&pRICH_regs->Sd.SyncSrc, 0);

	rich_fifo_reset();
	rich_fifo_status();
	rich_setup_readout(1200/8, 400/8);			// lookback 1.2us, capture 400ns
	
	rich_disable_all_tdc_channels();
	rich_enable_all_tdc_channels();
	
	/* Set trig source to pulser when ready to take events */
	rich_write32(&pRICH_regs->Sd.TrigSrc, SD_SRC_SEL_PULSER_DLY0);		// trigger source is pulser (delayed by TrigDelay)

  int thr = 300;
  rich_test_regs(thr);
  
  rich_write32(&pRICH_regs->MAROC_Cfg.DACAmplitude, 4095);

    double scalers[16];
  while(1)
  {
    rich_dump_scalers(scalers);
    usleep(1000000);
  }
  
	close(sockfd_reg);
	
	return 0;
}
