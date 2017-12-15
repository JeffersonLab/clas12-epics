#!/usr/bin/env python
import os,sys,epics,subprocess,datetime

PVNAMES='''
2;scaler_calc1;FcupCurrent
3;IPM2C21A;2c21Current
4;IPM2H01;2h01Current
5;B_SACLAYTGT:TT_T;TgtTemp
6;B_SACLAYTGT:PT_T;TgtPress
7;scalerS8b;DownL
8;scalerS9b;DownR
9;scalerS10b;DownT
10;scalerS11b;DownB
11;scalerS12b;MidL
12;scalerS13b;MidR
13;scalerS14b;MidT
14;scalerS15b;MidB
15;B_DET_FTC_FADC:avg;FTC:AvgCounts
16;B_DET_ECAL_TDC_SEC1_UI_E01-E12:avg;ECAL:UI:SEC1:1-12:avg
17;B_DET_ECAL_TDC_SEC2_UI_E01-E12:avg;ECAL:UI:SEC2:1-12:avg
18;B_DET_ECAL_TDC_SEC3_UI_E01-E12:avg;ECAL:UI:SEC3:1-12:avg
19;B_DET_ECAL_TDC_SEC4_UI_E01-E12:avg;ECAL:UI:SEC4:1-12:avg
20;B_DET_ECAL_TDC_SEC5_UI_E01-E12:avg;ECAL:UI:SEC5:1-12:avg
21;B_DET_ECAL_TDC_SEC6_UI_E01-E12:avg;ECAL:UI:SEC6:1-12:avg
22;B_DET_PCAL_TDC_SEC1_U_E01-E12:avg;PCAL:U:SEC1:1-12:avg
23;B_DET_PCAL_TDC_SEC2_U_E01-E12:avg;PCAL:U:SEC2:1-12:avg
24;B_DET_PCAL_TDC_SEC3_U_E01-E12:avg;PCAL:U:SEC3:1-12:avg
26;B_DET_PCAL_TDC_SEC4_U_E01-E12:avg;PCAL:U:SEC4:1-12:avg
27;B_DET_PCAL_TDC_SEC5_U_E01-E12:avg;PCAL:U:SEC5:1-12:avg
28;B_DET_PCAL_TDC_SEC6_U_E01-E12:avg;PCAL:U:SEC6:1-12:avg
29;B_DET_FTOF_TDC_SEC1_PANEL1B_E01-E06:avg;FTOF:1B:SEC1:1-6:avg
30;B_DET_FTOF_TDC_SEC2_PANEL1B_E01-E06:avg;FTOF:1B:SEC2:1-6:avg
31;B_DET_FTOF_TDC_SEC3_PANEL1B_E01-E06:avg;FTOF:1B:SEC3:1-6:avg
32;B_DET_FTOF_TDC_SEC4_PANEL1B_E01-E06:avg;FTOF:1B:SEC4:1-6:avg
33;B_DET_FTOF_TDC_SEC5_PANEL1B_E01-E06:avg;FTOF:1B:SEC5:1-6:avg
34;B_DET_FTOF_TDC_SEC6_PANEL1B_E01-E06:avg;FTOF:1B:SEC6:1-6:avg
35;B_DET_CTOF_FADC_U:avg;CTOF-U:avg
36;B_DET_CTOF_FADC_D:avg;CTOF-D:avg
37;B_DET_DC_HV_SEC1_R1_SL1_S:imon;DCHVCurrentS1SL1Sense
38;B_DET_DC_HV_SEC2_R1_SL1_S:imon;DCHVCurrentS2SL1Sense
39;B_DET_DC_HV_SEC3_R1_SL1_S:imon;DCHVCurrentS3SL1Sense
40;B_DET_DC_HV_SEC4_R1_SL1_S:imon;DCHVCurrentS4SL1Sense
41;B_DET_DC_HV_SEC5_R1_SL1_S:imon;DCHVCurrentS5SL1Sense
42;B_DET_DC_HV_SEC6_R1_SL1_S:imon;DCHVCurrentS6SL1Sense
43;B_DET_DC_HV_SEC1_R1_SL2_S:imon;DCHVCurrentS1SL2Sense
44;B_DET_DC_HV_SEC2_R1_SL2_S:imon;DCHVCurrentS2SL2Sense
45;B_DET_DC_HV_SEC3_R1_SL2_S:imon;DCHVCurrentS3SL2Sense
46;B_DET_DC_HV_SEC4_R1_SL2_S:imon;DCHVCurrentS4SL2Sense
47;B_DET_DC_HV_SEC5_R1_SL2_S:imon;DCHVCurrentS5SL2Sense
48;B_DET_DC_HV_SEC6_R1_SL2_S:imon;DCHVCurrentS6SL2Sense
37;B_DET_DC_HV_SEC1_R1_SL1_S:imon;DCHVCurrentS1SL1Field
38;B_DET_DC_HV_SEC2_R1_SL1_F:imon;DCHVCurrentS2SL1Field
39;B_DET_DC_HV_SEC3_R1_SL1_F:imon;DCHVCurrentS3SL1Field
40;B_DET_DC_HV_SEC4_R1_SL1_F:imon;DCHVCurrentS4SL1Field
41;B_DET_DC_HV_SEC5_R1_SL1_F:imon;DCHVCurrentS5SL1Field
42;B_DET_DC_HV_SEC6_R1_SL1_F:imon;DCHVCurrentS6SL1Field
43;B_DET_DC_HV_SEC1_R1_SL2_F:imon;DCHVCurrentS1SL2Field
44;B_DET_DC_HV_SEC2_R1_SL2_F:imon;DCHVCurrentS2SL2Field
45;B_DET_DC_HV_SEC3_R1_SL2_F:imon;DCHVCurrentS3SL2Field
46;B_DET_DC_HV_SEC4_R1_SL2_F:imon;DCHVCurrentS4SL2Field
47;B_DET_DC_HV_SEC5_R1_SL2_F:imon;DCHVCurrentS5SL2Field
48;B_DET_DC_HV_SEC6_R1_SL2_F:imon;DCHVCurrentS6SL2Field
49;B_SOL:MPS:I_ZFCT;SolenoidCurrent
50;B_DET_BMT_HV_SEC1_L1_STRIP:imon;BMT_SEC1_L1
51;B_DET_BMT_HV_SEC1_L2_STRIP:imon;BMT_SEC1_L2
52;B_DET_BMT_HV_SEC1_L3_STRIP:imon;BMT_SEC1_L3
53;B_DET_BMT_HV_SEC1_L4_STRIP:imon;BMT_SEC1_L4
54;B_DET_BMT_HV_SEC1_L5_STRIP:imon;BMT_SEC1_L5
55;B_DET_BMT_HV_SEC1_L6_STRIP:imon;BMT_SEC1_L6
56;B_DET_BMT_HV_SEC2_L1_STRIP:imon;BMT_SEC2_L1
57;B_DET_BMT_HV_SEC2_L2_STRIP:imon;BMT_SEC2_L2
58;B_DET_BMT_HV_SEC2_L3_STRIP:imon;BMT_SEC2_L3
59;B_DET_BMT_HV_SEC2_L4_STRIP:imon;BMT_SEC2_L4
60;B_DET_BMT_HV_SEC2_L5_STRIP:imon;BMT_SEC2_L5
61;B_DET_BMT_HV_SEC2_L6_STRIP:imon;BMT_SEC2_L6
62;B_DET_BMT_HV_SEC3_L1_STRIP:imon;BMT_SEC3_L1
63;B_DET_BMT_HV_SEC3_L2_STRIP:imon;BMT_SEC3_L2
64;B_DET_BMT_HV_SEC3_L3_STRIP:imon;BMT_SEC3_L3
65;B_DET_BMT_HV_SEC3_L4_STRIP:imon;BMT_SEC3_L4
66;B_DET_BMT_HV_SEC3_L5_STRIP:imon;BMT_SEC3_L5
67;B_DET_BMT_HV_SEC3_L6_STRIP:imon;BMT_SEC3_L6
68;B_DET_FMT_HV_IN_L1_STRIP:imon;FMT_IN_L1
69;B_DET_FMT_HV_IN_L2_STRIP:imon;FMT_IN_L2
70;B_DET_FMT_HV_IN_L3_STRIP:imon;FMT_IN_L3
71;B_DET_FMT_HV_IN_L4_STRIP:imon;FMT_IN_L4
72;B_DET_FMT_HV_IN_L5_STRIP:imon;FMT_IN_L5
73;B_DET_FMT_HV_IN_L6_STRIP:imon;FMT_IN_L6
74;B_DET_FMT_HV_OUT_L1_STRIP:imon;FMT_OUT_L1
75;B_DET_FMT_HV_OUT_L2_STRIP:imon;FMT_OUT_L2
76;B_DET_FMT_HV_OUT_L3_STRIP:imon;FMT_OUT_L3
77;B_DET_FMT_HV_OUT_L4_STRIP:imon;FMT_OUT_L4
78;B_DET_FMT_HV_OUT_L5_STRIP:imon;FMT_OUT_L5
79;B_DET_FMT_HV_OUT_L6_STRIP:imon;FMT_OUT_L6
'''

