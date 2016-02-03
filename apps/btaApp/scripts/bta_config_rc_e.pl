#!/bin/env perl 

use Pezca; 

use Tk;

{    
#
#   Initialize EPICS structure
#
    &init_epics ;
    
#
#   Read Back EPICS records into the 
#    EPICS structures
#  and  Initialize GUI layout
#
    &init_gui( &do_read_back ) ;

    1;	
}



###############################################################
#
#  Function to create the GUI layout.
#   The MainLoop is called here
#
###############################################################

sub init_gui
  { 
    local ( 
	   $MinCurrFlag,    $MaxCurrFlag, 
	   $LowCountFlag, 
	   $SixtyHzFlag,    $MinPolFlag, 
	   $MaxChAsymmFlag, $MaxBomRateFlag, 
	   $MinCurr,        $MaxCurr,
	   $MaxLowCount, 
	   $MaxSixtyHz,     $MinPol, 
	   $MaxChAsymm,     $MaxBomRate ) = @_ ;
    
    #
    #  Create the Main Canvas
    #
    $MainPad =  MainWindow->new;
    $MainPad->title('BTA Configuration Tool' );
    
    #
    #  Deal with the Menus
    #
    my $toplevel = $MainPad->toplevel;
    my $menubar = $toplevel->Menu(-type => 'menubar');
    $toplevel->configure(-menu => $menubar);
    
    my $modifier = 'Meta';	# Unix
    
    my $FileMenu = $menubar->cascade(-label => '~File', -tearoff => 0);
    $FileMenu->command(-label => 'Print ...', -command => [\&menus_error, 'Print'] );
    $FileMenu->separator;
    $FileMenu->command(-label => 'Quit',      -command => sub { exit 0 } );
    
    #
    #  Make a label
    #
    
    my $MainLabel = $MainPad -> Label(
				      -text => 'BEAM TIME ACCOUNTING  CONFIGURATION TOOL',
				      -font => 'Times 18',
				      -foreground => 'Green4');
    $MainLabel -> pack;
    
    #
    #  Divide the Canvas into 4 Frames
    #
    my @pl = qw/-side top -expand 1 -padx .5c -pady .5c/;
    my $UpperFrame  = $MainPad->Frame->pack(@pl);
    my $LowerFrame  = $MainPad->Frame->pack(@pl);
    
    my @pl = qw/-side left -expand 1 -padx .5c -pady .5c/;
    my $LeftFrame  = $UpperFrame->Frame->pack(@pl);
    my $RightFrame = $UpperFrame->Frame->pack(@pl);
    
    #
    #  Put the check buttons in the LEFT frame
    #    
    
    #
    #    Buttons for the Minimum current
    #
    
    my(@pl) = qw/-side top -pady 18 -anchor w/;
    my $ChButt1 = $LeftFrame->Checkbutton(
					  -text     => 'Minimum Current (nA)',
					  -variable => \$MinCurrFlag,
					  -relief   => 'flat')->pack(@pl);
    my $scale1 = $RightFrame->Scale(
				    qw/-orient horizontal -length 200 -width 10 
				    -from 0. -to 20. -resolution 0.1 -tickinterval 5. /
				    #				   -command/ => sub { print $MinCurr, "\n" } 
				   ) ;
    $scale1->configure( -variable  => \$MinCurr );
    $scale1->pack(qw/-side top -expand yes -anchor w/);
    
    #
    #    Buttons for the Maximum current
    #
    
    my(@pl) = qw/-side top -pady 18 -anchor w/;
    my $ChButt2 = $LeftFrame->Checkbutton(
					  -text     => 'Maximum Current (nA)',
					  -variable => \$MaxCurrFlag,
					  -relief   => 'flat')->pack(@pl);
    my $scale2 = $RightFrame->Scale(
				    qw/-orient horizontal -length 200 -width 10 
				    -from 0. -to 20. -resolution 0.1 -tickinterval 5. /
				   ) ;
    $scale2->configure( -variable  => \$MaxCurr );
    $scale2->pack(qw/-side top -expand yes -anchor w/);
    
    #
    #  Buttons for the Upstream counts
    #
    
    my(@pl) = qw/-side top -pady 18 -anchor w/;
    my $ChButt3 = $LeftFrame->Checkbutton(
					  -text     => 'Max Upstream Count Sum (Hz)',
					  -variable => \$LowCountFlag,
					  -relief   => 'flat')->pack(@pl);
    my $scale3 = $RightFrame->Scale(
				    qw/-orient horizontal -length 200 -width 10 
				    -from 0 -to 1000 -tickinterval 200 / 
				   ) ;
    $scale3->configure( -variable  => \$MaxLowCount );
    $scale3->pack(qw/-side top -expand yes -anchor w/);
    
    #
    #  Buttons for sixty Hertz limits
    # 
    
    my(@pl) = qw/-side top -pady 18 -anchor w/;
    my $ChButt4 = $LeftFrame->Checkbutton(
					  -text     => 'Max RMS for Beam (%)',
					  -variable => \$SixtyHzFlag,
					  -relief   => 'flat')->pack(@pl);
    my $scale4 = $RightFrame->Scale(
				    qw/-orient horizontal -length 200 -width 10 
				    -from 0 -to 40 -resolution 0.1 -tickinterval 10 /
				   ) ;
    $scale4->configure( -variable  => \$MaxSixtyHz );
    $scale4->pack(qw/-side top -expand yes -anchor w/);
    
    
    #
    #  Buttons for minimum polarization limit
    #
    
    my(@pl) = qw/-side top -pady 18 -anchor w/;
    my $ChButt5 = $LeftFrame->Checkbutton(
					  -text     => 'Minimum Polarization (%)',
					  -variable => \$MinPolFlag,
					  -relief   => 'flat')->pack(@pl);
    my $scale5 = $RightFrame->Scale(
				    qw/-orient horizontal -length 200 -width 10 
				    -from 0 -to 100 -tickinterval  20 /
				   ) ;
    $scale5->configure( -variable  => \$MinPol );
    $scale5->pack(qw/-side top -expand yes -anchor w/);
    
    #
    #  Button for Maximum beam charge asymmetry
    #
    
    my(@pl) = qw/-side top -pady 18 -anchor w/;
    my $ChButt6 = $LeftFrame->Checkbutton(
					  -text     => 'Max Charge Asymmetry (%)',
					  -variable => \$MaxChAsymmFlag,
					  -relief   => 'flat')->pack(@pl);
    my $scale6 = $RightFrame->Scale(
				    qw/-orient horizontal -length 200 -width 10 
				    -from 0. -to 1. -resolution 0.01 -tickinterval  0.25 /
				   ) ;
    $scale6->configure( -variable  => \$MaxChAsymm );
    $scale6->pack(qw/-side top -expand yes -anchor w/);
    
    #
    #  Button for Beam Offset Monitor counts
    #
    
    my(@pl) = qw/-side top -pady 18 -anchor w/;
    my $ChButt7 = $LeftFrame->Checkbutton(
					  -text     => 'Max BOM Rate(Hz)',
					  -variable => \$MaxBomRateFlag,
					  -relief   => 'flat')->pack(@pl);
    my $scale7 = $RightFrame->Scale(
				    qw/-orient horizontal -length 200 -width 10 
				    -from 0. -to 500. -tickinterval  100 /
				   ) ;
    $scale7->configure( -variable  => \$MaxBomRate );
    $scale7->pack(qw/-side top -expand yes -anchor w/);
    
    #
    #
    #  Define the big buttons at the bottom
    #
    #
    
    #
    #  Set Button
    #    
    my $BigButton = $LowerFrame->Button(
					-text    => 'Set Conditions',
					-command => [\&set_rec, 
						     \$MinCurrFlag,    \$MaxCurrFlag,  
						     \$LowCountFlag, 
						     \$SixtyHzFlag,    \$MinPolFlag, 
						     \$MaxChAsymmFlag, \$MaxBomRateFlag, 
						     \$MinCurr,        \$MaxCurr,
						     \$MaxLowCount, 
						     \$MaxSixtyHz,     \$MinPol, 
						     \$MaxChAsymm,     \$MaxBomRate]
				       );
    $BigButton->pack(qw/-side left -expand 1 -padx 15 -anchor w/);
    
    #
    # Readback button
    #
    my $BigButton = $LowerFrame->Button(
					-text    => 'Read Back',
					-command => sub { @list = &do_read_back ; 
							  $MinCurrFlag      = $list[0];
							  $MaxCurrFlag      = $list[1];
							  $LowCountFlag     = $list[2];
							  $SixtyHzFlag      = $list[3];
							  $MinPolFlag       = $list[4];
							  $MaxChAsymmFlag   = $list[5];
							  $MaxBomRateFlag   = $list[6];
							  $ChButt1->pack;
							  $ChButt2->pack;
							  $ChButt3->pack;
							  $ChButt4->pack;
							  $ChButt5->pack;
							  $ChButt6->pack;
							  $scale1->set($list[7]);
							  $scale2->set($list[8]);
							  $scale3->set($list[9]);
							  $scale4->set($list[10]); 
							  $scale5->set($list[11]); 
							  $scale6->set($list[12]); 
							  $scale7->set($list[13]); 
							}
				       );
    $BigButton->pack(qw/-side left -expand 1 -padx 15 -anchor w/);
    
    #
    #  Help Button
    #
    
    my $BigButton = $LowerFrame->Button(
					-text    => 'Help',
					-command => [\&show_help]   
				       );
    $BigButton->pack(qw/-side right -expand 1 -padx 15 -anchor w/);   
    
    #
    #  Dismiss Button
    #   
    
    my $BigButton = $LowerFrame->Button(
					-text    => 'Dismiss Window',
					-command => sub { exit 0 }   
				       );
    $BigButton->pack(qw/-side right -expand 1 -padx 15 -anchor w/);   
    
    
    MainLoop;
    
    1;   
  }


