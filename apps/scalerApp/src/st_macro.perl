#!/bin/env perl
$inputfile = $ARGV[0];
open(IN,$inputfile);
while($line = <IN>) {
    if ($line =~ /assign /){ # if this line has a channel name in it
	@field = split(/"/, $line);
        $pvname = $field[1];
        if (length($pvname) != 0){
            @pvparts = split(/\./, $pvname);
            $recordname = $pvparts[0];
            $fieldname = $pvparts[1];
            print "$field[0]\"B_", $recordname, "_{IOC}.", $fieldname. "\"", $field[2];
        } else {
            print $line;
        }
    } else {
    print $line; # original line
    }
}
close(IN);
exit;
