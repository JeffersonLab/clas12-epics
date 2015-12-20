# WARNING: DO NOT EDIT. This file was geneated at Sun Dec 20 10:34:39 EST 2015 by the a command like this:
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC1_R1_SL2'] = 7
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC1_R2_SL2'] = 10
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC1_R3_SL2'] = 13
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC2_R1_SL2'] = 17
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC2_R2_SL2'] = 20
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC2_R3_SL2'] = 23
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC3_R1_SL2'] = 27
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC3_R2_SL2'] = 30
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC3_R3_SL2'] = 33
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC4_R1_SL2'] = 37
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC4_R2_SL2'] = 40
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC4_R3_SL2'] = 43
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC5_R1_SL2'] = 47
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC5_R2_SL2'] = 50
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC5_R3_SL2'] = 53
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC6_R1_SL2'] = 57
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC6_R2_SL2'] = 60
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_DC_HV_SEC6_R3_SL2'] = 63
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC1_UO'] = 68
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC1_VI'] = 69
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC1_VO'] = 70
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC1_WI'] = 71
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC1_WO'] = 72
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC2_UO'] = 75
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC2_VI'] = 76
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC2_VO'] = 77
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC2_WI'] = 78
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC2_WO'] = 79
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC3_UO'] = 82
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC3_VI'] = 83
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC3_VO'] = 84
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC3_WI'] = 85
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC3_WO'] = 86
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC4_UO'] = 89
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC4_VI'] = 90
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC4_VO'] = 91
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC4_WI'] = 92
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC4_WO'] = 93
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC5_UO'] = 96
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC5_VI'] = 97
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC5_VO'] = 98
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC5_WI'] = 99
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC5_WO'] = 100
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC6_UO'] = 103
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC6_VI'] = 104
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC6_VO'] = 105
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC6_WI'] = 106
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_ECAL_HV_SEC6_WO'] = 107
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC1_PANEL1A_R'] = 113
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC1_PANEL1B_R'] = 116
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC1_PANEL2_R'] = 119
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC2_PANEL1A_R'] = 123
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC2_PANEL1B_R'] = 126
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC2_PANEL2_R'] = 129
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC3_PANEL1A_R'] = 133
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC3_PANEL1B_R'] = 136
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC3_PANEL2_R'] = 139
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC4_PANEL1A_R'] = 143
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC4_PANEL1B_R'] = 146
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC4_PANEL2_R'] = 149
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC5_PANEL1A_R'] = 153
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC5_PANEL1B_R'] = 156
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC5_PANEL2_R'] = 159
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC6_PANEL1A_R'] = 163
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC6_PANEL1B_R'] = 166
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_FTOF_HV_SEC6_PANEL2_R'] = 169
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC1_R'] = 174
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC2_R'] = 177
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC3_R'] = 180
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC4_R'] = 183
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC5_R'] = 186
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_LTCC_HV_SEC6_R'] = 189
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC1_V'] = 194
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC1_W'] = 195
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC2_V'] = 198
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC2_W'] = 199
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC3_V'] = 202
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC3_W'] = 203
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC4_V'] = 206
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC4_W'] = 207
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC5_V'] = 210
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC5_W'] = 211
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC6_V'] = 214
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('')

NodeIndex['B_DET_PCAL_HV_SEC6_W'] = 215
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
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
ElementRange.append('0,-1')

NodeIndex['B_HW_HVDC1'] = 217
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('0,-1')

NodeIndex['B_HW_HVDC1_Sl00'] = 218
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('0,-1')

NodeIndex['B_HW_HVDC1_Sl01'] = 219
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('24,23')

NodeIndex['B_HW_HVDC1_Sl02'] = 220
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('48,47')

NodeIndex['B_HW_HVDC1_Sl03'] = 221
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('72,71')

NodeIndex['B_HW_HVDC1_Sl04'] = 222
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('96,95')

NodeIndex['B_HW_HVDC1_Sl05'] = 223
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('120,119')

NodeIndex['B_HW_HVDC1_Sl06'] = 224
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('144,143')

NodeIndex['B_HW_HVDC1_Sl07'] = 225
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('168,167')

NodeIndex['B_HW_HVDC1_Sl08'] = 226
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('192,191')

NodeIndex['B_HW_HVDC1_Sl09'] = 227
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('216,215')

NodeIndex['B_HW_HVDC1_Sl10'] = 228
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('240,239')

NodeIndex['B_HW_HVDC1_Sl11'] = 229
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('264,263')

NodeIndex['B_HW_HVDC1_Sl12'] = 230
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('288,287')

NodeIndex['B_HW_HVDC1_Sl13'] = 231
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('312,311')

NodeIndex['B_HW_HVDC1_Sl14'] = 232
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('336,335')

NodeIndex['B_HW_HVDC1_Sl15'] = 233
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('360,359')

NodeIndex['B_HW_HVDC2'] = 234
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('384,383')

NodeIndex['B_HW_HVDC2_Sl00'] = 235
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('384,383')

NodeIndex['B_HW_HVDC2_Sl01'] = 236
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('408,407')

NodeIndex['B_HW_HVDC2_Sl02'] = 237
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('432,431')

NodeIndex['B_HW_HVDC2_Sl03'] = 238
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('456,455')

NodeIndex['B_HW_HVDC2_Sl04'] = 239
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('480,479')

NodeIndex['B_HW_HVDC2_Sl05'] = 240
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('504,503')

NodeIndex['B_HW_HVDC2_Sl06'] = 241
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('528,527')

NodeIndex['B_HW_HVDC2_Sl07'] = 242
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('552,551')

NodeIndex['B_HW_HVDC2_Sl08'] = 243
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('576,575')

NodeIndex['B_HW_HVDC2_Sl09'] = 244
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('600,599')

NodeIndex['B_HW_HVDC2_Sl10'] = 245
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('624,623')

NodeIndex['B_HW_HVDC2_Sl11'] = 246
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('648,647')

NodeIndex['B_HW_HVDC2_Sl12'] = 247
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('672,671')

NodeIndex['B_HW_HVDC2_Sl13'] = 248
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('696,695')

NodeIndex['B_HW_HVDC2_Sl14'] = 249
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('720,719')

NodeIndex['B_HW_HVDC2_Sl15'] = 250
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('744,743')

NodeIndex['B_HW_HVDC3'] = 251
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('768,767')

NodeIndex['B_HW_HVDC3_Sl00'] = 252
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('768,767')

NodeIndex['B_HW_HVDC3_Sl01'] = 253
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('792,791')

NodeIndex['B_HW_HVDC3_Sl02'] = 254
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('816,815')

NodeIndex['B_HW_HVDC3_Sl03'] = 255
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('840,839')

NodeIndex['B_HW_HVDC3_Sl04'] = 256
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('864,863')

NodeIndex['B_HW_HVDC3_Sl05'] = 257
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('888,887')

NodeIndex['B_HW_HVDC3_Sl06'] = 258
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('912,911')

NodeIndex['B_HW_HVDC3_Sl07'] = 259
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('936,935')

NodeIndex['B_HW_HVDC3_Sl08'] = 260
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('960,959')

