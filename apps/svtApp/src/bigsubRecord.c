#include <dbCommon.h>

#ifndef INCmenuYesNoH
#define INCmenuYesNoH
typedef enum {
	menuYesNoNO,
	menuYesNoYES
}menuYesNo;
#endif /*INCmenuYesNoH*/

#ifndef INCmenuSimmH
#define INCmenuSimmH
typedef enum {
	menuSimmNO,
	menuSimmYES,
	menuSimmRAW
}menuSimm;
#endif /*INCmenuSimmH*/

#ifndef INCmenuScanH
#define INCmenuScanH
typedef enum {
	menuScanPassive,
	menuScanEvent,
	menuScanI_O_Intr,
	menuScan10_second,
	menuScan5_second,
	menuScan2_second,
	menuScan1_second,
	menuScan_5_second,
	menuScan_2_second,
	menuScan_1_second
}menuScan;
#endif /*INCmenuScanH*/

#ifndef INCmenuPriorityH
#define INCmenuPriorityH
typedef enum {
	menuPriorityLOW,
	menuPriorityMEDIUM,
	menuPriorityHIGH
}menuPriority;
#endif /*INCmenuPriorityH*/

#ifndef INCmenuPiniH
#define INCmenuPiniH
typedef enum {
	menuPiniNO,
	menuPiniYES,
	menuPiniRUN,
	menuPiniRUNNING,
	menuPiniPAUSE,
	menuPiniPAUSED
}menuPini;
#endif /*INCmenuPiniH*/

#ifndef INCmenuOmslH
#define INCmenuOmslH
typedef enum {
	menuOmslsupervisory,
	menuOmslclosed_loop
}menuOmsl;
#endif /*INCmenuOmslH*/

#ifndef INCmenuIvoaH
#define INCmenuIvoaH
typedef enum {
	menuIvoaContinue_normally,
	menuIvoaDon_t_drive_outputs,
	menuIvoaSet_output_to_IVOV
}menuIvoa;
#endif /*INCmenuIvoaH*/

#ifndef INCmenuFtypeH
#define INCmenuFtypeH
typedef enum {
	menuFtypeSTRING,
	menuFtypeCHAR,
	menuFtypeUCHAR,
	menuFtypeSHORT,
	menuFtypeUSHORT,
	menuFtypeLONG,
	menuFtypeULONG,
	menuFtypeFLOAT,
	menuFtypeDOUBLE,
	menuFtypeENUM
}menuFtype;
#endif /*INCmenuFtypeH*/

#ifndef INCmenuCompressH
#define INCmenuCompressH
typedef enum {
	menuCompressN_to_1_First_Value,
	menuCompressN_to_1_Low_Value,
	menuCompressN_to_1_High_Value,
	menuCompressN_to_1_Average
}menuCompress;
#endif /*INCmenuCompressH*/

#ifndef INCmenuAlarmStatH
#define INCmenuAlarmStatH
typedef enum {
	menuAlarmStatNO_ALARM,
	menuAlarmStatREAD,
	menuAlarmStatWRITE,
	menuAlarmStatHIHI,
	menuAlarmStatHIGH,
	menuAlarmStatLOLO,
	menuAlarmStatLOW,
	menuAlarmStatSTATE,
	menuAlarmStatCOS,
	menuAlarmStatCOMM,
	menuAlarmStatTIMEOUT,
	menuAlarmStatHWLIMIT,
	menuAlarmStatCALC,
	menuAlarmStatSCAN,
	menuAlarmStatLINK,
	menuAlarmStatSOFT,
	menuAlarmStatBAD_SUB,
	menuAlarmStatUDF,
	menuAlarmStatDISABLE,
	menuAlarmStatSIMM,
	menuAlarmStatREAD_ACCESS,
	menuAlarmStatWRITE_ACCESS
}menuAlarmStat;
#endif /*INCmenuAlarmStatH*/

