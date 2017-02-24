program seq_crate4Off
/* option +r Re-entrant code */
option +r;

#define HVMODS  64
#define HVCTRLS  64
#define LVMODS  56
#define FULLMODS  28

/*** Crate Off button */
short offpb;
assign offpb to "vmetlsvt4:CRATEPB_OFF";
monitor offpb;

/*** High Voltage MPOD voltages */
double hvvol[HVMODS];
assign hvvol[0] to "B_SVT_HV_R2S1T_Slot9:outputMeasSenseV";
assign hvvol[1] to "B_SVT_HV_R2S1B_Slot9:outputMeasSenseV";
assign hvvol[2] to "B_SVT_HV_R2S2T_Slot9:outputMeasSenseV";
assign hvvol[3] to "B_SVT_HV_R2S2B_Slot9:outputMeasSenseV";
assign hvvol[4] to "B_SVT_HV_R2S3T_Slot9:outputMeasSenseV";
assign hvvol[5] to "B_SVT_HV_R2S3B_Slot9:outputMeasSenseV";
assign hvvol[6] to "B_SVT_HV_R2S4T_Slot9:outputMeasSenseV";
assign hvvol[7] to "B_SVT_HV_R2S4B_Slot9:outputMeasSenseV";
assign hvvol[8] to "B_SVT_HV_R2S5T_Slot9:outputMeasSenseV";
assign hvvol[9] to "B_SVT_HV_R2S5B_Slot9:outputMeasSenseV";
assign hvvol[10] to "B_SVT_HV_R2S6T_Slot9:outputMeasSenseV";
assign hvvol[11] to "B_SVT_HV_R2S6B_Slot9:outputMeasSenseV";
assign hvvol[12] to "B_SVT_HV_R2S7T_Slot9:outputMeasSenseV";
assign hvvol[13] to "B_SVT_HV_R2S7B_Slot9:outputMeasSenseV";
assign hvvol[14] to "B_SVT_HV_R2S8T_Slot9:outputMeasSenseV";
assign hvvol[15] to "B_SVT_HV_R2S8B_Slot9:outputMeasSenseV";
assign hvvol[16] to "B_SVT_HV_R2S9T_Slot10:outputMeasSenseV";
assign hvvol[17] to "B_SVT_HV_R2S9B_Slot10:outputMeasSenseV";
assign hvvol[18] to "B_SVT_HV_R2S10T_Slot10:outputMeasSenseV";
assign hvvol[19] to "B_SVT_HV_R2S10B_Slot10:outputMeasSenseV";
assign hvvol[20] to "B_SVT_HV_R2S11T_Slot10:outputMeasSenseV";
assign hvvol[21] to "B_SVT_HV_R2S11B_Slot10:outputMeasSenseV";
assign hvvol[22] to "B_SVT_HV_R2S12T_Slot10:outputMeasSenseV";
assign hvvol[23] to "B_SVT_HV_R2S12B_Slot10:outputMeasSenseV";
assign hvvol[24] to "B_SVT_HV_R2S13T_Slot10:outputMeasSenseV";
assign hvvol[25] to "B_SVT_HV_R2S13B_Slot10:outputMeasSenseV";
assign hvvol[26] to "B_SVT_HV_R2S14T_Slot10:outputMeasSenseV";
assign hvvol[27] to "B_SVT_HV_R2S14B_Slot10:outputMeasSenseV";
assign hvvol[28] to "B_SVT_HV_R3S1T_Slot8:outputMeasSenseV";
assign hvvol[29] to "B_SVT_HV_R3S1B_Slot8:outputMeasSenseV";
assign hvvol[30] to "B_SVT_HV_R3S2T_Slot8:outputMeasSenseV";
assign hvvol[31] to "B_SVT_HV_R3S2B_Slot8:outputMeasSenseV";
assign hvvol[32] to "B_SVT_HV_R3S3T_Slot8:outputMeasSenseV";
assign hvvol[33] to "B_SVT_HV_R3S3B_Slot8:outputMeasSenseV";
assign hvvol[34] to "B_SVT_HV_R3S4T_Slot8:outputMeasSenseV";
assign hvvol[35] to "B_SVT_HV_R3S4B_Slot8:outputMeasSenseV";
assign hvvol[36] to "B_SVT_HV_R3S5T_Slot8:outputMeasSenseV";
assign hvvol[37] to "B_SVT_HV_R3S5B_Slot8:outputMeasSenseV";
assign hvvol[38] to "B_SVT_HV_R3S6T_Slot8:outputMeasSenseV";
assign hvvol[39] to "B_SVT_HV_R3S6B_Slot8:outputMeasSenseV";
assign hvvol[40] to "B_SVT_HV_R3S7T_Slot8:outputMeasSenseV";
assign hvvol[41] to "B_SVT_HV_R3S7B_Slot8:outputMeasSenseV";
assign hvvol[42] to "B_SVT_HV_R3S8T_Slot8:outputMeasSenseV";
assign hvvol[43] to "B_SVT_HV_R3S8B_Slot8:outputMeasSenseV";
assign hvvol[44] to "B_SVT_HV_R3S9T_Slot9:outputMeasSenseV";
assign hvvol[45] to "B_SVT_HV_R3S9B_Slot9:outputMeasSenseV";
assign hvvol[46] to "B_SVT_HV_R3S10T_Slot9:outputMeasSenseV";
assign hvvol[47] to "B_SVT_HV_R3S10B_Slot9:outputMeasSenseV";
assign hvvol[48] to "B_SVT_HV_R3S11T_Slot9:outputMeasSenseV";
assign hvvol[49] to "B_SVT_HV_R3S11B_Slot9:outputMeasSenseV";
assign hvvol[50] to "B_SVT_HV_R3S12T_Slot9:outputMeasSenseV";
assign hvvol[51] to "B_SVT_HV_R3S12B_Slot9:outputMeasSenseV";
assign hvvol[52] to "B_SVT_HV_R3S13T_Slot9:outputMeasSenseV";
assign hvvol[53] to "B_SVT_HV_R3S13B_Slot9:outputMeasSenseV";
assign hvvol[54] to "B_SVT_HV_R3S14T_Slot9:outputMeasSenseV";
assign hvvol[55] to "B_SVT_HV_R3S14B_Slot9:outputMeasSenseV";
assign hvvol[56] to "B_SVT_HV_R3S15T_Slot9:outputMeasSenseV";
assign hvvol[57] to "B_SVT_HV_R3S15B_Slot9:outputMeasSenseV";
assign hvvol[58] to "B_SVT_HV_R3S16T_Slot9:outputMeasSenseV";
assign hvvol[59] to "B_SVT_HV_R3S16B_Slot9:outputMeasSenseV";
assign hvvol[60] to "B_SVT_HV_R3S17T_Slot10:outputMeasSenseV";
assign hvvol[61] to "B_SVT_HV_R3S17B_Slot10:outputMeasSenseV";
assign hvvol[62] to "B_SVT_HV_R3S18T_Slot10:outputMeasSenseV";
assign hvvol[63] to "B_SVT_HV_R3S18B_Slot10:outputMeasSenseV";
monitor hvvol;