NodeIndex['B_HW_HVDC3_Sl09'] = 261
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('984,983')

NodeIndex['B_HW_HVDC3_Sl10'] = 262
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1008,1007')

NodeIndex['B_HW_HVDC3_Sl11'] = 263
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1032,1031')

NodeIndex['B_HW_HVDC3_Sl12'] = 264
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1056,1055')

NodeIndex['B_HW_HVDC3_Sl13'] = 265
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1080,1079')

NodeIndex['B_HW_HVDC3_Sl14'] = 266
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1104,1103')

NodeIndex['B_HW_HVDC3_Sl15'] = 267
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1128,1127')

NodeIndex['B_HW_HVDC4'] = 268
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1152,1151')

NodeIndex['B_HW_HVDC4_Sl00'] = 269
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1152,1151')

NodeIndex['B_HW_HVDC4_Sl01'] = 270
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1176,1175')

NodeIndex['B_HW_HVDC4_Sl02'] = 271
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1200,1199')

NodeIndex['B_HW_HVDC4_Sl03'] = 272
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1224,1223')

NodeIndex['B_HW_HVDC4_Sl04'] = 273
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1248,1247')

NodeIndex['B_HW_HVDC4_Sl05'] = 274
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1272,1271')

NodeIndex['B_HW_HVDC4_Sl06'] = 275
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1296,1295')

NodeIndex['B_HW_HVDC4_Sl07'] = 276
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1320,1319')

NodeIndex['B_HW_HVDC4_Sl08'] = 277
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1344,1343')

NodeIndex['B_HW_HVDC4_Sl09'] = 278
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1368,1367')

NodeIndex['B_HW_HVDC4_Sl10'] = 279
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1392,1391')

NodeIndex['B_HW_HVDC4_Sl11'] = 280
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1416,1415')

NodeIndex['B_HW_HVDC4_Sl12'] = 281
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1440,1439')

NodeIndex['B_HW_HVDC4_Sl13'] = 282
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1464,1463')

NodeIndex['B_HW_HVDC4_Sl14'] = 283
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1488,1487')

NodeIndex['B_HW_HVDC4_Sl15'] = 284
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1512,1511')

NodeIndex['B_HW_HVECAL1'] = 285
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1536,1535')

NodeIndex['B_HW_HVECAL1_Sl00'] = 286
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1536,1535')

NodeIndex['B_HW_HVECAL1_Sl01'] = 287
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1560,1559')

NodeIndex['B_HW_HVECAL1_Sl02'] = 288
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1584,1583')

NodeIndex['B_HW_HVECAL1_Sl03'] = 289
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1608,1607')

NodeIndex['B_HW_HVECAL1_Sl04'] = 290
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1632,1631')

NodeIndex['B_HW_HVECAL1_Sl05'] = 291
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1656,1655')

NodeIndex['B_HW_HVECAL1_Sl06'] = 292
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1680,1679')

NodeIndex['B_HW_HVECAL1_Sl07'] = 293
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1704,1703')

NodeIndex['B_HW_HVECAL1_Sl08'] = 294
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1728,1727')

NodeIndex['B_HW_HVECAL1_Sl09'] = 295
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1752,1751')

NodeIndex['B_HW_HVECAL1_Sl10'] = 296
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1776,1775')

NodeIndex['B_HW_HVECAL1_Sl11'] = 297
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1800,1799')

NodeIndex['B_HW_HVECAL1_Sl12'] = 298
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1824,1823')

NodeIndex['B_HW_HVECAL1_Sl13'] = 299
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1848,1847')

NodeIndex['B_HW_HVECAL1_Sl14'] = 300
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1872,1871')

NodeIndex['B_HW_HVECAL1_Sl15'] = 301
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1896,1895')

NodeIndex['B_HW_HVECAL2'] = 302
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1920,1919')

NodeIndex['B_HW_HVECAL2_Sl00'] = 303
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1920,1919')

NodeIndex['B_HW_HVECAL2_Sl01'] = 304
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1944,1943')

NodeIndex['B_HW_HVECAL2_Sl02'] = 305
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1968,1967')

NodeIndex['B_HW_HVECAL2_Sl03'] = 306
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1992,1991')

NodeIndex['B_HW_HVECAL2_Sl04'] = 307
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2016,2015')

NodeIndex['B_HW_HVECAL2_Sl05'] = 308
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2040,2039')

NodeIndex['B_HW_HVECAL2_Sl06'] = 309
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2064,2063')

NodeIndex['B_HW_HVECAL2_Sl07'] = 310
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2088,2087')

NodeIndex['B_HW_HVECAL2_Sl08'] = 311
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2112,2111')

NodeIndex['B_HW_HVECAL2_Sl09'] = 312
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2136,2135')

NodeIndex['B_HW_HVECAL2_Sl10'] = 313
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2160,2159')

NodeIndex['B_HW_HVECAL2_Sl11'] = 314
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2184,2183')

NodeIndex['B_HW_HVECAL2_Sl12'] = 315
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2208,2207')

NodeIndex['B_HW_HVECAL2_Sl13'] = 316
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2232,2231')

NodeIndex['B_HW_HVECAL2_Sl14'] = 317
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2256,2255')

NodeIndex['B_HW_HVECAL2_Sl15'] = 318
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2280,2279')

NodeIndex['B_HW_HVECAL3'] = 319
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2304,2303')

NodeIndex['B_HW_HVECAL3_Sl00'] = 320
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2304,2303')

NodeIndex['B_HW_HVECAL3_Sl01'] = 321
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2328,2327')

NodeIndex['B_HW_HVECAL3_Sl02'] = 322
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2352,2351')

NodeIndex['B_HW_HVECAL3_Sl03'] = 323
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2376,2375')

NodeIndex['B_HW_HVECAL3_Sl04'] = 324
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2400,2399')

NodeIndex['B_HW_HVECAL3_Sl05'] = 325
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2424,2423')

NodeIndex['B_HW_HVECAL3_Sl06'] = 326
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2448,2447')

NodeIndex['B_HW_HVECAL3_Sl07'] = 327
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2472,2471')

NodeIndex['B_HW_HVECAL3_Sl08'] = 328
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2496,2495')

NodeIndex['B_HW_HVECAL3_Sl09'] = 329
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2520,2519')

NodeIndex['B_HW_HVECAL3_Sl10'] = 330
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2544,2543')

NodeIndex['B_HW_HVECAL3_Sl11'] = 331
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2568,2567')

NodeIndex['B_HW_HVECAL3_Sl12'] = 332
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2592,2591')

NodeIndex['B_HW_HVECAL3_Sl13'] = 333
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2616,2615')

NodeIndex['B_HW_HVECAL3_Sl14'] = 334
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2640,2639')

NodeIndex['B_HW_HVECAL3_Sl15'] = 335
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2664,2663')

NodeIndex['B_HW_HVECAL4'] = 336
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2688,2687')

NodeIndex['B_HW_HVECAL4_Sl00'] = 337
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2688,2687')

NodeIndex['B_HW_HVECAL4_Sl01'] = 338
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2712,2711')

NodeIndex['B_HW_HVECAL4_Sl02'] = 339
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2736,2735')

