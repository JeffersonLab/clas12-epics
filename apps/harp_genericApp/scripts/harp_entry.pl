#!/bin/env perl
#/apps/perl/bin/perl

#use lib ("/home/freyberg/INGRES");
use lib ("/home/hovanes/INGRES");

use OPLOG;

$comment_file = $ARGV[0];

open(IN, $comment_file);
while(<IN>) {
    s/\'/\'\'/g;
    if (/^\#/) {
	s/^\#/<TR><TD>/;
	s/\:/\<\/TD\>\<TD\>/g;
	$_ .= '</td></tr>';
    }
    $comment .= $_;
}
$tmp_comment = "info to be added later";

$database = 'clasprod';
if ($database =~ /clasprod/) {
#$database = 'clastest';
#if ($database =~ /clastest/) {
   $prev_id = 5044;
} else {
   $prev_id = 3163;
}

$oplog = new OPLOG(database      => $database,
		   system_type   => 'beam',
		   lost_time     => '0',
		   operators     => 'Clas Shift Operators',
		   email_address => 'stepanya@jlab.org');

print "done calling new OPLOG $oplog\n";


$oplog -> OPLOG_SET(subject    => 'Harp Scan',
#		    comment    => "$tmp_comment",
		    comment    => "$comment",
		    entry_type => 'routine',
		    prev_id       => $prev_id);

$run = $oplog->GET_RUN_NUMBER();
print "run number is $run\n";
if (!($run)) {
    $run == 666;
}
$oplog -> OPLOG_SET(run => $run);

$date_time = $oplog->GET_DATE_TIME();
$oplog -> OPLOG_SET(entry_date => $date_time);

$ok = $oplog -> OPLOG_MAKE_ENTRY();

$key = $oplog->GET_UNIQUE_SEQ();

$ok = $oplog -> OPLOG_DISCONNECT();

# now update the comment.....this is done in a kludgy why to try to 
# avoid the "string too large" error from ingres

#open(SQL, "> /tmp/harp_update.sql");
#print SQL "$comment \n";
#close(SQL);

#$cmd = "java update_oplog_comment  -db db5::$database -u $key -c /tmp/harp_update.sql";
#print "$cmd\n";
#system($cmd);
