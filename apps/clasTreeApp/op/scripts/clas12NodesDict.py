# WARNING: DO NOT EDIT. This file was geneated at Tue Dec 15 07:08:01 EST 2015 by the a command like this:
# ./parseEpicsRecordDump [options] ioc1.dump ioc2.dump .... 
# See the CLAS12 Slow Controls wiki for manuals, or the README in this directory
#

#Create the dictionaries to describe the nodes
NodeIndex              = {}
SubNodeNames           = []
ElementNames           = []
ElementRecordNames     = []
ElementRecordTypes     = []
ElementRecordFlags     = []
NodeRecordNames        = []
NodeRecordTypes        = []
ElementRange           = []

#Populate the dictionaries with the info for all the nodes

NodeIndex['B'] = 0
SubNodeNames.append('DET,HW,SYS')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET'] = 1
SubNodeNames.append('DC,ECAL,FTOF,LTCC,PCAL')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC'] = 2
SubNodeNames.append('HV')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV'] = 3
SubNodeNames.append('SEC1,SEC2,SEC3,SEC4,SEC5,SEC6')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC1'] = 4
SubNodeNames.append('R1,R2,R3')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC1_R1'] = 5
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC1_R1_SL1'] = 6
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC1_R1_SL2'] = 7
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC1_R2'] = 8
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC1_R2_SL1'] = 9
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC1_R2_SL2'] = 10
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC1_R3'] = 11
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC1_R3_SL1'] = 12
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC1_R3_SL2'] = 13
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC2'] = 14
SubNodeNames.append('R1,R2,R3')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC2_R1'] = 15
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC2_R1_SL1'] = 16
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC2_R1_SL2'] = 17
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC2_R2'] = 18
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC2_R2_SL1'] = 19
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC2_R2_SL2'] = 20
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC2_R3'] = 21
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC2_R3_SL1'] = 22
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC2_R3_SL2'] = 23
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC3'] = 24
SubNodeNames.append('R1,R2,R3')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC3_R1'] = 25
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC3_R1_SL1'] = 26
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC3_R1_SL2'] = 27
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC3_R2'] = 28
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC3_R2_SL1'] = 29
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC3_R2_SL2'] = 30
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC3_R3'] = 31
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC3_R3_SL1'] = 32
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC3_R3_SL2'] = 33
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC4'] = 34
SubNodeNames.append('R1,R2,R3')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC4_R1'] = 35
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC4_R1_SL1'] = 36
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC4_R1_SL2'] = 37
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC4_R2'] = 38
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC4_R2_SL1'] = 39
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC4_R2_SL2'] = 40
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC4_R3'] = 41
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC4_R3_SL1'] = 42
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC4_R3_SL2'] = 43
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC5'] = 44
SubNodeNames.append('R1,R2,R3')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC5_R1'] = 45
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC5_R1_SL1'] = 46
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC5_R1_SL2'] = 47
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC5_R2'] = 48
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC5_R2_SL1'] = 49
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC5_R2_SL2'] = 50
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC5_R3'] = 51
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC5_R3_SL1'] = 52
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC5_R3_SL2'] = 53
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC6'] = 54
SubNodeNames.append('R1,R2,R3')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC6_R1'] = 55
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC6_R1_SL1'] = 56
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC6_R1_SL2'] = 57
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC6_R2'] = 58
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC6_R2_SL1'] = 59
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC6_R2_SL2'] = 60
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC6_R3'] = 61
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC6_R3_SL1'] = 62
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC6_R3_SL2'] = 63
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL'] = 64
SubNodeNames.append('HV')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV'] = 65
SubNodeNames.append('SEC1,SEC2,SEC3,SEC4,SEC5,SEC6')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC1'] = 66
SubNodeNames.append('UI,UO,VI,VO,WI,WO')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC1_UI'] = 67
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC1_UO'] = 68
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC1_VI'] = 69
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC1_VO'] = 70
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC1_WI'] = 71
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC1_WO'] = 72
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC2'] = 73
SubNodeNames.append('UI,UO,VI,VO,WI,WO')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC2_UI'] = 74
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC2_UO'] = 75
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC2_VI'] = 76
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC2_VO'] = 77
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC2_WI'] = 78
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC2_WO'] = 79
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC3'] = 80
SubNodeNames.append('UI,UO,VI,VO,WI,WO')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC3_UI'] = 81
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC3_UO'] = 82
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC3_VI'] = 83
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC3_VO'] = 84
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC3_WI'] = 85
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC3_WO'] = 86
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC4'] = 87
SubNodeNames.append('UI,UO,VI,VO,WI,WO')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC4_UI'] = 88
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC4_UO'] = 89
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC4_VI'] = 90
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC4_VO'] = 91
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC4_WI'] = 92
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC4_WO'] = 93
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC5'] = 94
SubNodeNames.append('UI,UO,VI,VO,WI,WO')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC5_UI'] = 95
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC5_UO'] = 96
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC5_VI'] = 97
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC5_VO'] = 98
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC5_WI'] = 99
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC5_WO'] = 100
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC6'] = 101
SubNodeNames.append('UI,UO,VI,VO,WI,WO')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC6_UI'] = 102
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC6_UO'] = 103
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC6_VI'] = 104
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC6_VO'] = 105
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC6_WI'] = 106
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC6_WO'] = 107
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF'] = 108
SubNodeNames.append('HV')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV'] = 109
SubNodeNames.append('SEC1,SEC2,SEC3,SEC4,SEC5,SEC6')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC1'] = 110
SubNodeNames.append('PANEL1A,PANEL1B,PANEL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC1_PANEL1A'] = 111
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC1_PANEL1A_L'] = 112
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC1_PANEL1A_R'] = 113
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC1_PANEL1B'] = 114
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC1_PANEL1B_L'] = 115
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC1_PANEL1B_R'] = 116
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC1_PANEL2'] = 117
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC1_PANEL2_L'] = 118
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC1_PANEL2_R'] = 119
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC2'] = 120
SubNodeNames.append('PANEL1A,PANEL1B,PANEL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC2_PANEL1A'] = 121
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC2_PANEL1A_L'] = 122
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC2_PANEL1A_R'] = 123
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC2_PANEL1B'] = 124
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC2_PANEL1B_L'] = 125
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC2_PANEL1B_R'] = 126
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC2_PANEL2'] = 127
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC2_PANEL2_L'] = 128
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC2_PANEL2_R'] = 129
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC3'] = 130
SubNodeNames.append('PANEL1A,PANEL1B,PANEL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC3_PANEL1A'] = 131
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC3_PANEL1A_L'] = 132
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC3_PANEL1A_R'] = 133
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC3_PANEL1B'] = 134
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC3_PANEL1B_L'] = 135
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC3_PANEL1B_R'] = 136
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC3_PANEL2'] = 137
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC3_PANEL2_L'] = 138
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC3_PANEL2_R'] = 139
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC4'] = 140
SubNodeNames.append('PANEL1A,PANEL1B,PANEL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC4_PANEL1A'] = 141
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC4_PANEL1A_L'] = 142
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC4_PANEL1A_R'] = 143
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC4_PANEL1B'] = 144
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC4_PANEL1B_L'] = 145
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC4_PANEL1B_R'] = 146
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC4_PANEL2'] = 147
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC4_PANEL2_L'] = 148
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC4_PANEL2_R'] = 149
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC5'] = 150
SubNodeNames.append('PANEL1A,PANEL1B,PANEL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC5_PANEL1A'] = 151
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC5_PANEL1A_L'] = 152
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC5_PANEL1A_R'] = 153
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC5_PANEL1B'] = 154
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC5_PANEL1B_L'] = 155
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC5_PANEL1B_R'] = 156
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC5_PANEL2'] = 157
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC5_PANEL2_L'] = 158
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC5_PANEL2_R'] = 159
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC6'] = 160
SubNodeNames.append('PANEL1A,PANEL1B,PANEL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC6_PANEL1A'] = 161
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC6_PANEL1A_L'] = 162
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC6_PANEL1A_R'] = 163
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC6_PANEL1B'] = 164
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC6_PANEL1B_L'] = 165
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC6_PANEL1B_R'] = 166
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC6_PANEL2'] = 167
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC6_PANEL2_L'] = 168
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC6_PANEL2_R'] = 169
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC'] = 170
SubNodeNames.append('HV')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV'] = 171
SubNodeNames.append('SEC1,SEC2,SEC3,SEC4,SEC5,SEC6')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC1'] = 172
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC1_L'] = 173
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC1_R'] = 174
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC2'] = 175
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC2_L'] = 176
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC2_R'] = 177
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC3'] = 178
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC3_L'] = 179
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC3_R'] = 180
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC4'] = 181
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC4_L'] = 182
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC4_R'] = 183
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC5'] = 184
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC5_L'] = 185
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC5_R'] = 186
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC6'] = 187
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC6_L'] = 188
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC6_R'] = 189
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL'] = 190
SubNodeNames.append('HV')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV'] = 191
SubNodeNames.append('SEC1,SEC2,SEC3,SEC4,SEC5,SEC6')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC1'] = 192
SubNodeNames.append('U,V,W')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC1_U'] = 193
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62,E63,E64,E65,E66,E67,E68')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC1_V'] = 194
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC1_W'] = 195
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC2'] = 196
SubNodeNames.append('U,V,W')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC2_U'] = 197
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62,E63,E64,E65,E66,E67,E68')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC2_V'] = 198
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC2_W'] = 199
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC3'] = 200
SubNodeNames.append('U,V,W')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC3_U'] = 201
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62,E63,E64,E65,E66,E67,E68')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC3_V'] = 202
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC3_W'] = 203
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC4'] = 204
SubNodeNames.append('U,V,W')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC4_U'] = 205
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62,E63,E64,E65,E66,E67,E68')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC4_V'] = 206
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC4_W'] = 207
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC5'] = 208
SubNodeNames.append('U,V,W')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC5_U'] = 209
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62,E63,E64,E65,E66,E67,E68')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC5_V'] = 210
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC5_W'] = 211
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC6'] = 212
SubNodeNames.append('U,V,W')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC6_U'] = 213
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62,E63,E64,E65,E66,E67,E68')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC6_V'] = 214
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC6_W'] = 215
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW'] = 216
SubNodeNames.append('HVDC1,HVDC2,HVDC3,HVDC4,HVECAL1,HVECAL2,HVECAL3,HVECAL4,HVECAL5,HVECAL6,HVFTOF1,HVFTOF2,HVFTOF3,HVFTOF4,HVFTOF5,HVFTOF6,HVLTCC0,HVTEST0')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC1'] = 217
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC1_Sl00'] = 218
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC1_Sl01'] = 219
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC1_Sl02'] = 220
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC1_Sl03'] = 221
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC1_Sl04'] = 222
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC1_Sl05'] = 223
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC1_Sl06'] = 224
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC1_Sl07'] = 225
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC1_Sl08'] = 226
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC1_Sl09'] = 227
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC1_Sl10'] = 228
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC1_Sl11'] = 229
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC1_Sl12'] = 230
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC1_Sl13'] = 231
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC1_Sl14'] = 232
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC1_Sl15'] = 233
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC2'] = 234
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC2_Sl00'] = 235
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC2_Sl01'] = 236
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC2_Sl02'] = 237
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC2_Sl03'] = 238
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC2_Sl04'] = 239
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC2_Sl05'] = 240
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC2_Sl06'] = 241
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC2_Sl07'] = 242
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC2_Sl08'] = 243
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC2_Sl09'] = 244
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC2_Sl10'] = 245
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC2_Sl11'] = 246
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC2_Sl12'] = 247
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC2_Sl13'] = 248
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC2_Sl14'] = 249
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC2_Sl15'] = 250
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC3'] = 251
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC3_Sl00'] = 252
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC3_Sl01'] = 253
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC3_Sl02'] = 254
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC3_Sl03'] = 255
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC3_Sl04'] = 256
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC3_Sl05'] = 257
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC3_Sl06'] = 258
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC3_Sl07'] = 259
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC3_Sl08'] = 260
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC3_Sl09'] = 261
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC3_Sl10'] = 262
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC3_Sl11'] = 263
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC3_Sl12'] = 264
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC3_Sl13'] = 265
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC3_Sl14'] = 266
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC3_Sl15'] = 267
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC4'] = 268
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC4_Sl00'] = 269
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC4_Sl01'] = 270
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC4_Sl02'] = 271
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC4_Sl03'] = 272
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC4_Sl04'] = 273
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC4_Sl05'] = 274
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC4_Sl06'] = 275
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC4_Sl07'] = 276
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC4_Sl08'] = 277
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC4_Sl09'] = 278
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC4_Sl10'] = 279
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC4_Sl11'] = 280
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC4_Sl12'] = 281
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC4_Sl13'] = 282
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC4_Sl14'] = 283
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVDC4_Sl15'] = 284
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL1'] = 285
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL1_Sl00'] = 286
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL1_Sl01'] = 287
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL1_Sl02'] = 288
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL1_Sl03'] = 289
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL1_Sl04'] = 290
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL1_Sl05'] = 291
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL1_Sl06'] = 292
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL1_Sl07'] = 293
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL1_Sl08'] = 294
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL1_Sl09'] = 295
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL1_Sl10'] = 296
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL1_Sl11'] = 297
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL1_Sl12'] = 298
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL1_Sl13'] = 299
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL1_Sl14'] = 300
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL1_Sl15'] = 301
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL2'] = 302
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL2_Sl00'] = 303
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL2_Sl01'] = 304
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL2_Sl02'] = 305
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL2_Sl03'] = 306
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL2_Sl04'] = 307
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL2_Sl05'] = 308
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL2_Sl06'] = 309
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL2_Sl07'] = 310
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL2_Sl08'] = 311
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL2_Sl09'] = 312
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL2_Sl10'] = 313
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL2_Sl11'] = 314
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL2_Sl12'] = 315
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL2_Sl13'] = 316
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL2_Sl14'] = 317
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL2_Sl15'] = 318
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL3'] = 319
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL3_Sl00'] = 320
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL3_Sl01'] = 321
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL3_Sl02'] = 322
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL3_Sl03'] = 323
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL3_Sl04'] = 324
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL3_Sl05'] = 325
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL3_Sl06'] = 326
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL3_Sl07'] = 327
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL3_Sl08'] = 328
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL3_Sl09'] = 329
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL3_Sl10'] = 330
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL3_Sl11'] = 331
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL3_Sl12'] = 332
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL3_Sl13'] = 333
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL3_Sl14'] = 334
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL3_Sl15'] = 335
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL4'] = 336
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL4_Sl00'] = 337
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL4_Sl01'] = 338
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL4_Sl02'] = 339
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL4_Sl03'] = 340
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL4_Sl04'] = 341
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL4_Sl05'] = 342
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL4_Sl06'] = 343
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL4_Sl07'] = 344
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL4_Sl08'] = 345
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL4_Sl09'] = 346
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL4_Sl10'] = 347
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL4_Sl11'] = 348
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL4_Sl12'] = 349
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL4_Sl13'] = 350
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL4_Sl14'] = 351
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL4_Sl15'] = 352
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL5'] = 353
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL5_Sl00'] = 354
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL5_Sl01'] = 355
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL5_Sl02'] = 356
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL5_Sl03'] = 357
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL5_Sl04'] = 358
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL5_Sl05'] = 359
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL5_Sl06'] = 360
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL5_Sl07'] = 361
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL5_Sl08'] = 362
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL5_Sl09'] = 363
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL5_Sl10'] = 364
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL5_Sl11'] = 365
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL5_Sl12'] = 366
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL5_Sl13'] = 367
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL5_Sl14'] = 368
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL5_Sl15'] = 369
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL6'] = 370
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL6_Sl00'] = 371
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL6_Sl01'] = 372
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL6_Sl02'] = 373
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL6_Sl03'] = 374
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL6_Sl04'] = 375
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL6_Sl05'] = 376
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL6_Sl06'] = 377
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL6_Sl07'] = 378
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL6_Sl08'] = 379
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL6_Sl09'] = 380
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL6_Sl10'] = 381
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL6_Sl11'] = 382
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL6_Sl12'] = 383
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL6_Sl13'] = 384
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL6_Sl14'] = 385
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVECAL6_Sl15'] = 386
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF1'] = 387
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF1_Sl00'] = 388
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF1_Sl01'] = 389
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF1_Sl02'] = 390
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF1_Sl03'] = 391
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF1_Sl04'] = 392
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF1_Sl05'] = 393
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF1_Sl06'] = 394
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF1_Sl07'] = 395
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF1_Sl08'] = 396
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF1_Sl09'] = 397
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF1_Sl10'] = 398
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF1_Sl11'] = 399
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF1_Sl12'] = 400
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF1_Sl13'] = 401
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF1_Sl14'] = 402
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF1_Sl15'] = 403
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF2'] = 404
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF2_Sl00'] = 405
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF2_Sl01'] = 406
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF2_Sl02'] = 407
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF2_Sl03'] = 408
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF2_Sl04'] = 409
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF2_Sl05'] = 410
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF2_Sl06'] = 411
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF2_Sl07'] = 412
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF2_Sl08'] = 413
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF2_Sl09'] = 414
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF2_Sl10'] = 415
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF2_Sl11'] = 416
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF2_Sl12'] = 417
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF2_Sl13'] = 418
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF2_Sl14'] = 419
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF2_Sl15'] = 420
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF3'] = 421
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF3_Sl00'] = 422
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF3_Sl01'] = 423
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF3_Sl02'] = 424
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF3_Sl03'] = 425
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF3_Sl04'] = 426
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF3_Sl05'] = 427
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF3_Sl06'] = 428
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF3_Sl07'] = 429
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF3_Sl08'] = 430
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF3_Sl09'] = 431
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF3_Sl10'] = 432
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF3_Sl11'] = 433
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF3_Sl12'] = 434
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF3_Sl13'] = 435
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF3_Sl14'] = 436
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF3_Sl15'] = 437
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF4'] = 438
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF4_Sl00'] = 439
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF4_Sl01'] = 440
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF4_Sl02'] = 441
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF4_Sl03'] = 442
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF4_Sl04'] = 443
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF4_Sl05'] = 444
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF4_Sl06'] = 445
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF4_Sl07'] = 446
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF4_Sl08'] = 447
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF4_Sl09'] = 448
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF4_Sl10'] = 449
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF4_Sl11'] = 450
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF4_Sl12'] = 451
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF4_Sl13'] = 452
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF4_Sl14'] = 453
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF4_Sl15'] = 454
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF5'] = 455
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF5_Sl00'] = 456
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF5_Sl01'] = 457
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF5_Sl02'] = 458
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF5_Sl03'] = 459
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF5_Sl04'] = 460
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF5_Sl05'] = 461
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF5_Sl06'] = 462
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF5_Sl07'] = 463
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF5_Sl08'] = 464
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF5_Sl09'] = 465
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF5_Sl10'] = 466
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF5_Sl11'] = 467
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF5_Sl12'] = 468
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF5_Sl13'] = 469
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF5_Sl14'] = 470
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF5_Sl15'] = 471
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF6'] = 472
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF6_Sl00'] = 473
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF6_Sl01'] = 474
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF6_Sl02'] = 475
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF6_Sl03'] = 476
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF6_Sl04'] = 477
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF6_Sl05'] = 478
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF6_Sl06'] = 479
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF6_Sl07'] = 480
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF6_Sl08'] = 481
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF6_Sl09'] = 482
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF6_Sl10'] = 483
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF6_Sl11'] = 484
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF6_Sl12'] = 485
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF6_Sl13'] = 486
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF6_Sl14'] = 487
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVFTOF6_Sl15'] = 488
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVLTCC0'] = 489
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVLTCC0_Sl00'] = 490
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVLTCC0_Sl01'] = 491
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVLTCC0_Sl02'] = 492
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVLTCC0_Sl03'] = 493
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVLTCC0_Sl04'] = 494
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVLTCC0_Sl05'] = 495
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVLTCC0_Sl06'] = 496
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVLTCC0_Sl07'] = 497
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVLTCC0_Sl08'] = 498
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVLTCC0_Sl09'] = 499
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVLTCC0_Sl10'] = 500
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVLTCC0_Sl11'] = 501
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVLTCC0_Sl12'] = 502
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVLTCC0_Sl13'] = 503
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVLTCC0_Sl14'] = 504
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVLTCC0_Sl15'] = 505
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVTEST0'] = 506
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVTEST0_Sl00'] = 507
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVTEST0_Sl01'] = 508
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVTEST0_Sl02'] = 509
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVTEST0_Sl03'] = 510
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVTEST0_Sl04'] = 511
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVTEST0_Sl05'] = 512
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVTEST0_Sl06'] = 513
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVTEST0_Sl07'] = 514
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVTEST0_Sl08'] = 515
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVTEST0_Sl09'] = 516
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVTEST0_Sl10'] = 517
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVTEST0_Sl11'] = 518
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVTEST0_Sl12'] = 519
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVTEST0_Sl13'] = 520
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVTEST0_Sl14'] = 521
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_HW_HVTEST0_Sl15'] = 522
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS'] = 523
SubNodeNames.append('HV')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV'] = 524
SubNodeNames.append('DC,ECAL,FTOF,LTCC,PCAL')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC'] = 525
SubNodeNames.append('SEC1,SEC2,SEC3,SEC4,SEC5,SEC6')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC1'] = 526
SubNodeNames.append('R1,R2,R3')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC1_R1'] = 527
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC1_R1_SL1'] = 528
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC1_R1_SL2'] = 529
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC1_R2'] = 530
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC1_R2_SL1'] = 531
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC1_R2_SL2'] = 532
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC1_R3'] = 533
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC1_R3_SL1'] = 534
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC1_R3_SL2'] = 535
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC2'] = 536
SubNodeNames.append('R1,R2,R3')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC2_R1'] = 537
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC2_R1_SL1'] = 538
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC2_R1_SL2'] = 539
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC2_R2'] = 540
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC2_R2_SL1'] = 541
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC2_R2_SL2'] = 542
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC2_R3'] = 543
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC2_R3_SL1'] = 544
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC2_R3_SL2'] = 545
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC3'] = 546
SubNodeNames.append('R1,R2,R3')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC3_R1'] = 547
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC3_R1_SL1'] = 548
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC3_R1_SL2'] = 549
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC3_R2'] = 550
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC3_R2_SL1'] = 551
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC3_R2_SL2'] = 552
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC3_R3'] = 553
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC3_R3_SL1'] = 554
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC3_R3_SL2'] = 555
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC4'] = 556
SubNodeNames.append('R1,R2,R3')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC4_R1'] = 557
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC4_R1_SL1'] = 558
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC4_R1_SL2'] = 559
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC4_R2'] = 560
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC4_R2_SL1'] = 561
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC4_R2_SL2'] = 562
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC4_R3'] = 563
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC4_R3_SL1'] = 564
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC4_R3_SL2'] = 565
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC5'] = 566
SubNodeNames.append('R1,R2,R3')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC5_R1'] = 567
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC5_R1_SL1'] = 568
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC5_R1_SL2'] = 569
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC5_R2'] = 570
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC5_R2_SL1'] = 571
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC5_R2_SL2'] = 572
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC5_R3'] = 573
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC5_R3_SL1'] = 574
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC5_R3_SL2'] = 575
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC6'] = 576
SubNodeNames.append('R1,R2,R3')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC6_R1'] = 577
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC6_R1_SL1'] = 578
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC6_R1_SL2'] = 579
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC6_R2'] = 580
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC6_R2_SL1'] = 581
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC6_R2_SL2'] = 582
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC6_R3'] = 583
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC6_R3_SL1'] = 584
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_DC_SEC6_R3_SL2'] = 585
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL'] = 586
SubNodeNames.append('SEC1,SEC2,SEC3,SEC4,SEC5,SEC6')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC1'] = 587
SubNodeNames.append('UI,UO,VI,VO,WI,WO')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC1_UI'] = 588
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC1_UO'] = 589
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC1_VI'] = 590
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC1_VO'] = 591
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC1_WI'] = 592
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC1_WO'] = 593
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC2'] = 594
SubNodeNames.append('UI,UO,VI,VO,WI,WO')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC2_UI'] = 595
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC2_UO'] = 596
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC2_VI'] = 597
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC2_VO'] = 598
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC2_WI'] = 599
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC2_WO'] = 600
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC3'] = 601
SubNodeNames.append('UI,UO,VI,VO,WI,WO')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC3_UI'] = 602
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC3_UO'] = 603
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC3_VI'] = 604
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC3_VO'] = 605
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC3_WI'] = 606
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC3_WO'] = 607
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC4'] = 608
SubNodeNames.append('UI,UO,VI,VO,WI,WO')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC4_UI'] = 609
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC4_UO'] = 610
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC4_VI'] = 611
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC4_VO'] = 612
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC4_WI'] = 613
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC4_WO'] = 614
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC5'] = 615
SubNodeNames.append('UI,UO,VI,VO,WI,WO')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC5_UI'] = 616
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC5_UO'] = 617
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC5_VI'] = 618
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC5_VO'] = 619
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC5_WI'] = 620
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC5_WO'] = 621
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC6'] = 622
SubNodeNames.append('UI,UO,VI,VO,WI,WO')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC6_UI'] = 623
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC6_UO'] = 624
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC6_VI'] = 625
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC6_VO'] = 626
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC6_WI'] = 627
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_ECAL_SEC6_WO'] = 628
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF'] = 629
SubNodeNames.append('SEC1,SEC2,SEC3,SEC4,SEC5,SEC6')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC1'] = 630
SubNodeNames.append('PANEL1A,PANEL1B,PANEL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC1_PANEL1A'] = 631
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC1_PANEL1A_L'] = 632
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC1_PANEL1A_R'] = 633
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC1_PANEL1B'] = 634
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC1_PANEL1B_L'] = 635
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC1_PANEL1B_R'] = 636
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC1_PANEL2'] = 637
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC1_PANEL2_L'] = 638
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC1_PANEL2_R'] = 639
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC2'] = 640
SubNodeNames.append('PANEL1A,PANEL1B,PANEL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC2_PANEL1A'] = 641
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC2_PANEL1A_L'] = 642
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC2_PANEL1A_R'] = 643
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC2_PANEL1B'] = 644
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC2_PANEL1B_L'] = 645
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC2_PANEL1B_R'] = 646
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC2_PANEL2'] = 647
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC2_PANEL2_L'] = 648
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC2_PANEL2_R'] = 649
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC3'] = 650
SubNodeNames.append('PANEL1A,PANEL1B,PANEL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC3_PANEL1A'] = 651
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC3_PANEL1A_L'] = 652
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC3_PANEL1A_R'] = 653
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC3_PANEL1B'] = 654
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC3_PANEL1B_L'] = 655
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC3_PANEL1B_R'] = 656
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC3_PANEL2'] = 657
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC3_PANEL2_L'] = 658
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC3_PANEL2_R'] = 659
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC4'] = 660
SubNodeNames.append('PANEL1A,PANEL1B,PANEL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC4_PANEL1A'] = 661
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC4_PANEL1A_L'] = 662
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC4_PANEL1A_R'] = 663
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC4_PANEL1B'] = 664
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC4_PANEL1B_L'] = 665
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC4_PANEL1B_R'] = 666
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC4_PANEL2'] = 667
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC4_PANEL2_L'] = 668
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC4_PANEL2_R'] = 669
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC5'] = 670
SubNodeNames.append('PANEL1A,PANEL1B,PANEL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC5_PANEL1A'] = 671
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC5_PANEL1A_L'] = 672
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC5_PANEL1A_R'] = 673
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC5_PANEL1B'] = 674
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC5_PANEL1B_L'] = 675
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC5_PANEL1B_R'] = 676
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC5_PANEL2'] = 677
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC5_PANEL2_L'] = 678
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC5_PANEL2_R'] = 679
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC6'] = 680
SubNodeNames.append('PANEL1A,PANEL1B,PANEL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC6_PANEL1A'] = 681
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC6_PANEL1A_L'] = 682
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC6_PANEL1A_R'] = 683
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC6_PANEL1B'] = 684
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC6_PANEL1B_L'] = 685
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC6_PANEL1B_R'] = 686
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC6_PANEL2'] = 687
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC6_PANEL2_L'] = 688
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_FTOF_SEC6_PANEL2_R'] = 689
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_LTCC'] = 690
SubNodeNames.append('SEC1,SEC2,SEC3,SEC4,SEC5,SEC6')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_LTCC_SEC1'] = 691
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_LTCC_SEC1_L'] = 692
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_LTCC_SEC1_R'] = 693
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_LTCC_SEC2'] = 694
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_LTCC_SEC2_L'] = 695
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_LTCC_SEC2_R'] = 696
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_LTCC_SEC3'] = 697
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_LTCC_SEC3_L'] = 698
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_LTCC_SEC3_R'] = 699
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_LTCC_SEC4'] = 700
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_LTCC_SEC4_L'] = 701
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_LTCC_SEC4_R'] = 702
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_LTCC_SEC5'] = 703
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_LTCC_SEC5_L'] = 704
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_LTCC_SEC5_R'] = 705
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_LTCC_SEC6'] = 706
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_LTCC_SEC6_L'] = 707
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_LTCC_SEC6_R'] = 708
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL'] = 709
SubNodeNames.append('SEC1,SEC2,SEC3,SEC4,SEC5,SEC6')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC1'] = 710
SubNodeNames.append('U,V,W')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC1_U'] = 711
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62,E63,E64,E65,E66,E67,E68')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC1_V'] = 712
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC1_W'] = 713
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC2'] = 714
SubNodeNames.append('U,V,W')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC2_U'] = 715
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62,E63,E64,E65,E66,E67,E68')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC2_V'] = 716
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC2_W'] = 717
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC3'] = 718
SubNodeNames.append('U,V,W')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC3_U'] = 719
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62,E63,E64,E65,E66,E67,E68')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC3_V'] = 720
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC3_W'] = 721
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC4'] = 722
SubNodeNames.append('U,V,W')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC4_U'] = 723
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62,E63,E64,E65,E66,E67,E68')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC4_V'] = 724
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC4_W'] = 725
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC5'] = 726
SubNodeNames.append('U,V,W')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC5_U'] = 727
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62,E63,E64,E65,E66,E67,E68')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC5_V'] = 728
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC5_W'] = 729
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC6'] = 730
SubNodeNames.append('U,V,W')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC6_U'] = 731
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62,E63,E64,E65,E66,E67,E68')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC6_V'] = 732
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_SYS_HV_PCAL_SEC6_W'] = 733
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('Vmon,Imon,Vsetrbk,Vmax,rup,rdwn,stat,comms,pwonoff,v0set,i0set,trip,rampup,rampdn,svmax')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

