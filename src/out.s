.global _start
.text
_start:
LDR r0, =3
LDR r1, =2
LDR r2, =5
MUL r1, r1, r2
LDR r2, = 0
ADD r0, r0, r1
LDR r1, = 0
LDR r0, =4
LDR r1, =2
MUL r0, r0, r1
LDR r1, = 0
LDR r2, =6
LDR r3, =5
MUL r2, r2, r3
LDR r3, = 0
SUB r0, r0, r2
LDR r2, = 0
LDR r0, =10
LDR r1, =5
ADD r0, r0, r1
LDR r1, = 0
LDR r2, =1
LDR r3, =3
MUL r2, r2, r3
LDR r3, = 0
SUB r0, r0, r2
LDR r2, = 0