#ifndef INCmenuAlarmSevrH
#define INCmenuAlarmSevrH
typedef enum {
	menuAlarmSevrNO_ALARM,
	menuAlarmSevrMINOR,
	menuAlarmSevrMAJOR,
	menuAlarmSevrINVALID
}menuAlarmSevr;
#endif /*INCmenuAlarmSevrH*/
#ifndef INCbigsubH
#define INCbigsubH
typedef struct bigsubRecord {
	char		name[61];	/* Record Name */
	char		desc[41];	/* Descriptor */
	char		asg[29];	/* Access Security Group */
	epicsEnum16	scan;	/* Scan Mechanism */
	epicsEnum16	pini;	/* Process at iocInit */
	epicsInt16	phas;	/* Scan Phase */
	epicsInt16	evnt;	/* Event Number */
	epicsInt16	tse;	/* Time Stamp Event */
	DBLINK		tsel;	/* Time Stamp Link */
	epicsEnum16	dtyp;	/* Device Type */
	epicsInt16	disv;	/* Disable Value */
	epicsInt16	disa;	/* Disable */
	DBLINK		sdis;	/* Scanning Disable */
	epicsMutexId	mlok;	/* Monitor lock */
	ELLLIST		mlis;	/* Monitor List */
	epicsUInt8	disp;	/* Disable putField */
	epicsUInt8	proc;	/* Force Processing */
	epicsEnum16	stat;	/* Alarm Status */
	epicsEnum16	sevr;	/* Alarm Severity */
	epicsEnum16	nsta;	/* New Alarm Status */
	epicsEnum16	nsev;	/* New Alarm Severity */
	epicsEnum16	acks;	/* Alarm Ack Severity */
	epicsEnum16	ackt;	/* Alarm Ack Transient */
	epicsEnum16	diss;	/* Disable Alarm Sevrty */
	epicsUInt8	lcnt;	/* Lock Count */
	epicsUInt8	pact;	/* Record active */
	epicsUInt8	putf;	/* dbPutField process */
	epicsUInt8	rpro;	/* Reprocess  */
	struct asgMember *asp;	/* Access Security Pvt */
	struct putNotify *ppn;	/* addr of PUTNOTIFY */
	struct putNotifyRecord *ppnr;	/* pputNotifyRecord */
	struct scan_element *spvt;	/* Scan Private */
	struct rset	*rset;	/* Address of RSET */
	struct dset	*dset;	/* DSET address */
	void		*dpvt;	/* Device Private */
	struct dbRecordType *rdes;	/* Address of dbRecordType */
	struct lockRecord *lset;	/* Lock Set */
	epicsEnum16	prio;	/* Scheduling Priority */
	epicsUInt8	tpro;	/* Trace Processing */
	char bkpt;	/* Break Point */
	epicsUInt8	udf;	/* Undefined */
	epicsTimeStamp	time;	/* Time */
	DBLINK		flnk;	/* Forward Process Link */
	epicsFloat64	val;	/* Result */
	char		inam[16];	/* Init Routine Name */
	char		snam[16];	/* Subroutine Name */
	void *		sadr;	/* Subroutine Address */
	epicsInt16	styp;	/* Subr symbol type */
	DBLINK		inpa;	/* Input A */
	DBLINK		inpb;	/* Input B */
	DBLINK		inpc;	/* Input C */
	DBLINK		inpd;	/* Input D */
	DBLINK		inpe;	/* Input E */
	DBLINK		inpf;	/* Input F */
	DBLINK		inpg;	/* Input G */
	DBLINK		inph;	/* Input H */
	DBLINK		inpi;	/* Input I */
	DBLINK		inpj;	/* Input J */
	DBLINK		inpk;	/* Input K */
	DBLINK		inpl;	/* Input L */
	DBLINK		inpm;	/* Input M */
	DBLINK		inpn;	/* Input N */
	DBLINK		inpo;	/* Input O */
	DBLINK		inpp;	/* Input P */
	DBLINK		inpq;	/* Input Q */
	DBLINK		inpr;	/* Input R */
	DBLINK		inps;	/* Input S */
	DBLINK		inpt;	/* Input T */
	char		egu[16];	/* Units Name */
	epicsFloat32	hopr;	/* High Operating Rng */
	epicsFloat32	lopr;	/* Low Operating Range */
	epicsFloat32	hihi;	/* Hihi Alarm Limit */
	epicsFloat32	lolo;	/* Lolo Alarm Limit */
	epicsFloat32	high;	/* High Alarm Limit */
	epicsFloat32	low;	/* Low Alarm Limit */
	epicsInt16	prec;	/* Display Precision */
	epicsEnum16	brsv;	/* Bad Return Severity */
	epicsEnum16	hhsv;	/* Hihi Severity */
	epicsEnum16	llsv;	/* Lolo Severity */
	epicsEnum16	hsv;	/* High Severity */
	epicsEnum16	lsv;	/* Low Severity */
	epicsFloat64	hyst;	/* Alarm Deadband */
	epicsFloat64	adel;	/* Archive Deadband */
	epicsFloat64	mdel;	/* Monitor Deadband */
	epicsFloat64	a;	/* Value of Input A */
	epicsFloat64	b;	/* Value of Input B */
	epicsFloat64	c;	/* Value of Input C */
	epicsFloat64	d;	/* Value of Input D */
	epicsFloat64	e;	/* Value of Input E */
	epicsFloat64	f;	/* Value of Input F */
	epicsFloat64	g;	/* Value of Input G */
	epicsFloat64	h;	/* Value of Input H */
	epicsFloat64	i;	/* Value of Input I */
	epicsFloat64	j;	/* Value of Input J */
	epicsFloat64	k;	/* Value of Input K */
	epicsFloat64	l;	/* Value of Input L */
	epicsFloat64	m;	/* Value of Input M */
	epicsFloat64	n;	/* Value of Input N */
	epicsFloat64	o;	/* Value of Input O */
	epicsFloat64	p;	/* Value of Input P */
	epicsFloat64	q;	/* Value of Input Q */
	epicsFloat64	r;	/* Value of Input R */
	epicsFloat64	s;	/* Value of Input S */
	epicsFloat64	t;	/* Value of Input T */
	epicsFloat64	la;	/* Prev Value of A */
	epicsFloat64	lb;	/* Prev Value of B */
	epicsFloat64	lc;	/* Prev Value of C */
	epicsFloat64	ld;	/* Prev Value of D */
	epicsFloat64	le;	/* Prev Value of E */
	epicsFloat64	lf;	/* Prev Value of F */
	epicsFloat64	lg;	/* Prev Value of G */
	epicsFloat64	lh;	/* Prev Value of H */
	epicsFloat64	li;	/* Prev Value of I */
	epicsFloat64	lj;	/* Prev Value of J */
	epicsFloat64	lk;	/* Prev Value of K */
	epicsFloat64	ll;	/* Prev Value of L */
	epicsFloat64	lm;	/* Prev Value of M */
	epicsFloat64	ln;	/* Prev Value of N */
	epicsFloat64	lo;	/* Prev Value of O */
	epicsFloat64	lp;	/* Prev Value of P */
	epicsFloat64	lq;	/* Prev Value of Q */
	epicsFloat64	lr;	/* Prev Value of R */
	epicsFloat64	ls;	/* Prev Value of S */
	epicsFloat64	lt;	/* Prev Value of T */
	epicsFloat64	nla;	/* Non-link input A */
	epicsFloat64	nlb;	/* Non-link input B */
	epicsFloat64	nlc;	/* Non-link input C */
	epicsFloat64	nld;	/* Non-link input D */
	epicsFloat64	nle;	/* Non-link input E */
	epicsFloat64	nlf;	/* Non-link input F */
	epicsFloat64	nlg;	/* Non-link input G */
	epicsFloat64	nlh;	/* Non-link input H */
	epicsFloat64	nli;	/* Non-link input I */
	epicsFloat64	nlj;	/* Non-link input J */
	epicsFloat64	nlk;	/* Non-link input K */
	epicsFloat64	nll;	/* Non-link input L */
	epicsFloat64	nlm;	/* Non-link input M */
	epicsFloat64	nln;	/* Non-link input N */
	epicsFloat64	nlo;	/* Non-link input O */
	epicsFloat64	nlp;	/* Non-link input P */
	epicsFloat64	nlq;	/* Non-link input Q */
	epicsFloat64	nlr;	/* Non-link input R */
	epicsFloat64	nls;	/* Non-link input S */
	epicsFloat64	nlt;	/* Non-link input T */
	epicsFloat64	lnla;	/* Prev Value of NLA */
	epicsFloat64	lnlb;	/* Prev Value of NLB */
	epicsFloat64	lnlc;	/* Prev Value of NLC */
	epicsFloat64	lnld;	/* Prev Value of NLD */
	epicsFloat64	lnle;	/* Prev Value of NLE */
	epicsFloat64	lnlf;	/* Prev Value of NLF */
	epicsFloat64	lnlg;	/* Prev Value of NLG */
	epicsFloat64	lnlh;	/* Prev Value of NLH */
	epicsFloat64	lnli;	/* Prev Value of NLI */
	epicsFloat64	lnlj;	/* Prev Value of NLJ */
	epicsFloat64	lnlk;	/* Prev Value of NLK */
	epicsFloat64	lnll;	/* Prev Value of NLL */
	epicsFloat64	lnlm;	/* Prev Value of NLM */
	epicsFloat64	lnln;	/* Prev Value of NLN */
	epicsFloat64	lnlo;	/* Prev Value of NLO */
	epicsFloat64	lnlp;	/* Prev Value of NLP */
	epicsFloat64	lnlq;	/* Prev Value of NLQ */
	epicsFloat64	lnlr;	/* Prev Value of NLR */
	epicsFloat64	lnls;	/* Prev Value of NLS */
	epicsFloat64	lnlt;	/* Prev Value of NLT */
	epicsFloat64	lalm;	/* Last Value Alarmed */
	epicsFloat64	alst;	/* Last Value Archived */
	epicsFloat64	mlst;	/* Last Value Monitored */
	DBLINK		outa;	/* Output Link A */
	DBLINK		outb;	/* Output Link B */
	DBLINK		outc;	/* Output Link C */
	DBLINK		outd;	/* Output Link D */
	DBLINK		oute;	/* Output Link E */
	DBLINK		outf;	/* Output Link F */
	DBLINK		outg;	/* Output Link G */
	DBLINK		outh;	/* Output Link H */
	epicsFloat64	oa;	/* Output Value A */
	epicsFloat64	ob;	/* Output Value B */
	epicsFloat64	oc;	/* Output Value C */
	epicsFloat64	od;	/* Output Value D */
	epicsFloat64	oe;	/* Output Value E */
	epicsFloat64	of;	/* Output Value F */
	epicsFloat64	og;	/* Output Value G */
	epicsFloat64	oh;	/* Output Value H */
} bigsubRecord;
#define bigsubRecordNAME	0
#define bigsubRecordDESC	1
#define bigsubRecordASG	2
#define bigsubRecordSCAN	3
#define bigsubRecordPINI	4
#define bigsubRecordPHAS	5
#define bigsubRecordEVNT	6
#define bigsubRecordTSE	7
#define bigsubRecordTSEL	8
#define bigsubRecordDTYP	9
#define bigsubRecordDISV	10
#define bigsubRecordDISA	11
#define bigsubRecordSDIS	12
#define bigsubRecordMLOK	13
#define bigsubRecordMLIS	14
#define bigsubRecordDISP	15
#define bigsubRecordPROC	16
#define bigsubRecordSTAT	17
#define bigsubRecordSEVR	18
#define bigsubRecordNSTA	19
#define bigsubRecordNSEV	20
#define bigsubRecordACKS	21
#define bigsubRecordACKT	22
#define bigsubRecordDISS	23
#define bigsubRecordLCNT	24
#define bigsubRecordPACT	25
#define bigsubRecordPUTF	26
#define bigsubRecordRPRO	27
#define bigsubRecordASP	28
#define bigsubRecordPPN	29
#define bigsubRecordPPNR	30
#define bigsubRecordSPVT	31
#define bigsubRecordRSET	32
#define bigsubRecordDSET	33
#define bigsubRecordDPVT	34
#define bigsubRecordRDES	35
#define bigsubRecordLSET	36
#define bigsubRecordPRIO	37
#define bigsubRecordTPRO	38
#define bigsubRecordBKPT	39
#define bigsubRecordUDF	40
#define bigsubRecordTIME	41
#define bigsubRecordFLNK	42
#define bigsubRecordVAL	43
#define bigsubRecordINAM	44
#define bigsubRecordSNAM	45
#define bigsubRecordSADR	46
#define bigsubRecordSTYP	47
#define bigsubRecordINPA	48
#define bigsubRecordINPB	49
#define bigsubRecordINPC	50
#define bigsubRecordINPD	51
#define bigsubRecordINPE	52
#define bigsubRecordINPF	53
#define bigsubRecordINPG	54
#define bigsubRecordINPH	55
#define bigsubRecordINPI	56
#define bigsubRecordINPJ	57
#define bigsubRecordINPK	58
#define bigsubRecordINPL	59
#define bigsubRecordINPM	60
#define bigsubRecordINPN	61
#define bigsubRecordINPO	62
#define bigsubRecordINPP	63
#define bigsubRecordINPQ	64
#define bigsubRecordINPR	65
#define bigsubRecordINPS	66
#define bigsubRecordINPT	67
#define bigsubRecordEGU	68
#define bigsubRecordHOPR	69
#define bigsubRecordLOPR	70
#define bigsubRecordHIHI	71
#define bigsubRecordLOLO	72
#define bigsubRecordHIGH	73
#define bigsubRecordLOW	74
#define bigsubRecordPREC	75
#define bigsubRecordBRSV	76
#define bigsubRecordHHSV	77
#define bigsubRecordLLSV	78
#define bigsubRecordHSV	79
#define bigsubRecordLSV	80
#define bigsubRecordHYST	81
#define bigsubRecordADEL	82
#define bigsubRecordMDEL	83
#define bigsubRecordA	84
#define bigsubRecordB	85
#define bigsubRecordC	86
#define bigsubRecordD	87
#define bigsubRecordE	88
#define bigsubRecordF	89
#define bigsubRecordG	90
#define bigsubRecordH	91
#define bigsubRecordI	92
#define bigsubRecordJ	93
#define bigsubRecordK	94
#define bigsubRecordL	95
#define bigsubRecordM	96
#define bigsubRecordN	97
#define bigsubRecordO	98
#define bigsubRecordP	99
#define bigsubRecordQ	100
#define bigsubRecordR	101
#define bigsubRecordS	102
#define bigsubRecordT	103
#define bigsubRecordLA	104
#define bigsubRecordLB	105
#define bigsubRecordLC	106
#define bigsubRecordLD	107
#define bigsubRecordLE	108
#define bigsubRecordLF	109
#define bigsubRecordLG	110
#define bigsubRecordLH	111
#define bigsubRecordLI	112
#define bigsubRecordLJ	113
#define bigsubRecordLK	114
#define bigsubRecordLL	115
#define bigsubRecordLM	116
#define bigsubRecordLN	117
#define bigsubRecordLO	118
#define bigsubRecordLP	119
#define bigsubRecordLQ	120
#define bigsubRecordLR	121
#define bigsubRecordLS	122
#define bigsubRecordLT	123
#define bigsubRecordNLA	124
#define bigsubRecordNLB	125
#define bigsubRecordNLC	126
#define bigsubRecordNLD	127
#define bigsubRecordNLE	128
#define bigsubRecordNLF	129
#define bigsubRecordNLG	130
#define bigsubRecordNLH	131
#define bigsubRecordNLI	132
#define bigsubRecordNLJ	133
#define bigsubRecordNLK	134
#define bigsubRecordNLL	135
#define bigsubRecordNLM	136
#define bigsubRecordNLN	137
#define bigsubRecordNLO	138
#define bigsubRecordNLP	139
#define bigsubRecordNLQ	140
#define bigsubRecordNLR	141
#define bigsubRecordNLS	142
#define bigsubRecordNLT	143
#define bigsubRecordLNLA	144
#define bigsubRecordLNLB	145
#define bigsubRecordLNLC	146
#define bigsubRecordLNLD	147
#define bigsubRecordLNLE	148
#define bigsubRecordLNLF	149
#define bigsubRecordLNLG	150
#define bigsubRecordLNLH	151
#define bigsubRecordLNLI	152
#define bigsubRecordLNLJ	153
#define bigsubRecordLNLK	154
#define bigsubRecordLNLL	155
#define bigsubRecordLNLM	156
#define bigsubRecordLNLN	157
#define bigsubRecordLNLO	158
#define bigsubRecordLNLP	159
#define bigsubRecordLNLQ	160
#define bigsubRecordLNLR	161
#define bigsubRecordLNLS	162
#define bigsubRecordLNLT	163
#define bigsubRecordLALM	164
#define bigsubRecordALST	165
#define bigsubRecordMLST	166
#define bigsubRecordOUTA	167
#define bigsubRecordOUTB	168
#define bigsubRecordOUTC	169
#define bigsubRecordOUTD	170
#define bigsubRecordOUTE	171
#define bigsubRecordOUTF	172
#define bigsubRecordOUTG	173
#define bigsubRecordOUTH	174
#define bigsubRecordOA	175
#define bigsubRecordOB	176
#define bigsubRecordOC	177
#define bigsubRecordOD	178
#define bigsubRecordOE	179
#define bigsubRecordOF	180
#define bigsubRecordOG	181
#define bigsubRecordOH	182
#endif /*INCbigsubH*/
#ifdef GEN_SIZE_OFFSET
#ifdef __cplusplus
extern "C" {
#endif
#include <epicsExport.h>
static int bigsubRecordSizeOffset(dbRecordType *pdbRecordType)
{
    bigsubRecord *prec = 0;
  pdbRecordType->papFldDes[0]->size=sizeof(prec->name);
  pdbRecordType->papFldDes[0]->offset=(short)((char *)&prec->name - (char *)prec);
  pdbRecordType->papFldDes[1]->size=sizeof(prec->desc);
  pdbRecordType->papFldDes[1]->offset=(short)((char *)&prec->desc - (char *)prec);
  pdbRecordType->papFldDes[2]->size=sizeof(prec->asg);
  pdbRecordType->papFldDes[2]->offset=(short)((char *)&prec->asg - (char *)prec);
  pdbRecordType->papFldDes[3]->size=sizeof(prec->scan);
  pdbRecordType->papFldDes[3]->offset=(short)((char *)&prec->scan - (char *)prec);
  pdbRecordType->papFldDes[4]->size=sizeof(prec->pini);
  pdbRecordType->papFldDes[4]->offset=(short)((char *)&prec->pini - (char *)prec);
  pdbRecordType->papFldDes[5]->size=sizeof(prec->phas);
  pdbRecordType->papFldDes[5]->offset=(short)((char *)&prec->phas - (char *)prec);
  pdbRecordType->papFldDes[6]->size=sizeof(prec->evnt);
  pdbRecordType->papFldDes[6]->offset=(short)((char *)&prec->evnt - (char *)prec);
  pdbRecordType->papFldDes[7]->size=sizeof(prec->tse);
  pdbRecordType->papFldDes[7]->offset=(short)((char *)&prec->tse - (char *)prec);
  pdbRecordType->papFldDes[8]->size=sizeof(prec->tsel);
  pdbRecordType->papFldDes[8]->offset=(short)((char *)&prec->tsel - (char *)prec);
  pdbRecordType->papFldDes[9]->size=sizeof(prec->dtyp);
  pdbRecordType->papFldDes[9]->offset=(short)((char *)&prec->dtyp - (char *)prec);
  pdbRecordType->papFldDes[10]->size=sizeof(prec->disv);
  pdbRecordType->papFldDes[10]->offset=(short)((char *)&prec->disv - (char *)prec);
  pdbRecordType->papFldDes[11]->size=sizeof(prec->disa);
  pdbRecordType->papFldDes[11]->offset=(short)((char *)&prec->disa - (char *)prec);
  pdbRecordType->papFldDes[12]->size=sizeof(prec->sdis);
  pdbRecordType->papFldDes[12]->offset=(short)((char *)&prec->sdis - (char *)prec);
  pdbRecordType->papFldDes[13]->size=sizeof(prec->mlok);
  pdbRecordType->papFldDes[13]->offset=(short)((char *)&prec->mlok - (char *)prec);
  pdbRecordType->papFldDes[14]->size=sizeof(prec->mlis);
  pdbRecordType->papFldDes[14]->offset=(short)((char *)&prec->mlis - (char *)prec);
  pdbRecordType->papFldDes[15]->size=sizeof(prec->disp);
  pdbRecordType->papFldDes[15]->offset=(short)((char *)&prec->disp - (char *)prec);
  pdbRecordType->papFldDes[16]->size=sizeof(prec->proc);
  pdbRecordType->papFldDes[16]->offset=(short)((char *)&prec->proc - (char *)prec);
  pdbRecordType->papFldDes[17]->size=sizeof(prec->stat);
  pdbRecordType->papFldDes[17]->offset=(short)((char *)&prec->stat - (char *)prec);
  pdbRecordType->papFldDes[18]->size=sizeof(prec->sevr);
  pdbRecordType->papFldDes[18]->offset=(short)((char *)&prec->sevr - (char *)prec);
  pdbRecordType->papFldDes[19]->size=sizeof(prec->nsta);
  pdbRecordType->papFldDes[19]->offset=(short)((char *)&prec->nsta - (char *)prec);
  pdbRecordType->papFldDes[20]->size=sizeof(prec->nsev);
  pdbRecordType->papFldDes[20]->offset=(short)((char *)&prec->nsev - (char *)prec);
  pdbRecordType->papFldDes[21]->size=sizeof(prec->acks);
  pdbRecordType->papFldDes[21]->offset=(short)((char *)&prec->acks - (char *)prec);
  pdbRecordType->papFldDes[22]->size=sizeof(prec->ackt);
  pdbRecordType->papFldDes[22]->offset=(short)((char *)&prec->ackt - (char *)prec);
  pdbRecordType->papFldDes[23]->size=sizeof(prec->diss);
  pdbRecordType->papFldDes[23]->offset=(short)((char *)&prec->diss - (char *)prec);
  pdbRecordType->papFldDes[24]->size=sizeof(prec->lcnt);
  pdbRecordType->papFldDes[24]->offset=(short)((char *)&prec->lcnt - (char *)prec);
  pdbRecordType->papFldDes[25]->size=sizeof(prec->pact);
  pdbRecordType->papFldDes[25]->offset=(short)((char *)&prec->pact - (char *)prec);
  pdbRecordType->papFldDes[26]->size=sizeof(prec->putf);
  pdbRecordType->papFldDes[26]->offset=(short)((char *)&prec->putf - (char *)prec);
  pdbRecordType->papFldDes[27]->size=sizeof(prec->rpro);
  pdbRecordType->papFldDes[27]->offset=(short)((char *)&prec->rpro - (char *)prec);
  pdbRecordType->papFldDes[28]->size=sizeof(prec->asp);
  pdbRecordType->papFldDes[28]->offset=(short)((char *)&prec->asp - (char *)prec);
  pdbRecordType->papFldDes[29]->size=sizeof(prec->ppn);
  pdbRecordType->papFldDes[29]->offset=(short)((char *)&prec->ppn - (char *)prec);
  pdbRecordType->papFldDes[30]->size=sizeof(prec->ppnr);
  pdbRecordType->papFldDes[30]->offset=(short)((char *)&prec->ppnr - (char *)prec);
  pdbRecordType->papFldDes[31]->size=sizeof(prec->spvt);
  pdbRecordType->papFldDes[31]->offset=(short)((char *)&prec->spvt - (char *)prec);
  pdbRecordType->papFldDes[32]->size=sizeof(prec->rset);
  pdbRecordType->papFldDes[32]->offset=(short)((char *)&prec->rset - (char *)prec);
  pdbRecordType->papFldDes[33]->size=sizeof(prec->dset);
  pdbRecordType->papFldDes[33]->offset=(short)((char *)&prec->dset - (char *)prec);
  pdbRecordType->papFldDes[34]->size=sizeof(prec->dpvt);
  pdbRecordType->papFldDes[34]->offset=(short)((char *)&prec->dpvt - (char *)prec);
  pdbRecordType->papFldDes[35]->size=sizeof(prec->rdes);
  pdbRecordType->papFldDes[35]->offset=(short)((char *)&prec->rdes - (char *)prec);
  pdbRecordType->papFldDes[36]->size=sizeof(prec->lset);
  pdbRecordType->papFldDes[36]->offset=(short)((char *)&prec->lset - (char *)prec);
  pdbRecordType->papFldDes[37]->size=sizeof(prec->prio);
  pdbRecordType->papFldDes[37]->offset=(short)((char *)&prec->prio - (char *)prec);
  pdbRecordType->papFldDes[38]->size=sizeof(prec->tpro);
  pdbRecordType->papFldDes[38]->offset=(short)((char *)&prec->tpro - (char *)prec);
  pdbRecordType->papFldDes[39]->size=sizeof(prec->bkpt);
  pdbRecordType->papFldDes[39]->offset=(short)((char *)&prec->bkpt - (char *)prec);
  pdbRecordType->papFldDes[40]->size=sizeof(prec->udf);
  pdbRecordType->papFldDes[40]->offset=(short)((char *)&prec->udf - (char *)prec);
  pdbRecordType->papFldDes[41]->size=sizeof(prec->time);
  pdbRecordType->papFldDes[41]->offset=(short)((char *)&prec->time - (char *)prec);
  pdbRecordType->papFldDes[42]->size=sizeof(prec->flnk);
  pdbRecordType->papFldDes[42]->offset=(short)((char *)&prec->flnk - (char *)prec);
  pdbRecordType->papFldDes[43]->size=sizeof(prec->val);
  pdbRecordType->papFldDes[43]->offset=(short)((char *)&prec->val - (char *)prec);
  pdbRecordType->papFldDes[44]->size=sizeof(prec->inam);
  pdbRecordType->papFldDes[44]->offset=(short)((char *)&prec->inam - (char *)prec);
  pdbRecordType->papFldDes[45]->size=sizeof(prec->snam);
  pdbRecordType->papFldDes[45]->offset=(short)((char *)&prec->snam - (char *)prec);
  pdbRecordType->papFldDes[46]->size=sizeof(prec->sadr);
  pdbRecordType->papFldDes[46]->offset=(short)((char *)&prec->sadr - (char *)prec);
  pdbRecordType->papFldDes[47]->size=sizeof(prec->styp);
  pdbRecordType->papFldDes[47]->offset=(short)((char *)&prec->styp - (char *)prec);
  pdbRecordType->papFldDes[48]->size=sizeof(prec->inpa);
  pdbRecordType->papFldDes[48]->offset=(short)((char *)&prec->inpa - (char *)prec);
  pdbRecordType->papFldDes[49]->size=sizeof(prec->inpb);
  pdbRecordType->papFldDes[49]->offset=(short)((char *)&prec->inpb - (char *)prec);
  pdbRecordType->papFldDes[50]->size=sizeof(prec->inpc);
  pdbRecordType->papFldDes[50]->offset=(short)((char *)&prec->inpc - (char *)prec);
  pdbRecordType->papFldDes[51]->size=sizeof(prec->inpd);
  pdbRecordType->papFldDes[51]->offset=(short)((char *)&prec->inpd - (char *)prec);
  pdbRecordType->papFldDes[52]->size=sizeof(prec->inpe);
  pdbRecordType->papFldDes[52]->offset=(short)((char *)&prec->inpe - (char *)prec);
  pdbRecordType->papFldDes[53]->size=sizeof(prec->inpf);
  pdbRecordType->papFldDes[53]->offset=(short)((char *)&prec->inpf - (char *)prec);
  pdbRecordType->papFldDes[54]->size=sizeof(prec->inpg);
  pdbRecordType->papFldDes[54]->offset=(short)((char *)&prec->inpg - (char *)prec);
  pdbRecordType->papFldDes[55]->size=sizeof(prec->inph);
  pdbRecordType->papFldDes[55]->offset=(short)((char *)&prec->inph - (char *)prec);
  pdbRecordType->papFldDes[56]->size=sizeof(prec->inpi);
  pdbRecordType->papFldDes[56]->offset=(short)((char *)&prec->inpi - (char *)prec);
  pdbRecordType->papFldDes[57]->size=sizeof(prec->inpj);
  pdbRecordType->papFldDes[57]->offset=(short)((char *)&prec->inpj - (char *)prec);
  pdbRecordType->papFldDes[58]->size=sizeof(prec->inpk);
  pdbRecordType->papFldDes[58]->offset=(short)((char *)&prec->inpk - (char *)prec);
  pdbRecordType->papFldDes[59]->size=sizeof(prec->inpl);
  pdbRecordType->papFldDes[59]->offset=(short)((char *)&prec->inpl - (char *)prec);
  pdbRecordType->papFldDes[60]->size=sizeof(prec->inpm);
  pdbRecordType->papFldDes[60]->offset=(short)((char *)&prec->inpm - (char *)prec);
  pdbRecordType->papFldDes[61]->size=sizeof(prec->inpn);
  pdbRecordType->papFldDes[61]->offset=(short)((char *)&prec->inpn - (char *)prec);
  pdbRecordType->papFldDes[62]->size=sizeof(prec->inpo);
  pdbRecordType->papFldDes[62]->offset=(short)((char *)&prec->inpo - (char *)prec);
  pdbRecordType->papFldDes[63]->size=sizeof(prec->inpp);
  pdbRecordType->papFldDes[63]->offset=(short)((char *)&prec->inpp - (char *)prec);
  pdbRecordType->papFldDes[64]->size=sizeof(prec->inpq);
  pdbRecordType->papFldDes[64]->offset=(short)((char *)&prec->inpq - (char *)prec);
  pdbRecordType->papFldDes[65]->size=sizeof(prec->inpr);
  pdbRecordType->papFldDes[65]->offset=(short)((char *)&prec->inpr - (char *)prec);
  pdbRecordType->papFldDes[66]->size=sizeof(prec->inps);
  pdbRecordType->papFldDes[66]->offset=(short)((char *)&prec->inps - (char *)prec);
  pdbRecordType->papFldDes[67]->size=sizeof(prec->inpt);
  pdbRecordType->papFldDes[67]->offset=(short)((char *)&prec->inpt - (char *)prec);
  pdbRecordType->papFldDes[68]->size=sizeof(prec->egu);
  pdbRecordType->papFldDes[68]->offset=(short)((char *)&prec->egu - (char *)prec);
  pdbRecordType->papFldDes[69]->size=sizeof(prec->hopr);
  pdbRecordType->papFldDes[69]->offset=(short)((char *)&prec->hopr - (char *)prec);
  pdbRecordType->papFldDes[70]->size=sizeof(prec->lopr);
  pdbRecordType->papFldDes[70]->offset=(short)((char *)&prec->lopr - (char *)prec);
  pdbRecordType->papFldDes[71]->size=sizeof(prec->hihi);
  pdbRecordType->papFldDes[71]->offset=(short)((char *)&prec->hihi - (char *)prec);
  pdbRecordType->papFldDes[72]->size=sizeof(prec->lolo);
  pdbRecordType->papFldDes[72]->offset=(short)((char *)&prec->lolo - (char *)prec);
  pdbRecordType->papFldDes[73]->size=sizeof(prec->high);
  pdbRecordType->papFldDes[73]->offset=(short)((char *)&prec->high - (char *)prec);
  pdbRecordType->papFldDes[74]->size=sizeof(prec->low);
  pdbRecordType->papFldDes[74]->offset=(short)((char *)&prec->low - (char *)prec);
  pdbRecordType->papFldDes[75]->size=sizeof(prec->prec);
  pdbRecordType->papFldDes[75]->offset=(short)((char *)&prec->prec - (char *)prec);
  pdbRecordType->papFldDes[76]->size=sizeof(prec->brsv);
  pdbRecordType->papFldDes[76]->offset=(short)((char *)&prec->brsv - (char *)prec);
  pdbRecordType->papFldDes[77]->size=sizeof(prec->hhsv);
  pdbRecordType->papFldDes[77]->offset=(short)((char *)&prec->hhsv - (char *)prec);
  pdbRecordType->papFldDes[78]->size=sizeof(prec->llsv);
  pdbRecordType->papFldDes[78]->offset=(short)((char *)&prec->llsv - (char *)prec);
  pdbRecordType->papFldDes[79]->size=sizeof(prec->hsv);
  pdbRecordType->papFldDes[79]->offset=(short)((char *)&prec->hsv - (char *)prec);
  pdbRecordType->papFldDes[80]->size=sizeof(prec->lsv);
  pdbRecordType->papFldDes[80]->offset=(short)((char *)&prec->lsv - (char *)prec);
  pdbRecordType->papFldDes[81]->size=sizeof(prec->hyst);
  pdbRecordType->papFldDes[81]->offset=(short)((char *)&prec->hyst - (char *)prec);
  pdbRecordType->papFldDes[82]->size=sizeof(prec->adel);
  pdbRecordType->papFldDes[82]->offset=(short)((char *)&prec->adel - (char *)prec);
  pdbRecordType->papFldDes[83]->size=sizeof(prec->mdel);
  pdbRecordType->papFldDes[83]->offset=(short)((char *)&prec->mdel - (char *)prec);
  pdbRecordType->papFldDes[84]->size=sizeof(prec->a);
  pdbRecordType->papFldDes[84]->offset=(short)((char *)&prec->a - (char *)prec);
  pdbRecordType->papFldDes[85]->size=sizeof(prec->b);
  pdbRecordType->papFldDes[85]->offset=(short)((char *)&prec->b - (char *)prec);
  pdbRecordType->papFldDes[86]->size=sizeof(prec->c);
  pdbRecordType->papFldDes[86]->offset=(short)((char *)&prec->c - (char *)prec);
  pdbRecordType->papFldDes[87]->size=sizeof(prec->d);
  pdbRecordType->papFldDes[87]->offset=(short)((char *)&prec->d - (char *)prec);
  pdbRecordType->papFldDes[88]->size=sizeof(prec->e);
  pdbRecordType->papFldDes[88]->offset=(short)((char *)&prec->e - (char *)prec);
  pdbRecordType->papFldDes[89]->size=sizeof(prec->f);
  pdbRecordType->papFldDes[89]->offset=(short)((char *)&prec->f - (char *)prec);
  pdbRecordType->papFldDes[90]->size=sizeof(prec->g);
  pdbRecordType->papFldDes[90]->offset=(short)((char *)&prec->g - (char *)prec);
  pdbRecordType->papFldDes[91]->size=sizeof(prec->h);
  pdbRecordType->papFldDes[91]->offset=(short)((char *)&prec->h - (char *)prec);
  pdbRecordType->papFldDes[92]->size=sizeof(prec->i);
  pdbRecordType->papFldDes[92]->offset=(short)((char *)&prec->i - (char *)prec);
  pdbRecordType->papFldDes[93]->size=sizeof(prec->j);
  pdbRecordType->papFldDes[93]->offset=(short)((char *)&prec->j - (char *)prec);
  pdbRecordType->papFldDes[94]->size=sizeof(prec->k);
  pdbRecordType->papFldDes[94]->offset=(short)((char *)&prec->k - (char *)prec);
  pdbRecordType->papFldDes[95]->size=sizeof(prec->l);
  pdbRecordType->papFldDes[95]->offset=(short)((char *)&prec->l - (char *)prec);
  pdbRecordType->papFldDes[96]->size=sizeof(prec->m);
  pdbRecordType->papFldDes[96]->offset=(short)((char *)&prec->m - (char *)prec);
  pdbRecordType->papFldDes[97]->size=sizeof(prec->n);
  pdbRecordType->papFldDes[97]->offset=(short)((char *)&prec->n - (char *)prec);
  pdbRecordType->papFldDes[98]->size=sizeof(prec->o);
  pdbRecordType->papFldDes[98]->offset=(short)((char *)&prec->o - (char *)prec);
  pdbRecordType->papFldDes[99]->size=sizeof(prec->p);
  pdbRecordType->papFldDes[99]->offset=(short)((char *)&prec->p - (char *)prec);
  pdbRecordType->papFldDes[100]->size=sizeof(prec->q);
  pdbRecordType->papFldDes[100]->offset=(short)((char *)&prec->q - (char *)prec);
  pdbRecordType->papFldDes[101]->size=sizeof(prec->r);
  pdbRecordType->papFldDes[101]->offset=(short)((char *)&prec->r - (char *)prec);
  pdbRecordType->papFldDes[102]->size=sizeof(prec->s);
  pdbRecordType->papFldDes[102]->offset=(short)((char *)&prec->s - (char *)prec);
  pdbRecordType->papFldDes[103]->size=sizeof(prec->t);
  pdbRecordType->papFldDes[103]->offset=(short)((char *)&prec->t - (char *)prec);
  pdbRecordType->papFldDes[104]->size=sizeof(prec->la);
  pdbRecordType->papFldDes[104]->offset=(short)((char *)&prec->la - (char *)prec);
  pdbRecordType->papFldDes[105]->size=sizeof(prec->lb);
  pdbRecordType->papFldDes[105]->offset=(short)((char *)&prec->lb - (char *)prec);
  pdbRecordType->papFldDes[106]->size=sizeof(prec->lc);
  pdbRecordType->papFldDes[106]->offset=(short)((char *)&prec->lc - (char *)prec);
  pdbRecordType->papFldDes[107]->size=sizeof(prec->ld);
  pdbRecordType->papFldDes[107]->offset=(short)((char *)&prec->ld - (char *)prec);
  pdbRecordType->papFldDes[108]->size=sizeof(prec->le);
  pdbRecordType->papFldDes[108]->offset=(short)((char *)&prec->le - (char *)prec);
  pdbRecordType->papFldDes[109]->size=sizeof(prec->lf);
  pdbRecordType->papFldDes[109]->offset=(short)((char *)&prec->lf - (char *)prec);
  pdbRecordType->papFldDes[110]->size=sizeof(prec->lg);
  pdbRecordType->papFldDes[110]->offset=(short)((char *)&prec->lg - (char *)prec);
  pdbRecordType->papFldDes[111]->size=sizeof(prec->lh);
  pdbRecordType->papFldDes[111]->offset=(short)((char *)&prec->lh - (char *)prec);
  pdbRecordType->papFldDes[112]->size=sizeof(prec->li);
  pdbRecordType->papFldDes[112]->offset=(short)((char *)&prec->li - (char *)prec);
  pdbRecordType->papFldDes[113]->size=sizeof(prec->lj);
  pdbRecordType->papFldDes[113]->offset=(short)((char *)&prec->lj - (char *)prec);
  pdbRecordType->papFldDes[114]->size=sizeof(prec->lk);
  pdbRecordType->papFldDes[114]->offset=(short)((char *)&prec->lk - (char *)prec);
  pdbRecordType->papFldDes[115]->size=sizeof(prec->ll);
  pdbRecordType->papFldDes[115]->offset=(short)((char *)&prec->ll - (char *)prec);
  pdbRecordType->papFldDes[116]->size=sizeof(prec->lm);
  pdbRecordType->papFldDes[116]->offset=(short)((char *)&prec->lm - (char *)prec);
  pdbRecordType->papFldDes[117]->size=sizeof(prec->ln);
  pdbRecordType->papFldDes[117]->offset=(short)((char *)&prec->ln - (char *)prec);
  pdbRecordType->papFldDes[118]->size=sizeof(prec->lo);
  pdbRecordType->papFldDes[118]->offset=(short)((char *)&prec->lo - (char *)prec);
  pdbRecordType->papFldDes[119]->size=sizeof(prec->lp);
  pdbRecordType->papFldDes[119]->offset=(short)((char *)&prec->lp - (char *)prec);
  pdbRecordType->papFldDes[120]->size=sizeof(prec->lq);
  pdbRecordType->papFldDes[120]->offset=(short)((char *)&prec->lq - (char *)prec);
  pdbRecordType->papFldDes[121]->size=sizeof(prec->lr);
  pdbRecordType->papFldDes[121]->offset=(short)((char *)&prec->lr - (char *)prec);
  pdbRecordType->papFldDes[122]->size=sizeof(prec->ls);
  pdbRecordType->papFldDes[122]->offset=(short)((char *)&prec->ls - (char *)prec);
  pdbRecordType->papFldDes[123]->size=sizeof(prec->lt);
  pdbRecordType->papFldDes[123]->offset=(short)((char *)&prec->lt - (char *)prec);
  pdbRecordType->papFldDes[124]->size=sizeof(prec->nla);
  pdbRecordType->papFldDes[124]->offset=(short)((char *)&prec->nla - (char *)prec);
  pdbRecordType->papFldDes[125]->size=sizeof(prec->nlb);
  pdbRecordType->papFldDes[125]->offset=(short)((char *)&prec->nlb - (char *)prec);
  pdbRecordType->papFldDes[126]->size=sizeof(prec->nlc);
  pdbRecordType->papFldDes[126]->offset=(short)((char *)&prec->nlc - (char *)prec);
  pdbRecordType->papFldDes[127]->size=sizeof(prec->nld);
  pdbRecordType->papFldDes[127]->offset=(short)((char *)&prec->nld - (char *)prec);
  pdbRecordType->papFldDes[128]->size=sizeof(prec->nle);
  pdbRecordType->papFldDes[128]->offset=(short)((char *)&prec->nle - (char *)prec);
  pdbRecordType->papFldDes[129]->size=sizeof(prec->nlf);
  pdbRecordType->papFldDes[129]->offset=(short)((char *)&prec->nlf - (char *)prec);
  pdbRecordType->papFldDes[130]->size=sizeof(prec->nlg);
  pdbRecordType->papFldDes[130]->offset=(short)((char *)&prec->nlg - (char *)prec);
  pdbRecordType->papFldDes[131]->size=sizeof(prec->nlh);
  pdbRecordType->papFldDes[131]->offset=(short)((char *)&prec->nlh - (char *)prec);
  pdbRecordType->papFldDes[132]->size=sizeof(prec->nli);
  pdbRecordType->papFldDes[132]->offset=(short)((char *)&prec->nli - (char *)prec);
  pdbRecordType->papFldDes[133]->size=sizeof(prec->nlj);
  pdbRecordType->papFldDes[133]->offset=(short)((char *)&prec->nlj - (char *)prec);
  pdbRecordType->papFldDes[134]->size=sizeof(prec->nlk);
  pdbRecordType->papFldDes[134]->offset=(short)((char *)&prec->nlk - (char *)prec);
  pdbRecordType->papFldDes[135]->size=sizeof(prec->nll);
  pdbRecordType->papFldDes[135]->offset=(short)((char *)&prec->nll - (char *)prec);
  pdbRecordType->papFldDes[136]->size=sizeof(prec->nlm);
  pdbRecordType->papFldDes[136]->offset=(short)((char *)&prec->nlm - (char *)prec);
  pdbRecordType->papFldDes[137]->size=sizeof(prec->nln);
  pdbRecordType->papFldDes[137]->offset=(short)((char *)&prec->nln - (char *)prec);
  pdbRecordType->papFldDes[138]->size=sizeof(prec->nlo);
  pdbRecordType->papFldDes[138]->offset=(short)((char *)&prec->nlo - (char *)prec);
  pdbRecordType->papFldDes[139]->size=sizeof(prec->nlp);
  pdbRecordType->papFldDes[139]->offset=(short)((char *)&prec->nlp - (char *)prec);
  pdbRecordType->papFldDes[140]->size=sizeof(prec->nlq);
  pdbRecordType->papFldDes[140]->offset=(short)((char *)&prec->nlq - (char *)prec);
  pdbRecordType->papFldDes[141]->size=sizeof(prec->nlr);
  pdbRecordType->papFldDes[141]->offset=(short)((char *)&prec->nlr - (char *)prec);
  pdbRecordType->papFldDes[142]->size=sizeof(prec->nls);
  pdbRecordType->papFldDes[142]->offset=(short)((char *)&prec->nls - (char *)prec);
  pdbRecordType->papFldDes[143]->size=sizeof(prec->nlt);
  pdbRecordType->papFldDes[143]->offset=(short)((char *)&prec->nlt - (char *)prec);
  pdbRecordType->papFldDes[144]->size=sizeof(prec->lnla);
  pdbRecordType->papFldDes[144]->offset=(short)((char *)&prec->lnla - (char *)prec);
  pdbRecordType->papFldDes[145]->size=sizeof(prec->lnlb);
  pdbRecordType->papFldDes[145]->offset=(short)((char *)&prec->lnlb - (char *)prec);
  pdbRecordType->papFldDes[146]->size=sizeof(prec->lnlc);
  pdbRecordType->papFldDes[146]->offset=(short)((char *)&prec->lnlc - (char *)prec);
  pdbRecordType->papFldDes[147]->size=sizeof(prec->lnld);
  pdbRecordType->papFldDes[147]->offset=(short)((char *)&prec->lnld - (char *)prec);
  pdbRecordType->papFldDes[148]->size=sizeof(prec->lnle);
  pdbRecordType->papFldDes[148]->offset=(short)((char *)&prec->lnle - (char *)prec);
  pdbRecordType->papFldDes[149]->size=sizeof(prec->lnlf);
  pdbRecordType->papFldDes[149]->offset=(short)((char *)&prec->lnlf - (char *)prec);
  pdbRecordType->papFldDes[150]->size=sizeof(prec->lnlg);
  pdbRecordType->papFldDes[150]->offset=(short)((char *)&prec->lnlg - (char *)prec);
  pdbRecordType->papFldDes[151]->size=sizeof(prec->lnlh);
  pdbRecordType->papFldDes[151]->offset=(short)((char *)&prec->lnlh - (char *)prec);
  pdbRecordType->papFldDes[152]->size=sizeof(prec->lnli);
  pdbRecordType->papFldDes[152]->offset=(short)((char *)&prec->lnli - (char *)prec);
  pdbRecordType->papFldDes[153]->size=sizeof(prec->lnlj);
  pdbRecordType->papFldDes[153]->offset=(short)((char *)&prec->lnlj - (char *)prec);
  pdbRecordType->papFldDes[154]->size=sizeof(prec->lnlk);
  pdbRecordType->papFldDes[154]->offset=(short)((char *)&prec->lnlk - (char *)prec);
  pdbRecordType->papFldDes[155]->size=sizeof(prec->lnll);
  pdbRecordType->papFldDes[155]->offset=(short)((char *)&prec->lnll - (char *)prec);
  pdbRecordType->papFldDes[156]->size=sizeof(prec->lnlm);
  pdbRecordType->papFldDes[156]->offset=(short)((char *)&prec->lnlm - (char *)prec);
  pdbRecordType->papFldDes[157]->size=sizeof(prec->lnln);
  pdbRecordType->papFldDes[157]->offset=(short)((char *)&prec->lnln - (char *)prec);
  pdbRecordType->papFldDes[158]->size=sizeof(prec->lnlo);
  pdbRecordType->papFldDes[158]->offset=(short)((char *)&prec->lnlo - (char *)prec);
  pdbRecordType->papFldDes[159]->size=sizeof(prec->lnlp);
  pdbRecordType->papFldDes[159]->offset=(short)((char *)&prec->lnlp - (char *)prec);
  pdbRecordType->papFldDes[160]->size=sizeof(prec->lnlq);
  pdbRecordType->papFldDes[160]->offset=(short)((char *)&prec->lnlq - (char *)prec);
  pdbRecordType->papFldDes[161]->size=sizeof(prec->lnlr);
  pdbRecordType->papFldDes[161]->offset=(short)((char *)&prec->lnlr - (char *)prec);
  pdbRecordType->papFldDes[162]->size=sizeof(prec->lnls);
  pdbRecordType->papFldDes[162]->offset=(short)((char *)&prec->lnls - (char *)prec);
  pdbRecordType->papFldDes[163]->size=sizeof(prec->lnlt);
  pdbRecordType->papFldDes[163]->offset=(short)((char *)&prec->lnlt - (char *)prec);
  pdbRecordType->papFldDes[164]->size=sizeof(prec->lalm);
  pdbRecordType->papFldDes[164]->offset=(short)((char *)&prec->lalm - (char *)prec);
  pdbRecordType->papFldDes[165]->size=sizeof(prec->alst);
  pdbRecordType->papFldDes[165]->offset=(short)((char *)&prec->alst - (char *)prec);
  pdbRecordType->papFldDes[166]->size=sizeof(prec->mlst);
  pdbRecordType->papFldDes[166]->offset=(short)((char *)&prec->mlst - (char *)prec);
  pdbRecordType->papFldDes[167]->size=sizeof(prec->outa);
  pdbRecordType->papFldDes[167]->offset=(short)((char *)&prec->outa - (char *)prec);
  pdbRecordType->papFldDes[168]->size=sizeof(prec->outb);
  pdbRecordType->papFldDes[168]->offset=(short)((char *)&prec->outb - (char *)prec);
  pdbRecordType->papFldDes[169]->size=sizeof(prec->outc);
  pdbRecordType->papFldDes[169]->offset=(short)((char *)&prec->outc - (char *)prec);
  pdbRecordType->papFldDes[170]->size=sizeof(prec->outd);
  pdbRecordType->papFldDes[170]->offset=(short)((char *)&prec->outd - (char *)prec);
  pdbRecordType->papFldDes[171]->size=sizeof(prec->oute);
  pdbRecordType->papFldDes[171]->offset=(short)((char *)&prec->oute - (char *)prec);
  pdbRecordType->papFldDes[172]->size=sizeof(prec->outf);
  pdbRecordType->papFldDes[172]->offset=(short)((char *)&prec->outf - (char *)prec);
  pdbRecordType->papFldDes[173]->size=sizeof(prec->outg);
  pdbRecordType->papFldDes[173]->offset=(short)((char *)&prec->outg - (char *)prec);
  pdbRecordType->papFldDes[174]->size=sizeof(prec->outh);
  pdbRecordType->papFldDes[174]->offset=(short)((char *)&prec->outh - (char *)prec);
  pdbRecordType->papFldDes[175]->size=sizeof(prec->oa);
  pdbRecordType->papFldDes[175]->offset=(short)((char *)&prec->oa - (char *)prec);
  pdbRecordType->papFldDes[176]->size=sizeof(prec->ob);
  pdbRecordType->papFldDes[176]->offset=(short)((char *)&prec->ob - (char *)prec);
  pdbRecordType->papFldDes[177]->size=sizeof(prec->oc);
  pdbRecordType->papFldDes[177]->offset=(short)((char *)&prec->oc - (char *)prec);
  pdbRecordType->papFldDes[178]->size=sizeof(prec->od);
  pdbRecordType->papFldDes[178]->offset=(short)((char *)&prec->od - (char *)prec);
  pdbRecordType->papFldDes[179]->size=sizeof(prec->oe);
  pdbRecordType->papFldDes[179]->offset=(short)((char *)&prec->oe - (char *)prec);
  pdbRecordType->papFldDes[180]->size=sizeof(prec->of);
  pdbRecordType->papFldDes[180]->offset=(short)((char *)&prec->of - (char *)prec);
  pdbRecordType->papFldDes[181]->size=sizeof(prec->og);
  pdbRecordType->papFldDes[181]->offset=(short)((char *)&prec->og - (char *)prec);
  pdbRecordType->papFldDes[182]->size=sizeof(prec->oh);
  pdbRecordType->papFldDes[182]->offset=(short)((char *)&prec->oh - (char *)prec);
    pdbRecordType->rec_size = sizeof(*prec);
    return(0);
}
epicsExportRegistrar(bigsubRecordSizeOffset);
#ifdef __cplusplus
}
#endif
#endif /*GEN_SIZE_OFFSET*/
