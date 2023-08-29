;TASK 03
.MODEL SMALL

.STACK 100H

.DATA

 I DW "Input: $"
 L DW "Sunday $"
 M DW "Monday $"
 N DW "Tuesday $"
 O DW "Wednesday $"
 P DW "Thursday $"
 Q DW "Friday $"
 R DW "Saturday $"
 
.CODE
MAIN PROC

;initizlize DS

MOV AX,@DATA
MOV DS,AX

; enter your code here

  LEA DX, I
  MOV AH, 9
  INT 21h

  MOV AH, 1
  INT 21h 

  MOV BL, AL

  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH 
  INT 21h 
 
  CMP BL, 31H
  JE  OP1
  CMP BL, 32H
  JE  OP2
  CMP BL, 33H
  JE  OP3
  CMP BL, 34H
  JE  OP4
  CMP BL, 35H
  JE  OP5
  CMP BL, 36H
  JE  OP6 
  CMP BL, 37H
  JE  OP7
  JMP exit

OP1:
  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH 
  INT 21h
  LEA DX, L
  MOV AH, 9
  INT 21h
  JMP exit

OP2:
  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH 
  INT 21h
  LEA DX, M
  MOV AH, 9
  INT 21h
  JMP exit

OP3:
  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH 
  INT 21h
  LEA DX, N
  MOV AH, 9
  INT 21h
  JMP exit

OP4:
  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH 
  INT 21h
  LEA DX, O
  MOV AH, 9
  INT 21h
  JMP exit 

OP5:
  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH 
  INT 21h
  LEA DX, P
  MOV AH, 9
  INT 21h
  JMP exit
 
OP6:
  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH 
  INT 21h
  LEA DX, Q
  MOV AH, 9
  INT 21h
  JMP exit 

OP7:
  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH 
  INT 21h
  LEA DX, R
  MOV AH, 9
  INT 21h
  JMP exit

exit: 

;exit to DOS
MOV AX,4C00H
INT 21H

MAIN ENDP
   END MAIN