#
#
#   Initialize the EPICS structures used 
#    in this application
#
#


sub init_epics
  {
    $ENV{EPICS_CA_ADDR_LIST} = " 129.57.32.21 129.57.163.255 129.57.255.4";
    
    # Input fields for different Limiting Values    
    
    %ValueRec  = (  "FCUP"          => "scaler_calc1" , 
		    "SLM"           => "scaler_calc2" , 
		    "MOLLER_STAT"   => "moller_system_status" , 
		    "SCALER"        => "scaler_sum" , 
		    "POLAR"         => "beam_polarization", 
		    "SIXTYHZ_SLM"   => "sixtyHz_rms_1",  
		    "SIXTYHZ_FCUP"  => "sixtyHz_rms_2",  
		    "SIXTYHZ_RMS"   => "HLB:bta_60hz_rms",
		    "CHG_ASYMM"     => "q_asym_3", 
		    "HALL_STATUS"   => "PLC_HLB",
		    "BOM"           => "scaler_dS16a"
		 );
    
#  Generate hash of hashes containing empty 
#    EPICS record images 
    
    foreach $EpicsRec ( "Main", "Reg", "Mol", "Gen" )
      {
	foreach $EpicsField ( "INPA", "INPB", "INPC", "INPD", "INPE", "INPF", 
			      "INPG", "INPH", "INPI", "INPJ", "INPK", "INPL",
			      "A", "B", "C", "D", "E", "F",
			      "G", "H", "I", "J", "K", "L"
			    )
	  {
	    ( $Field, $Value ) = ( $EpicsField, "" );
	    $CalcRec{ $EpicsRec }{ $Field } = $Value ;
	  }	
	$CalcRec{ $EpicsRec }{ "CALC" } = "1" ;
      }
    $CalcRec{"Main"}{"Name"} = "HLB:bta_bm_present" ;
    $CalcRec{"Reg" }{"Name"} = "HLB:bta_reg_bm" ;
    $CalcRec{"Mol" }{"Name"} = "HLB:bta_mol_bm" ;
    $CalcRec{"Gen" }{"Name"} = "HLB:bta_gen_bm" ;
  }



