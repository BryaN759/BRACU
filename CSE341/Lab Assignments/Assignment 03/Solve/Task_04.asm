;TASK 04
.MODEL SMALL
 
.STACK 100H

.DATA

 X DB "1st Side:$" 
 Y DB "2nd Side:$"
 Z DB "3rd Side:$" 
 M DB "Y$"
 N DB "N$" 

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here

  LEA DX, X
  MOV AH, 9
  INT 21h

  MOV AH, 1
  INT 21h 
  
  SUB AL, 30h
  MOV BH, AL
  MUL BH
  MOV BH, AL

  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h

  LEA DX, Y
  MOV AH, 9
  INT 21h

  MOV AH, 1
  INT 21h  
  
  SUB AL, 30h
  MOV BL, AL
  MUL BL
  MOV BL, AL

  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h

  LEA DX, Z
  MOV AH, 9
  INT 21h

  MOV AH, 1
  INT 21h  
  
  SUB AL, 30h
  MOV CH, AL
  MUL CH
  MOV CH, AL

  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h


;Comparison starts

  CMP BH, BL
  JG  R1
  CMP BL, CH
  JG  PQ2
  CMP CH, BH
  JG  PQ3

R1: 
  CMP BH, CH
  JG  PQ

;FOR BH
PQ:
  ADD BL, CH
  CMP BL, BH
  JG  PQY
  JMP PQN 

;FOR BL
PQ2:
  ADD BH, CH
  CMP BH, BL
  JG  PQY
  JMP PQN

;FOR CL
PQ3:
  ADD BH, BL
  CMP BH, CH
  JG  PQY
  JMP PQN 
 
PQY:
  LEA DX, M
  MOV AH, 9
  INT 21h
  JMP exit

PQN:
  LEA DX, N
  MOV AH, 9
  INT 21h 

exit:

;exit to DOS 

MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN