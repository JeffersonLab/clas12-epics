#!/bin/env perl

#use lib ("/home/freyberg/PERL/lib/perl5/site_perl/5.005/sun4-solaris/");
use Pezca;

# set up the gain on the amplifier for currents < 100nA

$ok = Pezca::PutDouble('fcup_gain_bit0',0);
$ok = Pezca::PutDouble('fcup_gain_bit1',1);
$ok = Pezca::PutDouble('fcup_gain_bit2',0);

# for runs with current > 100nA

#$ok = Pezca::PutDouble('fcup_gain_bit0',1);
#$ok = Pezca::PutDouble('fcup_gain_bit1',0);
#$ok = Pezca::PutDouble('fcup_gain_bit2',0);

$ok = Pezca::PutDouble('fcup_cal',0);

#set up the scaler

$ok = Pezca::PutDouble('scaler.TP',1);
$ok = Pezca::PutDouble('display_mode',1);

(@date) = localtime(time);
$year = $date[5]+1900;
$month = $date[4]+1;
$filename="fcup_cal_$year\_$month\_$date[3]_$date[2]_$date[1]\.dat";
print "filename: $filename\n";
open(OUT,">/home/epics/data/FCUP/$filename");

# now loop over calibration values and read back
# fcup....

$step = 0.1;
$nstep = 10/$step;

for ($i=0; $i<10; $i=$i+$step) {

    $v_out = -1.0*$i;
    $ok = Pezca::PutDouble('fcup_cal',$v_out);
    $ok = Pezca::PutDouble('fcup_cal',$v_out);
    sleep 10;
    $n_done = $i/$nstep;
    print "$n_done out of $nstep settings done: ";
    for ($j=0; $j<1; $j++) {
	($ok, $fcup) = Pezca::GetDouble('scalerS16a');
	print OUT "$v_out   $fcup \n";
	print "CAL V: $v_out (V)  FCUP I: $fcup (nA)\n";
    }
}
close(OUT);
$ok = Pezca::PutDouble('fcup_cal',0.0);








