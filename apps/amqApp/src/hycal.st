
program hycal

float wf[1156]; assign wf to "B_DET_HYCAL_FADC:c:wf";
float xavg; assign xavg "B_DET_HYCAL_FADC:c:xavg";
float yavg; assign yavg "B_DET_HYCAL_FADC:c:yavg";
int i;
float x,y,sum;

ss hycal { 
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
            pvGet(wf);
            xavg = 0;
            yavg = 0;
            sum = 0;
            for (i=0; i<1156; ++i) {
                x =   i%34-17;
                y = -(i/34-17);
                xavg += x * wf[i];
                yavg += y * wf[i];
                sum += wf[i];
            }
            xavg /= sum;
            yavg /= sum;
            pvPut(xavg);
            pvPut(yavg);
        } state run
    }
}

