/* fr_xscalewf.st
 * A sequencer to set the X scale waveform.  The X scale waveform is used
 * as the X scale for plotting the raw current waveforms in the X-Y Plot on
 * screenin, and contains the X scale values in engineering unit -
 * millisecond.  Each value repersents 0.5ms.
 */

program frxscale

option +c; /* Wait for all database connections */

/* X Scale waveform */
float xscalewf[512];
assign xscalewf to "{R}_XSCALEWF";

float xscale;
int i;

ss frxscale
{
  state init
  {
    when () {
      xscale = 0;
      for (i = 0; i < 512; i++) {
        xscalewf[i] = xscale;
	xscale = xscale + 0.005;
      }
      pvPut(xscalewf);
    } state done
  }

  state done
  {
    /* idle forever */
    when (delay(1)) { } state done
  }
}
