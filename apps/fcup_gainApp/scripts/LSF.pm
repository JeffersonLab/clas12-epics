#!/bin/env perl

package LSF;
$LSF::Version="0.01";

require Exporter;
@ISA = qw(Exporter);
@EXPORT =qw(LSF);

sub LSF {
    my ($x_ref, $y_ref) = @_;

    my ($sum_x) = 0;
    my ($sum_y) = 0;
    my ($sum_xy) = 0;
    my ($sum_xx) = 0;
    my ($sum_xy) = 0;
    my (@parms) = (0.0,0.0);
    if ($#$x_ref != $#$y_ref) {
	print "X/Y arrays different length!!!!   ABORT LSF\n";
    } else {
	for ($i=0; $i < $#$x_ref; $i++) {
	     $sum_x = $sum_x + $$x_ref[$i];
	     $sum_y = $sum_y + $$y_ref[$i];
	     $sum_xx = $sum_xx + $$x_ref[$i]*$$x_ref[$i];
	     $sum_yy = $sum_yy + $$y_ref[$i]*$$y_ref[$i];
	     $sum_xy = $sum_xy + $$x_ref[$i]*$$y_ref[$i];
	}
	$denom = $i * $sum_xx - $sum_x*$sum_x;
	$intercept = $sum_xx * $sum_y - $sum_x*$sum_xy;
	$slope = $i*$sum_xy - $sum_x*$sum_y;
        if ($denom != 0) {
	    $slope = $slope/$denom;
	    $intercept = $intercept/$denom;
	    $parms[0] = $intercept;
            $parms[1] = $slope;
        }
    }

    return(\@parms);
}



