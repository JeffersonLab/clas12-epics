#!/usr/bin/env bash

if [ "$#" -ne 3 ]; then
	echo "Usage: $0 <location> <voltage> <value>"
	echo
	echo "All options are case insensitive"
	echo "<location> can be R1, R2, R3, R4, ALL"
	echo "<voltage> can be LV, HV"
	echo "<value> can be ON, OFF, STAT(US), VOLT(AGE), CURR(ENT)"
	echo "Parts in () are optional. curr and current are equivalent"
	exit 1
fi
# check for valid location setting
loc=${1,,}
case "$loc" in
"r1" | "r2" | "r3" | "r4" | "all")
	;;
*)
	echo "Invalid location. Must be one of: r1, r2, r3, r4, all"
	exit 2
esac	

# check for valid voltage setting
volt=${2,,}
case "$volt" in
"hv" | "lv")
	;;
*)
	echo "Invalid voltage. Must be one of: lv, hv"
	exit 2
esac	

# check for valid value setting
val=${3,,}
case "$val" in
"on" | "off" | "status" | "stat" | "voltage" | "volt" | "current" | "curr")
	;;
*)
	echo "Invalid setting. Must be one of: on, off (1, 0), stat(us), volt(age), curr(ent)"
	exit 2
esac	

# print status (on or off) of channels and exit
if [[ $val == 'status' || $val == "stat" ]]; then
	case "$loc" in
	"r1")
		case "$volt" in
		"lv")
			echo 'R1 LV'
			echo "`~/snmpbulkget -Cr40 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt1 outputSwitch`"
			exit 0;;
		"hv")
			echo 'R1 HV'
			echo "`~/snmpbulkget -Cr20 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt1 outputSwitch.U407`"
			exit 0;;
		esac
		;;
	"r2")
		case "$volt" in
		"lv")
			echo 'R2 LV'
			echo "`~/snmpbulkget -Cr56 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt4 outputSwitch`"
			exit 0;;
		"hv")
			echo 'R2 HV'
			echo "`~/snmpbulkget -Cr28 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt1 outputSwitch.U715`"
			exit 0;;
		esac
		;;
	"r3")
		case "$volt" in
		"lv")
			echo 'R3 LV'
			echo "`~/snmpbulkget -Cr56 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt3 outputSwitch`"
			echo "`~/snmpbulkget -Cr16 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt3 outputSwitch.U607`"
			exit 0;;
		"hv")
			echo 'R3 HV'
			echo "`~/snmpbulkget -Cr36 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt4 outputSwitch.U607`"
			exit 0;;
		esac
		;;
	"r4")
		case "$volt" in
		"lv")
			echo 'R4 LV | M1-12'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt5 outputSwitch`"
			echo 'R4 LV | M13-24'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt2 outputSwitch`"
			exit 0;;
		"hv")
			echo 'R4 HV'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt5 outputSwitch.U507`"
			exit 0;;
		esac
		;;
	"all")
		case "$volt" in
		"lv")
			echo 'R1 LV'
			echo "`~/snmpbulkget -Cr40 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt1 outputSwitch`"
			echo 'R2 LV'
			echo "`~/snmpbulkget -Cr56 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt4 outputSwitch`"
			echo 'R3 LV'
			echo "`~/snmpbulkget -Cr56 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt3 outputSwitch`"
			echo "`~/snmpbulkget -Cr16 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt3 outputSwitch.U607`"
			echo 'R4 LV | M1-12'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt5 outputSwitch`"
			echo 'R4 LV | M13-24'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt2 outputSwitch`"
			exit 0;;
		"hv")
			echo 'R1 HV'
			echo "`~/snmpbulkget -Cr20 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt1 outputSwitch.U407`"
			echo 'R2 HV'
			echo "`~/snmpbulkget -Cr28 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt1 outputSwitch.U715`"
			echo 'R3 HV'
			echo "`~/snmpbulkget -Cr36 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt4 outputSwitch.U607`"
			echo 'R4 HV'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt5 outputSwitch.U507`"
			exit 0;;
		esac
		;;
	esac
	# if we get this far something went wrong
	exit 3
