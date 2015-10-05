program quad_current

/* option +c; */

#define CALCULATE  1
#define CYCLE_PS   2

#define ALMOST_HALF 0.49999999999


double command;
assign command to "moller_quad_calculate";
monitor command;

float energy;
assign energy to "MBSY2C_energy";
monitor energy;

float old_energy;

float dynab_sug_set;
assign dynab_sug_set to "dynab_sug_set";

float dynac_sug_set;
assign dynac_sug_set to "dynac_sug_set";

float DYNABON;
assign DYNABON to "DYNABON";

float DYNABRESET;
assign DYNABRESET to "DYNABRESET";

float DYNABOFF;
assign DYNABOFF to "DYNABOFF";

float DYNABSETI;
assign DYNABSETI to "DYNABSETI";

float DYNACON;
assign DYNACON to "DYNACON";

float DYNACRESET;
assign DYNACRESET to "DYNACRESET";

float DYNACOFF;
assign DYNACOFF to "DYNACOFF";

float DYNACSETI;
assign DYNACSETI to "DYNACSETI";

int set_b;
int set_c;

ss quad_scan {
  state init {
	when () {
	    printf(" moller quad current calculator init state: energy=%f\n",energy);
	    old_energy = energy;

        set_b = upstream_quad(energy);
        set_c = downstream_quad(energy);

	    dynab_sug_set = set_b;
        dynac_sug_set = set_c;

	    printf("set_b dynab:%i,%f\n",set_b,dynab_sug_set);
	    printf("set_c dynab:%i,%f\n",set_c,dynac_sug_set);

        pvPut(dynab_sug_set);
        pvPut(dynac_sug_set);
        command = 2;
	    pvPut(command);
    } state get_command
  }

  state get_command {
    when (command == CALCULATE && energy !=0) {
	    printf(" moller quad current calculator init state: energy=%f\n",energy);
        old_energy = energy;
        set_b = upstream_quad(energy);
        set_c = downstream_quad(energy);

	    dynab_sug_set = set_b;
	    dynac_sug_set = set_c;

	    printf("set_b dynab:%i,%f\n",set_b,dynab_sug_set);
	    printf("set_c dynab:%i,%f\n",set_c,dynac_sug_set);

        pvPut(dynab_sug_set);
        pvPut(dynac_sug_set);
	    command = 0;
        pvPut(command);
    } state get_command
    
    when (command == CYCLE_PS) {
    } state set_zero

    when (old_energy != energy) {
        printf("Energy change!! Old %f New %f  recalculating quad set points",old_energy, energy);
	    command = CALCULATE;
        pvPut(command);
    } state get_command
    
    when (command != CALCULATE && delay(600)) {
    } state get_command
 }

  state set_zero {
    when () {
        DYNABSETI = 0.0;
        DYNACSETI = 0.0;
        pvPut(DYNABSETI);
        pvPut(DYNACSETI);
    } state hit_on
  }
  
  state hit_on {
    when (delay(2)) {
        DYNABON = 1;
        DYNACON = 1;
        pvPut(DYNABON);
        pvPut(DYNACON);
    } state hit_reset
  }
  
  state hit_reset {
    when (delay(1)) {
        DYNABRESET = 1;
        DYNACRESET = 1;
        pvPut(DYNABRESET);
        pvPut(DYNACRESET);
    } state hit_off
  }
  
  state hit_off {
    when (delay(1)) {
        DYNABOFF = 1;
        DYNACOFF = 1;
        pvPut(DYNABOFF);
        pvPut(DYNACOFF);

        command = 0;
        pvPut(command);
    } state get_command
  }
}


/* ---------------------------------------------------------------------- */
/* C functions                                                            */
/* ---------------------------------------------------------------------- */
%{
int upstream_quad(beam_energy)
    float beam_energy;
{
    float q1m0, q1m1, q1m2, q1m3;  /* quad 1 terms           */
    float gvc1, gvc2, gvc3, gvc4, gvc5;
                                 /* grad to curr terms     */
    float qradius;                 /* quad radius (in)       */
    float q1fld;                   /* quad 1 field (kG)      */
    float q1grad;                  /* quad 1 gradient (G/in) */
    float q1curr;                  /* quad 1 current (A)     */
    float energy;                  /* beam energy (GeV)      */

    q1m0 = -0.50868102221;
    q1m1 = -0.99269187356;
    q1m2 =  0.68615481813;
    q1m3 = -0.037955948119;

    gvc1 =  1.000E-02;
    gvc2 =  4.436E-01;
    gvc3 =  3.224E-05;
    gvc4 = -3.202E-08;
    gvc5 =  9.931E-12;

    qradius = 5.0675;

    energy = beam_energy/1000.;
    printf("upstream quad calculator --Now with energy corrections! %f\n", energy);


    q1fld = q1m0 + (q1m1 * energy) + (q1m2 * energy * energy)
            + (q1m3 * energy * energy * energy);

    q1grad = q1fld * 1000. / qradius;
    q1curr = gvc1 
            + gvc2 * q1grad 
            + gvc3 * q1grad * q1grad
            + gvc4 * q1grad * q1grad * q1grad 
            + gvc5 * q1grad * q1grad * q1grad * q1grad;

    q1curr = q1curr * 3.;    /* quads in parallel */

    printf("            Field (kG)   Gradient (G/in)   PS Current (A)\n");
    printf("   Quad 1   %f       %8.3f           %8.3f \n", q1fld, q1grad, q1curr);

    if (q1curr < 0) {
	    q1curr = -1.*q1curr;
    }
    return (int) q1curr;
}

int downstream_quad(beam_energy)
    float beam_energy;
{
    float q2m0, q2m1, q2m2;                 /* quad 2 terms           */
    float gvc1, gvc2, gvc3, gvc4, gvc5;     /* grad to curr terms     */
    float qradius;                 /* quad radius (in)       */
    float q2fld;                   /* quad 2 field (kG)      */
    float q2grad;                  /* quad 2 gradient (G/in) */
    float q2curr;                  /* quad 2 current (A)     */
    float energy;                  /* beam energy (GeV)      */

    q2m0 =  0.10761692242;
    q2m1 =  1.5485463189;
    q2m2 =  0.028639510611;

    gvc1 =  1.000E-02;
    gvc2 =  4.436E-01;
    gvc3 =  3.224E-05;
    gvc4 = -3.202E-08;
    gvc5 =  9.931E-12;

    qradius = 5.0675;
    energy = beam_energy/1000.;
    printf(" Downstream quad current calculator--- Now with energy corrections! %f\n",energy);

    q2fld = q2m0 + (q2m1 * energy) + (q2m2 * energy * energy);

    q2grad = q2fld * 1000. / qradius;

    q2curr =   gvc1 
            + gvc2 * q2grad 
            + gvc3 * q2grad * q2grad
            + gvc4 * q2grad * q2grad * q2grad 
            + gvc5 * q2grad * q2grad * q2grad * q2grad;

    q2curr = q2curr * 3.;

    printf("            Field (kG)   Gradient (G/in)   PS Current (A)\n");
    printf("   Quad 2   %f       %8.3f           %8.3f \n", q2fld, q2grad, q2curr);

    return (int) q2curr;
}

}%