NodeIndex['B_HW_HVECAL4_Sl03'] = 340
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2760,2759')

NodeIndex['B_HW_HVECAL4_Sl04'] = 341
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2784,2783')

NodeIndex['B_HW_HVECAL4_Sl05'] = 342
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2808,2807')

NodeIndex['B_HW_HVECAL4_Sl06'] = 343
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2832,2831')

NodeIndex['B_HW_HVECAL4_Sl07'] = 344
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2856,2855')

NodeIndex['B_HW_HVECAL4_Sl08'] = 345
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2880,2879')

NodeIndex['B_HW_HVECAL4_Sl09'] = 346
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2904,2903')

NodeIndex['B_HW_HVECAL4_Sl10'] = 347
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2928,2927')

NodeIndex['B_HW_HVECAL4_Sl11'] = 348
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2952,2951')

NodeIndex['B_HW_HVECAL4_Sl12'] = 349
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2976,2975')

NodeIndex['B_HW_HVECAL4_Sl13'] = 350
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3000,2999')

NodeIndex['B_HW_HVECAL4_Sl14'] = 351
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3024,3023')

NodeIndex['B_HW_HVECAL4_Sl15'] = 352
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3048,3047')

NodeIndex['B_HW_HVECAL5'] = 353
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3072,3071')

NodeIndex['B_HW_HVECAL5_Sl00'] = 354
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3072,3071')

NodeIndex['B_HW_HVECAL5_Sl01'] = 355
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3096,3095')

NodeIndex['B_HW_HVECAL5_Sl02'] = 356
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3120,3119')

NodeIndex['B_HW_HVECAL5_Sl03'] = 357
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3144,3143')

NodeIndex['B_HW_HVECAL5_Sl04'] = 358
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3168,3167')

NodeIndex['B_HW_HVECAL5_Sl05'] = 359
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3192,3191')

NodeIndex['B_HW_HVECAL5_Sl06'] = 360
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3216,3215')

NodeIndex['B_HW_HVECAL5_Sl07'] = 361
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3240,3239')

NodeIndex['B_HW_HVECAL5_Sl08'] = 362
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3264,3263')

NodeIndex['B_HW_HVECAL5_Sl09'] = 363
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3288,3287')

NodeIndex['B_HW_HVECAL5_Sl10'] = 364
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3312,3311')

NodeIndex['B_HW_HVECAL5_Sl11'] = 365
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3336,3335')

NodeIndex['B_HW_HVECAL5_Sl12'] = 366
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3360,3359')

NodeIndex['B_HW_HVECAL5_Sl13'] = 367
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3384,3383')

NodeIndex['B_HW_HVECAL5_Sl14'] = 368
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3408,3407')

NodeIndex['B_HW_HVECAL5_Sl15'] = 369
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3432,3431')

NodeIndex['B_HW_HVECAL6'] = 370
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3456,3455')

NodeIndex['B_HW_HVECAL6_Sl00'] = 371
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3456,3455')

NodeIndex['B_HW_HVECAL6_Sl01'] = 372
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3480,3479')

NodeIndex['B_HW_HVECAL6_Sl02'] = 373
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3504,3503')

NodeIndex['B_HW_HVECAL6_Sl03'] = 374
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3528,3527')

NodeIndex['B_HW_HVECAL6_Sl04'] = 375
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3552,3551')

NodeIndex['B_HW_HVECAL6_Sl05'] = 376
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3576,3575')

NodeIndex['B_HW_HVECAL6_Sl06'] = 377
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3600,3599')

NodeIndex['B_HW_HVECAL6_Sl07'] = 378
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3624,3623')

NodeIndex['B_HW_HVECAL6_Sl08'] = 379
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3648,3647')

NodeIndex['B_HW_HVECAL6_Sl09'] = 380
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3672,3671')

NodeIndex['B_HW_HVECAL6_Sl10'] = 381
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3696,3695')

NodeIndex['B_HW_HVECAL6_Sl11'] = 382
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3720,3719')

NodeIndex['B_HW_HVECAL6_Sl12'] = 383
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3744,3743')

NodeIndex['B_HW_HVECAL6_Sl13'] = 384
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3768,3767')

NodeIndex['B_HW_HVECAL6_Sl14'] = 385
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3792,3791')

NodeIndex['B_HW_HVECAL6_Sl15'] = 386
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3816,3815')

NodeIndex['B_HW_HVFTOF1'] = 387
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3840,3839')

NodeIndex['B_HW_HVFTOF1_Sl00'] = 388
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3840,3839')

NodeIndex['B_HW_HVFTOF1_Sl01'] = 389
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3864,3863')

NodeIndex['B_HW_HVFTOF1_Sl02'] = 390
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3888,3887')

NodeIndex['B_HW_HVFTOF1_Sl03'] = 391
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3912,3911')

NodeIndex['B_HW_HVFTOF1_Sl04'] = 392
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3936,3935')

NodeIndex['B_HW_HVFTOF1_Sl05'] = 393
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3960,3959')

NodeIndex['B_HW_HVFTOF1_Sl06'] = 394
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3984,3983')

NodeIndex['B_HW_HVFTOF1_Sl07'] = 395
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4008,4007')

NodeIndex['B_HW_HVFTOF1_Sl08'] = 396
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4032,4031')

NodeIndex['B_HW_HVFTOF1_Sl09'] = 397
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4056,4055')

NodeIndex['B_HW_HVFTOF1_Sl10'] = 398
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4080,4079')

NodeIndex['B_HW_HVFTOF1_Sl11'] = 399
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4104,4103')

NodeIndex['B_HW_HVFTOF1_Sl12'] = 400
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4128,4127')

NodeIndex['B_HW_HVFTOF1_Sl13'] = 401
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4152,4151')

NodeIndex['B_HW_HVFTOF1_Sl14'] = 402
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4176,4175')

NodeIndex['B_HW_HVFTOF1_Sl15'] = 403
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4200,4199')

NodeIndex['B_HW_HVFTOF2'] = 404
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4224,4223')

NodeIndex['B_HW_HVFTOF2_Sl00'] = 405
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4224,4223')

NodeIndex['B_HW_HVFTOF2_Sl01'] = 406
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4248,4247')

NodeIndex['B_HW_HVFTOF2_Sl02'] = 407
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4272,4271')

NodeIndex['B_HW_HVFTOF2_Sl03'] = 408
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4296,4295')

NodeIndex['B_HW_HVFTOF2_Sl04'] = 409
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4320,4319')

NodeIndex['B_HW_HVFTOF2_Sl05'] = 410
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4344,4343')

NodeIndex['B_HW_HVFTOF2_Sl06'] = 411
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4368,4367')

NodeIndex['B_HW_HVFTOF2_Sl07'] = 412
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4392,4391')

NodeIndex['B_HW_HVFTOF2_Sl08'] = 413
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4416,4415')

NodeIndex['B_HW_HVFTOF2_Sl09'] = 414
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4440,4439')

NodeIndex['B_HW_HVFTOF2_Sl10'] = 415
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4464,4463')

NodeIndex['B_HW_HVFTOF2_Sl11'] = 416
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4488,4487')

