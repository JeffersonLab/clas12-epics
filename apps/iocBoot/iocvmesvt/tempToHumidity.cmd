
# Assign Temp to Humidity  for dewpoint calculation
#   as per Brian Eng 9/26/2014
#   T1 should always go to H1 and T2 should always go to H2
#   on each sensor board.
dbpf("B_SVT_ENV_Hum_SB1_H1_SL11:Tn","0")
dbpf("B_SVT_ENV_Hum_SB2_H1_SL11:Tn","0")
dbpf("B_SVT_ENV_Hum_SB3_H1_SL11:Tn","0")
dbpf("B_SVT_ENV_Hum_SB4_H1_SL11:Tn","0")
dbpf("B_SVT_ENV_Hum_SB5_H1_SL11:Tn","0")
dbpf("B_SVT_ENV_Hum_SB6_H1_SL11:Tn","0")
dbpf("B_SVT_EX_ENV_Hum_SB1_H1_SL11:Tn","0")
dbpf("B_SVT_EX_ENV_Hum_SB2_H1_SL11:Tn","0")
dbpf("B_SVT_ENV_Hum_SB1_H2_SL11:Tn","1")
dbpf("B_SVT_ENV_Hum_SB2_H2_SL11:Tn","1")
dbpf("B_SVT_ENV_Hum_SB3_H2_SL11:Tn","1")
dbpf("B_SVT_ENV_Hum_SB4_H2_SL11:Tn","1")
dbpf("B_SVT_ENV_Hum_SB5_H2_SL11:Tn","1")
dbpf("B_SVT_ENV_Hum_SB6_H2_SL11:Tn","1")
dbpf("B_SVT_EX_ENV_Hum_SB1_H2_SL11:Tn","1")
dbpf("B_SVT_EX_ENV_Hum_SB2_H2_SL11:Tn","1")

