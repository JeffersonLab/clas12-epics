#!/bin/env perl

#use lib ("/home/freyberg/PERL/lib/perl5/site_perl/5.005/sun4-solaris/");
use Pezca; 

$chan = 'sixtyHz_'.$ARGV[0];
print "chan: $chan\n";
($error,@PMT1) = Pezca::GetList($chan);

$i = 0;
$x = 0;
$xx = 0;
print "@PMT1\n";
foreach $pmt (@PMT1) {
    $x = $x +  $pmt;
    $xx = $xx +  $pmt*$pmt;
    $i++;
}

print "$i $x $xx\n";

$df = ($x*$x)/($i*$xx);

print "duty factor: $df \n";
