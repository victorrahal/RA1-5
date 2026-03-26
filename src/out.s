.global _start
.text
_start:
LDR r0, =3
LDR r1, =2
MUL r2, r0, r1
LDR r0, =3
ADD r2, r2, r0
LDR r0, =4
SUB r2, r2, r0
LDR r0, =3
LDR r1, =2
ADD r3, r0, r1
LDR r0, =3
SUB r3, r3, r0
LDR r0, =4
MUL r3, r3, r0
LDR r0, =3
LDR r1, =2
SDIV r4, r0, r1
