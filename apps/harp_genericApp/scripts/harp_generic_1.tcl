#!/bin/env wish
#/apps/tcl/bin/wish
#!/usr/bin/wish 
#/apps/bin/tclsh

proc oldfilebrowse {filter gnuplot dir file chnnum} {
    global env filename scandir
    global lw args command browsedir browsefilter

    set browsedir $dir
    set browsefilter $filter
#    set command $COMMAND
#    set args $ARGUMENTS

    set lw .oldbrowse
    catch {destroy $lw}
    toplevel $lw
    wm title $lw "Pick a Scan File"
    wm iconname $lw "browsebox"
#    positionWindow $lw

    frame $lw.mbar2 -relief raised -bd 2
    frame $lw.dummy2 -width 7c 
    pack $lw.mbar2 $lw.dummy2 -side top -fill both

    menubutton $lw.mbar2.file  -text File -underline 0 -menu $lw.mbar2.file.menu
    menu $lw.mbar2.file.menu 
    $lw.mbar2.file.menu add command -label "Update directory listing" \
	    -command  {listfiles $browsedir $browsefilter} 
    $lw.mbar2.file.menu add command -label Close  -command {destroy $lw} 
    pack $lw.mbar2.file  -side left

    tk_menuBar $lw.mbar2 
    focus $lw.mbar2

    label $lw.dirtext -text "Directory:"
    entry $lw.direntry -width 20 -relief sunken -bd 2 -textvariable browsedir
    pack $lw.dirtext $lw.direntry -side top -fill x

    label $lw.filter -text "Filter:"
    entry $lw.filterentry -width 20 -relief sunken -bd 2 -textvariable browsefilter
    pack $lw.filter $lw.filterentry -side top -fill x

    label $lw.entrytext -text "Selected File:"
    entry $lw.entry -width 20 -relief sunken -bd 2 -textvariable filename
    pack $lw.entrytext $lw.entry -side top -fill x

    bind $lw.direntry <Return>    {listfiles $browsedir $browsefilter}
    bind $lw.filterentry <Return> {listfiles $browsedir $browsefilter}
    bind $lw.entry <Return>       {fit_and_plot $gnuplot $filename $channel_num}

    listbox $lw.files -relief raised -borderwidth 2 -yscrollcommand "$lw.scroll set" \
	    -xscrollcommand "$lw.scrollbot set"
    scrollbar $lw.scroll -command "$lw.files yview"
    scrollbar $lw.scrollbot -command "$lw.files xview" -orient horizontal
    pack $lw.scrollbot -side bottom -fill x
    pack $lw.scroll -side right -fill y
    pack $lw.files -fill both
 
# first update the directory

    listfiles $browsedir $browsefilter

}

#listfiles
proc listfiles {dir filter} {
    global lw filename browsedir browsefilter
    set browsedir $dir
    set browsefilter $filter
    $lw.files delete 0 end

    foreach i [lsort [glob $browsedir/$browsefilter]] {
	set dlist [split $i /]
	set len [llength $dlist]
	set j [lindex $dlist [expr [llength $dlist] -1]]

	$lw.files insert  end $j
    }
    set filename $j

# I think this double binding is breaking things

    bind $lw.files <Double-1> {set filename [selection get]; if ([file isdirectory $browsedir/$filename]) {listfiles $browsedir/$filename $browsefilter} else {fit_and_plot  $gnuplot $browsedir $filename  $chnnum}}

}

proc find_latest {prefix} {
    set recent 0
    foreach i [lsort [glob $prefix]] {
	set dlist [split $i /]
	set len [llength $dlist]
	set j [lindex $dlist [expr [llength $dlist] -1]]
        set mod_time [file mtime $i]
	if {$mod_time > $recent} {
	    set recent  $mod_time
	    set recent_file $j
	}
    } 
    return $recent_file
}

