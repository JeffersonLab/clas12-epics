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
/// my: it is actually the time with high current before trip occurs
#define S_PRD     0x0A    /* Set post ramp delay            */ 
/// my:
#define S_CHHV      0x0B    /* Set CHANNEL HV on/off                  */ 
/// my:
#define S_BDHV      0x0C    /* Set BOARD HV on/off                  */ 
#define S_VMAX      0x0D    /* Set MAX CHANNEL VOLATAGE                 */ 

// Group Operations
#define S_GRP_HV  0xFB /* Set HV on/off      */
#define S_GRP_DV  0xF2 /* Set demand voltage */
#define S_GRP_TC  0xF5 /* Set trip current   */
#define S_GRP_RDN 0xF3 /* Set ramp down      */
#define S_GRP_RUP 0xF4 /* Set ramp up        */

#endif