NodeIndex['B_HW_HVFTOF2_Sl12'] = 417
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4512,4511')

NodeIndex['B_HW_HVFTOF2_Sl13'] = 418
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4536,4535')

NodeIndex['B_HW_HVFTOF2_Sl14'] = 419
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4560,4559')

NodeIndex['B_HW_HVFTOF2_Sl15'] = 420
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4584,4583')

NodeIndex['B_HW_HVFTOF3'] = 421
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4608,4607')

NodeIndex['B_HW_HVFTOF3_Sl00'] = 422
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4608,4607')

NodeIndex['B_HW_HVFTOF3_Sl01'] = 423
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4632,4631')

NodeIndex['B_HW_HVFTOF3_Sl02'] = 424
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4656,4655')

NodeIndex['B_HW_HVFTOF3_Sl03'] = 425
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4680,4679')

NodeIndex['B_HW_HVFTOF3_Sl04'] = 426
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4704,4703')

NodeIndex['B_HW_HVFTOF3_Sl05'] = 427
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4728,4727')

NodeIndex['B_HW_HVFTOF3_Sl06'] = 428
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4752,4751')

NodeIndex['B_HW_HVFTOF3_Sl07'] = 429
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4776,4775')

NodeIndex['B_HW_HVFTOF3_Sl08'] = 430
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4800,4799')

NodeIndex['B_HW_HVFTOF3_Sl09'] = 431
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4824,4823')

NodeIndex['B_HW_HVFTOF3_Sl10'] = 432
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4848,4847')

NodeIndex['B_HW_HVFTOF3_Sl11'] = 433
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4872,4871')

NodeIndex['B_HW_HVFTOF3_Sl12'] = 434
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4896,4895')

NodeIndex['B_HW_HVFTOF3_Sl13'] = 435
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4920,4919')

NodeIndex['B_HW_HVFTOF3_Sl14'] = 436
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4944,4943')

NodeIndex['B_HW_HVFTOF3_Sl15'] = 437
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4968,4967')

NodeIndex['B_HW_HVFTOF4'] = 438
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4992,4991')

NodeIndex['B_HW_HVFTOF4_Sl00'] = 439
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4992,4991')

NodeIndex['B_HW_HVFTOF4_Sl01'] = 440
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5016,5015')

NodeIndex['B_HW_HVFTOF4_Sl02'] = 441
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5040,5039')

NodeIndex['B_HW_HVFTOF4_Sl03'] = 442
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5064,5063')

NodeIndex['B_HW_HVFTOF4_Sl04'] = 443
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5088,5087')

NodeIndex['B_HW_HVFTOF4_Sl05'] = 444
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5112,5111')

NodeIndex['B_HW_HVFTOF4_Sl06'] = 445
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5136,5135')

NodeIndex['B_HW_HVFTOF4_Sl07'] = 446
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5160,5159')

NodeIndex['B_HW_HVFTOF4_Sl08'] = 447
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5184,5183')

NodeIndex['B_HW_HVFTOF4_Sl09'] = 448
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5208,5207')

NodeIndex['B_HW_HVFTOF4_Sl10'] = 449
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5232,5231')

NodeIndex['B_HW_HVFTOF4_Sl11'] = 450
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5256,5255')

NodeIndex['B_HW_HVFTOF4_Sl12'] = 451
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5280,5279')

NodeIndex['B_HW_HVFTOF4_Sl13'] = 452
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5304,5303')

NodeIndex['B_HW_HVFTOF4_Sl14'] = 453
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5328,5327')

NodeIndex['B_HW_HVFTOF4_Sl15'] = 454
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5352,5351')

NodeIndex['B_HW_HVFTOF5'] = 455
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5376,5375')

NodeIndex['B_HW_HVFTOF5_Sl00'] = 456
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5376,5375')

NodeIndex['B_HW_HVFTOF5_Sl01'] = 457
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5400,5399')

NodeIndex['B_HW_HVFTOF5_Sl02'] = 458
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5424,5423')

NodeIndex['B_HW_HVFTOF5_Sl03'] = 459
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5448,5447')

NodeIndex['B_HW_HVFTOF5_Sl04'] = 460
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5472,5471')

NodeIndex['B_HW_HVFTOF5_Sl05'] = 461
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5496,5495')

NodeIndex['B_HW_HVFTOF5_Sl06'] = 462
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5520,5519')

NodeIndex['B_HW_HVFTOF5_Sl07'] = 463
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5544,5543')

NodeIndex['B_HW_HVFTOF5_Sl08'] = 464
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5568,5567')

NodeIndex['B_HW_HVFTOF5_Sl09'] = 465
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5592,5591')

NodeIndex['B_HW_HVFTOF5_Sl10'] = 466
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5616,5615')

NodeIndex['B_HW_HVFTOF5_Sl11'] = 467
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5640,5639')

NodeIndex['B_HW_HVFTOF5_Sl12'] = 468
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5664,5663')

NodeIndex['B_HW_HVFTOF5_Sl13'] = 469
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5688,5687')

NodeIndex['B_HW_HVFTOF5_Sl14'] = 470
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5712,5711')

NodeIndex['B_HW_HVFTOF5_Sl15'] = 471
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5736,5735')

NodeIndex['B_HW_HVFTOF6'] = 472
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5760,5759')

NodeIndex['B_HW_HVFTOF6_Sl00'] = 473
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5760,5759')

NodeIndex['B_HW_HVFTOF6_Sl01'] = 474
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5784,5783')

NodeIndex['B_HW_HVFTOF6_Sl02'] = 475
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5808,5807')

NodeIndex['B_HW_HVFTOF6_Sl03'] = 476
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5832,5831')

NodeIndex['B_HW_HVFTOF6_Sl04'] = 477
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5856,5855')

NodeIndex['B_HW_HVFTOF6_Sl05'] = 478
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5880,5879')

NodeIndex['B_HW_HVFTOF6_Sl06'] = 479
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5904,5903')

NodeIndex['B_HW_HVFTOF6_Sl07'] = 480
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5928,5927')

NodeIndex['B_HW_HVFTOF6_Sl08'] = 481
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5952,5951')

NodeIndex['B_HW_HVFTOF6_Sl09'] = 482
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('5976,5975')

NodeIndex['B_HW_HVFTOF6_Sl10'] = 483
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6000,5999')

NodeIndex['B_HW_HVFTOF6_Sl11'] = 484
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6024,6023')

NodeIndex['B_HW_HVFTOF6_Sl12'] = 485
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6048,6047')

NodeIndex['B_HW_HVFTOF6_Sl13'] = 486
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6072,6071')

NodeIndex['B_HW_HVFTOF6_Sl14'] = 487
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6096,6095')

NodeIndex['B_HW_HVFTOF6_Sl15'] = 488
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6120,6119')

NodeIndex['B_HW_HVLTCC0'] = 489
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6144,6143')

NodeIndex['B_HW_HVLTCC0_Sl00'] = 490
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6144,6143')

NodeIndex['B_HW_HVLTCC0_Sl01'] = 491
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6168,6167')

NodeIndex['B_HW_HVLTCC0_Sl02'] = 492
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6192,6191')

NodeIndex['B_HW_HVLTCC0_Sl03'] = 493
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6216,6215')

