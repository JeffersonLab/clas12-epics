#ifndef COMMAND_H
#define COMMAND_H

#define NoSupport 0x00    /* No device support for PV       */
#define G_Valid   0x80    /* Get HV validity                */
#define G_HV      0x81    /* Get HV on/off                  */
#define G_Alarm   0x82    /* Get Chassis alarm status       */
#define S_CE      0x01    /* Set enable/disable             */
#define S_DV      0x02    /* Set demand voltage             */
#define S_RDN     0x03    /* Set ramp down                  */
#define S_RUP     0x04    /* Set ramp up                    */
#define S_TC      0x05    /* Set trip current               */
#define S_MVDZ    0x06    /* Set measured voltage dead-zone */
#define S_MCDZ    0x07    /* Set measured current dead-zone */
#define S_HV      0x08    /* Set HV on/off                  */
#define S_SOT     0x09    /* Set samples over threshold     */
#define S_PRD     0x0A    /* Set post ramp delay            */ 
#define S_CHHV    0x0B    /* Set CHANNEL HV on/off          */ 
#define S_BDHV    0x0C    /* Set BOARD HV on/off            */ 
#define S_VMAX    0x0D    /* Set MAX CHANNEL VOLATAGE       */ 

// LV Boards:
#define S_UNVT    0x10    /* Set Under Voltage Threshold    */
#define S_OVVT    0x11    /* Set Over  Voltage Threshold    */
#define S_INTLK   0x12    /* Set Interlock Status           */

// Bipolar Boards:
#define S_POL     0x20    /* Set Polarity                   */

#define G_HVFS    0x01    /* HV Fan Stat                    */
#define G_PWFS    0x02    /* PW Fan Stat                    */
#define G_PWV     0x03    /* PW Voltage                     */
#define G_HVPW    0x04    /* HvPwSM                         */
#define G_MOD     0x05    /* Model Name                     */
#define G_SWR     0x06    /* Sowftware Release              */

#endif