/*** High Voltage MPOD controls */
int modhvctrl[HVCTRLS];
assign modhvctrl[0] to "B_SVT_HV_R2S1T_Slot9:outSwitch";
assign modhvctrl[1] to "B_SVT_HV_R2S1B_Slot9:outSwitch";
assign modhvctrl[2] to "B_SVT_HV_R2S2T_Slot9:outSwitch";
assign modhvctrl[3] to "B_SVT_HV_R2S2B_Slot9:outSwitch";
assign modhvctrl[4] to "B_SVT_HV_R2S3T_Slot9:outSwitch";
assign modhvctrl[5] to "B_SVT_HV_R2S3B_Slot9:outSwitch";
assign modhvctrl[6] to "B_SVT_HV_R2S4T_Slot9:outSwitch";
assign modhvctrl[7] to "B_SVT_HV_R2S4B_Slot9:outSwitch";
assign modhvctrl[8] to "B_SVT_HV_R2S5T_Slot9:outSwitch";
assign modhvctrl[9] to "B_SVT_HV_R2S5B_Slot9:outSwitch";
assign modhvctrl[10] to "B_SVT_HV_R2S6T_Slot9:outSwitch";
assign modhvctrl[11] to "B_SVT_HV_R2S6B_Slot9:outSwitch";
assign modhvctrl[12] to "B_SVT_HV_R2S7T_Slot9:outSwitch";
assign modhvctrl[13] to "B_SVT_HV_R2S7B_Slot9:outSwitch";
assign modhvctrl[14] to "B_SVT_HV_R2S8T_Slot9:outSwitch";
assign modhvctrl[15] to "B_SVT_HV_R2S8B_Slot9:outSwitch";
assign modhvctrl[16] to "B_SVT_HV_R2S9T_Slot10:outSwitch";
assign modhvctrl[17] to "B_SVT_HV_R2S9B_Slot10:outSwitch";
assign modhvctrl[18] to "B_SVT_HV_R2S10T_Slot10:outSwitch";
assign modhvctrl[19] to "B_SVT_HV_R2S10B_Slot10:outSwitch";
assign modhvctrl[20] to "B_SVT_HV_R2S11T_Slot10:outSwitch";
assign modhvctrl[21] to "B_SVT_HV_R2S11B_Slot10:outSwitch";
assign modhvctrl[22] to "B_SVT_HV_R2S12T_Slot10:outSwitch";
assign modhvctrl[23] to "B_SVT_HV_R2S12B_Slot10:outSwitch";
assign modhvctrl[24] to "B_SVT_HV_R2S13T_Slot10:outSwitch";
assign modhvctrl[25] to "B_SVT_HV_R2S13B_Slot10:outSwitch";
assign modhvctrl[26] to "B_SVT_HV_R2S14T_Slot10:outSwitch";
assign modhvctrl[27] to "B_SVT_HV_R2S14B_Slot10:outSwitch";
assign modhvctrl[28] to "B_SVT_HV_R3S1T_Slot8:outSwitch";
assign modhvctrl[29] to "B_SVT_HV_R3S1B_Slot8:outSwitch";
assign modhvctrl[30] to "B_SVT_HV_R3S2T_Slot8:outSwitch";
assign modhvctrl[31] to "B_SVT_HV_R3S2B_Slot8:outSwitch";
assign modhvctrl[32] to "B_SVT_HV_R3S3T_Slot8:outSwitch";
assign modhvctrl[33] to "B_SVT_HV_R3S3B_Slot8:outSwitch";
assign modhvctrl[34] to "B_SVT_HV_R3S4T_Slot8:outSwitch";
assign modhvctrl[35] to "B_SVT_HV_R3S4B_Slot8:outSwitch";
assign modhvctrl[36] to "B_SVT_HV_R3S5T_Slot8:outSwitch";
assign modhvctrl[37] to "B_SVT_HV_R3S5B_Slot8:outSwitch";
assign modhvctrl[38] to "B_SVT_HV_R3S6T_Slot8:outSwitch";
assign modhvctrl[39] to "B_SVT_HV_R3S6B_Slot8:outSwitch";
assign modhvctrl[40] to "B_SVT_HV_R3S7T_Slot8:outSwitch";
assign modhvctrl[41] to "B_SVT_HV_R3S7B_Slot8:outSwitch";
assign modhvctrl[42] to "B_SVT_HV_R3S8T_Slot8:outSwitch";
assign modhvctrl[43] to "B_SVT_HV_R3S8B_Slot8:outSwitch";
assign modhvctrl[44] to "B_SVT_HV_R3S9T_Slot9:outSwitch";
assign modhvctrl[45] to "B_SVT_HV_R3S9B_Slot9:outSwitch";
assign modhvctrl[46] to "B_SVT_HV_R3S10T_Slot9:outSwitch";
assign modhvctrl[47] to "B_SVT_HV_R3S10B_Slot9:outSwitch";
assign modhvctrl[48] to "B_SVT_HV_R3S11T_Slot9:outSwitch";
assign modhvctrl[49] to "B_SVT_HV_R3S11B_Slot9:outSwitch";
assign modhvctrl[50] to "B_SVT_HV_R3S12T_Slot9:outSwitch";
assign modhvctrl[51] to "B_SVT_HV_R3S12B_Slot9:outSwitch";
assign modhvctrl[52] to "B_SVT_HV_R3S13T_Slot9:outSwitch";
assign modhvctrl[53] to "B_SVT_HV_R3S13B_Slot9:outSwitch";
assign modhvctrl[54] to "B_SVT_HV_R3S14T_Slot9:outSwitch";
assign modhvctrl[55] to "B_SVT_HV_R3S14B_Slot9:outSwitch";
assign modhvctrl[56] to "B_SVT_HV_R3S15T_Slot9:outSwitch";
assign modhvctrl[57] to "B_SVT_HV_R3S15B_Slot9:outSwitch";
assign modhvctrl[58] to "B_SVT_HV_R3S16T_Slot9:outSwitch";
assign modhvctrl[59] to "B_SVT_HV_R3S16B_Slot9:outSwitch";
assign modhvctrl[60] to "B_SVT_HV_R3S17T_Slot10:outSwitch";
assign modhvctrl[61] to "B_SVT_HV_R3S17B_Slot10:outSwitch";
assign modhvctrl[62] to "B_SVT_HV_R3S18T_Slot10:outSwitch";
assign modhvctrl[63] to "B_SVT_HV_R3S18B_Slot10:outSwitch";

