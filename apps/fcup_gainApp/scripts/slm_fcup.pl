#!/bin/env perl

use Pezca; 
use lib ("$ENV{APP}/fcup_gain/scripts/");
use LSF;

$| = 1;

$n = 0;
print "FCUP(na) rawSLM  2C21(na) 2C24(na) 2H01(na)  Intercept  Slope\n";
print "--------------------------------------------------------------\n";
while (1) {
    ($error,$fcup) = Pezca::GetDouble('scaler_calc1');
    ($error,$bpm) = Pezca::GetDouble('IPM2C21A');
    ($error,$slm) = Pezca::GetDouble('scaler_calc2');
    ($error,$slm_raw) = Pezca::GetDouble('scalerS12a');
    ($error, $na_2c21) = Pezca::GetDouble('IPM2C21A.IENG');
    ($error, $na_2c24) = Pezca::GetDouble('IPM2C24A.IENG');
    ($error, $na_2h01) = Pezca::GetDouble('IPM2H01.IENG');

    if ($fcup > 0.5) {
	$fcup_array[$n] = &round_off($fcup);
	$slm_array[$n] = &round_off($slm);
	$c21_array[$n] = &round_off($na_2c21);
	$c24_array[$n] = &round_off($na_2c24);
	$h01_array[$n] = &round_off($na_2h01);


	if ($n > 10) {
	    $parm_ref = &LSF(\@fcup_array, \@slm_array);
	    $intercept = int($$parm_ref[0]);
	    $slope = $$parm_ref[1];

#	    $parm_ref = &LSF(\@2c12_array, \@slm_array);
	    print "$fcup_array[$n]   $slm_array[$n]   ";
	    print "$c21_array[$n]    $c24_array[$n]   $h01_array[$n] ";
	    print " $intercept  $slope\n";	
	}
	$n++;
    }
    sleep 1;
}


sub round_off {
    my ($x) = @_;

    $x = int(1000.*$x)/1000.;
}









