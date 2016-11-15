#!/usr/bin/perl

$motor_name = @ARGV[0];

$last_file_name = `ls -lt /home/epics/DATA/HARP_SCANS/$motor_name/ | grep $motor_name | awk '{print \$9}' | head -n1`;
chop $last_file_name;

print "$last_file_name \n";
#print "Kuku \n";

#$fitter_path = "/usr/clas12/hps/prod/tools/harp_fitter/harp_fitter.exe";    # This is the 1st fitter which is non-GUI
$fitter_path = "/usr/clas12/hps/prod/tools/harp_fitter/Fitter.exe";  # A Fitter with a ROOT GUI

system("$fitter_path $motor_name/$last_file_name &");
