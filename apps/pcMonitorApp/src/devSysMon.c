/* devSysMon.c Miroslaw Dach SLS/PSI 16.10.2004*/
/* originally created for EPICS 3.14.1 */
/* For EPICS 3.14.7 compatibility it was introduced */
/* #include "epicsExport.h" */
/* and epicsExportAddress function for every device support */  
/* This device support reads the uptime from /proc/uptime and converts it 
   to human readable format */
/* it examines also following files to obtain CPU load, load avg and mem info
   /proc/loadavg
   /proc/stat
   /proc/meminfo
   */

#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#include "alarm.h"
#include "cvtTable.h"
#include "dbDefs.h"
#include "dbAccess.h"
#include "recGbl.h"
#include "recSup.h"
#include "devSup.h"
#include "link.h"
#include "stringinRecord.h"
#include "aiRecord.h"

#include <sys/types.h>
#include <unistd.h>
#include <fcntl.h>
#include "/usr/include/linux/version.h"

#include <sys/time.h>
#include <time.h>

#include <sys/socket.h>
#include <sys/ioctl.h>
#include <net/if.h>
#include <netdb.h>

#include <sys/utsname.h>
/* in vesrion 3.14.7 #include "epicsExport.h" */
#include "epicsExport.h"


#define DEBUG 0


static int get_uptime(void);           /* get formated time from /proc/uptime */
static void format_uptime(char *str1); /* set formated up time in str1 */
static double getAvgLoad(char * parm); /* get the avg load for parm= 1min ora 5min ora 15min */

/*------------------------- Create the dset for devUptime ------------------*/
static long init_record_s();
static long read_uptime();
struct {
    long            number;
    DEVSUPFUN       report;
    DEVSUPFUN       init;
    DEVSUPFUN       init_record;
    DEVSUPFUN       get_ioint_info;
    DEVSUPFUN       read;
}devUpTime={
    5,
    NULL,
    NULL,
    init_record_s,
    NULL,
    read_uptime,
};
epicsExportAddress(dset,devUpTime); 


static long init_record_s(pStringIn)
    struct stringinRecord    *pStringIn;
{
    if(recGblInitConstantLink(&pStringIn->inp,DBF_STRING,&pStringIn->val))
        pStringIn->udf = FALSE;
    return(0);
}


static long read_uptime(pStringIn)
    struct stringinRecord    *pStringIn;
{
    /*     long status; */
    struct timeval        iheure;
    int    iCurTime=0;
    int    iUpTime=0;

    struct vmeio *pvmeio = &pStringIn->inp.value.vmeio;

    /* status = dbGetLink(&(pStringIn->inp),DBF_STRING, &(pStringIn->val),0,0); */
    /*If return was succesful then set undefined false*/
    /* sprintf(pStringIn->val,"ala %d",get_uptime()); */
    if(!strcmp(pvmeio->parm,"CURTIME")){

        gettimeofday(&iheure,NULL);
        sprintf(pStringIn->val,"%.16s",&(ctime((time_t *)&iheure.tv_sec))[0]);

    }
    else if(!strcmp(pvmeio->parm,"BOOTIME")){
        gettimeofday(&iheure,NULL);
        iCurTime=iheure.tv_sec;
        iUpTime=get_uptime();
        iCurTime=iCurTime-iUpTime;
        sprintf(pStringIn->val,"%.16s",&(ctime((time_t *)&iCurTime))[0]);
    }
    else if(!strcmp(pvmeio->parm,"UPTIME")){
        format_uptime(pStringIn->val);
    }
    /* if(!status) */  pStringIn->udf = FALSE;
    return(0);
}

/*-----------------  get uptime in seconds -----------------------*/

int get_uptime(void){

    if (DEBUG) fprintf(stderr,"enter get_uptime\n");

    char str_seconds[80];  
    FILE *proc_file;
    int int_seconds;



    if((proc_file=fopen("/proc/uptime","r"))==NULL)
    { fprintf(stderr,"Cannot open /proc/uptime for reading!\n");
        return 0; /*before  exit(127); */
    } 

    fscanf(proc_file,"%s",str_seconds);   
    int_seconds=strtol(str_seconds,NULL,10);

    fclose(proc_file);


    return int_seconds;

}/* get_uptime */

