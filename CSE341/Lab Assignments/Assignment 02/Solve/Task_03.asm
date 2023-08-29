;TASK 03
.MODEL SMALL
 
.STACK 100H

.DATA 

 A DB 'Enter First Initial: $'
 B DB 'Enter Second Initial: $'
 C DB 'Enter Third Initial: $'

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here

  MOV AH, 9
  LEA DX, A
  INT 21H

  MOV AH, 1
  INT 21H
  MOV BL, AL

  MOV AH, 2
  MOV DL, 0DH
  INT 21H
  MOV DL, 0AH
  INT 21H 

  MOV AH, 9
  LEA DX, B
  INT 21H

  MOV AH, 1
  INT 21H
  MOV BH, AL

  MOV AH, 2
  MOV DL, 0DH
  INT 21H
  MOV DL, 0AH
  INT 21H 

  MOV AH, 9
  LEA DX, C
  INT 21H

  MOV AH, 1
  INT 21H
  MOV CL, AL

  MOV AH, 2
  MOV DL, 0DH
  INT 21H
  MOV DL, 0AH
  INT 21H

  MOV DL, CL
  INT 21H

  MOV AH, 2
  MOV DL, 0DH
  INT 21H
  MOV DL, 0AH
  INT 21H

  MOV DL, BH
  INT 21H

  MOV AH, 2
  MOV DL, 0DH
  INT 21H
  MOV DL, 0AH
  INT 21H

  MOV DL, BL
  INT 21H

;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 