NodeIndex['B_HW_HVLTCC0_Sl04'] = 494
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6240,6239')

NodeIndex['B_HW_HVLTCC0_Sl05'] = 495
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6264,6263')

NodeIndex['B_HW_HVLTCC0_Sl06'] = 496
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6288,6287')

NodeIndex['B_HW_HVLTCC0_Sl07'] = 497
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6312,6311')

NodeIndex['B_HW_HVLTCC0_Sl08'] = 498
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6336,6335')

NodeIndex['B_HW_HVLTCC0_Sl09'] = 499
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6360,6359')

NodeIndex['B_HW_HVLTCC0_Sl10'] = 500
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6384,6383')

NodeIndex['B_HW_HVLTCC0_Sl11'] = 501
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6408,6407')

NodeIndex['B_HW_HVLTCC0_Sl12'] = 502
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6432,6431')

NodeIndex['B_HW_HVLTCC0_Sl13'] = 503
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6456,6455')

NodeIndex['B_HW_HVLTCC0_Sl14'] = 504
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6480,6479')

NodeIndex['B_HW_HVLTCC0_Sl15'] = 505
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6504,6503')

NodeIndex['B_HW_HVTEST0'] = 506
SubNodeNames.append('Sl00,Sl01,Sl02,Sl03,Sl04,Sl05,Sl06,Sl07,Sl08,Sl09,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6528,6527')

NodeIndex['B_HW_HVTEST0_Sl00'] = 507
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6528,6527')

NodeIndex['B_HW_HVTEST0_Sl01'] = 508
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6552,6551')

NodeIndex['B_HW_HVTEST0_Sl02'] = 509
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6576,6575')

NodeIndex['B_HW_HVTEST0_Sl03'] = 510
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6600,6599')

NodeIndex['B_HW_HVTEST0_Sl04'] = 511
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6624,6623')

NodeIndex['B_HW_HVTEST0_Sl05'] = 512
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6648,6647')

NodeIndex['B_HW_HVTEST0_Sl06'] = 513
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6672,6671')

NodeIndex['B_HW_HVTEST0_Sl07'] = 514
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6696,6695')

NodeIndex['B_HW_HVTEST0_Sl08'] = 515
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6720,6719')

NodeIndex['B_HW_HVTEST0_Sl09'] = 516
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6744,6743')

NodeIndex['B_HW_HVTEST0_Sl10'] = 517
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6768,6767')

NodeIndex['B_HW_HVTEST0_Sl11'] = 518
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6792,6791')

NodeIndex['B_HW_HVTEST0_Sl12'] = 519
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6816,6815')

NodeIndex['B_HW_HVTEST0_Sl13'] = 520
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6840,6839')

NodeIndex['B_HW_HVTEST0_Sl14'] = 521
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6864,6863')

