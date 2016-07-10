#!/usr/bin/perl -w

use Pezca;
use POSIX qw(strftime);

&KILL_OTHER_INSTANCES_OF_SCRIPT();

$dir = "/home/epics/data";

# measurement configuration
$PV_length = "claspcal:scint_length";
$PV_step   = "claspcal:step_size";
$PV_nread  = "claspcal:nread";
# monitoring
$PV_last   = "claspcal:last_measurement";
$PV_status = "claspcal:status";
# motor
$PV_setpos = "claspcal:m1.VAL";
$PV_getpos = "claspcal:m1.RBV";
$PV_mDMOV  = "claspcal:m1.DMOV";
$PV_mSTAT  = "claspcal:m1.STAT";
# scintillator/file name
$PV_name   = "claspcal:scint_name";
$PV_sector = "claspcal:sector";
$PV_layer  = "claspcal:layer";
$PV_view   = "claspcal:view";
$PV_number = "claspcal:number";
# fiber bundle set
$PV_fiberbundle = "claspcal:fiberbundle";
$PV_fiberset    = "claspcal:fiberset";

print "Starting ...\nReading a new configuration\n";

$length  = &GETPV($PV_length,'numeric');
$step    = &GETPV($PV_step,  'numeric');
$nread   = &GETPV($PV_nread, 'numeric');
$nread = int($nread);
#$last    = &GETPV($PV_last,  'numeric');
#$status  = &GETPV($PV_status,'string');
$getpos  = &GETPV($PV_getpos,'numeric');
$sector  = &GETPV($PV_sector,'string');
$layer   = &GETPV($PV_layer, 'string');
$view    = &GETPV($PV_view,  'string');
$number  = &GETPV($PV_number,'numeric');
$fiberbundle = &GETPV($PV_fiberbundle,'numeric');
$fiberset    = &GETPV($PV_fiberset,   'numeric');

#$ = &GETPV($PV_,'numeric');
#$ = &GETPV($PV_,'string');

#($err,$name) = Pezca::GetString($PV_name);
#if ($err) {print "Pezca::GetString failed, errcode = $err , PV = $PV_name\n";}
#print "scint_name = $name\n";



# --- ZRST, "Idle"
# --- ONST, "Scanning - Moving"
# --- TWST, "Scanning - Recording"
# --- THST, "Moving home"
# --- FRST, "ERROR - Invalid scintillator number in view"
# --- FVST, "ERROR - Invalid length"
# --- SXST, "ERROR - Invalid step size"


# Reset status
$err = Pezca::PutDouble($PV_status,0);
$err = Pezca::PutString($PV_name,"");

if ($nread < 2) {
    print "ERROR :: Invalid number of readings\n";
    $err = Pezca::PutDouble($PV_status,7);
    exit;
}