void format_uptime(char *str1){
    int curr,min,hour,day;
    //int sec;

    curr=get_uptime();

    day=curr/86400;
    curr=curr%86400;
    hour=curr/3600;
    curr=curr%3600;
    min=curr/60;
    //sec=curr%60;
    if(day==0)
        sprintf(str1,"%02d:%02d",hour,min);
    else if (day==1)
        sprintf(str1,"%02d day %02d:%02d",day,hour,min);
    else
        sprintf(str1,"%02d days %02d:%02d",day,hour,min);

    if (DEBUG) fprintf(stderr,"exit get_uptime\n");
}

/*---------------------------  get the AVG load ------------------------------------*/

static long init_record_ai();
static long read_avg_load();
struct {
    long            number;
    DEVSUPFUN       report;
    DEVSUPFUN       init;
    DEVSUPFUN       init_record_ai;
    DEVSUPFUN       get_ioint_info;
    DEVSUPFUN       read_ai;
    DEVSUPFUN       special_linconv;
}devAvgLoad={
    6,
    NULL,
    NULL,
    init_record_ai,
    NULL,
    read_avg_load,
    NULL
};

epicsExportAddress(dset,devAvgLoad);

static long init_record_ai(pAiIn)
    struct aiRecord    *pAiIn;
{
    if(recGblInitConstantLink(&pAiIn->inp,DBF_DOUBLE,&pAiIn->val))
        pAiIn->udf = FALSE;
    return(0);
}


static long read_avg_load(pAiIn)
    struct aiRecord    *pAiIn;
{

    long status=0;

    struct vmeio *pvmeio = &pAiIn->inp.value.vmeio;
    /* status = dbGetLink(&(pAiIn->inp),DBF_DOUBLE, &(pAiIn->val),0,0); */
    /*If return was succesful then set undefined false*/  

    pAiIn->val=getAvgLoad(pvmeio->parm);

    if(!status) pAiIn->udf = FALSE;
    return(2); /* no convertion fron rval to val */
}


double getAvgLoad(char * parm){

    if (DEBUG) fprintf(stderr,"enter getAvgLoad\n");

    /* FILE *proc_file;
       double avg1min=0;
       double avg5min=0;
       double avg15min=0;
       char str1[30]="";
       char str2[30]=""; */
    double val=0;

    double avg[3];

    if(getloadavg(avg,sizeof(avg))<0)
    { fprintf(stderr,"load avearage was unobtainable.\n");
        return val; /* before exit(127); */
    } 

    /* if((proc_file=fopen("/proc/loadavg","r"))==NULL)
       { fprintf(stderr,"Cannot open /proc/loadavg for reading!\n");
       return val; 
       } 

       fscanf(proc_file,"%lf %lf %lf %s %s",&avg1min,&avg5min,&avg15min,str1,str2); */


    if(!strcmp(parm,"1min")){
        val=avg[0];
        /* val=avg1min; */
    }
    else if(!strcmp(parm,"5min")){
        val=avg[1];
        /* val=avg5min;*/
    }	
    else{
        val=avg[2];
        /* val=avg15min;*/
    } 


    if (DEBUG) fprintf(stderr,"exit getAvgLoad\n");

    /* fclose(proc_file);*/
    return val;
}

/*-------------------------------------------------------------------*/
/*        CPU and MEMory usage functions                             */
/*-------------------------------------------------------------------*/

#define BAD_OPEN_MESSAGE					\
    "Error: /proc must be mounted\n"				\
"  To mount /proc at boot you need an /etc/fstab line like:\n"	\
"      /proc   /proc   proc    defaults\n"			\
"  In the meantime, mount /proc /proc -t proc\n"


#define STAT_FILE    "/proc/stat"
static int stat_fd = -1;
#define MEMINFO_FILE "/proc/meminfo"
static int meminfo_fd = -1;
static int iFile2BufStstus = -1; 
static char buf[2048];
//static char buf[1024];
/* int show_memory = 1;    show memory summary */
/*        iFile2BufStstus = -1;                                   \
          return -1; before _exit(1); 	      		\ */

#define FILE_TO_BUF(filename, fd) do{				\
    static int n;						\
    iFile2BufStstus = 0;                                        \
    if (fd == -1 && (fd = open(filename, O_RDONLY)) == -1) {	\
        fprintf(stderr, BAD_OPEN_MESSAGE);			\
        close(fd);						\
        iFile2BufStstus = -1;                                   \
        return 0; /* before _exit(1); */       		\
    }								\
    lseek(fd, 0L, SEEK_SET);					\
    if ((n = read(fd, buf, sizeof buf - 1)) < 0) {		\
        perror(filename);					\
        close(fd);						\
        fd = -1;						\
        return 0;						\
    }								\
    buf[n] = '\0';						\
}while(0)

#define SET_IF_DESIRED(x,y)  if(x) *(x) = (y)	/* evals 'x' twice */
#define LINUX_VERSION(x,y,z)   (0x10000*(x) + 0x100*(y) + z)

#define JT unsigned long
int four_cpu_numbers(JT *uret, JT *nret, JT *sret, JT *iret) {
    static JT u, n, s, i;
    JT user_j, nice_j, sys_j, idle_j;
    int iStatus=0;

    FILE_TO_BUF(STAT_FILE,stat_fd);
    if (iFile2BufStstus == -1)
        return (-1);
    sscanf(buf, "cpu %lu %lu %lu %lu", &user_j, &nice_j, &sys_j, &idle_j);

    if(user_j>=u) {
        SET_IF_DESIRED(uret, user_j-u);
    }
    else{
        SET_IF_DESIRED(uret, u-user_j);
        iStatus=1;
    }

    if(nice_j>=n){
        SET_IF_DESIRED(nret, nice_j-n);
    }
    else{
        SET_IF_DESIRED(nret, n-nice_j);
        iStatus=1;
    }

    if(sys_j>=s){
        SET_IF_DESIRED(sret,  sys_j-s);
    }
    else{
        SET_IF_DESIRED(sret,  s-sys_j);
        iStatus=1;
    }

    if(idle_j>=i){
        SET_IF_DESIRED(iret, idle_j-i);
    }
    else{
        SET_IF_DESIRED(iret, i-idle_j);
        iStatus=1;
    }

    u=user_j;
    n=nice_j;
    s=sys_j;
    i=idle_j;

    return iStatus;
}
#undef JT

#define MAX_ROW 3	/* these are a little liberal for flexibility */
#define MAX_COL 7

enum meminfo_row { meminfo_main = 0,
    meminfo_swap };


enum meminfo_col { meminfo_total = 0, meminfo_used, meminfo_free,
    meminfo_shared, meminfo_buffers, meminfo_cached
};