NodeIndex['B_HW_HVTEST0_Sl15'] = 522
SubNodeNames.append('')
ElementNames.append('Ch00,Ch01,Ch02,Ch03,Ch04,Ch05,Ch06,Ch07,Ch08,Ch09,Ch10,Ch11,Ch12,Ch13,Ch14,Ch15,Ch16,Ch17,Ch18,Ch19,Ch20,Ch21,Ch22,Ch23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('6888,6887')

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
ElementRange.append('0,4391')

NodeIndex['B_SYS_HV_DC'] = 525
SubNodeNames.append('SEC1,SEC2,SEC3,SEC4,SEC5,SEC6')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('0,647')

NodeIndex['B_SYS_HV_DC_SEC1'] = 526
SubNodeNames.append('R1,R2,R3')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('0,107')

NodeIndex['B_SYS_HV_DC_SEC1_R1'] = 527
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('0,35')

NodeIndex['B_SYS_HV_DC_SEC1_R1_SL1'] = 528
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('0,17')

NodeIndex['B_SYS_HV_DC_SEC1_R1_SL2'] = 529
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('18,35')

NodeIndex['B_SYS_HV_DC_SEC1_R2'] = 530
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('36,71')

NodeIndex['B_SYS_HV_DC_SEC1_R2_SL1'] = 531
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('36,53')

NodeIndex['B_SYS_HV_DC_SEC1_R2_SL2'] = 532
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('54,71')

NodeIndex['B_SYS_HV_DC_SEC1_R3'] = 533
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('72,107')

NodeIndex['B_SYS_HV_DC_SEC1_R3_SL1'] = 534
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('72,89')

NodeIndex['B_SYS_HV_DC_SEC1_R3_SL2'] = 535
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('90,107')

NodeIndex['B_SYS_HV_DC_SEC2'] = 536
SubNodeNames.append('R1,R2,R3')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('108,215')

NodeIndex['B_SYS_HV_DC_SEC2_R1'] = 537
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('108,143')

NodeIndex['B_SYS_HV_DC_SEC2_R1_SL1'] = 538
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('108,125')

NodeIndex['B_SYS_HV_DC_SEC2_R1_SL2'] = 539
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('126,143')

NodeIndex['B_SYS_HV_DC_SEC2_R2'] = 540
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('144,179')

NodeIndex['B_SYS_HV_DC_SEC2_R2_SL1'] = 541
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('144,161')

NodeIndex['B_SYS_HV_DC_SEC2_R2_SL2'] = 542
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('162,179')

NodeIndex['B_SYS_HV_DC_SEC2_R3'] = 543
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('180,215')

NodeIndex['B_SYS_HV_DC_SEC2_R3_SL1'] = 544
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('180,197')

NodeIndex['B_SYS_HV_DC_SEC2_R3_SL2'] = 545
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('198,215')

NodeIndex['B_SYS_HV_DC_SEC3'] = 546
SubNodeNames.append('R1,R2,R3')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('216,323')

NodeIndex['B_SYS_HV_DC_SEC3_R1'] = 547
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('216,251')

NodeIndex['B_SYS_HV_DC_SEC3_R1_SL1'] = 548
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('216,233')

NodeIndex['B_SYS_HV_DC_SEC3_R1_SL2'] = 549
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('234,251')

NodeIndex['B_SYS_HV_DC_SEC3_R2'] = 550
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('252,287')

NodeIndex['B_SYS_HV_DC_SEC3_R2_SL1'] = 551
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('252,269')

NodeIndex['B_SYS_HV_DC_SEC3_R2_SL2'] = 552
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('270,287')

NodeIndex['B_SYS_HV_DC_SEC3_R3'] = 553
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('288,323')

NodeIndex['B_SYS_HV_DC_SEC3_R3_SL1'] = 554
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('288,305')

NodeIndex['B_SYS_HV_DC_SEC3_R3_SL2'] = 555
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('306,323')

NodeIndex['B_SYS_HV_DC_SEC4'] = 556
SubNodeNames.append('R1,R2,R3')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('324,431')

NodeIndex['B_SYS_HV_DC_SEC4_R1'] = 557
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('324,359')

NodeIndex['B_SYS_HV_DC_SEC4_R1_SL1'] = 558
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('324,341')

NodeIndex['B_SYS_HV_DC_SEC4_R1_SL2'] = 559
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('342,359')

NodeIndex['B_SYS_HV_DC_SEC4_R2'] = 560
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('360,395')

NodeIndex['B_SYS_HV_DC_SEC4_R2_SL1'] = 561
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('360,377')

NodeIndex['B_SYS_HV_DC_SEC4_R2_SL2'] = 562
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('378,395')

NodeIndex['B_SYS_HV_DC_SEC4_R3'] = 563
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('396,431')

NodeIndex['B_SYS_HV_DC_SEC4_R3_SL1'] = 564
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('396,413')

NodeIndex['B_SYS_HV_DC_SEC4_R3_SL2'] = 565
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('414,431')

NodeIndex['B_SYS_HV_DC_SEC5'] = 566
SubNodeNames.append('R1,R2,R3')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('432,539')

NodeIndex['B_SYS_HV_DC_SEC5_R1'] = 567
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('432,467')

NodeIndex['B_SYS_HV_DC_SEC5_R1_SL1'] = 568
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('432,449')

NodeIndex['B_SYS_HV_DC_SEC5_R1_SL2'] = 569
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('450,467')

NodeIndex['B_SYS_HV_DC_SEC5_R2'] = 570
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('468,503')

NodeIndex['B_SYS_HV_DC_SEC5_R2_SL1'] = 571
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('468,485')

NodeIndex['B_SYS_HV_DC_SEC5_R2_SL2'] = 572
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('486,503')

NodeIndex['B_SYS_HV_DC_SEC5_R3'] = 573
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('504,539')

NodeIndex['B_SYS_HV_DC_SEC5_R3_SL1'] = 574
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('504,521')

NodeIndex['B_SYS_HV_DC_SEC5_R3_SL2'] = 575
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('522,539')

NodeIndex['B_SYS_HV_DC_SEC6'] = 576
SubNodeNames.append('R1,R2,R3')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('540,647')

NodeIndex['B_SYS_HV_DC_SEC6_R1'] = 577
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('540,575')

NodeIndex['B_SYS_HV_DC_SEC6_R1_SL1'] = 578
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('540,557')

NodeIndex['B_SYS_HV_DC_SEC6_R1_SL2'] = 579
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('558,575')

NodeIndex['B_SYS_HV_DC_SEC6_R2'] = 580
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('576,611')

NodeIndex['B_SYS_HV_DC_SEC6_R2_SL1'] = 581
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('576,593')

NodeIndex['B_SYS_HV_DC_SEC6_R2_SL2'] = 582
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('594,611')

NodeIndex['B_SYS_HV_DC_SEC6_R3'] = 583
SubNodeNames.append('SL1,SL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('612,647')

NodeIndex['B_SYS_HV_DC_SEC6_R3_SL1'] = 584
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('612,629')

NodeIndex['B_SYS_HV_DC_SEC6_R3_SL2'] = 585
SubNodeNames.append('')
ElementNames.append('F01-08,F09-16,F17-24,F25-32,F33-48,F49-64,F65-80,F81-112,G01-32,G33-112,S01-08,S09-16,S17-24,S25-32,S33-48,S49-64,S65-80,S81-112')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('630,647')

NodeIndex['B_SYS_HV_ECAL'] = 586
SubNodeNames.append('SEC1,SEC2,SEC3,SEC4,SEC5,SEC6')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('648,1943')

NodeIndex['B_SYS_HV_ECAL_SEC1'] = 587
SubNodeNames.append('UI,UO,VI,VO,WI,WO')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('648,863')

NodeIndex['B_SYS_HV_ECAL_SEC1_UI'] = 588
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('648,683')

NodeIndex['B_SYS_HV_ECAL_SEC1_UO'] = 589
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('684,719')

NodeIndex['B_SYS_HV_ECAL_SEC1_VI'] = 590
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('720,755')

NodeIndex['B_SYS_HV_ECAL_SEC1_VO'] = 591
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('756,791')

NodeIndex['B_SYS_HV_ECAL_SEC1_WI'] = 592
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('792,827')

NodeIndex['B_SYS_HV_ECAL_SEC1_WO'] = 593
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('828,863')

NodeIndex['B_SYS_HV_ECAL_SEC2'] = 594
SubNodeNames.append('UI,UO,VI,VO,WI,WO')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('864,1079')

NodeIndex['B_SYS_HV_ECAL_SEC2_UI'] = 595
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('864,899')

NodeIndex['B_SYS_HV_ECAL_SEC2_UO'] = 596
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('900,935')

NodeIndex['B_SYS_HV_ECAL_SEC2_VI'] = 597
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('936,971')

NodeIndex['B_SYS_HV_ECAL_SEC2_VO'] = 598
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('972,1007')

NodeIndex['B_SYS_HV_ECAL_SEC2_WI'] = 599
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1008,1043')

NodeIndex['B_SYS_HV_ECAL_SEC2_WO'] = 600
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1044,1079')

NodeIndex['B_SYS_HV_ECAL_SEC3'] = 601
SubNodeNames.append('UI,UO,VI,VO,WI,WO')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1080,1295')

NodeIndex['B_SYS_HV_ECAL_SEC3_UI'] = 602
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1080,1115')

NodeIndex['B_SYS_HV_ECAL_SEC3_UO'] = 603
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1116,1151')

NodeIndex['B_SYS_HV_ECAL_SEC3_VI'] = 604
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1152,1187')

NodeIndex['B_SYS_HV_ECAL_SEC3_VO'] = 605
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1188,1223')

NodeIndex['B_SYS_HV_ECAL_SEC3_WI'] = 606
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1224,1259')

NodeIndex['B_SYS_HV_ECAL_SEC3_WO'] = 607
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1260,1295')

NodeIndex['B_SYS_HV_ECAL_SEC4'] = 608
SubNodeNames.append('UI,UO,VI,VO,WI,WO')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1296,1511')

NodeIndex['B_SYS_HV_ECAL_SEC4_UI'] = 609
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1296,1331')

NodeIndex['B_SYS_HV_ECAL_SEC4_UO'] = 610
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1332,1367')

NodeIndex['B_SYS_HV_ECAL_SEC4_VI'] = 611
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1368,1403')

NodeIndex['B_SYS_HV_ECAL_SEC4_VO'] = 612
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1404,1439')

NodeIndex['B_SYS_HV_ECAL_SEC4_WI'] = 613
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1440,1475')

NodeIndex['B_SYS_HV_ECAL_SEC4_WO'] = 614
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1476,1511')

NodeIndex['B_SYS_HV_ECAL_SEC5'] = 615
SubNodeNames.append('UI,UO,VI,VO,WI,WO')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1512,1727')

NodeIndex['B_SYS_HV_ECAL_SEC5_UI'] = 616
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1512,1547')

NodeIndex['B_SYS_HV_ECAL_SEC5_UO'] = 617
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1548,1583')

NodeIndex['B_SYS_HV_ECAL_SEC5_VI'] = 618
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1584,1619')

NodeIndex['B_SYS_HV_ECAL_SEC5_VO'] = 619
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1620,1655')

NodeIndex['B_SYS_HV_ECAL_SEC5_WI'] = 620
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1656,1691')

NodeIndex['B_SYS_HV_ECAL_SEC5_WO'] = 621
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1692,1727')

NodeIndex['B_SYS_HV_ECAL_SEC6'] = 622
SubNodeNames.append('UI,UO,VI,VO,WI,WO')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1728,1943')

NodeIndex['B_SYS_HV_ECAL_SEC6_UI'] = 623
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1728,1763')

NodeIndex['B_SYS_HV_ECAL_SEC6_UO'] = 624
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1764,1799')

NodeIndex['B_SYS_HV_ECAL_SEC6_VI'] = 625
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1800,1835')

NodeIndex['B_SYS_HV_ECAL_SEC6_VO'] = 626
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1836,1871')

NodeIndex['B_SYS_HV_ECAL_SEC6_WI'] = 627
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1872,1907')

NodeIndex['B_SYS_HV_ECAL_SEC6_WO'] = 628
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1908,1943')

NodeIndex['B_SYS_HV_FTOF'] = 629
SubNodeNames.append('SEC1,SEC2,SEC3,SEC4,SEC5,SEC6')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1944,3023')

NodeIndex['B_SYS_HV_FTOF_SEC1'] = 630
SubNodeNames.append('PANEL1A,PANEL1B,PANEL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1944,2123')

NodeIndex['B_SYS_HV_FTOF_SEC1_PANEL1A'] = 631
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1944,1989')

NodeIndex['B_SYS_HV_FTOF_SEC1_PANEL1A_L'] = 632
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1944,1966')

NodeIndex['B_SYS_HV_FTOF_SEC1_PANEL1A_R'] = 633
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1967,1989')

NodeIndex['B_SYS_HV_FTOF_SEC1_PANEL1B'] = 634
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1990,2113')

NodeIndex['B_SYS_HV_FTOF_SEC1_PANEL1B_L'] = 635
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('1990,2051')

NodeIndex['B_SYS_HV_FTOF_SEC1_PANEL1B_R'] = 636
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2052,2113')

NodeIndex['B_SYS_HV_FTOF_SEC1_PANEL2'] = 637
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2114,2123')

NodeIndex['B_SYS_HV_FTOF_SEC1_PANEL2_L'] = 638
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2114,2118')

NodeIndex['B_SYS_HV_FTOF_SEC1_PANEL2_R'] = 639
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2119,2123')

NodeIndex['B_SYS_HV_FTOF_SEC2'] = 640
SubNodeNames.append('PANEL1A,PANEL1B,PANEL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2124,2303')

NodeIndex['B_SYS_HV_FTOF_SEC2_PANEL1A'] = 641
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2124,2169')

NodeIndex['B_SYS_HV_FTOF_SEC2_PANEL1A_L'] = 642
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2124,2146')

NodeIndex['B_SYS_HV_FTOF_SEC2_PANEL1A_R'] = 643
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2147,2169')

NodeIndex['B_SYS_HV_FTOF_SEC2_PANEL1B'] = 644
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2170,2293')

NodeIndex['B_SYS_HV_FTOF_SEC2_PANEL1B_L'] = 645
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2170,2231')

NodeIndex['B_SYS_HV_FTOF_SEC2_PANEL1B_R'] = 646
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2232,2293')

NodeIndex['B_SYS_HV_FTOF_SEC2_PANEL2'] = 647
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2294,2303')

NodeIndex['B_SYS_HV_FTOF_SEC2_PANEL2_L'] = 648
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2294,2298')

NodeIndex['B_SYS_HV_FTOF_SEC2_PANEL2_R'] = 649
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2299,2303')

NodeIndex['B_SYS_HV_FTOF_SEC3'] = 650
SubNodeNames.append('PANEL1A,PANEL1B,PANEL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2304,2483')

NodeIndex['B_SYS_HV_FTOF_SEC3_PANEL1A'] = 651
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2304,2349')

NodeIndex['B_SYS_HV_FTOF_SEC3_PANEL1A_L'] = 652
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2304,2326')

NodeIndex['B_SYS_HV_FTOF_SEC3_PANEL1A_R'] = 653
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2327,2349')

NodeIndex['B_SYS_HV_FTOF_SEC3_PANEL1B'] = 654
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2350,2473')

NodeIndex['B_SYS_HV_FTOF_SEC3_PANEL1B_L'] = 655
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2350,2411')

NodeIndex['B_SYS_HV_FTOF_SEC3_PANEL1B_R'] = 656
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2412,2473')

NodeIndex['B_SYS_HV_FTOF_SEC3_PANEL2'] = 657
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2474,2483')

NodeIndex['B_SYS_HV_FTOF_SEC3_PANEL2_L'] = 658
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2474,2478')

NodeIndex['B_SYS_HV_FTOF_SEC3_PANEL2_R'] = 659
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2479,2483')

NodeIndex['B_SYS_HV_FTOF_SEC4'] = 660
SubNodeNames.append('PANEL1A,PANEL1B,PANEL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2484,2663')

NodeIndex['B_SYS_HV_FTOF_SEC4_PANEL1A'] = 661
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2484,2529')

NodeIndex['B_SYS_HV_FTOF_SEC4_PANEL1A_L'] = 662
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2484,2506')

NodeIndex['B_SYS_HV_FTOF_SEC4_PANEL1A_R'] = 663
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2507,2529')

NodeIndex['B_SYS_HV_FTOF_SEC4_PANEL1B'] = 664
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2530,2653')

NodeIndex['B_SYS_HV_FTOF_SEC4_PANEL1B_L'] = 665
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2530,2591')

NodeIndex['B_SYS_HV_FTOF_SEC4_PANEL1B_R'] = 666
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2592,2653')

NodeIndex['B_SYS_HV_FTOF_SEC4_PANEL2'] = 667
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2654,2663')

NodeIndex['B_SYS_HV_FTOF_SEC4_PANEL2_L'] = 668
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2654,2658')

NodeIndex['B_SYS_HV_FTOF_SEC4_PANEL2_R'] = 669
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2659,2663')

NodeIndex['B_SYS_HV_FTOF_SEC5'] = 670
SubNodeNames.append('PANEL1A,PANEL1B,PANEL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2664,2843')

NodeIndex['B_SYS_HV_FTOF_SEC5_PANEL1A'] = 671
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2664,2709')

NodeIndex['B_SYS_HV_FTOF_SEC5_PANEL1A_L'] = 672
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2664,2686')

NodeIndex['B_SYS_HV_FTOF_SEC5_PANEL1A_R'] = 673
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2687,2709')

NodeIndex['B_SYS_HV_FTOF_SEC5_PANEL1B'] = 674
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2710,2833')

NodeIndex['B_SYS_HV_FTOF_SEC5_PANEL1B_L'] = 675
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2710,2771')

NodeIndex['B_SYS_HV_FTOF_SEC5_PANEL1B_R'] = 676
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2772,2833')

NodeIndex['B_SYS_HV_FTOF_SEC5_PANEL2'] = 677
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2834,2843')

NodeIndex['B_SYS_HV_FTOF_SEC5_PANEL2_L'] = 678
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2834,2838')

NodeIndex['B_SYS_HV_FTOF_SEC5_PANEL2_R'] = 679
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2839,2843')

NodeIndex['B_SYS_HV_FTOF_SEC6'] = 680
SubNodeNames.append('PANEL1A,PANEL1B,PANEL2')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2844,3023')

NodeIndex['B_SYS_HV_FTOF_SEC6_PANEL1A'] = 681
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2844,2889')

NodeIndex['B_SYS_HV_FTOF_SEC6_PANEL1A_L'] = 682
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2844,2866')

NodeIndex['B_SYS_HV_FTOF_SEC6_PANEL1A_R'] = 683
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2867,2889')

NodeIndex['B_SYS_HV_FTOF_SEC6_PANEL1B'] = 684
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2890,3013')

NodeIndex['B_SYS_HV_FTOF_SEC6_PANEL1B_L'] = 685
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2890,2951')

NodeIndex['B_SYS_HV_FTOF_SEC6_PANEL1B_R'] = 686
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('2952,3013')

NodeIndex['B_SYS_HV_FTOF_SEC6_PANEL2'] = 687
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3014,3023')

NodeIndex['B_SYS_HV_FTOF_SEC6_PANEL2_L'] = 688
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3014,3018')

NodeIndex['B_SYS_HV_FTOF_SEC6_PANEL2_R'] = 689
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3019,3023')

NodeIndex['B_SYS_HV_LTCC'] = 690
SubNodeNames.append('SEC1,SEC2,SEC3,SEC4,SEC5,SEC6')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3024,3239')

NodeIndex['B_SYS_HV_LTCC_SEC1'] = 691
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3024,3059')

NodeIndex['B_SYS_HV_LTCC_SEC1_L'] = 692
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3024,3041')

NodeIndex['B_SYS_HV_LTCC_SEC1_R'] = 693
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3042,3059')

NodeIndex['B_SYS_HV_LTCC_SEC2'] = 694
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3060,3095')

NodeIndex['B_SYS_HV_LTCC_SEC2_L'] = 695
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3060,3077')

NodeIndex['B_SYS_HV_LTCC_SEC2_R'] = 696
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3078,3095')

NodeIndex['B_SYS_HV_LTCC_SEC3'] = 697
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3096,3131')

NodeIndex['B_SYS_HV_LTCC_SEC3_L'] = 698
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3096,3113')

NodeIndex['B_SYS_HV_LTCC_SEC3_R'] = 699
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3114,3131')

NodeIndex['B_SYS_HV_LTCC_SEC4'] = 700
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3132,3167')

NodeIndex['B_SYS_HV_LTCC_SEC4_L'] = 701
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3132,3149')

NodeIndex['B_SYS_HV_LTCC_SEC4_R'] = 702
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3150,3167')

NodeIndex['B_SYS_HV_LTCC_SEC5'] = 703
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3168,3203')

NodeIndex['B_SYS_HV_LTCC_SEC5_L'] = 704
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3168,3185')

NodeIndex['B_SYS_HV_LTCC_SEC5_R'] = 705
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3186,3203')

NodeIndex['B_SYS_HV_LTCC_SEC6'] = 706
SubNodeNames.append('L,R')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3204,3239')

NodeIndex['B_SYS_HV_LTCC_SEC6_L'] = 707
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3204,3221')

NodeIndex['B_SYS_HV_LTCC_SEC6_R'] = 708
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3222,3239')

NodeIndex['B_SYS_HV_PCAL'] = 709
SubNodeNames.append('SEC1,SEC2,SEC3,SEC4,SEC5,SEC6')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3240,4391')

NodeIndex['B_SYS_HV_PCAL_SEC1'] = 710
SubNodeNames.append('U,V,W')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3240,3431')

NodeIndex['B_SYS_HV_PCAL_SEC1_U'] = 711
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62,E63,E64,E65,E66,E67,E68')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3240,3307')

NodeIndex['B_SYS_HV_PCAL_SEC1_V'] = 712
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3308,3369')

NodeIndex['B_SYS_HV_PCAL_SEC1_W'] = 713
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3370,3431')

NodeIndex['B_SYS_HV_PCAL_SEC2'] = 714
SubNodeNames.append('U,V,W')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3432,3623')

NodeIndex['B_SYS_HV_PCAL_SEC2_U'] = 715
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62,E63,E64,E65,E66,E67,E68')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3432,3499')

