#!/bin/env perl

use Pezca; 

$chan = 'sixtyHz_'.$ARGV[0];
($error,@PMT1) = Pezca::GetList($chan);
($error,$dwel) = Pezca::GetDouble('sixtyHz_0.DWEL');
($error,$fcup_gain) = Pezca::GetDouble('fcup_slope');
($error,$slm_gain) = Pezca::GetDouble('slm_slope');

$i = 0;
$x = 0;
$xx = 0;
foreach $pmt (@PMT1) {
    $x = $x +  $pmt;
    $xx = $xx +  $pmt*$pmt;
    $i++;
    $t = $dwel*$i;
    $rate = $pmt/$dwel;
    if ($ARGV[0] == 2) {
	$rate = $rate/$fcup_gain;
    } elsif ($ARGV[0] == 1) {
	$rate = $rate/$slm_gain;
    }
    print "$t $rate $pmt $slm_gain\n";
}




