#!/bin/env perl

# this script makes an entry in the operator log
# dumping the present values of the epics beam scaler
# display

use lib ("/home/hovanes/INGRES");
use OPLOG;

use Pezca; 
use Tk;

$comment_string = 'Please enter informational comments here and click "Make Log Entry"\n';


# create the text entry widget
my $tk_main = MainWindow->new;

my $tk_label = $tk_main -> Label(-text=>'Scaler Log Entry Comments');
$tk_label -> pack;
my $tk_text = $tk_main->Scrolled(Text,
				 -relief => sunken,
				 -borderwidth => 2,
				 -setgrid => true,
				 -width => 80,
				 -height => 20,
				 -scrollbars=>'e'
				 );

my $tk_ok_button = $tk_main->Button(-text => 'Make Log Entry',
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
    $oplog = new OPLOG(database      => $database,
		       system_type   => 'beam',
		       lost_time     => '0',
		       email_address => 'stepanya@jlab.org',
		       subject       => 'EPICS Scaler values for electron run',
		       entry_type    => 'routine',
		       operators     => 'CLAS shift takers',
		       prev_id       => $prev_id
		       );

    $run = $oplog->GET_RUN_NUMBER();
    $oplog -> OPLOG_SET(run => $run);
    
    $date_time = $oplog->GET_DATE_TIME();
    $oplog -> OPLOG_SET(entry_date => $date_time);
    
    $data_string = &MAKE_STRING;

    $comment =~ s/\'/\'\'/g;
    $comment .= "\n$data_string";

#    print " $comment \n" ;

    $oplog -> OPLOG_SET(comment    => $comment );
   
    $ok = $oplog -> OPLOG_MAKE_ENTRY();
    
    $key = $oplog->GET_UNIQUE_SEQ();

    $lok = $oplog-> OPLOG_DISCONNECT();


}
sub MAKE_STRING {
    my @records = qw(scalerS2b scalerS3b scalerS4b scalerS5b
		     scaler_eS2b scaler_eS3b scaler_eS4b scaler_eS5b
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
		     scaler_dS5b scaler_dS6b 
		     scaler.TP display_mode HLB:bta_cur_stor 
		     scaler_c.TP display_c_mode MBSY2C_energy IGL1I00HALLBDF
		     IGL1I00DAC2 psub_ab_pos
		     IGL1I00DI24_24M  WienAngle
		     q_asym_3 q_asym_7
		     power_60Hz_1 power_60Hz_2 power_60Hz_3 
		     power_60Hz_4 power_60Hz_5 power_60Hz_6 
		     radiator_long.RBV 
		     rad_at_home rad_at_a rad_at_b rad_at_c rad_at_d 
		     harp_2h00_at_home harp_2h00_at_a harp_2h00_at_b harp_2h00_at_c 
		     collimator.RBV 
		     PSPECIRBCK PSPECr.B1 PSPECr.B3  Hac_PS_LS450:FLD_DATA 
		     TMIRBCK  Hac_TGR_LS450:FLD_DATA MTIRBCK  
		     scaler_dS16b scalerS7b
		     scaler_calc2 slm_fcup_ratio 
		     scaler_dS16a  pspec_logic_ai_0  pspec_logic_ai_1
		     RASTCYCLETIME RASTPATSIZEX RASTPATSIZEY 
		     RASTXOFFSET RASTYOFFSET RASTRUNSTATUS RASTFEEDBACKSET 
		     ITC502_2_T1 hallbpttgt PI8210 LL8240 hallbptpol 
		     Rclas1M torus_current torus_polarity 
		     FC_vac_jac_top_temp FC_vac_jac_upstr_temp 
		     FC_beam_stop_water_in_temp FC_beam_stop_water_out_temp
		     );
    foreach $r (@records) {
#      print "Connecting to record $r \n" ;
	($errcode, $val{$r}) = Pezca::GetDouble($r);
#      print "Received value  $val{$r} \n" ;
    }

    $str  = "<pre>\n";
    $str .= "                Beam Halo  Scalers   \n";
    $str .= "                Top        Right     Bottom       Left\n";
    $str .= sprintf("Upstream:    %9.0f  %9.0f  %9.0f   %9.0f\n",
		    $val{scalerS2b},$val{scalerS5b},
		    $val{scalerS3b},$val{scalerS4b});
    $str .= sprintf("Downstream:  %9.0f  %9.0f  %9.0f   %9.0f\n",
		    $val{scaler_eS2b},$val{scaler_eS3b},
		    $val{scaler_eS4b},$val{scaler_eS5b});
    $str .= sprintf("Tagger MOR (MOR):  %10.1f\n", $val{pspec_logic_ai_0});
    $str .= sprintf("Pair Spectrometer LxR: %10.1f\n", $val{pspec_logic_ai_1});    
    $str .= "\n";
    $str .= "                 SC and EC rates   \n";
    $str .= " Sector=>     1          2          3           4           5           6    \n";
    $str .= sprintf(" SC:  %9.0f  %9.0f  %9.0f   %9.0f   %9.0f   %9.0f\n",
		    $val{scaler_cS2b},$val{scaler_cS3b},
		    $val{scaler_cS4b},$val{scaler_cS5b},
		    $val{scaler_cS6b},$val{scaler_cS7b});
    $str .= sprintf(" EC:  %9.0f  %9.0f  %9.0f   %9.0f   %9.0f   %9.0f\n",
		    $val{scaler_cS8b},$val{scaler_cS9b},
		    $val{scaler_cS10b},$val{scaler_cS11b},
		    $val{scaler_cS12b},$val{scaler_cS13b});
    $str .= "\n\n";

    $str .= "     Beam Position   and Currents   \n";
    $str .= "          X          Y        I \n";
    $str .= sprintf("2C21  %6.3f    %6.3f    %6.3f\n",
		    $val{'IPM2C21A.XPOS'},$val{'IPM2C21A.YPOS'},$val{IPM2C21A});
    $str .= sprintf("2C24  %6.3f    %6.3f    %6.3f\n",
		    $val{'IPM2C24A.XPOS'},$val{'IPM2C24A.YPOS'},$val{IPM2C24A});
    $str .= sprintf("2H01  %6.3f    %6.3f    %6.3f\n",
		    $val{'IPM2H01.XPOS'},$val{'IPM2H01.YPOS'},$val{IPM2H01});
    $str .= sprintf("FCUP                      %6.3f\n",$val{scaler_calc1});
    $str .= sprintf("SLM                       %6.3f ,      FCUP/SLM  Ratio       %6.4f\n", 
		                                $val{scaler_calc2}, $val{slm_fcup_ratio} );
    $str .= "\n";

    $str .= "Raster Magnet:  Status:  $val{''}    Feedback:  $val{''}    \n";
    $str .= "                X Offset:  $val{'RASTXOFFSET'}      Y Offset:  $val{'RASTYOFFSET'} \n";
    $str .= "                X Size  :  $val{'RASTPATSIZEX'}    Y Size:  $val{'RASTPATSIZEY'}   ";
    $str .= "  Cycle Time:  $val{'RASTCYCLETIME'} \n\n";

    $str .= "Polarized Target :  Type:  $val{'hallbpttgt'}         T_T:  $val{ITC502_2_T1}  \n";
    $str .= "                    BD:  $val{'PI8210'}     LHe Level:  $val{'LL8240'}   Polarization:  $val{'hallbptpol'} \n\n";

    $str .= sprintf("Beam Charge Asymmetry  FCUP: %4.3f   SLM: %4.3f\n\n",$val{'q_asym_7'},$val{'q_asym_3'});
    $str .= "Sixty Hz Power Components\n";
    $str .=  sprintf("SLM: %4.3f  FCUP: %4.3f PMT1: %4.3f PMT2 %4.3f PMT3: %4.3f PMT4: %4.3f\n\n",
		     $val{'power_60Hz_1'},$val{'power_60Hz_2'},$val{'power_60Hz_3'},
		     $val{'power_60Hz_4'},$val{'power_60Hz_5'},$val{'power_60Hz_6'});
    $str .= "          Trim Magnet Settings     \n";
    $str .= " 2C21H    2C21V     2C22H     2C23V      2H01H     2H01V  \n";
    $str .= sprintf("%6.2f   %6.2f   %6.2f   %6.2f    %6.2f    %6.2f\n",
		    $val{'MBC2C21H.BDL'},$val{'MBC2C21V.BDL'},
		    $val{'MBC2C22H.BDL'},$val{'MBC2C23V.BDL'},
		    $val{'MDN2H01H.BDL'},$val{'MDN2H01V.BDL'});
    $str .= "\n";
    $str .= "SLIT position: $val{SMRPOSB}   Laser Power: $val{'IGL1I00DAC2'} Attenuator: $val{'psub_ab_pos'} \n";
    $str .= "\n";
    $str .= sprintf("Helicity Configuration:  Sync Rate: %4.2f +Helicity Rate: %4.2f \n\n",
		    $val{'scaler_dS5b'},$val{'scaler_dS6b'});
    $str .= "Wien Angle: $val{'WienAngle'}  1/2 Wave Plate: $val{'IGL1I00DI24_24M'} \n";
    $str .= "B Beam energy(MeV): $val{MBSY2C_energy}    B Beam Duty Factor(\%): $val{IGL1I00HALLBDF} \n\n";
    $str .= "       Scaler Configuration   \n";
    $str .= "halo time/mode: $val{'scaler.TP'}\/$val{display_mode}  SC/EC time/mode: $val{'scaler_c.TP'}\/$val{display_c_mode} \n";
    $str .= "Master current from : $val{'HLB:bta_cur_stor'} \n";

# photon stuff
    $str .="...................photon devices.........................\n";
    $str .="Tagger Radiator Position: $val{'radiator_long.RBV'} \n";
    $str .="Tagger Harp Stick:  home: $val{'rad_at_home'}  A: $val{'rad_at_a'} B: $val{'rad_at_b'} C: $val{'rad_at_c'} D: $val{'rad_at_d'} \n";
    $str .="Converters: home: $val{'harp_2h00_at_home'}  0.01\% : $val{'harp_2h00_at_a'}   0.1\% : $val{'harp_2h00_at_b'} 1\% : $val{'harp_2h00_at_c'} \n";
    $str .="Collimator Position: $val{'collimator.RBV'} \n\n";

    if ($val{'PSPECr.B3'} == 0) {
	$pspec_pol = 'POSITIVE';
    } else {
	$pspec_pol = 'NEGATIVE';
    }
    $str .="Pair Spec Dipole:  Current: $val{'PSPECIRBCK'}  Polarity: $pspec_pol  Field: $val{'Hac_PS_LS450:FLD_DATA'} \n\n";  
    $str .="Tagger Magnet:  Current: $val{'TMIRBCK'}     Field:   $val{'Hac_TGR_LS450:FLD_DATA'} \n\n";  
    $str .="Minitorus Current:  $val{'MTIRBCK'} \n\n" ;
    $str .="Torus :  Current: $val{'Rclas1M'}   Signed Current: $val{'torus_current'}   Polarity: $val{'torus_polarity'} \n\n" ;
#    $str .="DVCS Solenoid Current:   $val{'MSL2H01M'} \n\n";


    $str .="FCUP Temps         Up:  $val{'FC_vac_jac_top_temp'}            Down:  $val{'FC_vac_jac_upstr_temp'}  \n";
    $str .="Stopper Temps      In:  $val{'FC_beam_stop_water_in_temp'}            Out:  $val{'FC_beam_stop_water_out_temp'} \n\n";


    $str .= "</pre>";
    return($str);
}

