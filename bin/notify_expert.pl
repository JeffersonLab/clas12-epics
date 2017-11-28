#!/bin/env perl 

# this script notifies expert and makes an entry in the operator log

#use OPLOG;
use DBI; 
use Tk;

#must be parameter
##$contact = "online";

$numArgs = $#ARGV + 1;
if($numArgs!=1) {
  die "Must be one argument: system type\n";
}
foreach $argnum (0 .. $#ARGV) {
   $contact = $ARGV[$argnum];
}
print "contact=$contact\n";


$comment_string = '';


# create the text entry widget
my $tk_main = MainWindow->new;

$tk_main->title("Page Expert:  $contact");

my $tk_label = $tk_main -> Label(-text=>'Enter the message');
$tk_label -> pack;
my $tk_text = $tk_main->Scrolled(Text,
				 -relief => sunken,
				 -borderwidth => 2,
				 -setgrid => true,
				 -width => 60,
				 -height => 5,
				 -scrollbars=>'e'
				 );

my $tk_ok_button = $tk_main->Button(-text => 'SEND',
				    -command => [\&make_elog_entry, $tk_text]);
my $tk_dismiss = $tk_main->Button(-text=>'DISMISS',
				  -command=>[$tk_main => 'destroy']);
$tk_text->insert('0.0',$comment_string);
$tk_text->mark(qw/set insert 0.0/);

$tk_text->pack(qw/-expand yes -fill both/);
$tk_ok_button -> pack(-side=> 'left',
		      -padx=>2);
$tk_dismiss -> pack(-side=>'right',
		    -padx=>2);

MainLoop;

sub make_elog_entry {
    my ($my_text) = @_;
    $comment = $my_text->get('1.0','end');
    $tk_main ->destroy();

    $database = 'clasprod';
    if ($database =~ /clasprod/) {
	$prev_id = 7323;
    } else {
	$prev_id = 3003;
    }

#  connect to database
    ($dbh=DBI->connect("DBI:mysql:$database:clondb1","clasrun","")) 
    || die "Failed to connect to MySQL database\n";

#  search for specified contact record
    $sql="select email,primary_pager_or_cell,backup_pager_or_cell".
    " from oplog_system_type where contact='$contact' and primary_pager_or_cell!='NULL'";
    ($sth=$dbh->prepare($sql)) || die "Can't prepare $sql: $dbh->errstr\n";
    ($sth->execute) || die "Can't execute the query: $sth->errstr\n";

# NEED TO CHECK IF SPECIFIED contact EXISTS IN DB !!!!!


# extract database info
    while(@row=$sth->fetchrow_array) {
      $email                 = $row[0];
      $primary_pager_or_cell = $row[1];
      $backup_pager_or_cell  = $row[2];
    }
    print "email=$email\n";
###    $date=`date +%Y%m%d-%H:%M`;
###    chomp $date;

# making comment
    $comment =~ s/\'/\'\'/g;
    $comment .= "\n$data_string";

    print "Comment: $comment \n" ;


# create message file
    open(TMP,">/tmp/notify_expert.tmp");
    print TMP "$comment";
    close(TMP);

# send email
    $subject="From shift operator: $contact problem";
    if(length($email)>0) {
      $cmd="cat /tmp/notify_expert.tmp | mailx -S smtp=smtp://smtpmail.jlab.org -s \"$subject\" $email";
      print "Sending to >$email<\n" ;
	  system($cmd);
    }

# send message(s)
    $subject="$contact";
    if(length($primary_pager_or_cell)>0) {
      $cmd="cat /tmp/notify_expert.tmp | mailx -S smtp=smtp://smtpmail.jlab.org -s \"$subject\" $primary_pager_or_cell";
      print "Sending to >$primary_pager_or_cell<\n" ;
	  system($cmd);
    }
    if(length($backup_pager_or_cell)>0) {
      $cmd="cat /tmp/notify_expert.tmp | mailx -S smtp=smtp://smtpmail.jlab.org -s \"$subject\" $backup_pager_or_cell";
      print "Sending to >$backup_pager_or_cell<\n" ;
	  system($cmd);
    }


# make log entry
#    $oplog = new OPLOG(database      => $database,
#		       system_type   => '$contact',
#		       lost_time     => '0',
#		       email_address => '$email',
#		       subject       => "Message to expert",
#		       entry_type    => 'routine',
#		       operators     => 'CLAS shift takers',
#		       prev_id       => $prev_id
#		       );
#    $run = $oplog->GET_RUN_NUMBER();
#    $oplog -> OPLOG_SET(run => $run);
#    $date_time = $oplog->GET_DATE_TIME();
#    $oplog -> OPLOG_SET(entry_date => $date_time);
#    $oplog -> OPLOG_SET(comment    => $comment );
#    $ok = $oplog -> OPLOG_MAKE_ENTRY();
#    $lok = $oplog-> OPLOG_DISCONNECT();
}
