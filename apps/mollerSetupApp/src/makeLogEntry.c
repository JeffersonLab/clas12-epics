#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <automoller.h>

void makeLogEntry(
        char* filename,
        float pol,
        float epol,
        float bca,
        float ebca,
        float energy,
        float slmhv,
        float quadB,
        float quadC,
        float helm,
        int tgt,
        int hwp,
        char* logcom,
        char* logusr,
        int runno,
        int coda_runno,
        char* startTime,
        char* endTime) {
    char *dir="/home/epics/DATA/MOELLER";
    char cmd[1000];
    char body[1000];
    char stgt[100];
    char shwp[100];
    switch (tgt) {
        case TGT_LEFT:
            strcpy(stgt,"Left");
            break;
        case TGT_RIGHT:
            strcpy(stgt,"Right");
            break;
        case TGT_EMPTY:
            strcpy(stgt,"Empty");
            break;
        case TGT_ALUM:
            strcpy(stgt,"Aluminum");
            break;
        default:
            strcpy(stgt,"Unknown");
            break;
    }
    switch (hwp) {
        case HWP_IN:
            strcpy(shwp,"IN");
            break;
        case HWP_OUT:
            strcpy(shwp,"OUT");
            break;
        default:
            strcpy(shwp,"Unknown");
            break;
    }
    //sprintf(filename,"moeller_04-16-18_19:37:57.txt");
    sprintf(body,
            "User Comments = %s<br><br>"
            "<table border=1>"
            "<tr><td>Polarization (%%) </td><td> %.3f +/- %.3f</td></tr>"
            "<tr><td>Beam Charge Asymmetry </td><td> %.3f +/- %.3f</td></tr>"
            "<tr><td>Half Wave Plate </td><td> %s</td></tr>"
            "<tr><td>Target Position </td><td> %s</td></tr>"
            "<tr><td>Beam Energy (MeV) </td><td> %.1f</td></tr>"
            "<tr><td>Quad Current (A) </td><td> %.1f/%.1f</td></tr>"
            "<tr><td>Helmholtz Current (A) </td><td> %.1f</td></tr>"
            "<tr><td>SLM Voltage (V) </td><td> %.1f</td></tr>"
            "<tr><td>CODA Run Number </td><td> %d</td></tr>"
            "<tr><td>Moller Run Number </td><td> %d</td></tr>"
            "<tr><td>Run Start Time </td><td> %s</td></tr>"
            "<tr><td>Run End Time </td><td> %s</td></tr>"
            "</table>",
            logcom,pol,epol,bca,ebca,shwp,stgt,energy,quadB,quadC,helm,slmhv,coda_runno,runno,startTime,endTime);
    sprintf(cmd,"echo '%s' | logentry --html -l HBLOG -t 'Moller Run #%d' -a %s/%s -e '%s' -b -",
            body,runno,dir,filename,logusr);
    fprintf(stderr,cmd);
	system(cmd);
}