LOGBOOK='HBLOG'
LOGENTRY='/cs/certified/apps/logentrycli/PRO/bin/logentry'
OUTSTUB=os.getenv('HOME')+'/lumiscan/lumiscan'

PVS,TABLE=[],[]

def getPrettyTime():
  pt=str(datetime.datetime.now())
  pt=pt.split('.')[0].replace(' ','_')
  return pt

FILENAME=OUTSTUB+'_'+getPrettyTime()+'.txt'

def loadPVs():
  for row in PVNAMES.split():
    row=row.replace(' ','')
    cols=row.strip().split(';')
    number=cols.pop(0)
    name=cols.pop(0)
    name=name.replace(' ','')
    desc=' '.join(cols)
    PVS.append({'name':name,'pv':epics.pv.PV(name),'desc':desc})

def printTable(file=None):
  if not file: file=sys.stdout
  print >> file, '%19s'%'Time',
  for pv in PVS:
    fmt='%%%ds'%(len(pv['desc'])+1)
    print >> file, fmt%pv['desc'],
  print >> file
  for row in TABLE:
    print >> file, '%19s'%row[0],
    for icol in range(1,len(row)):
      fmt='%%%d.3e'%(len(PVS[icol-1]['desc'])+1)
      print >> file, fmt%row[icol],
    print >> file
  print >> file

def takeSnapshot():
  vals=[getPrettyTime()]
  for pv in PVS: vals.append(pv['pv'].get())
  TABLE.append(vals)
  if len(TABLE)>1e3:
    print 'Exiting.  Table is too big.'
    printTable()
    sys.exit()

def writeTableToFile():
  oo=open(FILENAME,'w+')
  printTable(oo)
  oo.close()
  print 'Data table is here: '+oo.name
  return FILENAME

def makeLogEntry():
  cmd=[LOGENTRY,'-l',LOGBOOK,'-t','CLAS12 Luminosity Scan','-a',FILENAME,'-b',FILENAME]
  pp=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  out,err = pp.communicate()
  if out: print out
  if err: print err

#############################################

loadPVs()

while True:
  takeSnapshot()
  printTable(None)
  writeTableToFile()
  print 'Press Return to take next snapshot and append table.'
  print 'Press L and then Return to write table to file, send to logbook, and quit.'
  print 'Press Q and then Return to write table to file and quit.'
  print 'Filename is '+FILENAME
  userInput=raw_input()
  if userInput=='L':
    makeLogEntry()
    sys.exit()
  if userInput=='Q':
    sys.exit()