unsigned  long **meminfo(void){

    if (DEBUG) fprintf(stderr,"enter meminfo\n");

    static unsigned long *row[MAX_ROW + 1];		/* row pointers */
    static unsigned long num[MAX_ROW * MAX_COL];	/* number storage */
    char *p;
    char fieldbuf[12];		/* bigger than any field name or size in kb */
    int i, j, k, l;
    int linux_version_code;


    linux_version_code=LINUX_VERSION_CODE;
    FILE_TO_BUF(MEMINFO_FILE,meminfo_fd);

    if (DEBUG) fprintf(stderr,"1 meminfo\n");

    if (iFile2BufStstus == -1)
        return NULL; 
    if (!row[0])				/* init ptrs 1st time through */
        for (i=0; i < MAX_ROW; i++)		/* std column major order: */
            row[i] = num + MAX_COL*i;		/* A[i][j] = A + COLS*i + j */
    p = buf;
    for (i=0; i < MAX_ROW; i++)			/* zero unassigned fields */
        for (j=0; j < MAX_COL; j++)
            row[i][j] = 0;
    if (linux_version_code < LINUX_VERSION(2,0,0)) {
        for (i=0; i < MAX_ROW && *p; i++) {                /* loop over rows */
            while(*p && !isdigit(*p)) p++;          /* skip chars until a digit */
            for (j=0; j < MAX_COL && *p; j++) {     /* scanf column-by-column */
                l = sscanf(p, "%lu%n", row[i] + j, &k);
                p += k;                             /* step over used buffer */
                if (*p == '\n' || l < 1)            /* end of line/buffer */
                    break;
            }
        }
    }
    else {
        if (DEBUG) fprintf(stderr,"2 meminfo\n");
        while(*p) {
            //fprintf(stderr,fieldbuf);
            //fprintf(stderr,"\n");
            //fprintf(stderr,p);
            //fprintf(stderr,"\n");
            sscanf(p,"%11s%n",fieldbuf,&k);
            if(!strcmp(fieldbuf,"MemTotal:")) {
                if (DEBUG) fprintf(stderr,"A meminfo\n");
                p+=k;
                sscanf(p," %lu",&(row[meminfo_main][meminfo_total]));
                row[meminfo_main][meminfo_total]<<=10;
                while(*p++ != '\n');
            }
            else if(!strcmp(fieldbuf,"MemFree:")) {
                if (DEBUG) fprintf(stderr,"B meminfo\n");
                p+=k;
                sscanf(p," %lu",&(row[meminfo_main][meminfo_free]));
                row[meminfo_main][meminfo_free]<<=10;
                while(*p++ != '\n');
            }
            else if(!strcmp(fieldbuf,"MemShared:")) {
                if (DEBUG) fprintf(stderr,"C meminfo\n");
                p+=k;
                sscanf(p," %lu",&(row[meminfo_main][meminfo_shared]));
                row[meminfo_main][meminfo_shared]<<=10;
                while(*p++ != '\n');
            }
            else if(!strcmp(fieldbuf,"Buffers:")) {
                if (DEBUG) fprintf(stderr,"D meminfo\n");
                p+=k;
                sscanf(p," %lu",&(row[meminfo_main][meminfo_buffers]));
                row[meminfo_main][meminfo_buffers]<<=10;
                while(*p++ != '\n');
            }
            else if(!strcmp(fieldbuf,"Cached:")) {
                if (DEBUG) fprintf(stderr,"E meminfo\n");
                p+=k;
                sscanf(p," %lu",&(row[meminfo_main][meminfo_cached]));
                row[meminfo_main][meminfo_cached]<<=10;
                while(*p++ != '\n');
            }
            else if(!strcmp(fieldbuf,"SwapTotal:")) {
                if (DEBUG) fprintf(stderr,"F meminfo\n");
                p+=k;
                sscanf(p," %lu",&(row[meminfo_swap][meminfo_total]));
                row[meminfo_swap][meminfo_total]<<=10;
                while(*p++ != '\n');
            }
            else if(!strcmp(fieldbuf,"SwapFree:")) {
                if (DEBUG) fprintf(stderr,"G meminfo\n");
                p+=k;
                sscanf(p," %lu",&(row[meminfo_swap][meminfo_free]));
                row[meminfo_swap][meminfo_free]<<=10;
                while(*p++ != '\n');
            }
            else {
                if (DEBUG) fprintf(stderr,"\nH meminfo\n");
                if (DEBUG) fprintf(stderr,p);
                while(*p++ != '\n'); /* ignore lines we don't understand */
            }
        }		
        if (DEBUG) fprintf(stderr,"3 meminfo\n");
        row[meminfo_swap][meminfo_used]=row[meminfo_swap][meminfo_total]-row[meminfo_swap][meminfo_free];
        row[meminfo_main][meminfo_used]=row[meminfo_main][meminfo_total]-row[meminfo_main][meminfo_free];
    }
    if (DEBUG) fprintf(stderr,"exit meminfo\n");
    return row;					/* NULL return ==> error */
}

/*------------------------------------------------------------*/
/*         CPU record specyfication                           */
/*------------------------------------------------------------*/

static long init_record_aiCPU();
static long read_CPU_load();
struct {
    long            number;
    DEVSUPFUN       report;
    DEVSUPFUN       init;
    DEVSUPFUN       init_record_ai;
    DEVSUPFUN       get_ioint_info;
    DEVSUPFUN       read_ai;
    DEVSUPFUN       special_linconv;
}devCPULoad={
    6,
    NULL,
    NULL,
    init_record_aiCPU,
    NULL,
    read_CPU_load,
    NULL
};

