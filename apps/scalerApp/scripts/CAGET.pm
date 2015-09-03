#!/bin/env perl

package CAGET;
$CAGET::Version="0.01";

require Exporter;
@ISA = qw(Exporter);
@EXPORT =qw(CAGET  CAPUT);

sub CAGET {
    my ($epics_record) = @_;

    my ($value) = 0;
    my ($name) = 0;

    $ntries = 0;
    $not_done = 1;
    while ($not_done  && $ntries < 9) {
	sleep $ntries;
	open(CA, "caget $epics_record |");
	while(<CA>) {
	    chop;
	    if (/^$epics_record\s\s\s\s\s\s/) {
		($r_name, $value) = split;
		$not_done = 0;
	    }
	}
	if ($not_done != 0) {
	    $ntries++;
	}
	close(CA);
    }
	   
    if ($ntries >= 5) {
	$value = '9999.99';
    }
    return($value);
}

sub CAPUT {
    my ($epics_record, $value) = @_;

    $ntries = 0;
    $not_done = 1;
    while ($not_done  && $ntries < 9) {
	sleep $ntries;
	open(CA, "caput $epics_record $value |");
	while(<CA>) {
	    chop;
	    if (/^New :\s+$epics_record\s\s\s+/) {
		($junk,$colon,$r_name, $value) = split;
		$not_done = 0;
	    }
	}
	if ($not_done != 0) {
	    $ntries++;
	}
	close(CA);
    }
	   
    if ($ntries >= 5) {
	$value = '9999.99';
    }
    return($value);
}