fi

# print voltage of channels and exit
if [[ $val == 'volt' || $val == 'voltage' ]]; then
	case "$loc" in
	"r1")
		case "$volt" in
		"lv")
			echo 'R1 LV'
			echo "`~/snmpbulkget -Cr40 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt1 outputMeasurementSenseVoltage`"
			exit 0;;
		"hv")
			echo 'R1 HV'
			echo "`~/snmpbulkget -Cr20 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt1 outputMeasurementSenseVoltage.U407`"
			exit 0;;
		esac
		;;
	"r2")
		case "$volt" in
		"lv")
			echo 'R2 LV'
			echo "`~/snmpbulkget -Cr40 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt4 outputMeasurementSenseVoltage`"
			echo "`~/snmpbulkget -Cr16 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt4 outputMeasurementSenseVoltage.U407`"
			exit 0;;
		"hv")
			echo 'R2 HV'
			echo "`~/snmpbulkget -Cr28 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt1 outputMeasurementSenseVoltage.U715`"
			exit 0;;
		esac
		;;
	"r3")
		case "$volt" in
		"lv")
			echo 'R3 LV'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt3 outputMeasurementSenseVoltage`"
			echo "`~/snmpbulkget -Cr24 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt3 outputMeasurementSenseVoltage.U507`"
			exit 0;;
		"hv")
			echo 'R3 HV'
			echo "`~/snmpbulkget -Cr36 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt4 outputMeasurementSenseVoltage.U607`"
			exit 0;;
		esac
		;;
	"r4")
		case "$volt" in
		"lv")
			echo 'R4 LV | M1-12'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt5 outputMeasurementSenseVoltage`"
			echo 'R4 LV | M13-24'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt2 outputMeasurementSenseVoltage`"
			exit 0;;
		"hv")
			echo 'R4 HV'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt5 outputMeasurementSenseVoltage.U507`"
			exit 0;;
		esac
		;;
	"all")
		case "$volt" in
		"lv")
			echo 'R1 LV'
			echo "`~/snmpbulkget -Cr40 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt1 outputMeasurementSenseVoltage`"
			echo 'R2 LV'
			echo "`~/snmpbulkget -Cr40 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt4 outputMeasurementSenseVoltage`"
			echo "`~/snmpbulkget -Cr16 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt4 outputMeasurementSenseVoltage.U407`"
			echo 'R3 LV'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt3 outputMeasurementSenseVoltage`"
			echo "`~/snmpbulkget -Cr24 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt3 outputMeasurementSenseVoltage.U507`"
			echo 'R4 LV | M1-12'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt5 outputMeasurementSenseVoltage`"
			echo 'R4 LV | M13-24'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt2 outputMeasurementSenseVoltage`"
			exit 0;;
		"hv")
			echo 'R1 HV'
			echo "`~/snmpbulkget -Cr20 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt1 outputMeasurementSenseVoltage.U407`"
			echo 'R2 HV'
			echo "`~/snmpbulkget -Cr28 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt1 outputMeasurementSenseVoltage.U715`"
			echo 'R3 HV'
			echo "`~/snmpbulkget -Cr36 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt4 outputMeasurementSenseVoltage.U607`"
			echo 'R4 HV'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt5 outputMeasurementSenseVoltage.U507`"
			exit 0;;
		esac
		;;
	esac
	# if we get this far something went wrong
	exit 3
fi