epicsExportAddress(dset,devCPULoad);

static long init_record_aiCPU(pAiIn)
    struct aiRecord    *pAiIn;
{
    if(recGblInitConstantLink(&pAiIn->inp,DBF_DOUBLE,&pAiIn->val))
        pAiIn->udf = FALSE;
    /* pthread_mutex_init(&readCPUmutex,NULL); */
    return(0);
}

static float  _system_ticks = 0, _user_ticks = 0, _nice_ticks = 0, _idle_ticks = 0;

static long read_CPU_load(pAiIn)
    struct aiRecord    *pAiIn;
{
    if (DEBUG) fprintf(stderr,"enter read_CPU_load\n");

    long status=0;
    unsigned long system_ticks = 0, user_ticks = 0, nice_ticks = 0, idle_ticks = 0;

    int iStatus=0;
    unsigned long sum=0;
    /* double       dSum=0;
       float        fIdle=0;
       double       dV1;
       double       dV2;
       double       dV3;
       double       dV4; */

    struct vmeio *pvmeio = &pAiIn->inp.value.vmeio;
    /* status = dbGetLink(&(pAiIn->inp),DBF_DOUBLE, &(pAiIn->val),0,0); */
    /*If return was succesful then set undefined false*/  

    /* pthread_mutex_lock(&readCPUmutex); */
    if(!strcmp(pvmeio->parm,"PROC")){
        iStatus=four_cpu_numbers(&user_ticks,&nice_ticks,&system_ticks,&idle_ticks);
        if ( iStatus == -1)
            return (2);

        /*if(iStatus==1){
          printf("prev: idle %.2f nice %.2f system %.2f use %.2f \n",_idle_ticks,_nice_ticks,_system_ticks,_user_ticks);
          } */

        sum = user_ticks+nice_ticks+system_ticks+idle_ticks;
        if (sum !=0  ){
            _user_ticks   = (float)((double)((double)(user_ticks   * 100.0) / (double)sum));
            _system_ticks = (float)((double)((double)(system_ticks * 100.0) / (double)sum));
            _nice_ticks   = (float)((double)((double)(nice_ticks   * 100.0) / (double)sum));
            _idle_ticks   = (float)((double)((double)(idle_ticks   * 100.0) / (double)sum)); 

            /*if(iStatus==1){
              printf("new: idle %.2f nice %.2f system %.2f use %.2f \n",_idle_ticks,_nice_ticks,_system_ticks,_user_ticks);
              }*/

            if(_idle_ticks>201) {
                fprintf(stderr,"CPU load: Wrong Calculation\n");
                /*  dSum=(double)user_ticks+(double)nice_ticks+(double)system_ticks+(double)idle_ticks;
                    printf("dSum %f\n",dSum);
                    dV1=user_ticks;
                    dV2=nice_ticks;
                    dV3=system_ticks;
                    dV4=idle_ticks;
                    dSum=dV1+dV2+dV3+dV4;
                    printf("dSum2 %f idleTicks %f %f %f %f %f\n",dSum,(dV4/dSum)*100.0, (dV4*100.0)/dSum,_user_ticks,_system_ticks,_nice_ticks);
                    printf("idle %lu nice %lu system %lu use %lu \n",idle_ticks,nice_ticks,system_ticks,user_ticks);
                    fIdle=(float)((double)((((double)idle_ticks)   * 100.0) /(double) sum));
                    printf("sum %lu sumd %f idle1 %lu idle2 %lu ilded %lu idlef %f\n", sum,dSum,(unsigned long)((idle_ticks  / dSum)*100.0),(unsigned long)(idle_ticks ),(unsigned long)((idle_ticks   * 100)/dSum),fIdle); */
            }

        }/* if sum !=0 */
    }

    /* printf("CPU states:"
       " %2ld.%ld%% user, %2ld.%ld%% system,"
       " %2ld.%ld%% nice, %2ld.%ld%% idle",
       user_ticks / 10UL, user_ticks % 10UL,
       system_ticks / 10UL, system_ticks % 10UL,
       nice_ticks / 10UL, nice_ticks % 10UL,
       idle_ticks / 10UL, idle_ticks % 10UL); */