if ($ARGV[0] eq 'scint') {
# check user input
    if ( 
	 ($view eq 'U' && $number > 84 ) ||
	 ($view eq 'V' && $number > 78 ) ||
	 ($view eq 'W' && $number > 78 ) ||
	 $number < 1 
	 ){
	print "ERROR :: Invalid number of scintilator\n";
	$err = Pezca::PutDouble($PV_status,4);
	exit;
    }
    if ($length < 0. || $length > 445) {
	print "ERROR :: Invalid measurement length\n";
	$err = Pezca::PutDouble($PV_status,5);
	exit;
    }
    if ($step <= 0.01) {
	print "ERROR :: Invalid measurement step size\n";
	$err = Pezca::PutDouble($PV_status,6);
	exit;
    }
    
    if ($number<10) {
	$name=$sector.$layer.$view."_0$number";
    } else {
	$name=$sector.$layer.$view."_$number";
    }
    $v=0;
    while ( -e "$dir/${name}_v${v}.dat" ){
	$v++;
    }
    $err = Pezca::PutString($PV_name,"$dir/${name}_v${v}.dat");

##to test things
#&READ_OUT(15, 0);
#exit;
    
# scan
    open(OUT,">>$dir/${name}_v${v}.dat");

# HV On
#$err = Pezca::PutDouble("B/HVON_SET_03_03",1);
#$err = Pezca::PutDouble("B_hv_pcal_04_03_CE",1);
    
    $err = Pezca::PutDouble($PV_status,3);
    &MOVE_MOTOR(-500);
# calibrate motor position
    $err = Pezca::PutDouble("claspcal:m1.SET",1);
    $err = Pezca::PutDouble("claspcal:m1.VAL",0);
    $err = Pezca::PutDouble("claspcal:m1.DVAL",0);
    $err = Pezca::PutDouble("claspcal:m1.RVAL",0);
    $err = Pezca::PutDouble("claspcal:m1.SET",0);
    
    $curpos=0;
    $i=0;
    while ($curpos <= $length){
	print "Current position is at $curpos\n";
	$err = Pezca::PutDouble($PV_status,1);
	&MOVE_MOTOR($curpos);
	$err = Pezca::PutDouble($PV_status,2);
	$str = &READ_OUT($nread,$curpos);
	print OUT "$str\n";
	$i++;
	$curpos = $i*$step;
    }
    close(OUT);
    
# backup the file
    system("scp -p $dir/${name}_v${v}.dat clas12ec\@jlabl1:data");
    
# HV Off
#$err = Pezca::PutDouble("B/HVON_SET_03_03",0);
#$err = Pezca::PutDouble("B_hv_pcal_04_03_CE",0);
    
} elsif($ARGV[0] eq 'fiber') {

    $str = "B".$fiberbundle."S".$fiberset;

    open(OUT,"+< $dir/fiber.dat");
    while(<OUT>){
	($name, $pos1, $mean1, $err1, $pos2, $mean2, $err2 ) = split(/\s/,$_);
	print "$name -  $pos1 $mean1 $err1 - $pos2 $mean2 $err2\n";
	if ($name eq $str) {
	    print "ERROR :: Duplicate Fiber set name\n";
	    $err = Pezca::PutDouble($PV_status,8);	
	    exit;
	}
    }
#    close(IN);

# scan
#    open(OUT,">>$dir/fiber.dat");

    $str .= "\t";
    $err = Pezca::PutDouble($PV_status,1);    &MOVE_MOTOR(350);
    $err = Pezca::PutDouble($PV_status,2);    $str .= &READ_OUT($nread,350);

    $str .= "\t";    
    $err = Pezca::PutDouble($PV_status,1);    &MOVE_MOTOR(433);
    $err = Pezca::PutDouble($PV_status,2);    $str .= &READ_OUT($nread,433);

    print  "$str\n";
    print OUT "$str\n";
    $err = Pezca::PutDouble($PV_status,0);	

    close(OUT);

# backup the file
    system("scp -p $dir/fiber.dat clas12ec\@jlabl1:data");
    
} else {
    print "ERROR :: Unsupported argumment, must be scint or fiber\n";
}


&MOVE_MOTOR(500); # move to other end
$err = Pezca::PutDouble($PV_status,0);
exit;
# -----------------------------------------------------

sub READ_OUT(){

#print DEVPORT "MEAS:CURR? ; *WAI \012";
#print DEVPORT "MEAS:CURR? ; *WAI \012";

    $nread = $_[0];
    $max_readings_per_set = 800;
    $nset = int($nread / $max_readings_per_set);
    $modulus = $nread % $max_readings_per_set;

    $n=0;
    $s2 = 0;
    $m = 0;
    system("stty '1:0:cbd:0:3:1c:7f:15:4:5:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0' -F /dev/ttyUSB0");
    open(DEVPORT, "+< /dev/ttyUSB0");
#    open(DEVPORT, "> /tmp/text2gpib.cmd");
    # Specify device address to talk
    print DEVPORT "++addr 16\012";
    # ID string of device
#    $_ = WR2DEV("*IDN?");
#    if (! m/KEITHLEY INSTRUMENTS INC.,MODEL 2001/){
#	print "Not a KEITHLEY MODEL 2001. Change the device or contact expert.\n";
#	print "The device is $_\n";
#    }
    for $i (0 .. $nset) {

	# Reset controls in INIT, ARM:LAY1, ARM:LAY2 and TRIG subsystems 
	# and put trigger model in IDLE state. 
	&WR2DEV("*RST;*OPC?");
	
	# Reset STATus subsystem (not affected by *RST)
	&WR2DEV(":STAT:PRES; *CLS; *WAI; *OPC?");
	
	# Set to measure DCI
	&WR2DEV(":SENS:FUNC 'CURRENT:DC'; *OPC?");
	
	# Enable Buffer Full(BFL) register bit
	&WR2DEV(":STAT:MEAS:ENAB 512; *WAI; :STAT:MEAS:ENAB?");
	
	# Enable Measurement Summary Bit (MSB)
	&WR2DEV("*SRE 1; *SRE?");

	$n2read = $max_readings_per_set;
	if ($i == $nset) { $n2read = $modulus; }

	# Set number of triggers
	&WR2DEV(":TRIG:COUN $n2read; :TRIG:COUN?");

	# TRACe subsystem is not affected by *RST!
	&WR2DEV(":TRAC:POIN $n2read; :TRAC:POIN?");
	# Compact data to fit in buffer
	&WR2DEV(":TRAC:EGR COMP; :TRAC:EGR?");
	# ???
	&WR2DEV(":trac:feed sens1;:TRAC:feed:cont next; *OPC?");
	sleep(5);
	# Start everything off and running
	&WR2DEV(":INIT; *OPC?");

	while (&WR2DEV("*STB?")==0){
	    sleep(5);
	}
	&WR2DEV(":FORM:ELEM READ; :FORM:ELEM?");
	
	sleep(5);
	@readings = split(',',&WR2DEV(":TRAC:DATA?"));
	
	for(@readings) {
	    chomp;
	    $m += abs $_;
	    $s2+= $_*$_;
	    $n += 1;
	    print "$n $_ $m $s2 \n";
	}
	if ($n == 0) {
	    return;
	}
	$mean = $m / $n;
	$s = $s2 / $n;
	$rms = sqrt($s - $mean*$mean);

	print "$n $mean $rms\n";
	$err = Pezca::PutDouble($PV_last,$mean);

	&WR2DEV(":SYST:ERR?");
	&WR2DEV(":STAT:QUE?");
	&WR2DEV(":STAT:OPER?");
# reseting to default configuration
	&WR2DEV("*RST; :SYST:PRES; *OPC?");
	&WR2DEV(":SENS:FUNC 'CURRENT:DC'; *OPC?");

    }
    close(DEVPORT);

    ($err,$getpos) = Pezca::GetDouble($PV_getpos);
    $now_string = strftime "%Y%m%d %H%M%S", localtime;
    #print OUT "$now_string\t$_[1] $getpos\t$n $mean $rms\n";
    return "$_[1]\t$mean $rms";
}

