//
// Brian Raue's Moller Quad Current calculation
//
//   input:  beamEnergy [GeV]
//   output: quadCurrent [Amps]
//
double calcQuadCurrent(float beamEnergy) {
      const double a0=-0.703138;
      const double a1=0.3467019;
      const double a2=0.1071944;
      const double a3=-0.00384008;
      const double a4=7.38246E-05;
      const double I0=15.20179318;
      const double I1=74.67546956;
      const double I2=4.819365945;
      const double I3=-0.629171841;
      const double I4=0.028959561;
      const double I5=3.16195E-06;
      // beamEnergy (GeV):
      const double E=beamEnergy;
      // magnetic field (kG):
      const double B=a0+a1*E+a2*E*E+a3*E*E*E+a4*E*E*E*E;
      // current per coil (A):
      const double I=I0+I1*B+I2*B*B+I3*B*B*B+I4*B*B*B*B+I5*B*B*B*B*B;
      // power supply current (A):
      return I*3;
}
