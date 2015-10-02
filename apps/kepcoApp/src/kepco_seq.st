program kepco_seq

option +c;  /* wait for db connections */

#define N_POLARITY   -18.0
#define P_POLARITY   +18.0
#define ON             1
#define OFF            0

double v_set;
assign v_set          to "kepcoseti.VAL";
monitor v_set;

double i_readback;
assign i_readback          to "hallb_sf_xy560_0_19.VAL";
monitor i_readback;

double k_command;
assign k_command      to "kepco_command.VAL";
monitor k_command;

double kepco_off;
assign kepco_off to "kepco_off.VAL";

double kepco_negative;
assign kepco_negative to "kepco_negative.VAL";

double kepco_positive;
assign kepco_positive to "kepco_positive.VAL";

/*--------------------------------------------------------------*/
/* kepco power supply sequencer                                 */
/* for moller helmholtz coils                                   */
/*--------------------------------------------------------------*/

ss kepco_init 
{

/* first initialize the kepco DAC to put out zero volts */

  state init 
  {
    when () 
    {
	printf("Initializing kepco to 0 volts\n");
	v_set  = 0.0;
	pvPut(v_set);
	printf("Initializing kepco_command tp 99\n");
	k_command = 99.;
	pvPut(k_command);
	printf("Done with kepco initialization\n");
	kepco_off = ON;
	kepco_negative = OFF;
	kepco_positive = OFF;
	pvPut(kepco_off);
	pvPut(kepco_negative);
	pvPut(kepco_positive);
    } state get_command
  }

/* Now keep probing for commands and take appropriate action */

  state get_command
  {
    when ( k_command == 0.0 ) 
    {
/*       printf("Setting kepco to 0 volts: command 0\n");  */

	kepco_off = OFF;
        kepco_positive = OFF;
        kepco_negative = OFF;
        pvPut(kepco_off);
        pvPut(kepco_negative);
        pvPut(kepco_positive);
    } state set_zero

    when ( k_command == -1.0 )
    {
/*	printf("Setting kepco to 0 volts first then -18: command -1\n"); */
	v_set  = 0.0;
	pvPut(v_set);

	kepco_off = OFF;
        kepco_positive = OFF;
        kepco_negative = OFF;
        pvPut(kepco_off);
        pvPut(kepco_negative);
        pvPut(kepco_positive);
    } state set_negative

   
    when ( k_command == 1.0 )
    {
/*	printf("Setting kepco to 0 volts first then +18: command 1\n"); */
	v_set  = 0.0;
	pvPut(v_set);

	kepco_off = OFF;
        kepco_positive = OFF;
        kepco_negative = OFF;
        pvPut(kepco_off);
        pvPut(kepco_negative);
        pvPut(kepco_positive);    } state set_positive

    when ( k_command == 99.0 && delay(10) )
    {
/*	printf("kepco command 99 do nothing\n");  */
     ;
    } state check_readback
  }

  state check_readback
  {
     when()
     {
      kepco_off = OFF;
      kepco_positive = OFF;
      kepco_negative = OFF;

      if (i_readback < -0.25) {
	kepco_negative = ON;
      } else if (i_readback > 0.25) {
        kepco_positive = ON;
      } else {
        kepco_off = ON;
      }	
      pvPut(kepco_off);
      pvPut(kepco_negative);
      pvPut(kepco_positive);

     } state get_command
  }

  state set_zero
  {
     when () 
     {
/*       printf("Setting kepco to 0 volts\n"); */
       v_set  = 0.;
       pvPut(v_set);
       k_command = 99.;
       pvPut(k_command);
     } state get_command
  } 

  state set_positive
  {
      when ( v_set == 0.0 && delay(10.0) ) {
/*          printf("Setting kepco to +18 volts\n"); */
	  v_set  = P_POLARITY;
	  pvPut(v_set);
          k_command = 99.;
          pvPut(k_command);
        } state get_command
  }

  state set_negative
  {
	when ( v_set == 0.0 && delay(10.0) ) {
/*          printf("Setting kepco to -18 volts\n"); */
	  v_set  = N_POLARITY;
	  pvPut(v_set);
          k_command = 99.;
          pvPut(k_command);
        } state get_command
  }
}