# -----------------------------------------------------
# Write/Read 2 Device
sub WR2DEV(){
    $cmd = $_[0];
#    print "$cmd\n"; return;
    print "COMMAND -> $cmd\n";

    print DEVPORT "$cmd\012";
    $line = <DEVPORT>;

    print "REPLY ---> $line\n";
    return $line;
}
# -----------------------------------------------------

sub READ_OUT1(){





#print DEVPORT "MEAS:CURR? ; *WAI \012";
#print DEVPORT "MEAS:CURR? ; *WAI \012";

    $nread = $_[0];
    $max_readings_per_set = 250;
    $nset = int($nread / $max_readings_per_set);
    $modulus = $nread % $max_readings_per_set;

    $n=0;
    $s2 = 0;
    $m = 0;

    open(DEVPORT, "+< /dev/ttyUSB0");
#    open(DEVPORT, "> /tmp/text2gpib.cmd");
    print DEVPORT "++addr 16\012";
    print DEVPORT "*IDN?\012";
    $line = <DEVPORT>;
    print "IDN ---> $line\n";
    for $i (0 .. $nset) {

	$n2read = $max_readings_per_set;
	if ($i == $nset) { $n2read = $modulus; }

	print "Totoal number to read $nread\nNumbers to read in this set $n2read\n";

#	print DEVPORT ":SYST:ERR? \012";
#	$line = <DEVPORT>; print "$line";
	print DEVPORT "*RST; *CLS; *OPC?\012";
	print DEVPORT ":INIT:CONT 0; :ABORT; *OPC?\012";

#	print DEVPORT ":CONF:CURRENT:DC\012";
	print DEVPORT ":SENS:FUNC 'CURRENT:DC'; OPC?\012";

	print DEVPORT ":SYST:AZER:STAT 1; :SYST:AZER:STAT?\012";
	print DEVPORT ":SENS:CURR:DC:AVER:STAT 0;:SENS:CURR:DC:AVER:STAT?\012";
	print DEVPORT ":SENS:CURR:DC:NPLC 0.01; :SENS:CURR:DC:NPLC?\012";
#	print DEVPORT ":SENS:CURR:DC:RANG 10\012";
	print DEVPORT ":SENS:CURR:DC:DIG 7; :SENS:CURR:DC:DIG?\012";
	print DEVPORT ":CURR:DC:AVER:COUN 1; :CURR:DC:AVER:COUN?\012";
## 	print DEVPORT ":TRAC:CLE\012";
	print DEVPORT ":FORM:ELEM READ; :FORM:ELEM?\012";
	print DEVPORT ":TRIG:COUN 1; :TRIG:COUN?\012";
#	print DEVPORT ":SAMPLE:COUN $n2read\012";
	print DEVPORT ":TRIG:DEL 0; *OPC?\012";
	print DEVPORT ":TRIG:SOUR IMM; :TRIG:SOUR?\012";
	print DEVPORT ":DISP:ENAB 0; :DISP:ENAB?\012";
#	print DEVPORT ":INIT\012";
	sleep(1);
#	print DEVPORT "*IDN?\012"; $line = <DEVPORT>; print "0 IDN ---> $line\n";
	print DEVPORT ":READ?\012";
	print DEVPORT ":DISP:ENAB 1; :DISP:ENAB?\012";
	
	$line = <DEVPORT>; print "$line";

#	$line = <DEVPORT>; print "\n--\n$line";
	@readings = split(',',$line);
	
	for(@readings) {
	    chomp;
	    $m += $_;
	    $s2+= $_*$_;
	    $n += 1;
	    #print "$n $_ $m $s2 \n";
	}
	if ($n == 0) {
	    return;
	}
	$mean = $m / $n;
	$s = $s2 / $n;
	$rms = sqrt($s - $mean*$mean);

	print DEVPORT "*IDN?\012"; $line = <DEVPORT>; print "1 IDN ---> $line\n";
	print "$n $mean $rms\n";
	$err = Pezca::PutDouble($PV_last,$mean);
#	print DEVPORT "OPC?\012";

	print DEVPORT ":SYST:ERR? \012";	$line = <DEVPORT>; #$print "$line";
	print DEVPORT ":STAT:QUE? \012";	$line = <DEVPORT>; #$print "$line";
	print DEVPORT ":STAT:OPER? \012";	$line = <DEVPORT>; #$print "$line";
# reseting to default configuration
	print DEVPORT ":SYST:PRES; *OPC?\012";
	print DEVPORT ":SENS:FUNC 'CURRENT:DC'; *OPC?\012";

#	print DEVPORT ":SYSTEM:LOCAL\012";
    }
    close(DEVPORT);

    ($err,$getpos) = Pezca::GetDouble($PV_getpos);
    $now_string = strftime "%Y%m%d %H%M%S", localtime;
    print OUT "$now_string\t$_[1] $getpos\t$n $mean $rms\n";
}