##################################################################
#
# A function to Read Back the values for the 
#  GUI variable and return them as a list 
#
##################################################################

sub do_read_back
  {
    
    my  
      $MinCurrFlag,    $MaxCurrFlag,  
      $LowCountFlag, 
      $SixtyHzFlag,    $MinPolFlag, 
      $MaxChAsymmFlag, $MaxBomRateFlag,
      $MinCurr,        $MaxCurr,
      $MaxLowCount, 
      $MaxSixtyHz,     $MinPol, 
      $MaxChAsymm,     $MaxBomRate;
    
    print "READING back EPICS Records... \n" ;
    $Err = 0;
    foreach $EpicsRec ( "Main", "Reg", "Mol", "Gen" )
      {
	foreach $EpicsField ( "INPA", "INPB", "INPC", "INPD", "INPE", "INPF", 
			      "INPG", "INPH", "INPI", "INPJ", "INPK", "INPL",
			      "CALC"
			    )
	  {
	    
	    $RecField = $CalcRec{$EpicsRec}{"Name"} . "\." . $EpicsField  ;
	    
	    ( $Err, $CalcRec{$EpicsRec}{$EpicsField} ) = Pezca::GetString( $RecField ) ;
	    
	    #	    print "$RecField, $CalcRec{$EpicsRec}{$EpicsField} \n" ;
	    $Err |= Err ;
	  }
	
	foreach $EpicsField (  'A', 'B', 'C', 'D', 'E', 'F',
			       'G', 'H', 'I', 'J', 'K', 'L' )
	  {
	    $RecField = $CalcRec{$EpicsRec}{"Name"} . "\." . $EpicsField  ;
	    
	    ( $Err, $CalcRec{$EpicsRec}{$EpicsField} ) = Pezca::GetDouble( $RecField ) ;
	    
	    #	    print "$RecField, $CalcRec{$EpicsRec}{$EpicsField} \n" ;
	    $Err |= Err ;	    
	  }
      }
    
    $MinCurrFlag      =  ( $CalcRec{"Reg"}{"CALC"} =~ /A\>/ ) && 
      ( $CalcRec{"Main"}{"CALC"} =~ /A/ );
    $MaxCurrFlag      =  ( $CalcRec{"Reg"}{"CALC"} =~ /F\</ ) && 
      ( $CalcRec{"Main"}{"CALC"} =~ /A/ );
    $LowCountFlag     =  ( $CalcRec{"Reg"}{"CALC"} =~ /B\</ ) && 
      ( $CalcRec{"Main"}{"CALC"} =~ /A/ );
    $SixtyHzFlag      =  ( $CalcRec{"Reg"}{"CALC"} =~ /D\</ ) && 
      ( $CalcRec{"Main"}{"CALC"} =~ /A/ );
    $MinPolFlag       =  ( $CalcRec{"Reg"}{"CALC"} =~ /C\)\>/ ) && 
      ( $CalcRec{"Main"}{"CALC"} =~ /A/ );
    $MaxChAsymmFlag   =  ( $CalcRec{"Gen"}{"CALC"} =~ /B\)\</ ) && 
      ( $CalcRec{"Main"}{"CALC"} =~ /C/ );
    $MaxBomRateFlag   =  ( $CalcRec{"Reg"}{"CALC"} =~ /E\</ ) && 
      ( $CalcRec{"Main"}{"CALC"} =~ /A/ );
    
    #    $MinCurr      =  $CalcRec{"Reg"}{"G"} * 1000.;
    $MinCurr      =  $CalcRec{"Reg"}{"G"};
    $MaxCurr      =  $CalcRec{"Reg"}{"L"};
    $MaxLowCount  =  $CalcRec{"Reg"}{"H"};
    #    $MaxSixtyHz   =  $CalcRec{"Gen"}{"G"};
    #    $MaxSixtyHz   =  $CalcRec{"Gen"}{"G"} * 100. ;
    #    $MaxSixtyHz   =  $CalcRec{"Reg"}{"J"} * 100. ;
    $MaxSixtyHz   =  $CalcRec{"Reg"}{"J"} ;
    $MinPol       =  $CalcRec{"Reg"}{"I"};	
    #    $MaxChAsymm   =  $CalcRec{"Gen"}{"H"} * 100. ;
    $MaxChAsymm   =  $CalcRec{"Gen"}{"H"}  ;
    $MaxBomRate   =  $CalcRec{"Reg"}{"K"}  ;
    
    print "EPICS records have been READ with Exit Code $Err \n";
    
    &init_epics;
    
    #    print "F1 = ",  $MinCurrFlag, "F2 = ", $LowCountFlag, 
    #	"F3 = ", $SixtyHzFlag,    "F4 = ", $MinPolFlag, 
    #	"V1 = ", $MinCurr,        "V2 = ",   $MaxLowCount, 
    #	"V3 = ", $MaxSixtyHz,     "V4 = ",   $MinPol  , "\n" ;
    
    my @ReturnValue = ( 
		       $MinCurrFlag,    $MaxCurrFlag,   
		       $LowCountFlag, 
		       $SixtyHzFlag,    $MinPolFlag, 
		       $MaxChAsymmFlag, $MaxBomRateFlag,
		       $MinCurr,        $MaxCurr,   
		       $MaxLowCount, 
		       $MaxSixtyHz,     $MinPol, 
		       $MaxChAsymm,     $MaxBomRate );
    
    @ReturnValue ;
  }


