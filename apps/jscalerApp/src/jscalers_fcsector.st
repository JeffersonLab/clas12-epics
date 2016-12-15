
program seqJscalersFC ("S=1")

option -c;
option -r;

int ii;
string stmp;

string msg;               assign msg to       "B_DET_FC_SEQJSCALERS_SEC{S}:msg";
float ftof_fadc[1000];    assign ftof_fadc to {};
float ftof_fadc_wf[1000]; assign ftof_fadc_wf to "B_DET_FTOF_FADC_SEC{S}";

ss seqJscalersFC {

    state init {
      when (pvConnectCount() < pvChannelCount())
      {
        sprintf(msg,"Waiting for PVs (%d/%d)",pvConnectCount(),pvChannelCount());
        printf("Waiting for PVs (%d/%d)",pvConnectCount(),pvChannelCount());
        pvPut(msg);
      } state init
      
      when () {
        for (ii=1; ii<=23; ii++)
        {
          sprintf(stmp,"B_DET_FTOF_FADC_SEC{S}_PANEL1A_L_E%.2d:c1",ii);
          pvAssign(ftof_fadc[ii],stmp);
        }
      } state run
    }

    state run {
      when ()
      {
        for (ii=1; ii<=23; ii++)
        {
          pvGet(ftof_fadc[ii]);
          ftof_fadc_wf[ii]=ftof_fadc[ii];
        }
        pvPut(ftof_fadc_wf);
        epicsThreadSleep(1);
      } state run
    }

}