# -----------------------------------------------------

sub MOVE_MOTOR(){

    $pos = $_[0];
    print "Moving motor to position $pos\t";
    $err = Pezca::PutDouble($PV_setpos,$pos);
    $dmov = 0;
    $stat = 0;
    while ($dmov == 0 && $stat == 0) {
	($err, $dmov) = Pezca::GetDouble($PV_mDMOV);
	($err, $stat) = Pezca::GetDouble($PV_mSTAT);
	sleep(1);
    }
    print "Finished\n";
    return;
}

# -----------------------------------------------------

sub GETPV(){
    ($PV,$type) = @_;

    if      ($type eq 'numeric') {
	($err,$val) = Pezca::GetDouble($PV);
	if ($err) {print "Pezca::GetDouble failed, errcode = $err\n";}
	print "$PV = $val\n";
    } elsif ($type eq 'string')  {
	($err,$val) = Pezca::GetString($PV);
	if ($err) {print "Pezca::GetString failed, errcode = $err\n";}
	print "$PV = $val\n";
    }
    return $val;
}

# -----------------------------------------------------

sub KILL_OTHER_INSTANCES_OF_SCRIPT {

# Kill other instances of this script running. 
# Returns number of processes killed.

    print "checking for other instances of this script\n";
    $result = 0;
    #open(PS, "/usr/ucb/ps -auxwww |");
    open(PS, "/bin/ps -e -o pid,cmd | grep scanKeithley2001.pl |");

    $my_pid = $$;
    $my_perl_script = $0;
    while(<PS>) {
        chop;
        if (/$my_perl_script/) {
            @test = split(/\s+/,$_);
            $pid = $test[0];
#	    print "xxx $my_pid : $pid : \n$my_perl_script\n$_\n---\n";
	    $i = 1;
	    if ($test[1]=~/perl/) {
		$i = 2;
		if ($test[2]=~/^-/) {
		    $i = 3;
		}
	    }
#	    print "$i -- $my_pid : $pid : \n$my_perl_script\n$_\n---\n";
	    if ( ($my_pid != $pid) && ($i >= 2) ) {
		print "\nkilling = $pid my_pid = $my_pid\n";
		print "my_perl_script = $my_perl_script\n";
		print "script_to_kill = $_\n\n";
		kill 9, $pid;
		$result++;
	    }
        }
    }
    close(PS);
    return($result);
}
