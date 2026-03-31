.global _start
.data
.align 3
val_1_9: .double 1.9
val_3_9: .double 3.9
val_7_0: .double 7.0
val_2_0: .double 2.0
val_9_0: .double 9.0
val_12_0: .double 12.0
val_18_0: .double 18.0
val_10_0: .double 10.0
val_3_0: .double 3.0
val_4_0: .double 4.0
val_0_0: .double 0.0
val_1_0: .double 1.0
val_9_1: .double 9.1
val_2_8: .double 2.8
val_8_5: .double 8.5
val_5_0: .double 5.0
memo_MEM: .double 0.0
resultado_0: .double 0.0
resultado_1: .double 0.0
resultado_2: .double 0.0
resultado_3: .double 0.0
resultado_4: .double 0.0
resultado_5: .double 0.0
resultado_6: .double 0.0
resultado_7: .double 0.0
resultado_8: .double 0.0
resultado_9: .double 0.0
resultado_10: .double 0.0
resultado_11: .double 0.0
resultado_12: .double 0.0
resultado_13: .double 0.0
resultado_14: .double 0.0
resultado_15: .double 0.0
resultado_16: .double 0.0
.text
.arm
.fpu vfpv3
.align 2
_start:
LDR R0, =val_1_9
VLDR.F64 D0, [R0]
LDR R0, =val_3_9
VLDR.F64 D1, [R0]
VADD.F64 D0, D0, D1
LDR R0, =resultado_0
VSTR.F64 D0, [R0]
LDR R0, =val_7_0
VLDR.F64 D0, [R0]
LDR R0, =val_2_0
VLDR.F64 D1, [R0]
VMUL.F64 D0, D0, D1
LDR R0, =val_9_0
VLDR.F64 D2, [R0]
VSUB.F64 D0, D0, D2
LDR R0, =resultado_1
VSTR.F64 D0, [R0]
LDR R0, =val_12_0
VLDR.F64 D0, [R0]
LDR R0, =memo_MEM
VSTR.F64 D0, [R0]
LDR R0, =resultado_2
VSTR.F64 D0, [R0]
LDR R0, =val_18_0
VLDR.F64 D0, [R0]
LDR R0, =val_9_0
VLDR.F64 D1, [R0]
VDIV.F64 D0, D0, D1
VCVT.S32.F64 S0, D0
VCVT.F64.S32 D0, S0
LDR R0, =resultado_3
VSTR.F64 D0, [R0]
LDR R0, =val_10_0
VLDR.F64 D0, [R0]
LDR R0, =val_2_0
VLDR.F64 D1, [R0]
VDIV.F64 D0, D0, D1
LDR R0, =resultado_4
VSTR.F64 D0, [R0]
LDR R0, =val_7_0
VLDR.F64 D0, [R0]
LDR R0, =val_2_0
VLDR.F64 D1, [R0]
VMOV.F64 D6, D0
VMOV.F64 D7, D1
LDR R0, =val_1_0
VLDR.F64 D5, [R0]
pot_0:
VCVT.S32.F64 S0, D7
VMOV R2, S0
CMP R2, #1
BLE potFim_0
VMUL.F64 D6, D6, D0
VSUB.F64 D7, D7, D5
B pot_0
potFim_0:
VMOV.F64 D0, D6
LDR R0, =resultado_5
VSTR.F64 D0, [R0]
LDR R0, =val_3_0
VLDR.F64 D0, [R0]
LDR R0, =val_4_0
VLDR.F64 D1, [R0]
VMUL.F64 D0, D0, D1
LDR R0, =resultado_6
VSTR.F64 D0, [R0]
LDR R0, =val_0_0
VLDR.F64 D0, [R0]
UDF #2
LDR R0, =resultado_7
VSTR.F64 D0, [R0]
LDR R0, =val_1_0
VLDR.F64 D0, [R0]
LDR R0, =val_2_0
VLDR.F64 D1, [R0]
VADD.F64 D0, D0, D1
LDR R0, =val_3_0
VLDR.F64 D2, [R0]
LDR R0, =val_4_0
VLDR.F64 D3, [R0]
VADD.F64 D2, D2, D3
VMUL.F64 D0, D0, D2
LDR R0, =resultado_8
VSTR.F64 D0, [R0]
LDR R0, =val_2_0
VLDR.F64 D0, [R0]
LDR R0, =val_3_0
VLDR.F64 D1, [R0]
VMUL.F64 D0, D0, D1
LDR R0, =val_1_0
VLDR.F64 D2, [R0]
VADD.F64 D0, D0, D2
LDR R0, =val_2_0
VLDR.F64 D3, [R0]
VDIV.F64 D0, D0, D3
LDR R0, =resultado_9
VSTR.F64 D0, [R0]
LDR R0, =val_9_1
VLDR.F64 D0, [R0]
LDR R0, =val_2_0
VLDR.F64 D1, [R0]
VSUB.F64 D0, D0, D1
LDR R0, =val_2_8
VLDR.F64 D2, [R0]
LDR R0, =val_1_0
VLDR.F64 D3, [R0]
VADD.F64 D2, D2, D3
VMUL.F64 D0, D0, D2
LDR R0, =resultado_10
VSTR.F64 D0, [R0]
LDR R0, =val_8_5
VLDR.F64 D0, [R0]
LDR R0, =resultado_3
VLDR.F64 D0, [R0]
LDR R0, =resultado_11
VSTR.F64 D0, [R0]
LDR R0, =val_10_0
VLDR.F64 D0, [R0]
LDR R0, =val_4_0
VLDR.F64 D1, [R0]
VDIV.F64 D0, D0, D1
VCVT.S32.F64 S0, D0
VCVT.F64.S32 D0, S0
LDR R0, =resultado_12
VSTR.F64 D0, [R0]
LDR R0, =val_1_0
VLDR.F64 D0, [R0]
LDR R0, =val_4_0
VLDR.F64 D1, [R0]
VADD.F64 D0, D0, D1
LDR R0, =val_5_0
VLDR.F64 D2, [R0]
VMUL.F64 D0, D0, D2
LDR R0, =resultado_13
VSTR.F64 D0, [R0]
LDR R0, =val_12_0
VLDR.F64 D0, [R0]
LDR R0, =val_3_0
VLDR.F64 D1, [R0]
VSUB.F64 D0, D0, D1
LDR R0, =val_10_0
VLDR.F64 D2, [R0]
LDR R0, =val_3_0
VLDR.F64 D3, [R0]
VADD.F64 D2, D2, D3
VADD.F64 D0, D0, D2
LDR R0, =resultado_14
VSTR.F64 D0, [R0]
LDR R0, =val_2_0
VLDR.F64 D0, [R0]
LDR R0, =memo_MEM
VSTR.F64 D0, [R0]
LDR R0, =resultado_15
VSTR.F64 D0, [R0]
LDR R0, =memo_MEM
VLDR.F64 D0, [R0]
LDR R0, =resultado_16
VSTR.F64 D0, [R0]
    MOV R7, #1
    SWI #0
