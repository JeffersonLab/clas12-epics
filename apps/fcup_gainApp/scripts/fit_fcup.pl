#!/bin/env perl

# make a list of files in ../data

opendir DATADIR, '../data';
@data_files = grep !/^\.\.?$/, readdir DATADIR;

open(OUT, ">fit_results.txt");
foreach $f (@data_files) {
    @pieces = split(/\_/,$f);
    $date = "$pieces[4]/$pieces[3]/$pieces[2]-$pieces[5]:$pieces[6]";
    $cmd = "rm fit.log\n";
    system("$cmd");
    print "fitting $f  $date\n";
    open(GNUPLOT , "| gnuplot");
    print GNUPLOT "f(x) = a + b*x\n";
    print GNUPLOT "a=-100.0\n";
    print GNUPLOT "b=9300.0\n";
    print GNUPLOT "fit [x=0.2:*] f(x) \'../data/$f\' using ((1.00022*abs(\$1))/399.86e-3):2 via a,b \n";

    close(GNUPLOT);
    open(RESULTS, "< fit.log");
    $lconverge = 0;
    while(<RESULTS>) {
	chop;
	if (/^Final set of param/) {
	    $lconverge =1;
        }
	if ($lconverge) {
	    if (/^a\s+=/) {
		@line = split;
		$a = $line[2];
		$da = $line[4]
	    }
	    if (/^b\s+=/) {
		@line = split;
		$b = $line[2];
		$db = $line[4];
		print OUT "$date $a $da $b $db";
	    }
        }
    }
    $cmd = "rm fit.log\n";
    system("$cmd");
    open(GNUPLOT , "| gnuplot");
    print GNUPLOT "f(x) = a + b*x\n";
    print GNUPLOT "a=-100.0\n";
    print GNUPLOT "b=9300.0\n";
    print GNUPLOT "fit [x=*:*] f(x) \'../data/$f\' using ((1.00022*abs(\$1))/399.86e-3):2 via a,b \n";

    close(GNUPLOT);
    open(RESULTS, "< fit.log");
    $lconverge = 0;
    while(<RESULTS>) {
	chop;
	if (/^Final set of param/) {
	    $lconverge =1;
        }
	if ($lconverge) {
	    if (/^a\s+=/) {
		@line = split;
		$a = $line[2];
		$da = $line[4]
	    }
	    if (/^b\s+=/) {
		@line = split;
		$b = $line[2];
		$db = $line[4];
		print OUT " $a $da $b $db";
	    }
        }
    }
    $sum = 0.0;
    $n = 0;
    open(IN, "< ../data/$f");
    while(<IN>) {
	chop;
	if (/^-0\s+/) {
	    print "$_\n";
	    ($j,$offset) = split;
	    $sum = $sum + $offset;
            $n++;
	}
    }
    close(IN);
    if ($n > 0 ) {
	$offset = $sum/$n;
	print OUT " $offset\n";
    } else {
        print OUT "\n";
    }
    close(RESULTS);
}
close(OUT);
