#include "ellLib.h"
#include "epicsMutex.h"
#include "link.h"
#include "epicsTime.h"
#include "epicsTypes.h"
#ifndef INCxxxH
#define INCxxxH
typedef struct xxxRecord {
	char		name[61]; /*Record Name*/
	char		desc[29]; /*Descriptor*/
	char		asg[29]; /*Access Security Group*/
	epicsEnum16	scan;	/*Scan Mechanism*/
	epicsEnum16	pini;	/*Process at iocInit*/
	short		phas;	/*Scan Phase*/
	short		evnt;	/*Event Number*/
	short		tse;	/*Time Stamp Event*/
	DBLINK		tsel;	/*Time Stamp Link*/
	epicsEnum16	dtyp;	/*Device Type*/
	short		disv;	/*Disable Value*/
	short		disa;	/*Disable*/
	DBLINK		sdis;	/*Scanning Disable*/
	epicsMutexId	mlok;	/*Monitor lock*/
	ELLLIST		mlis;	/*Monitor List*/
	unsigned char	disp;	/*Disable putField*/
	unsigned char	proc;	/*Force Processing*/
	epicsEnum16	stat;	/*Alarm Status*/
	epicsEnum16	sevr;	/*Alarm Severity*/
	epicsEnum16	nsta;	/*New Alarm Status*/
	epicsEnum16	nsev;	/*New Alarm Severity*/
	epicsEnum16	acks;	/*Alarm Ack Severity*/
	epicsEnum16	ackt;	/*Alarm Ack Transient*/
	epicsEnum16	diss;	/*Disable Alarm Sevrty*/
	unsigned char	lcnt;	/*Lock Count*/
	unsigned char	pact;	/*Record active*/
	unsigned char	putf;	/*dbPutField process*/
	unsigned char	rpro;	/*Reprocess */
	void		*asp;	/*Access Security Pvt*/
	struct putNotify *ppn;	/*addr of PUTNOTIFY*/
	struct putNotifyRecord *ppnr;	/*pputNotifyRecord*/
	struct scan_element *spvt;	/*Scan Private*/
	struct rset	*rset;	/*Address of RSET*/
	struct dset	*dset;	/*DSET address*/
	void		*dpvt;	/*Device Private*/
	struct dbRecordType *rdes;	/*Address of dbRecordType*/
	struct lockRecord *lset;	/*Lock Set*/
	epicsEnum16	prio;	/*Scheduling Priority*/
	unsigned char	tpro;	/*Trace Processing*/
	char bkpt;	/*Break Point*/
	unsigned char	udf;	/*Undefined*/
	epicsTimeStamp	time;	/*Time*/
	DBLINK		flnk;	/*Forward Process Link*/
	double		val;	/*Current EGU Value*/
	DBLINK		inp;	/*Input Specification*/
	short		prec;	/*Display Precision*/
	char		egu[16]; /*Engineering Units*/
	float		hopr;	/*High Operating Range*/
	float		lopr;	/*Low Operating Range*/
	float		hihi;	/*Hihi Alarm Limit*/
	float		lolo;	/*Lolo Alarm Limit*/
	float		high;	/*High Alarm Limit*/
	float		low;	/*Low Alarm Limit*/
	epicsEnum16	hhsv;	/*Hihi Severity*/
	epicsEnum16	llsv;	/*Lolo Severity*/
	epicsEnum16	hsv;	/*High Severity*/
	epicsEnum16	lsv;	/*Low Severity*/
	double		hyst;	/*Alarm Deadband*/
	double		adel;	/*Archive Deadband*/
	double		mdel;	/*Monitor Deadband*/
	double		lalm;	/*Last Value Alarmed*/
	double		alst;	/*Last Value Archived*/
	double		mlst;	/*Last Val Monitored*/
} xxxRecord;
#define xxxRecordNAME	0
#define xxxRecordDESC	1
#define xxxRecordASG	2
#define xxxRecordSCAN	3
#define xxxRecordPINI	4
#define xxxRecordPHAS	5
#define xxxRecordEVNT	6
#define xxxRecordTSE	7
#define xxxRecordTSEL	8
#define xxxRecordDTYP	9
#define xxxRecordDISV	10
#define xxxRecordDISA	11
#define xxxRecordSDIS	12
#define xxxRecordMLOK	13
#define xxxRecordMLIS	14
#define xxxRecordDISP	15
#define xxxRecordPROC	16
#define xxxRecordSTAT	17
#define xxxRecordSEVR	18
#define xxxRecordNSTA	19
#define xxxRecordNSEV	20
#define xxxRecordACKS	21
#define xxxRecordACKT	22
#define xxxRecordDISS	23
#define xxxRecordLCNT	24
#define xxxRecordPACT	25
#define xxxRecordPUTF	26
#define xxxRecordRPRO	27
#define xxxRecordASP	28
#define xxxRecordPPN	29
#define xxxRecordPPNR	30
#define xxxRecordSPVT	31
#define xxxRecordRSET	32
#define xxxRecordDSET	33
#define xxxRecordDPVT	34
#define xxxRecordRDES	35
#define xxxRecordLSET	36
#define xxxRecordPRIO	37
#define xxxRecordTPRO	38
#define xxxRecordBKPT	39
#define xxxRecordUDF	40
#define xxxRecordTIME	41
#define xxxRecordFLNK	42
#define xxxRecordVAL	43
#define xxxRecordINP	44
#define xxxRecordPREC	45
#define xxxRecordEGU	46
#define xxxRecordHOPR	47
#define xxxRecordLOPR	48
#define xxxRecordHIHI	49
#define xxxRecordLOLO	50
#define xxxRecordHIGH	51
#define xxxRecordLOW	52
#define xxxRecordHHSV	53
#define xxxRecordLLSV	54
#define xxxRecordHSV	55
#define xxxRecordLSV	56
#define xxxRecordHYST	57
#define xxxRecordADEL	58
#define xxxRecordMDEL	59
#define xxxRecordLALM	60
#define xxxRecordALST	61
#define xxxRecordMLST	62
#endif /*INCxxxH*/
#ifdef GEN_SIZE_OFFSET
#ifdef __cplusplus
extern "C" {
#endif
#include <epicsExport.h>
static int xxxRecordSizeOffset(dbRecordType *pdbRecordType)
{
    xxxRecord *prec = 0;
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
  pdbRecordType->papFldDes[44]->size=sizeof(prec->inp);
  pdbRecordType->papFldDes[44]->offset=(short)((char *)&prec->inp - (char *)prec);
  pdbRecordType->papFldDes[45]->size=sizeof(prec->prec);
  pdbRecordType->papFldDes[45]->offset=(short)((char *)&prec->prec - (char *)prec);
  pdbRecordType->papFldDes[46]->size=sizeof(prec->egu);
  pdbRecordType->papFldDes[46]->offset=(short)((char *)&prec->egu - (char *)prec);
  pdbRecordType->papFldDes[47]->size=sizeof(prec->hopr);
  pdbRecordType->papFldDes[47]->offset=(short)((char *)&prec->hopr - (char *)prec);
  pdbRecordType->papFldDes[48]->size=sizeof(prec->lopr);
  pdbRecordType->papFldDes[48]->offset=(short)((char *)&prec->lopr - (char *)prec);
  pdbRecordType->papFldDes[49]->size=sizeof(prec->hihi);
  pdbRecordType->papFldDes[49]->offset=(short)((char *)&prec->hihi - (char *)prec);
  pdbRecordType->papFldDes[50]->size=sizeof(prec->lolo);
  pdbRecordType->papFldDes[50]->offset=(short)((char *)&prec->lolo - (char *)prec);
  pdbRecordType->papFldDes[51]->size=sizeof(prec->high);
  pdbRecordType->papFldDes[51]->offset=(short)((char *)&prec->high - (char *)prec);
  pdbRecordType->papFldDes[52]->size=sizeof(prec->low);
  pdbRecordType->papFldDes[52]->offset=(short)((char *)&prec->low - (char *)prec);
  pdbRecordType->papFldDes[53]->size=sizeof(prec->hhsv);
  pdbRecordType->papFldDes[53]->offset=(short)((char *)&prec->hhsv - (char *)prec);
  pdbRecordType->papFldDes[54]->size=sizeof(prec->llsv);
  pdbRecordType->papFldDes[54]->offset=(short)((char *)&prec->llsv - (char *)prec);
  pdbRecordType->papFldDes[55]->size=sizeof(prec->hsv);
  pdbRecordType->papFldDes[55]->offset=(short)((char *)&prec->hsv - (char *)prec);
  pdbRecordType->papFldDes[56]->size=sizeof(prec->lsv);
  pdbRecordType->papFldDes[56]->offset=(short)((char *)&prec->lsv - (char *)prec);
  pdbRecordType->papFldDes[57]->size=sizeof(prec->hyst);
  pdbRecordType->papFldDes[57]->offset=(short)((char *)&prec->hyst - (char *)prec);
  pdbRecordType->papFldDes[58]->size=sizeof(prec->adel);
  pdbRecordType->papFldDes[58]->offset=(short)((char *)&prec->adel - (char *)prec);
  pdbRecordType->papFldDes[59]->size=sizeof(prec->mdel);
  pdbRecordType->papFldDes[59]->offset=(short)((char *)&prec->mdel - (char *)prec);
  pdbRecordType->papFldDes[60]->size=sizeof(prec->lalm);
  pdbRecordType->papFldDes[60]->offset=(short)((char *)&prec->lalm - (char *)prec);
  pdbRecordType->papFldDes[61]->size=sizeof(prec->alst);
  pdbRecordType->papFldDes[61]->offset=(short)((char *)&prec->alst - (char *)prec);
  pdbRecordType->papFldDes[62]->size=sizeof(prec->mlst);
  pdbRecordType->papFldDes[62]->offset=(short)((char *)&prec->mlst - (char *)prec);
    pdbRecordType->rec_size = sizeof(*prec);
    return(0);
}
epicsExportRegistrar(xxxRecordSizeOffset);
#ifdef __cplusplus
}
#endif
#endif /*GEN_SIZE_OFFSET*/