proc get_epics {scandir filename} {

    global epics_comments electronic_gains

    set epics_comments ""
    set file [open $scandir/$filename]

    set electronic_gains(fcup_slope) 9264;
    set electronic_gains(slm_slope) 30776; 
    set electronic_gains(fcup_offset) 0;
    set electronic_gains(slm_offset) -1611; 

    while { [gets $file line] >= 0} {
	if [regexp {^#} $line] {
	    set epics_comments "$epics_comments\n$line"
	}
    }
}
proc pop_epics_param {} {

    global w_epics epics_comments

    set w_epics .epics_param
    toplevel $w_epics
    wm title $w_epics "Hall B Beamline Info for this scan"
    wm iconname $w_epics "Harp Scan Beam Info"

    label $w_epics.instructions -text "Hall B beamline configuration for this scan:"
    pack $w_epics.instructions -side top -in $w_epics
    text $w_epics.text -relief sunken -bd 2 -height 10 -width 100 -yscrollcommand "$w_epics.scroll set"
    scrollbar $w_epics.scroll -command "$w_epics.text yview"
    pack $w_epics.scroll -side right -fill y -in $w_epics
    pack $w_epics.text -side top -in $w_epics

    button $w_epics.dismiss -text DISMISS -command {destroy .epics_param}
    pack  $w_epics.dismiss -side left -in $w_epics
    $w_epics.text insert end "$epics_comments"
}

proc get_current {norm_flag counts clock_cnts} {
    global electronic_gains;

    if {$norm_flag == 12} {
	set current [expr ((1e7*$counts/$clock_cnts)-$electronic_gains(slm_offset))/$electronic_gains(slm_slope)];
    } else {
	set current [expr ((1e7*$counts/$clock_cnts)-$electronic_gains(fcup_offset))/$electronic_gains(fcup_slope)];
    }
    return $current
}
proc find_peak {scandir filename {channel 3}} {

    global x_max y_max x_norm_max y_norm_max x_index y_index x_center y_center
    global fit_params norm_flag

    set x_max 0
    set y_max 0
    set x_index 0
    set y_index 0
    set i 0
    set cos45 0.707106781
    set file [open $scandir/$filename]
    set channel [expr $channel-1]
    set norm_ok  0

    while { [gets $file line] >= 0} {
	if [regexp {^[0-9]} $line] {
	    set counts [split $line { }]
	    set position($i) [lindex $counts 0]
	    set norm_cnts [lindex $counts $norm_flag]
	    set clock_cnts [lindex $counts 1]
	    set norm($i) [get_current $norm_flag $norm_cnts $clock_cnts];
	    set data($i) [lindex $counts $channel]
	    if {$norm($i) == 0} {
              set norm_ok 1
            }
	    incr i
	}
    }
    close $file
    if {$norm_ok == 1} {
       set norm_flag 0
    }
    for {set j 0} {$j < [expr $i/2]} {incr j} {
	if {$data($j) > $x_max} {
	    set x_max [expr $data($j)]
	    set x_index [expr $j]
	}
    }
    for {set j [expr $i/2]} {$j < $i} {incr j} {
	if {$data($j) > $y_max} {
	    set y_max [expr $data($j)]
	    set y_index [expr $j]
	}
    }
    if {$norm_flag != 0} {
	set x_norm_max [expr double($x_max)/double($norm($x_index))]
	set y_norm_max [expr double($y_max)/double($norm($y_index))]
    } else {
	set x_norm_max [expr double($x_max)]
	set y_norm_max [expr double($y_max)]
    }
    set x_center [expr $position($x_index)*$cos45]
    set y_center [expr $position($y_index)*$cos45]

#    set fit_params(back_x) 0.001
#    set fit_params(back_y) 0.001

    set fit_params(sigma_x) 0.075
    set fit_params(sigma_y) 0.075

    set fit_params(amp_x) [expr $x_norm_max]
    set fit_params(amp_y) [expr $y_norm_max]

    set fit_params(mean_x) [expr $x_center]
    set fit_params(mean_y) [expr $y_center]
}

proc back_est {scandir filename {channel 3}} {

    global fit_params fit_param_errs norm_flag back_sum back_cnts

    puts "back_est: norm_flag: $norm_flag"
    set i 0
    set cos45 0.707106781
    set file [open $scandir/$filename]
    set channel [expr $channel-1]

    while { [gets $file line] >= 0} {
	if [regexp {^[0-9]} $line] {
	    set counts [split $line { }]
	    if {$norm_flag != 0} {
		set d [lindex $counts $channel]
		set n_cnts [lindex $counts $norm_flag]
		set c_cnts [lindex $counts 1]
		set n [get_current $norm_flag $n_cnts $c_cnts]
		set d_over_n [expr double($d)/double($n + 0.001)]
		set data($i) $d_over_n
	    } else {
		set data($i) [lindex $counts $channel]
	    }
	    set position($i) [lindex $counts 0]
	    incr i
	}
    }
    close $file
    set back_sum 0
    set back_cnts 1
    for {set j 0} {$j < [expr $i-1]} {incr j} {
	set h_pos [expr $position($j)*0.707];
	if {[expr abs($h_pos-$fit_params(mean_x))] >  3.0 && 
	    [expr abs($h_pos-$fit_params(mean_x))] < 15.0  &&
	    [expr abs($h_pos-$fit_params(mean_y))] >  3.0 && 
	    [expr abs($h_pos-$fit_params(mean_y))] < 15.0 } {

	    set back_sum [expr double($data($j) + $back_sum)]
	    set back_cnts [expr $back_cnts+1]
	}
    }
    set bin_size [expr ($position(1) - $position(2))*0.707]
    puts "back_cnts $back_cnts back_sum $back_sum\n";
    set back_cnts [expr $back_cnts]
    set fit_params(back_x) [expr double($back_sum)/$back_cnts]
    set fit_params(back_y) [expr double($back_sum)/$back_cnts]
    set fit_param_errs(back_x) [expr double(sqrt($back_sum))/$back_cnts]
    set fit_param_errs(back_y) [expr double(sqrt($back_sum))/$back_cnts]
}

proc do_fits {gnuplot scandir filename {chnnum 3} } {

    global x_max y_max x_norm_max y_norm_max x_index y_index x_center y_center
    global norm_flag
    global range  gui_range
    global fit_flag fit_params electronic_gains

    set range [expr double($gui_range)/10.]
    set cos45 0.707106781
    set x_range_low  [expr $x_center - $range]
    set x_range_high [expr $x_center + $range]
    set y_range_low  [expr $y_center - $range]
    set y_range_high [expr $y_center + $range]

    puts $gnuplot "back_x  = $fit_params(back_x)\n";
    puts $gnuplot "amp_x   = $fit_params(amp_x)\n";
    puts $gnuplot "mean_x  = $fit_params(mean_x)\n";
    puts $gnuplot "sigma_x = $fit_params(sigma_x)\n";

    puts $gnuplot "back_y  = $fit_params(back_y)\n";
    puts $gnuplot "amp_y   = $fit_params(amp_y)\n";
    puts $gnuplot "mean_y  = $fit_params(mean_y)\n";
    puts $gnuplot "sigma_y = $fit_params(sigma_y)\n";

    puts "back_x  = $fit_params(back_x)\n";
    puts "amp_x   = $fit_params(amp_x)\n";
    puts "mean_x  = $fit_params(mean_x)\n";
    puts "sigma_x = $fit_params(sigma_x)\n";

    puts "back_y  = $fit_params(back_y)\n";
    puts "amp_y   = $fit_params(amp_y)\n";
    puts "mean_y  = $fit_params(mean_y)\n";
    puts "sigma_y = $fit_params(sigma_y)\n";

    if {$fit_flag == 1} {
	puts  "g(x) = $fit_params(back_x) + amp_x*exp(-0.5*((mean_x-x)/sigma_x)**2) \n";
	puts  "h(x) = $fit_params(back_y) + amp_y*exp(-0.5*((mean_y-x)/sigma_y)**2) \n";

#	puts $gnuplot "g(x) = back_x + amp_x*exp(-0.5*((mean_x-x)/sigma_x)**2) \n";
#	puts $gnuplot "h(x) = back_y + amp_y*exp(-0.5*((mean_y-x)/sigma_y)**2) \n";

	puts $gnuplot "g(x) = $fit_params(back_x) + amp_x*exp(-0.5*((mean_x-x)/sigma_x)**2) \n";
	puts $gnuplot "h(x) = $fit_params(back_y) + amp_y*exp(-0.5*((mean_y-x)/sigma_y)**2) \n";
    } elseif {$fit_flag == 2} {
	puts $gnuplot "g(x) = $fit_params(back_x) + amp_x*exp(-0.5*((mean_x-x)/sigma_x)**2) + amp2_x*exp(-0.5*((mean_x-x)/sigma2_x)**2) \n";
	puts $gnuplot "h(x) = $fit_params(back_y) + amp_y*exp(-0.5*((mean_y-x)/sigma_y)**2) + amp2_y*exp(-0.5*((mean_y-x)/sigma2_y)**2)\n";

	puts $gnuplot "amp2_x   = amp_x/100.\n";
	puts $gnuplot "sigma2_x = sigma1_x/10.\n";
	puts $gnuplot "amp2_y   = amp_y/100.\n";
	puts $gnuplot "sigma2_y = sigma1_y/10.\n";
    }

    if {$norm_flag == 12} {
	set slope [expr $electronic_gains(slm_slope)]
	set offset [expr $electronic_gains(slm_offset)]
    } elseif {$norm_flag == 16} {
	set slope [expr $electronic_gains(fcup_slope)]
	set offset [expr $electronic_gains(fcup_offset)]
    } else {
	set slope 1
        set gain 1
    }
    if {$norm_flag != 0} {
	set n_chan [expr $norm_flag+1]
	set fit_chan "((\$$chnnum)/((\$$n_chan * (1e7/\$2) + $offset)/$slope))"
	set error_chan ":(sqrt(\$$chnnum + \$$n_chan)/((\$$n_chan * (1e7/\$2) + $offset)/$slope))"
    } else {
	set fit_chan "(\$$chnnum)"
	set error_chan ""
    }
    if {$fit_flag ==1} {
	puts  "fit \[x=$x_range_low:$x_range_high\] g(x) \'$scandir\/$filename\' using (\$1*$cos45):$fit_chan$error_chan via amp_x, mean_x, sigma_x \n";
	puts $gnuplot "fit \[x=$x_range_low:$x_range_high\] g(x) \'$scandir\/$filename\' using (\$1*$cos45):$fit_chan$error_chan via amp_x, mean_x, sigma_x\n";
    } else {
	puts $gnuplot "fit \[x=$x_range_low:$x_range_high\] g(x) \'$scandir\/$filename\' using (\$1*$cos45):$fit_chan:$error_chan via amp_x, mean_x, sigma_x, amp2_x, sigma2_x \n";
    }

    
    get_fit_params $gnuplot

    if {$fit_flag ==1} {
#	puts  "fit \[x=$y_range_low:$y_range_high\] h(x) \'$scandir\/$filename\' using (\$1*$cos45):$fit_chan$error_chan via amp_y, mean_y, sigma_y \n"; 
	puts $gnuplot "fit \[x=$y_range_low:$y_range_high\] h(x) \'$scandir\/$filename\' using (\$1*$cos45):$fit_chan$error_chan via amp_y, mean_y, sigma_y\n"; 
    } else {
	puts $gnuplot "fit \[x=$y_range_low:$y_range_high\] h(x) \'$scandir\/$filename\' using (\$1*$cos45):$fit_chan$error_chan via amp_y, mean_y, sigma_y, amp2_y, sigma2_y\n"; 
    }

    get_fit_params $gnuplot

    get_quality_controls
}

proc get_fit_params {gnuplot} {
    global fit_params fit_param_errs fit_vars fit_flag

    set fit_vars {back_x amp_x mean_x sigma_x back_y amp_y mean_y sigma_y \
	amp2_x sigma2_x amp2_y sigma2_y}

    flush $gnuplot
    set found 0
    while {[gets $gnuplot line] >= 0  && $found <= 7} {
	if {[regexp {(_x)} $line]} {
	    set type 0
	}
	if {[regexp {(_y)} $line]} {
	    set type 1
	}
	if {[regexp {(_x)|(_y)} $line] && [regexp {(\+/\-)} $line]} {
	    set line [string trim $line]
	    set test [regsub -all { +} $line { } line]
	    set pieces [split $line { }]
#	    if {abs([lindex $pieces 2]) < 1e+5} {
#		set fit_params([lindex $pieces 0]) \
#			[expr round(100.*[lindex $pieces 2])/100.]
#		puts "$line \n";
#		set fit_param_errs([lindex $pieces 0]) \
#			[expr round(1.*[lindex $pieces 4])/1.]
#	    } else {
		set fit_params([lindex $pieces 0]) [lindex $pieces 2]
		set fit_param_errs([lindex $pieces 0]) [lindex $pieces 4]
#	    }
	    incr found
	}
	if {[regexp {^correlation} $line]} {
	    set found 10
	}
	if {[regexp {Undefined} $line] || \
		[regexp {Singular} $line] || \
		[regexp {non-positive} $line] || \
		[regexp {BREAK} $line] } {
	    set found 99
	}
    }
    if {$found == 99 || $found != 10} {
	puts $gnuplot "show variables; show variables\n";
	flush $gnuplot
	set found 0
	if [info exists type] {
	    while {[gets $gnuplot line] >= 0  && $found <= 1} {
		if {(([regexp {(_y)} $line] && $type==1) || \
			([regexp {(_x)} $line] && $type ==0)) && \
			[regexp {(=)} $line]} {
		    set line [string trim $line]
		    set test [regsub -all { +} $line { } line]
		    set pieces [split $line { }]
		    if {abs([lindex $pieces 2]) < 1e+6} {
			set fit_params([lindex $pieces 0]) \
				[expr round(10000.*[lindex $pieces 2])/10000.]
		    } else {
			set fit_params([lindex $pieces 0]) \
				[lindex $pieces 2]
		    }
		    set fit_param_errs([lindex $pieces 0]) 0
		}
		if [regexp {Variables} $line]  {
		    incr found
		}
	    }

	}
    }
    if {$fit_flag == 1} {
	foreach v $fit_vars {
	    if {[regexp {2} $v] &&[info exist fit_params($v)]} {unset fit_params($v)}
	}
    }
}

proc get_quality_controls {} {
    global fit_params fit_param_errs fit_vars qc

    if {$fit_param_errs(sigma_x) != 0} {
	set s_x [expr $fit_params(amp_x)*$fit_params(sigma_x)*2.50663]
        set b_x [expr $fit_params(back_x)*$fit_params(sigma_x)*6/7.78]
	set qc(sn_x) [expr $s_x/($b_x+0.0001)]
	set qc(sn_x_e) [expr $qc(sn_x)*\sqrt(\
		pow($fit_param_errs(sigma_x)/$fit_params(sigma_x),2) + \
		pow($fit_param_errs(amp_x)/$fit_params(amp_x),2))]
#		pow($fit_param_errs(back_x)/$fit_params(back_x),2))]
    } else {
	set qc(sn_x) -9999
	set qc(sn_x_e) 0
    }
    if {$fit_param_errs(sigma_y) != 0} {
	set s_y [expr $fit_params(amp_y)*$fit_params(sigma_y)*2.50663]
        set b_y [expr $fit_params(back_y)*$fit_params(sigma_y)*6/7.78]
	set qc(sn_y) [expr $s_y/($b_y+0.0001)]
	set qc(sn_y_e) [expr $qc(sn_y)*\sqrt(\
		pow($fit_param_errs(sigma_y)/$fit_params(sigma_y),2) + \
		pow($fit_param_errs(amp_y)/$fit_params(amp_y),2))]
#		pow($fit_param_errs(back_y)/$fit_params(back_y),2))]
    } else {
	set qc(sn_y) -9999
	set qc(sn_y_e) 0
    }
    set txt [.right.middle.left configure]
    if {$fit_params(sigma_x) > 0.250} {
	.sigma_x_out configure -bg #f00
	.sigma_x_error configure -bg #f00
    } else {
	.sigma_x_out configure -bg #d9d9d9
	.sigma_x_error configure -bg #d9d9d9
    }

    if {$fit_params(sigma_y) > 0.250} {
	.sigma_y_out configure -bg #f00
	.sigma_y_error configure -bg #f00
    } else {
	.sigma_y_out configure -bg #d9d9d9
	.sigma_y_error configure -bg #d9d9d9
    }
    if {$fit_param_errs(sigma_y) == 0.0} {
	.sigma_y_error configure -bg #f00
    } else {
	.sigma_y_error configure -bg #d9d9d9
    }
    if {$fit_param_errs(sigma_x) == 0.0} {
	.sigma_x_error configure -bg #f00
    } else {
	.sigma_x_error configure -bg #d9d9d9
    }

    if {[expr $qc(sn_x) - $qc(sn_x_e)] < 1e+4} {
	.qc_x_out configure -bg #f00
	.qc_x_error configure -bg #f00
    } else {
	.qc_x_out configure -bg #d9d9d9
	.qc_x_error configure -bg #d9d9d9
    }

    if {[expr $qc(sn_y) - $qc(sn_y_e)] < 1e+4} {
	.qc_y_out configure -bg #f00
	.qc_y_error configure -bg #f00
    } else {
	.qc_y_out configure -bg #d9d9d9
	.qc_y_error configure -bg #d9d9d9
    }

}
proc make_plot {gnuplot scandir filename {chnnum 3} {terminal x11} {output none} } {

    global x_max y_max x_norm_max y_norm_max x_index y_index x_center y_center
    global fit_params  fit_param_errs norm_flag
    global range gui_range fit_vars y_scale pmt_list
    global back_sum back_cnts electronic_gains

    #if [regexp tagger $filename] {
    #	set forward 0
    #} else {
    #	set forward 1
    #}

    # tagger x and y directions swapped back so always forward should be 1
    set forward 1
    
    set range [expr double($gui_range)/10.]
    set cos45 0.707106781
    set x_range_low [expr $x_center - $range]
    set x_range_high [expr $x_center + $range]
    set y_range_low [expr $y_center - $range]
    set y_range_high [expr $y_center + $range]

    if {$norm_flag == 12} {
	set slope [expr $electronic_gains(slm_slope)]
	set offset [expr $electronic_gains(slm_offset)]
    } elseif {$norm_flag == 16} {
	set slope [expr $electronic_gains(fcup_slope)]
	set offset [expr $electronic_gains(fcup_offset)]
    } else {
	set slope 1
        set gain 1
    }
    if {$norm_flag != 0} {
	set n_chan [expr $norm_flag+1]
	set fit_chan "((\$$chnnum)/((\$$n_chan * (1e7/\$2) + $offset)/$slope))"
	set error_chan "(sqrt(\$$chnnum)/((\$$n_chan * (1e7/\$2) + $offset)/$slope))"
	puts $gnuplot "set ylabel \'PMT  (cnts/nA)\' \n";
    } else {
	set fit_chan "(\$$chnnum)"
	set error_chan "(sqrt(\$$chnnum))"
	puts $gnuplot "set ylabel \'PMT  (cnts)\' \n";
    }

    if {[string match {postscript} $terminal]} {
	set terminal "$terminal landscape color"
    } 
    puts $gnuplot "set terminal $terminal\n"
    if {![string match {none} $output]} {
	puts $gnuplot "set output \"$output\"\n"
    }          
    puts $gnuplot "set size 1.0,1.0\n";
    puts $gnuplot "set origin 0.0,0.0\n";
    puts $gnuplot "set multiplot\n";
    puts $gnuplot "set grid\n";
    set y_plot_min [expr (0.1+$back_sum/$back_cnts)/10.];
    puts "y_plot_min: $y_plot_min\n";
    if {$y_scale == 2} {
	puts $gnuplot "set logscale y1\n";
        puts $gnuplot "set yrange \[$y_plot_min:*\] \n";
    } else {
	puts $gnuplot "set nologscale y1\n";
        puts $gnuplot "set yrange \[0:*\] \n";
    }
    puts $gnuplot "set size 0.45,0.75\n";
    puts $gnuplot "set origin 0.0, 0.0\n";
    puts $gnuplot "set notitle\n";
    puts $gnuplot "set nokey\n";

    puts $gnuplot "set xrange \[$x_range_low:$x_range_high\]\n";
    if $forward {
	puts $gnuplot "set xlabel \'X (mm)\'\n";
    } else {
	puts $gnuplot "set xlabel \'Y (mm)\'\n";
    }

    puts $gnuplot "set nolabel\n";
    set label_index 1
    set height 1.35
    puts $gnuplot "set label $label_index \"$filename\" at graph 0.1,$height left \n"
    incr label_index
    set height 1.3
    foreach v $fit_vars {
	if [info exists fit_params($v)] {
	    if [regexp {(_x)} fit_params($v)] {
		set height [expr $height - 0.05]
		if $forward {
		    set var_name $v
		} else {
		    regsub _x $v _y var_name
		}
		puts $gnuplot "set label $label_index \"$var_name = $fit_params($v) +/- $fit_param_errs($v)\" at graph 0.1,$height left\n"
		incr label_index
	    }
	}
    }
#    puts  "plot \'$scandir/$filename\' using (\$1*$cos45):$fit_chan:($error_chan) title 'X scan' with yerrorbars, g(x)  \n";
    puts $gnuplot "plot \'$scandir/$filename\' using (\$1*$cos45):$fit_chan:($error_chan) title 'X scan' with yerrorbars, g(x)  \n";

    if $forward {
	puts $gnuplot "set xlabel \'Y (mm)\'\n";
    } else {
	puts $gnuplot "set xlabel \'X (mm)\'\n";
    }
    puts $gnuplot "set origin 0.5, 0.0\n";
    puts $gnuplot "set xrange \[$y_range_low:$y_range_high\]\n";

    puts $gnuplot "set nolabel\n";
    set label_index 1
    set height 1.35
    puts $gnuplot "set label $label_index \"PMT Channel: [lindex $pmt_list [expr $chnnum-3]]\" at graph 0.1,$height left \n"
    incr label_index

    set height 1.3
    foreach v $fit_vars {
	if [info exists fit_params($v)] {
	    if [regexp {(_y)} fit_params($v)] {
		set height [expr $height - 0.05]
		if $forward {
		    set var_name $v
		} else {
		    regsub _y $v _x var_name
		}
		puts $gnuplot "set label $label_index \"$var_name = $fit_params($v) +/- $fit_param_errs($v)\" at graph 0.1,$height left\n"
		incr label_index
	    }
	}
    }
    puts $gnuplot "plot \'$scandir/$filename\' using (\$1*$cos45):$fit_chan:($error_chan) title 'Y scan' with yerrorbars, h(x)  \n";


    puts $gnuplot "set nomultiplot\n";
 

    flush $gnuplot
}

proc fit_and_plot {gnuplot scandir filename {chnnum 3}} {

    puts "chnnum = $chnnum\n"

    puts "get_epics\n"
    get_epics $scandir $filename 
    puts "find_peak\n"
    find_peak $scandir $filename $chnnum
    puts "back_est\n"
    back_est  $scandir $filename $chnnum
    puts "do_fits\n"
    do_fits $gnuplot $scandir $filename $chnnum
    puts "make_plots\n"
    make_plot $gnuplot $scandir $filename $chnnum
}

proc printplot {gnuplot scandir filename channel_num {printer "lpr -Pclonhp"}} {
    global p_command pc default_printer

    make_plot $gnuplot $scandir $filename $channel_num postscript /tmp/scan.ps

    set p_command [lindex [split "$printer"] 0]
    set pc [lreplace [split "$printer"] 0 0]
    puts "$p_command :: $pc"
    after 2000 {
	puts "$p_command  $pc /tmp/scan.ps"
	exec $p_command  $pc /tmp/scan.ps
    }
}
proc print_setup {gnuplot scandir filename chnnum} {
    global default_printer

    set w .printbox
    toplevel $w
    wm title $w "Printer Command"
    wm iconname $w "printbox"

    if [info exists env(PRINTER)] {
	set default_printer  "lpr -d$env(PRINTER)"
    } else {
	set default_printer "lpr -Pclonhp2"
    }
    label $w.label -text "Print Command"
    entry $w.entry -width 20 -relief sunken -bd 2 -textvariable default_printer
    bind $w.entry <Return> {printplot $gnuplot $scandir $filename $chnnum $default_printer; destroy .printbox}

    pack $w.label $w.entry -side top -padx 1m -pady 2m 
}

proc pop_log_entry {gnuplot scandir filename chnnum} {

    global w_comment
    set w_comment .log_entry
    toplevel $w_comment
    wm title $w_comment "Harp Scan Log Entry Comments"
    wm iconname $w_comment "Log Entry"

    label $w_comment.instructions -text "Enter comments for this harp scan below:"
    pack $w_comment.instructions -side top -in $w_comment
    text $w_comment.text -relief sunken -bd 2 -height 5 -yscrollcommand ".log_entry.scroll set"
    scrollbar $w_comment.scroll -command "$w_comment.text yview"
    pack $w_comment.scroll -side right -fill y -in $w_comment
    pack $w_comment.text -side top -in $w_comment

    button $w_comment.elog -text "MAKE LOG ENTRY" -command {make_elog_entry $gnuplot $scandir $filename $chnnum}
    button $w_comment.dismiss -text DISMISS -command {destroy .log_entry}
    pack $w_comment.elog $w_comment.dismiss -side left -in $w_comment
}
proc make_elog_entry {gnuplot scandir filename chnnum} {
    global w_comment pmt_list fit_params fit_param_errs env epics_comments

    set comment [string trimright [.log_entry.text get 1.0 4096.0]]
    regsub -all {'} $comment {''} comment
    set i [regsub .txt $filename "_[lindex $pmt_list [expr $chnnum-3]]" image]
    make_plot $gnuplot $scandir $filename $chnnum gif  /u/group/clas/www/clasweb/html/LOGBOOK_IMAGES/HARP_SCANS/$image.gif
    destroy .log_entry


    set i [regsub .txt $filename "_[lindex $pmt_list [expr $chnnum-3]]" e_comment]
#    puts $e_comment
    set e_file [open /tmp/$e_comment.txt w]
    puts $e_file $comment
    puts $e_file "<BR>Filename: $filename     \n";
    puts $e_file "<BR>PMT channel: [lindex $pmt_list [expr $chnnum-3]] <BR>\n";
    puts $e_file "<img src=http://clasweb.jlab.org/LOGBOOK_IMAGES/HARP_SCANS/$image.gif>\n";
    puts $e_file "<table border>\n";
    puts $e_file "$epics_comments"
    puts $e_file "\n</table>\n";
    close $e_file

    exec $env(APP)/harp_generic/scripts/harp_entry.pl /tmp/$e_comment.txt
    exec rm /tmp/$e_comment.txt
}

# main portion of script

global range gui_range fit_flag y_scale fit_params fit_param_errs qc norm_flag
global pmt_list default_printer

set env(FIT_LOG)  /dev/null
set tcl_precision 5
set range 2.0
set gui_range [expr $range*10.0]

set scandir /home/epics/DATA/E_SCANS
#set scandir /home/freyberg/EPICS/app/harp_generic/scripts

set filename [find_latest $scandir/*harp_*\.txt]  

# set the default/favorite harp scan channel
set chnnum 14

set gnuplot [open |/home/freyberg/GNUPLOT/gnuplot r+]
set fit_flag 1

# norm_flag: 0->unnormalized 16->FCUP   12->SLM
set norm_flag 0

set y_scale 2
set default_printer "lpr -Pclonhp2"



frame .mbar -relief raised -bd 2
frame .dummy -width 16c
pack .mbar .dummy -side top -fill x

menubutton .mbar.file -text File -underline 0 -menu .mbar.file.menu

menu .mbar.file.menu 
.mbar.file.menu add command -label Open  \
	-command {oldfilebrowse harp_*.txt \
	$gnuplot $scandir $filename $chnnum} 
.mbar.file.menu add command -label "Print Setup"  \
	-command {print_setup  $gnuplot $scandir $filename $chnnum}
.mbar.file.menu add command -label Print  \
	-command {printplot $gnuplot $scandir $filename $chnnum $default_printer}
.mbar.file.menu add command -label Print@MCC  \
	-command {printplot $gnuplot $scandir $filename $chnnum "lpr -Pmcc104d"}

.mbar.file.menu add command -label Exit  -command exit

pack .mbar.file -side left
tk_menuBar .mbar mbar.file 
focus .mbar

frame .left
frame .right
pack .left -side left -padx 3m -pady 5m
pack .right -side right -padx 5m -pady 5m
frame .right.top
frame .right.topm
frame .right.top.left
frame .right.top.right
frame .right.top.right2
frame .right.top.bottom
frame .right.middle
frame .right.qc
frame .right.middle.left
frame .right.middle.right
frame .right.middle.pm
frame .right.middle.error
frame .right.bottom 
frame .right.qc.left
frame .right.qc.right
frame .right.qc.pm
frame .right.qc.error

pack .right.top .right.topm .right.middle .right.qc .right.bottom -side top  -in .right
pack .right.middle.left .right.middle.right \
	.right.middle.pm .right.middle.error \
	-side left -in .right.middle
pack .right.top.left .right.top.right .right.top.right2 -side left -in .right.top
pack .right.top.bottom -side bottom -in .right.top -anchor s
pack .right.qc.left .right.qc.right .right.qc.pm .right.qc.error -side left -in .right.qc

set j 2
set pmt_list {upstrm_top upstrm_bottom upstrm_right upstrm_left \
	ps_cua ps_primex upstrm_LeftRight upstrm_TopBottom \
	upstrm_right-h+ upstrm_right-h- n/a tag_top  tag_left tag_right}

set pack_list {}
foreach i $pmt_list {
    incr j
    radiobutton .$i -text $i -variable chnnum -value $j -anchor w \
	    -command {fit_and_plot $gnuplot $scandir $filename $chnnum}
    pack  .$i  -in .left -side top -fill x -anchor w
}

radiobutton .linear -text "Linear Scale" -variable y_scale -value 1 \
	-command {fit_and_plot $gnuplot $scandir $filename $chnnum}
radiobutton .logscale -text "Log Scale" -variable y_scale -value 2 \
	-command {fit_and_plot $gnuplot $scandir $filename $chnnum}
pack  .linear .logscale  -in .right.top.left -side top -anchor nw

#radiobutton .gaussian -text Gaussian -variable fit_flag -value 1  \
#	-command {fit_and_plot $gnuplot $scandir $filename $chnnum}
#radiobutton .two_gaussian -text Two-Gaussian -variable fit_flag -value 2  \
#	-command {fit_and_plot $gnuplot $scandir $filename $chnnum}
#pack  .gaussian .two_gaussian  -in .right.top.right -side top -anchor nw

radiobutton .normalize_fcup -text "Normalized to F-Cup" -variable norm_flag -value 16  \
	-command {fit_and_plot $gnuplot $scandir $filename $chnnum}
radiobutton .normalize_slm -text "Normalized to SLM" -variable norm_flag -value 12  \
	-command {fit_and_plot $gnuplot $scandir $filename $chnnum}
radiobutton .unnormalize -text Un-Normalized -variable norm_flag -value 0  \
	-command {fit_and_plot $gnuplot $scandir $filename $chnnum}
pack  .normalize_fcup .normalize_slm .unnormalize  -in .right.top.right2 -side top -anchor nw

scale .delta -label "Fit/Display region around peak (mm*10)" -from 5 -to 70 \
	-length 8c -orient horizontal \
	-variable gui_range 
pack .delta -side bottom -in .right.topm -anchor s -fill x

button .plot -text PLOT -command {fit_and_plot $gnuplot $scandir $filename $chnnum}
button .elog -text "MAKE LOG ENTRY" -command {pop_log_entry $gnuplot $scandir $filename $chnnum}
button .binfo -text "Beamline Info" -command {pop_epics_param}
button .print -text PRINT -command {printplot $gnuplot $scandir $filename $chnnum $default_printer}
button .print_mcc -text PRINT@MCC -command {printplot $gnuplot $scandir $filename $chnnum "lpr -Pmcc104d"}
button .exit -text EXIT -command {destroy .; exit}
pack .plot .print .print_mcc .elog .binfo .exit -side left -in .right.bottom -pady 8m


label .sigma_x_text -text "sigma_x:"
pack .sigma_x_text -side top -in .right.middle.left -fill x
label .sigma_x_out -textvariable fit_params(sigma_x)
pack .sigma_x_out -side top -in .right.middle.right -fill x
label .sigma_x_pm -text "+/-"
pack .sigma_x_pm -side top -in .right.middle.pm -fill x
label .sigma_x_error -textvariable fit_param_errs(sigma_x)
pack .sigma_x_error -side top -in .right.middle.error -fill x

label .sigma_y_text -text "sigma_y:"
pack .sigma_y_text -side top -in .right.middle.left -fill x
label .sigma_y_out -textvariable fit_params(sigma_y)
pack .sigma_y_out -side top -in .right.middle.right -fill x
label .sigma_y_pm -text "+/-"
pack .sigma_y_pm -side top -in .right.middle.pm -fill x
label .sigma_y_error -textvariable fit_param_errs(sigma_y)
pack .sigma_y_error -side top -in .right.middle.error -fill x

label .qc_x_text -text "Signal/Background (x):"
pack .qc_x_text -side top -in .right.qc.left -fill x
label .qc_x_out -textvariable qc(sn_x)
pack .qc_x_out -side top -in .right.qc.right -fill x
label .qc_x_pm -text "+/-"
pack .qc_x_pm -side top -in .right.qc.pm -fill x
label .qc_x_error -textvariable qc(sn_x_e)
pack .qc_x_error -side top -in .right.qc.error -fill x

label .qc_y_text -text "Signal/Background (y):"
pack .qc_y_text -side top -in .right.qc.left -fill x
label .qc_y_out -textvariable qc(sn_y)
pack .qc_y_out -side top -in .right.qc.right -fill x
label .qc_y_pm -text "+/-"
pack .qc_y_pm -side top -in .right.qc.pm -fill x
label .qc_y_error -textvariable qc(sn_y_e)
pack .qc_y_error -side top -in .right.qc.error -fill x

fit_and_plot $gnuplot $scandir $filename $chnnum

