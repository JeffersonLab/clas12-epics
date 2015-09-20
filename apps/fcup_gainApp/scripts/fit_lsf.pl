#!/bin/env perl

# make a list of files in ../data
use lib ("$ENV{APP}/fcup_gain/scripts/");
use LSF;

opendir DATADIR, '/home/epics/DATA/FCUP';
@data_files = grep !/^\.\.?$/, readdir DATADIR;

open(OUT, ">fit_results.txt");
foreach $f (@data_files) {
    undef(@x);
    undef(@y);
    @pieces = split(/\_/,$f);
    ($min) = split(/\./, $pieces[6]);
    $hour = $pieces[5];
    if ($hour > 9) {
	$h_string = "$hour";
    } else {
	$h_string = "0$hour";
    }
    if ($min > 9) {
	$m_string = "$min";
    } else {
	$m_string = "0$min";
    }
    $date = "$pieces[4]/$pieces[3]/$pieces[2]-$h_string:$m_string";

    open(IN, "< /home/epics/DATA/FCUP/$f");
    $i=0;
    $n_zero = 0.;
    $sum_zero = 0;
    while(<IN>) {
	chop;
	if (/^-/) {
	    print "$_\n";
	    ($x[$i],$y[$i]) = split;
#
#  This is the crux of the calibration.  
#      At some point the DAC was calibrated
#      such that V_true = V_set*1.00022
#
#      The load resistor was measured to be:  399.86 MegOhms
#      I = V/R    I is in nA, V is in Volts and R is GigaOhms
#
#      For BONUS the resistor was changed and its value was determined to be:
#            R_bonus = 41.410 Meg Ohms
#
	    $load = 0.39986;
#	    $load = 0.041410;
	    $x[$i] = (-1.00022*$x[$i])/$load;
	    if (/^-0\s+/) {
		$n_zero++;
		$sum_zero = $sum_zero + $y[$i];
	    }
            $i++;
	}
    }
    close(IN);
    if ($n_zero != 0) {
	$offset = int($sum_zero/$n_zero);
    } else {
	$offset = 0;
    }
    $parm_ref = &LSF(\@x, \@y);
    $intercept = int($$parm_ref[0]);
    print OUT "$date $offset $intercept $$parm_ref[1]\n";
    close(RESULTS);
}
close(OUT);
