program ramp

string msg;  assign msg   to "{P}i:ramp:msg";
float vset;  assign vset  to "{P}v:set";
float iset;  assign iset  to "{P}i:set";  monitor iset;
float imon;  assign imon  to "{P}i:rbk";  monitor imon;
float iramp; assign iramp to "{P}i:ramp"; monitor iramp;
int fault;   assign fault to "{P}fault";  monitor fault;

evflag ev_ramp; sync iramp ev_ramp;

float rampstep=555; float tolerance=10; int timeout=30;

int nsteps; int istep; float itarget; float istart;

%{
extern double fabs(double);
int equals(float x1,float x2,float tolerance) { return fabs(x1-x2) < tolerance; }
}%

ss ramp {

    state start {

        entry {
            sprintf(msg,"Initialized");
            printf("%s\n",msg);
            pvPut(msg);
            efClear(ev_ramp);
        }

        when() {} state idle
    }

    state idle {

        when (efTestAndClear(ev_ramp) && fault==0) {
            sprintf(msg,"Ramp triggered");
            printf("%s\n",msg);
            pvPut(msg);
            vset = 60;
            pvPut(vset);
            epicsThreadSleep(1);
        } state ramp

    }

    state ramp {

        entry {
            istart = imon;
            itarget = iramp;
            nsteps = (int)(fabs(itarget-istart)/rampstep) + 1;
            istep = 0;
            sprintf(msg,"Entered ramp: %.1f -> %.1f in %d steps",istart,itarget,nsteps);
            printf("%s\n",msg);
            pvPut(msg);
        }

        when (fault != 0) {
            sprintf(msg,"Ramp aborted due to hardware fault.");
            printf("%s\n",msg);
            pvPut(msg);
        } state idle

        when (delay(timeout)) {
            sprintf(msg,"Ramp aborted due to failure to reach setpoint.");
            printf("%s\n",msg);
            pvPut(msg);
        } state idle

        when (efTestAndClear(ev_ramp)) {
            sprintf(msg,"Ramp aborted due to user interference.");
            printf("%s\n",msg);
            pvPut(msg);
        } state reramp

        when(equals(imon, itarget, tolerance)) {
            sprintf(msg,"Ramp to %.1f finished sucecsfully.",itarget);
            printf("%s\n",msg);
            pvPut(msg);
        } state idle

        when(delay(2) && istep < nsteps && equals(imon, iset, tolerance)) {
            if (istep+1 == nsteps) iset = itarget;
            else iset = istart + (istep+1)*(itarget>istart?1:-1)*rampstep;
            sprintf(msg,"Ramp step: %d/%d,  %.1f -> %.1f -> %.1f",istep+1,nsteps,istart,iset,itarget);
            printf("%s\n",msg);
            epicsThreadSleep(1);
            pvPut(msg);
            pvPut(iset);
            istep += 1;
        } state ramp

    }

    state reramp {
        when () {} state ramp
    }

}

