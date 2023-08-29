;TASK 02
.MODEL SMALL
 
.STACK 100H

.DATA 
 
 L DB "1st Input: $"
 M DB "2nd Input: $"
 N DB "Not Divisible $"
 O DB "Divisible $"

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here

  LEA DX, L
  MOV AH, 9
  INT 21h

  MOV AH,1
  INT 21h 

  MOV BH, AL
  SUB BH, 30h

  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h

  LEA DX, M
  MOV AH, 9
  INT 21h

  MOV AH,1
  INT 21h 

  MOV BL, AL
  SUB BL, 30h

  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h

  ADD BH, BL
  MOV AL, BH
  MOV AH, 0

  MOV CH, 2
  DIV CH
 
  CMP AH, 0
  JE  D

  MOV AL, BH
  MOV AH, 0 
  MOV CH, 3
  DIV CH

  CMP AH, 0
  JE  ND 
  JG  ND

D:
  LEA DX, O
  MOV AH, 9
  INT 21h
  JMP exit

ND:
  LEA DX, N
  MOV AH, 9
  INT 21h
  JMP exit
 
exit:
 
;exit to DOS 

MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN