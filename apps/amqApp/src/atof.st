program atof

float wf[780]; assign wf to "B_DET_ATOF_TDC:c";
float wf0[52]; assign wf0 to "B_DET_ATOF_TDC_M0:c";
float wf1[52]; assign wf1 to "B_DET_ATOF_TDC_M1:c";
float wf2[52]; assign wf2 to "B_DET_ATOF_TDC_M2:c";
float wf3[52]; assign wf3 to "B_DET_ATOF_TDC_M3:c";
float wf4[52]; assign wf4 to "B_DET_ATOF_TDC_M4:c";
float wf5[52]; assign wf5 to "B_DET_ATOF_TDC_M5:c";
float wf6[52]; assign wf6 to "B_DET_ATOF_TDC_M6:c";
float wf7[52]; assign wf7 to "B_DET_ATOF_TDC_M7:c";
float wf8[52]; assign wf8 to "B_DET_ATOF_TDC_M8:c";
float wf9[52]; assign wf9 to "B_DET_ATOF_TDC_M9:c";
float wf10[52]; assign wf10 to "B_DET_ATOF_TDC_M10:c";
float wf11[52]; assign wf11 to "B_DET_ATOF_TDC_M11:c";
float wf12[52]; assign wf12 to "B_DET_ATOF_TDC_M12:c";
float wf13[52]; assign wf13 to "B_DET_ATOF_TDC_M13:c";
float wf14[52]; assign wf14 to "B_DET_ATOF_TDC_M14:c";
int j;
string stmp;

ss atof {

    state start {
        when () {
        } state run
    }

    state run {
        
        when (pvConnectCount() < pvChannelCount()) {
            printf("Waiting for PVs (%d/%d)\n",pvConnectCount(),pvChannelCount());
        } state run

        when () {
            epicsThreadSleep(1);
            pvGet(wf0);
            pvGet(wf1);
            pvGet(wf2);
            pvGet(wf3);
            pvGet(wf4);
            pvGet(wf5);
            pvGet(wf6);
            pvGet(wf7);
            pvGet(wf8);
            pvGet(wf9);
            pvGet(wf10);
            pvGet(wf11);
            pvGet(wf12);
            pvGet(wf13);
            pvGet(wf14);
            for (j=0; j<52; ++j) {
                wf[52*0+j] = wf0[j];
                wf[52*1+j] = wf1[j];
                wf[52*2+j] = wf2[j];
                wf[52*3+j] = wf3[j];
                wf[52*4+j] = wf4[j];
                wf[52*5+j] = wf5[j];
                wf[52*6+j] = wf6[j];
                wf[52*7+j] = wf7[j];
                wf[52*8+j] = wf8[j];
                wf[52*9+j] = wf9[j];
                wf[52*10+j] = wf10[j];
                wf[52*11+j] = wf11[j];
                wf[52*12+j] = wf12[j];
                wf[52*13+j] = wf13[j];
                wf[52*14+j] = wf14[j];
            }
            pvPut(wf);
        } state run
    }
}