    if(!strcmp(pvmeio->parm,"IDLE"))
        pAiIn->val=_idle_ticks;
    else if (!strcmp(pvmeio->parm,"NICE"))
        pAiIn->val=_nice_ticks;
    else if (!strcmp(pvmeio->parm,"SYSTEM"))
        pAiIn->val=_system_ticks;
    else if (!strcmp(pvmeio->parm,"USER"))
        pAiIn->val=_user_ticks;
    else
        pAiIn->val=_idle_ticks;

    if(!status) pAiIn->udf = FALSE;
    /* pthread_mutex_unlock(&readCPUmutex); */
    if (DEBUG) fprintf(stderr,"exit read_CPU_load\n");
    return(2); /* no convertion fron rval to val */
}



/*------------------------------------------------------------*/
/*         MEM record specyfication                           */
/*------------------------------------------------------------*/

static long init_record_aiMEM();
static long read_MEM_load();
struct {
    long            number;
    DEVSUPFUN       report;
    DEVSUPFUN       init;
    DEVSUPFUN       init_record_ai;
    DEVSUPFUN       get_ioint_info;
    DEVSUPFUN       read_ai;
    DEVSUPFUN       special_linconv;
}devMEMLoad={
    6,
    NULL,
    NULL,
    init_record_aiMEM,
    NULL,
    read_MEM_load,
    NULL
};

epicsExportAddress(dset,devMEMLoad);

static long init_record_aiMEM(pAiIn)
    struct aiRecord    *pAiIn;
{
    if(recGblInitConstantLink(&pAiIn->inp,DBF_DOUBLE,&pAiIn->val))
        pAiIn->udf = FALSE;
    return(0);
}


static long read_MEM_load(pAiIn)
    struct aiRecord    *pAiIn;
{
    if (DEBUG) fprintf(stderr,"enter read_MEM_load\n");

    long status=0;
    static unsigned long **mem;

    struct vmeio *pvmeio = &pAiIn->inp.value.vmeio;
    /* status = dbGetLink(&(pAiIn->inp),DBF_DOUBLE, &(pAiIn->val),0,0); */
    /*If return was succesful then set undefined false*/  

    if(!strcmp(pvmeio->parm,"PROC")){
        if (!(mem = meminfo()) ||  mem[meminfo_main][meminfo_total] == 0) {	/* cannot normalize mem usage */
            fprintf(stderr, "Cannot get size of memory from /proc/meminfo\n");
            return(2); /* bofore exit(1); */
        }
    }
    if(!strcmp(pvmeio->parm,"MEMAV"))
        pAiIn->val=mem[meminfo_main][meminfo_total] >> 10;
    else if (!strcmp(pvmeio->parm,"MEMUSED"))
        pAiIn->val=mem[meminfo_main][meminfo_used] >> 10;
    else if (!strcmp(pvmeio->parm,"MEMFREE"))
        pAiIn->val=mem[meminfo_main][meminfo_free] >> 10;
    else if (!strcmp(pvmeio->parm,"MEMSHRD"))
        pAiIn->val=mem[meminfo_main][meminfo_shared] >> 10;
    else if (!strcmp(pvmeio->parm,"MEMBUFF"))
        pAiIn->val=mem[meminfo_main][meminfo_buffers] >> 10;
    else if (!strcmp(pvmeio->parm,"SWAPAV"))
        pAiIn->val=mem[meminfo_swap][meminfo_total] >> 10;
    else if (!strcmp(pvmeio->parm,"SWAPUSED"))
        pAiIn->val=mem[meminfo_swap][meminfo_used] >> 10;
    else if (!strcmp(pvmeio->parm,"SWAPFREE"))
        pAiIn->val=mem[meminfo_swap][meminfo_free] >> 10;
    else if (!strcmp(pvmeio->parm,"SWAPCACH"))
        pAiIn->val=mem[meminfo_total][meminfo_cached] >> 10;
    else 
        pAiIn->val=mem[meminfo_main][meminfo_free] >> 10;