/*** Low Voltage MPOD voltages */
double lvvol[LVMODS];
assign lvvol[0] to "B_SVT_LV_VA_R2S1T_Slot1:outputMeasSenseV";
assign lvvol[1] to "B_SVT_LV_VD_R2S1T_Slot1:outputMeasSenseV";
assign lvvol[2] to "B_SVT_LV_VA_R2S1B_Slot1:outputMeasSenseV";
assign lvvol[3] to "B_SVT_LV_VD_R2S1B_Slot1:outputMeasSenseV";
assign lvvol[4] to "B_SVT_LV_VA_R2S2T_Slot1:outputMeasSenseV";
assign lvvol[5] to "B_SVT_LV_VD_R2S2T_Slot1:outputMeasSenseV";
assign lvvol[6] to "B_SVT_LV_VA_R2S2B_Slot1:outputMeasSenseV";
assign lvvol[7] to "B_SVT_LV_VD_R2S2B_Slot1:outputMeasSenseV";
assign lvvol[8] to "B_SVT_LV_VA_R2S3T_Slot2:outputMeasSenseV";
assign lvvol[9] to "B_SVT_LV_VD_R2S3T_Slot2:outputMeasSenseV";
assign lvvol[10] to "B_SVT_LV_VA_R2S3B_Slot2:outputMeasSenseV";
assign lvvol[11] to "B_SVT_LV_VD_R2S3B_Slot2:outputMeasSenseV";
assign lvvol[12] to "B_SVT_LV_VA_R2S4T_Slot2:outputMeasSenseV";
assign lvvol[13] to "B_SVT_LV_VD_R2S4T_Slot2:outputMeasSenseV";
assign lvvol[14] to "B_SVT_LV_VA_R2S4B_Slot2:outputMeasSenseV";
assign lvvol[15] to "B_SVT_LV_VD_R2S4B_Slot2:outputMeasSenseV";
assign lvvol[16] to "B_SVT_LV_VA_R2S5T_Slot3:outputMeasSenseV";
assign lvvol[17] to "B_SVT_LV_VD_R2S5T_Slot3:outputMeasSenseV";
assign lvvol[18] to "B_SVT_LV_VA_R2S5B_Slot3:outputMeasSenseV";
assign lvvol[19] to "B_SVT_LV_VD_R2S5B_Slot3:outputMeasSenseV";
assign lvvol[20] to "B_SVT_LV_VA_R2S6T_Slot3:outputMeasSenseV";
assign lvvol[21] to "B_SVT_LV_VD_R2S6T_Slot3:outputMeasSenseV";
assign lvvol[22] to "B_SVT_LV_VA_R2S6B_Slot3:outputMeasSenseV";
assign lvvol[23] to "B_SVT_LV_VD_R2S6B_Slot3:outputMeasSenseV";
assign lvvol[24] to "B_SVT_LV_VA_R2S7T_Slot4:outputMeasSenseV";
assign lvvol[25] to "B_SVT_LV_VD_R2S7T_Slot4:outputMeasSenseV";
assign lvvol[26] to "B_SVT_LV_VA_R2S7B_Slot4:outputMeasSenseV";
assign lvvol[27] to "B_SVT_LV_VD_R2S7B_Slot4:outputMeasSenseV";
assign lvvol[28] to "B_SVT_LV_VA_R2S8T_Slot4:outputMeasSenseV";
assign lvvol[29] to "B_SVT_LV_VD_R2S8T_Slot4:outputMeasSenseV";
assign lvvol[30] to "B_SVT_LV_VA_R2S8B_Slot4:outputMeasSenseV";
assign lvvol[31] to "B_SVT_LV_VD_R2S8B_Slot4:outputMeasSenseV";
assign lvvol[32] to "B_SVT_LV_VA_R2S9T_Slot5:outputMeasSenseV";
assign lvvol[33] to "B_SVT_LV_VD_R2S9T_Slot5:outputMeasSenseV";
assign lvvol[34] to "B_SVT_LV_VA_R2S9B_Slot5:outputMeasSenseV";
assign lvvol[35] to "B_SVT_LV_VD_R2S9B_Slot5:outputMeasSenseV";
assign lvvol[36] to "B_SVT_LV_VA_R2S10T_Slot5:outputMeasSenseV";
assign lvvol[37] to "B_SVT_LV_VD_R2S10T_Slot5:outputMeasSenseV";
assign lvvol[38] to "B_SVT_LV_VA_R2S10B_Slot5:outputMeasSenseV";
assign lvvol[39] to "B_SVT_LV_VD_R2S10B_Slot5:outputMeasSenseV";
assign lvvol[40] to "B_SVT_LV_VA_R2S11T_Slot6:outputMeasSenseV";
assign lvvol[41] to "B_SVT_LV_VD_R2S11T_Slot6:outputMeasSenseV";
assign lvvol[42] to "B_SVT_LV_VA_R2S11B_Slot6:outputMeasSenseV";
assign lvvol[43] to "B_SVT_LV_VD_R2S11B_Slot6:outputMeasSenseV";
assign lvvol[44] to "B_SVT_LV_VA_R2S12T_Slot6:outputMeasSenseV";
assign lvvol[45] to "B_SVT_LV_VD_R2S12T_Slot6:outputMeasSenseV";
assign lvvol[46] to "B_SVT_LV_VA_R2S12B_Slot6:outputMeasSenseV";
assign lvvol[47] to "B_SVT_LV_VD_R2S12B_Slot6:outputMeasSenseV";
assign lvvol[48] to "B_SVT_LV_VA_R2S13T_Slot7:outputMeasSenseV";
assign lvvol[49] to "B_SVT_LV_VD_R2S13T_Slot7:outputMeasSenseV";
assign lvvol[50] to "B_SVT_LV_VA_R2S13B_Slot7:outputMeasSenseV";
assign lvvol[51] to "B_SVT_LV_VD_R2S13B_Slot7:outputMeasSenseV";
assign lvvol[52] to "B_SVT_LV_VA_R2S14T_Slot7:outputMeasSenseV";
assign lvvol[53] to "B_SVT_LV_VD_R2S14T_Slot7:outputMeasSenseV";
assign lvvol[54] to "B_SVT_LV_VA_R2S14B_Slot7:outputMeasSenseV";
assign lvvol[55] to "B_SVT_LV_VD_R2S14B_Slot7:outputMeasSenseV";
monitor lvvol;

