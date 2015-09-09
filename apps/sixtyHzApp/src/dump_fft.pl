#!/bin/env perl

#use lib ("/home/freyberg/PERL/lib/perl5/site_perl/5.005/sun4-solaris/");
use Pezca; 

$i = 0;
while (1) {
    $i++;
    ($error,@fft) = Pezca::GetList('fft_0');


    for ($i=0; $i<240; $i++) {
	print "$i $fft[$i] \n";
    }
    print "\n\n";
    sleep 10;
}