NodeIndex['B_SYS_HV_PCAL_SEC2_V'] = 716
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3500,3561')

NodeIndex['B_SYS_HV_PCAL_SEC2_W'] = 717
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3562,3623')

NodeIndex['B_SYS_HV_PCAL_SEC3'] = 718
SubNodeNames.append('U,V,W')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3624,3815')

NodeIndex['B_SYS_HV_PCAL_SEC3_U'] = 719
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62,E63,E64,E65,E66,E67,E68')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3624,3691')

NodeIndex['B_SYS_HV_PCAL_SEC3_V'] = 720
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3692,3753')

NodeIndex['B_SYS_HV_PCAL_SEC3_W'] = 721
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3754,3815')

NodeIndex['B_SYS_HV_PCAL_SEC4'] = 722
SubNodeNames.append('U,V,W')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3816,4007')

NodeIndex['B_SYS_HV_PCAL_SEC4_U'] = 723
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62,E63,E64,E65,E66,E67,E68')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3816,3883')

NodeIndex['B_SYS_HV_PCAL_SEC4_V'] = 724
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3884,3945')

NodeIndex['B_SYS_HV_PCAL_SEC4_W'] = 725
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('3946,4007')

NodeIndex['B_SYS_HV_PCAL_SEC5'] = 726
SubNodeNames.append('U,V,W')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4008,4199')

