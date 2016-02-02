#!/bin/csh -f
set roc_name_snmp = ( ltcc0 \
                      pcal0 \
                      hps2 \
                      adcecal1   hps12      \
                      hps1       hps2       dcrb1      tdcecal1   \
                      tdcpcal1   tdcftof1   adcpcal1   adcftof1   \
                      adcecal1   adcftof6   tdcftof6   adcpcal6   \
                      tdcpcal6   adcecal6   tdcecal6   adcecal5   \
                      tdcecal5   adcpcal5   tdcpcal5   adcftof5   \
                      tdcftof5   adcecal4   tdcecal4   adcpcal4   \
                      tdcpcal4   adcftof4   tdcftof4   adcecal2   \
                      tdcecal2   adcpcal2   tdcpcal2   adcftof2   \
                      tdcftof2   adcecal3   tdcecal3   adcpcal3   \
                      tdcpcal3   adcftof3   tdcftof3   hps11 \
                      dcrb2 \
                      ctof1 \
                      adcft1     adcft2 \
                      adcft3 )

set ip_snmp = ( 129.57.86.47 \
                129.57.86.44 \
                129.57.69.40 \
                129.57.167.80   129.57.167.20  \
                129.57.167.164  129.57.167.165  129.57.86.53    129.57.167.52  \
                129.57.167.54   129.57.167.73   129.57.167.81   129.57.167.156 \
                129.57.167.80   129.57.167.157  129.57.167.158  129.57.167.39  \
                129.57.167.163  129.57.167.38   129.57.167.40   129.57.167.169 \
                129.57.167.170  129.57.167.171  129.57.167.176  129.57.167.177 \
                129.57.167.178  129.57.167.189  129.57.167.186  129.57.167.188 \
                129.57.167.185  129.57.167.187  129.57.167.183  129.57.167.212 \
                129.57.167.192  129.57.167.216  129.57.167.211  129.57.167.251 \
                129.57.167.21   129.57.167.32   129.57.167.22   129.57.167.34  \
                129.57.167.19   129.57.167.37   129.57.167.27   129.57.167.93 \
                129.57.86.67 \
                129.57.86.79 \
                129.57.86.102   129.57.86.103 \
                129.57.86.104 )

foreach ii (`seq 50`)
echo dbLoadRecords\(\"db/wienerR.db\",\"SCAN=\$\{scan\},HOST=$roc_name_snmp[$ii],IP=$ip_snmp[$ii]\"\)
echo dbLoadRecords\(\"db/wienerW.db\",\"HOST=$roc_name_snmp[$ii],IP=$ip_snmp[$ii]\"\)
echo dbLoadRecords\(\"db/vmePedestals.db\",\"HOST=$roc_name_snmp[$ii],IP=$ip_snmp[$ii],VXS_FLAG=1\"\)
echo
end


