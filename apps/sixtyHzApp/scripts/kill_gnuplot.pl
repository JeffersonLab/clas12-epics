#!/bin/env perl

open(PS," ps -a |");

while(<PS>) {
    chop;
    if (/gnuplot/) {
	s/^\s*//;
	($pid) = split(/\s+/,$_);
	$cmd = "kill -9 $pid";
	print "$cmd \n";
	system($cmd);
    }
}

