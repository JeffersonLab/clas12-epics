#!/bin/env perl

use lib ("$ENV{APP}/scaler/scripts/");
use CAGET;

# set up the gain on the amplifier

$ok = &CAPUT('fcup_gain_bit0',0);
$ok = &CAPUT('fcup_gain_bit1',1);
$ok = &CAPUT('fcup_gain_bit2',0);


# now loop over calibration values and read back
# fcup....

for ($i=0; $i<20; $i++) {

    $v_out = -1.0*$i/2.;
    $ok = &CAPUT('fcup_cal',$v_out);
    sleep 30;
}