    if(!status) pAiIn->udf = FALSE;
    if (DEBUG) fprintf(stderr,"exit read_MEM_load\n");
    return(2); /* no convertion fron rval to val */
}

static long init_record_IP();
static long read_uptime_IP();
struct {
    long            number;
    DEVSUPFUN       report;
    DEVSUPFUN       init;
    DEVSUPFUN       init_record;
    DEVSUPFUN       get_ioint_info;
    DEVSUPFUN       read;
}devIpAddr={
    5,
    NULL,
    NULL,
    init_record_IP,
    NULL,
    read_uptime_IP,
};

epicsExportAddress(dset,devIpAddr);

static long init_record_IP(pStringIn)
    struct stringinRecord    *pStringIn;
{
    if(recGblInitConstantLink(&pStringIn->inp,DBF_STRING,&pStringIn->val))
        pStringIn->udf = FALSE;
    return(0);
}


static long read_uptime_IP(pStringIn)
    struct stringinRecord    *pStringIn;
{
    if (DEBUG) fprintf(stderr,"enter read_uptime_IP\n");
    int s;
    struct ifreq ifr;
    unsigned long iPAddr;

    if ((s=socket(AF_INET, SOCK_DGRAM, 0)) < 0)
        return 0;

    strcpy(ifr.ifr_name, "eth0");

    if (! ioctl(s, SIOCGIFADDR, &ifr))
    {
        iPAddr=((struct sockaddr_in *)&ifr.ifr_addr)->sin_addr.s_addr;
        sprintf(pStringIn->val,"%lu:%lu:%lu:%lu",iPAddr%256,(iPAddr/256)%256,(iPAddr/65536)%256,(iPAddr/16777216)%256);
    }
    close(s);
    /* if(!status)*/  pStringIn->udf = FALSE;
    if (DEBUG) fprintf(stderr,"exit read_uptime_IP\n");
    return(0);
}
/*-------------- get host info ---------------------------*/

static long init_record_Info();
static long read_uptime_Info();
struct {
    long            number;
    DEVSUPFUN       report;
    DEVSUPFUN       init;
    DEVSUPFUN       init_record;
    DEVSUPFUN       get_ioint_info;
    DEVSUPFUN       read;
}devUname={
    5,
    NULL,
    NULL,
    init_record_Info,
    NULL,
    read_uptime_Info,
};

epicsExportAddress(dset,devUname);

static long init_record_Info(pStringIn)
    struct stringinRecord    *pStringIn;
{
    if(recGblInitConstantLink(&pStringIn->inp,DBF_STRING,&pStringIn->val))
        pStringIn->udf = FALSE;
    return(0);
}


static long read_uptime_Info(pStringIn)
    struct stringinRecord    *pStringIn;
{
    if (DEBUG) fprintf(stderr,"enter read_uptime_Info\n");
    /* long status; */
    struct utsname name;

    struct vmeio *pvmeio = &pStringIn->inp.value.vmeio;
    /* status = dbGetLink(&(pStringIn->inp),DBF_STRING, &(pStringIn->val),0,0); */
    /*If return was succesful then set undefined false*/
    /* sprintf(pStringIn->val,"ala %d",get_uptime()); */

    if (uname (&name) == -1){
        fprintf(stderr,"UP time info: cannot get system name\n");
    }
    else{
        if(!strcmp(pvmeio->parm,"SYSNAME"))
            sprintf(pStringIn->val,"%.*s",(int)sizeof(pStringIn->val)-1,name.sysname);
        else if(!strcmp(pvmeio->parm,"RELEASE"))
            sprintf(pStringIn->val,"%.*s",(int)sizeof(pStringIn->val)-1,name.release);
        else if(!strcmp(pvmeio->parm,"VERSION"))
            sprintf(pStringIn->val,"%.*s",(int)sizeof(pStringIn->val)-1,name.version);
        else if(!strcmp(pvmeio->parm,"MACHINE"))
            sprintf(pStringIn->val,"%.*s",(int)sizeof(pStringIn->val)-1,name.machine);
    }

    /* if(!status) */ pStringIn->udf = FALSE;
    if (DEBUG) fprintf(stderr,"exit read_uptime_Info\n");
    return(0);
}

