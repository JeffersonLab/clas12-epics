program level_check

float voltage;
assign voltage to "Input_voltage";
monitor voltage;

short light;
assign light to "Indicator_light";

ss volt_check {
  state light_off {
    when (voltage > 5.0) {
      /* turn light on */
      light = TRUE;
      pvPut(light);
    } state light_on
  }

  state light_on {
    when (voltage < 5.0) {
      /* turn light off */
      light = FALSE;
      pvPut(light);
    } state light_off
  }
}