#
#
#   A function to put the variables from GUI  
#     into the EPICS database
#
#

sub set_rec
  {
    local (  $MinCurrFlag,    $MaxCurrFlag, 
	     $LowCountFlag, 
	     $SixtyHzFlag,    $MinPolFlag, 
	     $MaxChAsymmFlag, $MaxBomRateFlag,
	     $MinCurr,        $MaxCurr, 
	     $MaxLowCount, 
	     $MaxSixtyHz,     $MinPol, 
	     $MaxChAsymm,     $MaxBomRate ) = @_ ;
    
    &init_epics;
    
    $CalcRec{"Gen"}{"INPA"}  = $ValueRec{"HALL_STATUS"} ;
    $CalcRec{"Gen"}{"INPG"}  = "6" ;
    $CalcRec{"Gen"}{"G"}     = "6" ;
    $CalcRec{"Gen"}{"CALC"} .= "\&\&A\=G" ;
    
    if ( $$MinCurrFlag )
      {
	#	my $MinCurrNA = 0.001 * $$MinCurr;
	my $MinCurrNA = 1.0 * $$MinCurr;
	
	$CalcRec{"Reg"}{"INPA"}  = $ValueRec{'FCUP'} ; 
	$CalcRec{"Reg"}{"INPG"}  = "$MinCurrNA" ;
	$CalcRec{"Reg"}{"G"}     = "$MinCurrNA" ;
	$CalcRec{"Reg"}{"CALC"} .= "\&\&A\>G" ;
	
	$CalcRec{"Mol"}{"INPA"}  = $ValueRec{'SLM'} ; 
	$CalcRec{"Mol"}{"INPG"}  = "$MinCurrNA" ;
	$CalcRec{"Mol"}{"G"}     = "$MinCurrNA" ;
	$CalcRec{"Mol"}{"INPB"}  = $ValueRec{'MOLLER_STAT'} ; 
	$CalcRec{"Mol"}{"INPH"}  = "9" ;
	$CalcRec{"Mol"}{"H"}     = "9" ;
	$CalcRec{"Mol"}{"CALC"} .= "\&\&A\>G\&\&B\>H" ;
	
	if ( $$MaxCurrFlag && ( $$MaxCurr > $$MinCurr ) )
	  {
	    my $MaxCurrNA = 1.0 * $$MaxCurr;	
	    $CalcRec{"Reg"}{"INPF"}  = $ValueRec{'FCUP'} ; 
	    $CalcRec{"Reg"}{"INPL"}  = "$MaxCurrNA" ;
	    $CalcRec{"Reg"}{"L"}     = "$MaxCurrNA" ;
	    $CalcRec{"Reg"}{"CALC"} .= "\&\&F\<L" ;	 
	    
	    $CalcRec{"Mol"}{"INPD"}  = $ValueRec{'SLM'} ; 
	    $CalcRec{"Mol"}{"INPJ"}  = "$MaxCurrNA" ;
	    $CalcRec{"Mol"}{"J"}     = "$MaxCurrNA" ;
	    $CalcRec{"Mol"}{"CALC"} .= "\&\&D\<J" ;
	  }
	
	if ( $$LowCountFlag ) 
	  {
	    $CalcRec{"Reg"}{"INPB"}  = $ValueRec{'SCALER'} ;     
	    $CalcRec{"Reg"}{"INPH"}  = "$$MaxLowCount" ; 
	    $CalcRec{"Reg"}{"H"}     = "$$MaxLowCount" ; 
	    $CalcRec{"Reg"}{"CALC"} .= "\&\&B\<H" ;	    
	  }
	
	if ( $$SixtyHzFlag )
	  {
	    #	    $MaxSixtyHzRT = 0.01 * $$MaxSixtyHz ;
	    #	    $CalcRec{"Reg"}{"INPD"}  = $ValueRec{"SIXTYHZ_FCUP"} ;
	    $CalcRec{"Reg"}{"INPD"}  = $ValueRec{"SIXTYHZ_RMS"} ;
	    $CalcRec{"Reg"}{"INPJ"}  = "$$MaxSixtyHz" ;
	    $CalcRec{"Reg"}{"J"}     = "$$MaxSixtyHz" ;
	    $CalcRec{"Reg"}{"CALC"} .= "\&\&D\<J" ;
	    
	    $CalcRec{"Mol"}{"INPC"}  = $ValueRec{"SIXTYHZ_SLM"} ;
	    $CalcRec{"Mol"}{"INPI"}  = "$$MaxSixtyHz" ;
	    $CalcRec{"Mol"}{"I"}     = "$$MaxSixtyHz" ;
	    $CalcRec{"Mol"}{"CALC"} .= "\&\&C\<I" ;
	  }
	
	if ( $$MinPolFlag )
	  {
	    $CalcRec{"Reg"}{"INPC"}  = $ValueRec{"POLAR"} ;
	    $CalcRec{"Reg"}{"INPI"}  = "$$MinPol" ;
	    $CalcRec{"Reg"}{"I"}     = "$$MinPol" ;
	    $CalcRec{"Reg"}{"CALC"} .= "\&\&ABS(C)\>I" ;
	  }
	
	if ( $$MaxChAsymmFlag )
	  {
	    #	    $MaxChAsymmRT = 0.01 * $$MaxChAsymm ;
	    $MaxChAsymmRT = 1. * $$MaxChAsymm ;
	    $CalcRec{"Gen"}{"INPB"}  = $ValueRec{"CHG_ASYMM"} ;
	    $CalcRec{"Gen"}{"INPH"}  = "$MaxChAsymmRT" ;
	    $CalcRec{"Gen"}{"H"}     = "$MaxChAsymmRT" ;
	    $CalcRec{"Gen"}{"CALC"} .= "\&\&ABS(B)\<H" ;
	  }
	
	if ( $$MaxBomRateFlag )
	  {
	    $CalcRec{"Reg"}{"INPE"}  = $ValueRec{"BOM"} ;
	    $CalcRec{"Reg"}{"INPK"}  = "$$MaxBomRate" ;
	    $CalcRec{"Reg"}{"K"}     = "$$MaxBomRate" ;
	    $CalcRec{"Reg"}{"CALC"} .= "\&\&E\<K" ;
	  }
      }
    
    $CalcRec{"Main"}{"CALC"}     = "\(\(A||B\)&&C\)\?1\:0" ;
    $CalcRec{"Main"}{"INPA"}     = $CalcRec{"Reg"}{"Name"}."\.VAL PP" ;
    $CalcRec{"Main"}{"INPB"}     = $CalcRec{"Mol"}{"Name"}."\.VAL PP" ;
    $CalcRec{"Main"}{"INPC"}     = $CalcRec{"Gen"}{"Name"}."\.VAL PP" ;	    
    
    
    foreach $EpicsRec ( "Main", "Reg", "Mol", "Gen" )
      {
	foreach $EpicsField ( "INPA", "INPB", "INPC", "INPD", "INPE", "INPF", 
			      "INPG", "INPH", "INPI", "INPJ", "INPK", "INPL", "CALC" )
	  {
	    print "$EpicsRec $EpicsField \: $CalcRec{$EpicsRec}{$EpicsField} \n" ;
	  }
	print "\n" ;
      }
    
    #
    #   This is where the records are set via Pezca::PutString
    #
    print "Setting EPICS Records... \n" ;
    $Err = 0;
    foreach $EpicsRec ( "Main", "Reg", "Mol", "Gen" )
      {
	foreach $EpicsField ( "INPA", "INPB", "INPC", "INPD", "INPE", "INPF", 
			      "INPG", "INPH", "INPI", "INPJ", "INPK", "INPL",
			      "A", "B", "C", "D", "E", "F",
			      "G", "H", "I", "J", "K", "L",
			      "CALC"
			    )
	  {
	    $RecField = $CalcRec{ $EpicsRec }{ "Name" }."\.$EpicsField"  ;
	    #	    print "$EpicsRec $EpicsField \: $RecField, $CalcRec{$EpicsRec}{$EpicsField} \n" ;
	    
	    $Err |= Pezca::PutString( $RecField, $CalcRec{$EpicsRec}{$EpicsField} );
	  }
	#	print "\n" ;
      }
    
    print "EPICS records have been set with Exit Code $Err \n";
    
    #  Want to call init_epics so that all the 
    #   EPICS structures are reset to avoid 
    #  ".=" confusions
    
    &init_epics ;	
  }