/*** High Voltage MPOD controls */
int modlvctrl[LVMODS];
assign modlvctrl[0] to "B_SVT_LV_VA_R2S1T_Slot1:onOff";
assign modlvctrl[1] to "B_SVT_LV_VD_R2S1T_Slot1:onOff";
assign modlvctrl[2] to "B_SVT_LV_VA_R2S1B_Slot1:onOff";
assign modlvctrl[3] to "B_SVT_LV_VD_R2S1B_Slot1:onOff";
assign modlvctrl[4] to "B_SVT_LV_VA_R2S2T_Slot1:onOff";
assign modlvctrl[5] to "B_SVT_LV_VD_R2S2T_Slot1:onOff";
assign modlvctrl[6] to "B_SVT_LV_VA_R2S2B_Slot1:onOff";
assign modlvctrl[7] to "B_SVT_LV_VD_R2S2B_Slot1:onOff";
assign modlvctrl[8] to "B_SVT_LV_VA_R2S3T_Slot2:onOff";
assign modlvctrl[9] to "B_SVT_LV_VD_R2S3T_Slot2:onOff";
assign modlvctrl[10] to "B_SVT_LV_VA_R2S3B_Slot2:onOff";
assign modlvctrl[11] to "B_SVT_LV_VD_R2S3B_Slot2:onOff";
assign modlvctrl[12] to "B_SVT_LV_VA_R2S4T_Slot2:onOff";
assign modlvctrl[13] to "B_SVT_LV_VD_R2S4T_Slot2:onOff";
assign modlvctrl[14] to "B_SVT_LV_VA_R2S4B_Slot2:onOff";
assign modlvctrl[15] to "B_SVT_LV_VD_R2S4B_Slot2:onOff";
assign modlvctrl[16] to "B_SVT_LV_VA_R2S5T_Slot3:onOff";
assign modlvctrl[17] to "B_SVT_LV_VD_R2S5T_Slot3:onOff";
assign modlvctrl[18] to "B_SVT_LV_VA_R2S5B_Slot3:onOff";
assign modlvctrl[19] to "B_SVT_LV_VD_R2S5B_Slot3:onOff";
assign modlvctrl[20] to "B_SVT_LV_VA_R2S6T_Slot3:onOff";
assign modlvctrl[21] to "B_SVT_LV_VD_R2S6T_Slot3:onOff";
assign modlvctrl[22] to "B_SVT_LV_VA_R2S6B_Slot3:onOff";
assign modlvctrl[23] to "B_SVT_LV_VD_R2S6B_Slot3:onOff";
assign modlvctrl[24] to "B_SVT_LV_VA_R2S7T_Slot4:onOff";
assign modlvctrl[25] to "B_SVT_LV_VD_R2S7T_Slot4:onOff";
assign modlvctrl[26] to "B_SVT_LV_VA_R2S7B_Slot4:onOff";
assign modlvctrl[27] to "B_SVT_LV_VD_R2S7B_Slot4:onOff";
assign modlvctrl[28] to "B_SVT_LV_VA_R2S8T_Slot4:onOff";
assign modlvctrl[29] to "B_SVT_LV_VD_R2S8T_Slot4:onOff";
assign modlvctrl[30] to "B_SVT_LV_VA_R2S8B_Slot4:onOff";
assign modlvctrl[31] to "B_SVT_LV_VD_R2S8B_Slot4:onOff";
assign modlvctrl[32] to "B_SVT_LV_VA_R2S9T_Slot5:onOff";
assign modlvctrl[33] to "B_SVT_LV_VD_R2S9T_Slot5:onOff";
assign modlvctrl[34] to "B_SVT_LV_VA_R2S9B_Slot5:onOff";
assign modlvctrl[35] to "B_SVT_LV_VD_R2S9B_Slot5:onOff";
assign modlvctrl[36] to "B_SVT_LV_VA_R2S10T_Slot5:onOff";
assign modlvctrl[37] to "B_SVT_LV_VD_R2S10T_Slot5:onOff";
assign modlvctrl[38] to "B_SVT_LV_VA_R2S10B_Slot5:onOff";
assign modlvctrl[39] to "B_SVT_LV_VD_R2S10B_Slot5:onOff";
assign modlvctrl[40] to "B_SVT_LV_VA_R2S11T_Slot6:onOff";
assign modlvctrl[41] to "B_SVT_LV_VD_R2S11T_Slot6:onOff";
assign modlvctrl[42] to "B_SVT_LV_VA_R2S11B_Slot6:onOff";
assign modlvctrl[43] to "B_SVT_LV_VD_R2S11B_Slot6:onOff";
assign modlvctrl[44] to "B_SVT_LV_VA_R2S12T_Slot6:onOff";
assign modlvctrl[45] to "B_SVT_LV_VD_R2S12T_Slot6:onOff";
assign modlvctrl[46] to "B_SVT_LV_VA_R2S12B_Slot6:onOff";
assign modlvctrl[47] to "B_SVT_LV_VD_R2S12B_Slot6:onOff";
assign modlvctrl[48] to "B_SVT_LV_VA_R2S13T_Slot7:onOff";
assign modlvctrl[49] to "B_SVT_LV_VD_R2S13T_Slot7:onOff";
assign modlvctrl[50] to "B_SVT_LV_VA_R2S13B_Slot7:onOff";
assign modlvctrl[51] to "B_SVT_LV_VD_R2S13B_Slot7:onOff";
assign modlvctrl[52] to "B_SVT_LV_VA_R2S14T_Slot7:onOff";
assign modlvctrl[53] to "B_SVT_LV_VD_R2S14T_Slot7:onOff";
assign modlvctrl[54] to "B_SVT_LV_VA_R2S14B_Slot7:onOff";
assign modlvctrl[55] to "B_SVT_LV_VD_R2S14B_Slot7:onOff";

