program trigbitclean

// make reentrant (required for multiple instances):
option +r;

int i;
float raw[32];
float prescaled[32];
float prescales[32];
assign raw to "{INP}";
assign prescaled to "{OUT}";
assign prescales to "{PRE}";
monitor raw;
monitor prescales;
evflag trigger; sync raw trigger;

ss trigbitclean {
  state start {
    when (efTestAndClear(trigger)) {
      for (i=0; i<32; ++i)
          prescaled[i] = prescales[i] > 0 ? raw[i] / prescales[i] : 0;
      pvPut(prescaled);
    } state start
  }
}


