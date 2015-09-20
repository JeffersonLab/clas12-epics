#!/apps/perl/bin/perl

# this script makes an entry in the operator log
# dumping the present values of the epics beam scaler
# display

use lib ("/home/freyberg/INGRES");
use OPLOG;

use lib ("$ENV{APP}/scaler/scripts/");
use CAGET;

$oplog = new OPLOG(database      => 'clasprod',
		   system_type   => 'beam',
		   lost_time     => '0',
		   email_address => 'freyberg@jlab.org',
		   subject       => 'EPICS Scaler values',
		   entry_type    => 'routine',
		   operators     => 'CLAS shift takers');

$run = $oplog->GET_RUN_NUMBER();
$oplog -> OPLOG_SET(run => $run);

$date_time = $oplog->GET_DATE_TIME();
$oplog -> OPLOG_SET(entry_date => $date_time);

$comment_string = &MAKE_STRING;

$oplog -> OPLOG_SET(comment    => "$comment_string");

$ok = $oplog -> OPLOG_MAKE_ENTRY();

$lok = $oplog-> OPLOG_DISCONNECT();

sub MAKE_STRING {
    my @records = qw(scalerS2b scalerS3b scalerS4b scalerS5b
		     scalerS6b scalerS7b scalerS8b scalerS9b
		     scaler_cS2b scaler_cS3b scaler_cS4b
		     scaler_cS5b scaler_cS6b scaler_cS7b
		     scaler_cS8b scaler_cS9b scaler_cS10b
		     scaler_cS11b scaler_cS12b scaler_cS13b
		     IPM2C21A IPM2C24A IPM2H01 scaler_calc1
		     IPM2C21A.XPOS IPM2C24A.XPOS IPM2H01.XPOS
		     IPM2C21A.YPOS IPM2C24A.YPOS IPM2H01.YPOS
		     MBC2C21H.BDL MBC2C21V.BDL MBC2C22H.BDL
		     MBC2C23V.BDL MDN2H01H.BDL MDN2H01V.BDL
		     IGL1I00OD16_16 SMRPOSB
		     scaler.TP display_mode
		     scaler_c.TP display_c_mode MBSY2C_energy IGL1I00HALLBDF
		     );
    foreach $r (@records) {
	$val{$r} = &CAGET($r);
    }

    $str = "Please click \"Modify\" and place informational comments here\n";
    $str .= "<pre>\n";
    $str .= "                Beam Halo  Scalers   \n";
    $str .= "                Top        Right     Bottom       Left\n";
    $str .= sprintf("Upstream:    %9.0f  %9.0f  %9.0f   %9.0f\n",$val{scalerS2b},$val{scalerS5b},
		    $val{scalerS3b},$val{scalerS4b});
    $str .= sprintf("Downstream:  %9.0f  %9.0f  %9.0f   %9.0f\n",$val{scalerS6b},$val{scalerS9b},
		    $val{scalerS7b},$val{scalerS8b});
    $str .= "\n";
    $str .= "                 SC and EC rates   \n";
    $str .= " Sector=>     1          2          3           4           5           6    \n";
    $str .= sprintf(" SC:  %9.0f  %9.0f  %9.0f   %9.0f   %9.0f   %9.0f\n",$val{scaler_cS2b},$val{scaler_cS3b},
		    $val{scaler_cS4b},$val{scaler_cS5b},$val{scaler_cS6b},$val{scaler_cS7b});
    $str .= sprintf(" EC:  %9.0f  %9.0f  %9.0f   %9.0f   %9.0f   %9.0f\n",$val{scaler_cS8b},$val{scaler_cS9b},
		    $val{scaler_cS10b},$val{scaler_cS11b},$val{scaler_cS12b},$val{scaler_cS13b});
    $str .= "\n";
    $str .= "     Beam Position   and Currents   \n";
    $str .= "          X          Y        I \n";
    $str .= sprintf("2C21  %6.3f    %6.3f    %6.3f\n",$val{'IPM2C21A.XPOS'},$val{'IPM2C21A.YPOS'},$val{IPM2C21A});
    $str .= sprintf("2C24  %6.3f    %6.3f    %6.3f\n",$val{'IPM2C24A.XPOS'},$val{'IPM2C24A.YPOS'},$val{IPM2C24A});
    $str .= sprintf("2H01  %6.3f    %6.3f    %6.3f\n",$val{'IPM2H01.XPOS'},$val{'IPM2H01.YPOS'},$val{IPM2H01});
    $str .= sprintf("FCUP                      %6.3f\n",$val{scaler_calc1});
    $str .= "\n";
    $str .= "          Trim Magnet Settings     \n";
    $str .= " 2C21H    2C21V     2C22H     2C23V      2H01H     2H01V  \n";
    $str .= sprintf("%6.2f   %6.2f   %6.2f   %6.2f    %6.2f    %6.2f\n",$val{'MBC2C21H.BDL'},$val{'MBC2C21V.BDL'},
		    $val{'MBC2C22H.BDL'},$val{'MBC2C23V.BDL'},$val{'MDN2H01H.BDL'},$val{'MDN2H01V.BDL'});
    $str .= "\n";
    $str .= "SLIT position: $val{SMRPOSB}   1/2 waveplate at injector: $val{IGL1I00OD16_16}  \n\n";
    $str .= "B Beam energy(MeV): $val{MBSY2C_energy}    B Beam Duty Factor(\%): $val{IGL1I00HALLBDF} \n\n";
    $str .= "       Scaler Configuration   \n";
    $str .= "halo time/mode: $val{'scaler.TP'}\/$val{display_mode}  SC/EC time/mode: $val{'scaler_c.TP'}\/$val{display_c_mode} \n";

    $str .= "</pre>";
    return($str);
}