/*** sequencer watchdog ***/
int watchdog;
assign watchdog to "vmetlsvt4:crateoff_seq_htbt";

/*** Local variables */
int   i;
int   hvalloff;
int   lvalloff; 
int   allhvmodoff;
int   j;
int   k;

ss mpodoffall_ss {
    state init {
/*******************************************************
 * Init: 
 *******************************************************/
      when () {
        /*** Set all off flags false ***/
        hvalloff=0; 
        lvalloff=0;
        watchdog = 1;
        pvPut(watchdog);
      } state mpodoffall_wait
    }

    state mpodoffall_wait {
/*******************************************************
 * Wait Cmd: Wait for mpod crate off command           *
 *******************************************************/

/*** MPOD Controls */
      when (offpb) {
          for (i=0; i < HVCTRLS; i++) {
             modhvctrl[i]=0; /* send off command */
             pvPut(modhvctrl[i]);
          }
          allhvmodoff = 0;
          hvalloff = 0;
      } state check_hvoff
      
      when (delay(0.5)){
          watchdog = watchdog * -1;
          pvPut(watchdog);
      } state mpodoffall_wait
    }
    
    state check_hvoff {

      when (hvalloff && allhvmodoff ) {
          lvalloff = 0;
      } state check_lvoff

      when (!hvalloff ) {
        /* checks all hv modules in crate */
        hvalloff = 1;  /* assume all off then check */
        for( i=0; i< HVCTRLS; i++) {
            if( hvvol[i] > 0.1 ) { 
                   modhvctrl[i]=0;  /* send off command again */
                   pvPut(modhvctrl[i]);
                   hvalloff = 0;
            }
        }
        watchdog = watchdog * -1;
        pvPut(watchdog);
      } state check_hvoff

      when (!allhvmodoff ) {
        /* check hv modules that have corresponding lv modules in crate */
        allhvmodoff = 1; /* assume all off then check */
        for( i=0; i< FULLMODS; i++) {
           /* if hv is off send command for lv off */
            if( hvvol[i] < 1.0 ) {
                  j=2*i;
                  k=(2*i)+1;
                  modlvctrl[j]=0; 
                  pvPut(modlvctrl[j]);
                  modlvctrl[k]=0; 
                  pvPut(modlvctrl[k]);
            } else {
                  allhvmodoff = 0;
            }
         }
        watchdog = watchdog * -1;
        pvPut(watchdog);
      } state check_hvoff
    }
    
    state check_lvoff {
      when (hvalloff && lvalloff) {
      } state mpodoffall_wait

      when ( delay(1) ) {
        lvalloff = 1; /* assume all off then check them all */
        for( i=0; i< LVMODS; i++ ) {
            if( lvvol[i] > 0.1 ) { 
                   modlvctrl[i]=0;  /* send off command again */
                   pvPut(modlvctrl[i]);
                   lvalloff = 0;
            }
        }
        watchdog = watchdog * -1;
        pvPut(watchdog);
      } state check_lvoff
    }
}
