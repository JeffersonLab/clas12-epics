/* drvV450.h */

/* sergey from 3122 */

struct  v450_registers {
  unsigned short regs[46];
  unsigned short data[32];
  unsigned short control[48];
  unsigned short res1;
  unsigned short bist_dac;
  unsigned short buffer[128];

  /* to make structure size equal to 2048 - will be used to increment boards addresses */
  unsigned short spare[2048-256];

}; 

typedef struct v450_registers v450;

/* Highland V450 ADC memory map register offsets  and sizes*/
#define vximfr  regs[0x00/2]
#define vxitype regs[0x02/2]
#define serial  regs[0x06/2]
#define romid   regs[0x08/2]
#define romrev  regs[0x0A/2]
#define mcount  regs[0x0C/2]
#define dfilt   regs[0x0E/2]
#define cflags  regs[0x10/2]
#define rflags  regs[0x12/2]
#define relays  regs[0x16/2]
#define uled    regs[0x18/2]
#define mode    regs[0x1A/2]
#define calid   regs[0x1C/2]
#define biss    regs[0x1E/2]
#define macro   regs[0x20/2]
#define param0  regs[0x22/2]
#define param1  regs[0x24/2]
#define param2  regs[0x26/2]
#define ycal    regs[0x28/2]
#define dcal    regs[0x2A/2]
#define fake1   regs[0x2C/2]
#define fake2   regs[0x2E/2]

#define rtda    regs[0x30/2]
#define tmpa    regs[0x32/2]
#define rtdb    regs[0x34/2]
#define tmpb    regs[0x36/2]
#define rtdc    regs[0x38/2]
#define tmpc    regs[0x3A/2]
#define rtdd    regs[0x3C/2]
#define tmpd    regs[0x3E/2]
#define tmpr    regs[0x40/2]
#define rahi    regs[0x44/2]
#define ralo    regs[0x46/2]
#define rbhi    regs[0x48/2]
#define rblo    regs[0x4A/2]
#define rchi    regs[0x4C/2]
#define rclo    regs[0x4E/2]
#define rdhi    regs[0x50/2]
#define rdlo    regs[0x52/2]
#define trhi    regs[0x54/2]
#define trlo    regs[0x56/2]
#define lbhi    regs[0x58/2]
#define lblo    regs[0x5A/2]

#define CTL0    regs[0x9C/2]
#define CTL1    regs[0xA2/2]
#define CTL2    regs[0xA8/2]
#define CTL3    regs[0xAE/2]
#define CTL4    regs[0xB4/2]
#define CTL5    regs[0xBA/2]
#define CTL6    regs[0xC0/2]
#define CTL7    regs[0xC6/2]
#define CTL8    regs[0xCC/2]
#define CTL9    regs[0xD2/2]
#define CTL10    regs[0xD8/2]
#define CTL11    regs[0xDE/2]
#define CTL12    regs[0xE4/2]
#define CTL13    regs[0xEA/2]
#define CTL14    regs[0xF0/2]
#define CTL15    regs[0xF6/2]
#define board0	regs[0xeff0c000/2]  // VME Address of V450 Board 0
#define board1	regs[0xeff0c000/2]  // VME Address of V450 Board 1
#define board2	regs[0xeff0c000/2]  // VME Address of V450 Board 2
#define board3	regs[0xeff0c000/2]  // VME Address of V450 Board 3
#define board4	regs[0xeff0c000/2]  // VME Address of V450 Board 4
#define board5	regs[0xeff0c000/2]  // VME Address of V450 Board 5
#define board6	regs[0xeff0c000/2]  // VME Address of V450 Board 6
#define board7	regs[0xeff0c000/2]  // VME Address of V450 Board 7
#define board8	regs[0xeff0c000/2]  // VME Address of V450 Board 8

/* Highland V450 ADC control and status register definitions */
#define rtd_on		0x1


/* 3122: memory map register offsets  and sizes*/
#define bir     regs[0x00/2] /* board ID register */
#define csr     regs[0x02/2] /* control and status register */
#define ccr     regs[0x04/2] /* configuration control register */  
#define rcr 	regs[0x06/2] /* rate control register */
#define icr 	regs[0x08/2] /* interrupt control register */
#define ivr 	regs[0x0A/2] /* interrupt vector register */
#define src 	regs[0x0C/2] /* software reset command */
#define stc 	regs[0x0E/2] /* software trigger command */
#define gain	regs[0x10/2] /* auto gain */
#define tr0 	regs[0x20/2] /* interval timer 0 register */
#define tr1 	regs[0x22/2] /* interval timer 1 register */
#define dcr 	regs[0x24/2] /* data counter register */
#define tcr 	regs[0x26/2] /* timer control register */

/* 3122: control and status register definitions */
#define LED_ON		0x0000 /* bit 15 */
#define LED_OFF		0x8000 /* bit 15 */
#define OFFSET_BIN	0x0000 /* bit 14 */
#define TWOS_COMP	0x4000 /* bit 14 */
#define SOFT_TRIG	0x0000 /* bits 13 and 12 */
#define EXT_TRIG	0x1000 /* bits 13 and 12 */
#define TIME_TRIG	0x2000 /* bits 13 and 12 */
#define END_BUFFER	0x0000 /* bit 10 */
#define MID_BUFFER	0x0400 /* bit 10 */

/* 3122: configuration and control register definitions */
#define GAIN_1X		0x0000 /* bits 9 and 8 */
#define GAIN_10X	0x0100 /* bits 9 and 8 */
#define GAIN_AUTO	0x0200 /* bits 9 and 8 */
#define AUTO_SCAN	0x0000 /* bits 7 and 6 */
#define SINGLE_SCAN	0x0040 /* bits 7 and 6 */