# print current of channels and exit
if [[ $val == 'curr' || $val == 'current' ]]; then
	case "$loc" in
	"r1")
		case "$volt" in
		"lv")
			echo 'R1 LV'
			echo "`~/snmpbulkget -Cr40 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt1 outputMeasurementCurrent`"
			exit 0;;
		"hv")
			echo 'R1 HV'
			echo "`~/snmpbulkget -Op 20.12 -Cr20 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt1 outputMeasurementCurrent.U407`"
			exit 0;;
		esac
		;;
	"r2")
		case "$volt" in
		"lv")
			echo 'R2 LV'
			echo "`~/snmpbulkget -Cr40 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt4 outputMeasurementCurrent`"
			echo "`~/snmpbulkget -Cr16 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt4 outputMeasurementCurrent.U407`"
			exit 0;;
		"hv")
			echo 'R2 HV'
			echo "`~/snmpbulkget -Op 20.12 -Cr28 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt1 outputMeasurementCurrent.U715`"
			exit 0;;
		esac
		;;
	"r3")
		case "$volt" in
		"lv")
			echo 'R3 LV'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt3 outputMeasurementCurrent`"
			echo "`~/snmpbulkget -Cr24 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt3 outputMeasurementCurrent.U507`"
			exit 0;;
		"hv")
			echo 'R3 HV'
			echo "`~/snmpbulkget -Op 20.12 -Cr36 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt4 outputMeasurementCurrent.U607`"
			exit 0;;
		esac
		;;
	"r4")
		case "$volt" in
		"lv")
			echo 'R4 LV | M1-12'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt5 outputMeasurementCurrent`"
			echo 'R4 LV | M13-24'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt2 outputMeasurementCurrent`"
			exit 0;;
		"hv")
			echo 'R4 HV'
			echo "`~/snmpbulkget -Op 20.12 -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt5 outputMeasurementCurrent.U507`"
			exit 0;;
		esac
		;;
	"all")
		case "$volt" in
		"lv")
			echo 'R1 LV'
			echo "`~/snmpbulkget -Cr40 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt1 outputMeasurementCurrent`"
			echo 'R2 LV'
			echo "`~/snmpbulkget -Cr40 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt4 outputMeasurementCurrent`"
			echo "`~/snmpbulkget -Cr16 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt4 outputMeasurementCurrent.U407`"
			echo 'R3 LV'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt3 outputMeasurementCurrent`"
			echo "`~/snmpbulkget -Cr24 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt3 outputMeasurementCurrent.U507`"
			echo 'R4 LV | M1-12'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt5 outputMeasurementCurrent`"
			echo 'R4 LV | M13-24'
			echo "`~/snmpbulkget -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt2 outputMeasurementCurrent`"
			exit 0;;
		"hv")
			echo 'R1 HV'
			echo "`~/snmpbulkget -Op 20.12 -Cr20 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt1 outputMeasurementCurrent.U407`"
			echo 'R2 HV'
			echo "`~/snmpbulkget -Op 20.12 -Cr28 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt1 outputMeasurementCurrent.U715`"
			echo 'R3 HV'
			echo "`~/snmpbulkget -Op 20.12 -Cr36 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt4 outputMeasurementCurrent.U607`"
			echo 'R4 HV'
			echo "`~/snmpbulkget -Op 20.12 -Cr48 -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c public vmetlsvt5 outputMeasurementCurrent.U507`"
			exit 0;;
		esac
		;;
	esac
	# if we get this far something went wrong
	exit 3
fi

# arg1 = hostname
# arg2 = ch
# arg3 = on(1)/off(0)
function ch_sw {
	echo "`snmpset -v2c -m +WIENER-CRATE-MIB -M /usr/share/snmp/mibs -c guru $1 outputSwitch.U$2 i $3`"
}

function r1_lv {
	for j in {0..4}
	do
		for i in {0..7}
		do
			ch_sw vmetlsvt1 $(($j*100 + $i)) $1
		done
	done
}

function r1_hv {
	for i in {600..615}
	do
		ch_sw vmetlsvt1 $i $1
	done
	for i in {700..703}
	do
		ch_sw vmetlsvt1 $i $1
	done
}

function r2_lv {
	for j in {0..6}
	do
		for i in {0..7}
		do
			ch_sw vmetlsvt4 $(($j*100 + $i)) $1
		done
	done
}

function r2_hv {
	for i in {800..815}
	do
		ch_sw vmetlsvt1 $i $1
	done
	for i in {900..911}
	do
		ch_sw vmetlsvt1 $i $1
	done
}

function r3_lv {
	for j in {0..8}
	do
		for i in {0..7}
		do
			ch_sw vmetlsvt3 $(($j*100 + $i)) $1
		done
	done
}

function r3_hv {
	for j in {7..8}
	do
		for i in {0..15}
		do
			ch_sw vmetlsvt4 $(($j*100 + $i)) $1
		done
	done
	for i in {900..903}
	do
		ch_sw vmetlsvt4 $i $1
	done
}

function r4_lv {
	for j in {0..5}
	do
		for i in {0..7}
		do
			ch_sw vmetlsvt5 $(($j*100 + $i)) $1
		done
	done
	for j in {0..5}
	do
		for i in {0..7}
		do
			ch_sw vmetlsvt2 $(($j*100 + $i)) $1
		done
	done
}

function r4_hv {
	for j in {7..9}
	do
		for i in {0..15}
		do
			ch_sw vmetlsvt5 $(($j*100 + $i)) $1
		done
	done
}

# turn voltages on
#
# no effort is made to ensure proper sequencing
# i.e. LV not checked when turning on HV
if [[ $val == 'on' ]]; then
	case "$loc" in
	"r1")
		case "$volt" in
		"lv")
			r1_lv 1
			exit 0;;
		"hv")
			r1_hv 1
			exit 0;;
		esac
		;;
	"r2")
		case "$volt" in
		"lv")
			r2_lv 1
			exit 0;;
		"hv")
			r2_hv 1
			exit 0;;
		esac
		;;
	"r3")
		case "$volt" in
		"lv")
			r3_lv 1
			exit 0;;
		"hv")
			r3_hv 1
			exit 0;;
		esac
		;;
	"r4")
		case "$volt" in
		"lv")
			r4_lv 1
			exit 0;;
		"hv")
			r4_hv 1
			exit 0;;
		esac
		;;
	"all")
		case "$volt" in
		"lv")
			r1_lv 1
			r2_lv 1
			r3_lv 1
			r4_lv 1
			exit 0;;
		"hv")
			r1_hv 1
			r2_hv 1
			r3_hv 1
			r4_hv 1
			exit 0;;
		esac
		;;
	esac
	# if we get this far something went wrong
	exit 3
fi

# turn voltages off
#
# no effort is made to ensure proper sequencing
# i.e. HV not checked when turning on LV
if [[ $val == 'off' ]]; then
	case "$loc" in
	"r1")
		case "$volt" in
		"lv")
			r1_lv 0
			exit 0;;
		"hv")
			r1_hv 0
			exit 0;;
		esac
		;;
	"r2")
		case "$volt" in
		"lv")
			r2_lv 0
			exit 0;;
		"hv")
			r2_hv 0
			exit 0;;
		esac
		;;
	"r3")
		case "$volt" in
		"lv")
			r3_lv 0
			exit 0;;
		"hv")
			r3_hv 0
			exit 0;;
		esac
		;;
	"r4")
		case "$volt" in
		"lv")
			r4_lv 0
			exit 0;;
		"hv")
			r4_hv 0
			exit 0;;
		esac
		;;
	"all")
		case "$volt" in
		"lv")
			r1_lv 0
			r2_lv 0
			r3_lv 0
			r4_lv 0
			exit 0;;
		"hv")
			r1_hv 0
			r2_hv 0
			r3_hv 0
			r4_hv 0
			exit 0;;
		esac
		;;
	esac
	# if we get this far something went wrong
	exit 3
fi

# if we get this far something went wrong
exit 3