NodeIndex['B_SYS_HV_PCAL_SEC5_U'] = 727
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62,E63,E64,E65,E66,E67,E68')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4008,4075')

NodeIndex['B_SYS_HV_PCAL_SEC5_V'] = 728
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4076,4137')

NodeIndex['B_SYS_HV_PCAL_SEC5_W'] = 729
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4138,4199')

NodeIndex['B_SYS_HV_PCAL_SEC6'] = 730
SubNodeNames.append('U,V,W')
ElementNames.append('')
ElementRecordNames.append('')
ElementRecordTypes.append('')
ElementRecordFlags.append('')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4200,4391')

NodeIndex['B_SYS_HV_PCAL_SEC6_U'] = 731
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62,E63,E64,E65,E66,E67,E68')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4200,4267')

NodeIndex['B_SYS_HV_PCAL_SEC6_V'] = 732
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4268,4329')

NodeIndex['B_SYS_HV_PCAL_SEC6_W'] = 733
SubNodeNames.append('')
ElementNames.append('E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62')
ElementRecordNames.append('vmon,imon,vsetrbk,isetrbk,vmaxrbk,ruprbk,rdnrbk,stat,comms,pwonoff,vset,iset,trip,rup,rdn,vmax,type')
ElementRecordTypes.append('bigsub,ao,ao,ao,ao,ao,ao,ao,ao,ao,bo,ao,ao,ao,ao,ao,ao,ai')
ElementRecordFlags.append('#PB,#GR,#GR,,#PD,#PD,,')
NodeRecordNames.append('')
NodeRecordTypes.append('')
ElementRange.append('4330,4391')