########################################################
#
#  Function to handle errors
#   from the GUI.
#
########################################################
sub menus_error {

    # Generate a background error, which may even be displayed in a window if
    # using ErrorDialog. 

    my($msg) = @_;

    $msg = "No action has been defined for \"$msg\".";
    $MainPad->BackTrace($msg);

} # end menus_error



###################################################################
#
#  A function called when Help is requested from the 
#          GUI 
#
###################################################################

sub show_help 
{
    $HelpPad =  MainWindow->new;
    $HelpPad->configure( -title => 'Help Window' );
    $HelpPad->Label(qw/-wraplength 4.5i -justify left -pady 20 -text/ => 
    '     This is a Beam Accounting Configuration Tool intended to be used by the Run Coordinator (RC) or the PDL to configure the requirements for the beam time accounting (BTA) software. These settings are used by the BTA software running on one of the IOC\'s at MCC to decide wether the beam is acceptable or not. No other software in Hall-B uses these settings. If any of the conditions is not satisfied, the beam will be considered unacceptable, and the down-time will be counted against the Accelerator, unless the down-time was explicitly asked for by  Hall B, or the Accelerator is in the Configuration Change state. 
     To enable a criteria, check the corresponding box, then adjust the corresponding limiting  value using the slide bar on the right to the desired value. After all needed modifiactions are made, click on "Set Chosen Conditions" button to load these settings into the BTA software.', 
     -font => 'Times 14')->pack;
    my $BigButton = $HelpPad->Button(
					-text    => 'Close',
					-command => [ $HelpPad => 'destroy'  ]   
					);
    $BigButton->pack(qw/-side right -expand 1 -padx 35 -anchor w/);   

}













