;TASK 01
.MODEL SMALL

.STACK 100H

.DATA
 
 X DB "Input: $" 
 Y DB "Output: $"

.CODE
MAIN PROC

;initizlize DS

MOV AX,@DATA
MOV DS,AX

; enter your code here

  LEA DX, X
  MOV AH, 9
  INT 21h
  MOV AH, 1
  INT 21h
  MOV BH, AL
  SUB BH, 30h

  MOV AH, 1
  INT 21h
  MOV BL, AL 
  SUB BL, 30h 

  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h
  
  LEA DX, Y
  MOV AH, 9
  INT 21h
  
  CMP BH, BL
  JG  A
  JMP B 

A:       
  CMP BL, BH
  JG  EXIT
  
  MOV AH, 0
  MOV AL, BL
  MOV DH, 3
  DIV DH

  CMP AH, 0
  JE  YES
  JMP NO 

B:
  CMP BH, BL  
  JG  EXIT
  
  MOV AH, 0
  MOV AL, BH
  MOV DH, 3
  DIV DH 

  CMP AH, 0
  JE  YES2
  JMP NO2  

NO: 
  INC BL
  JMP A 

NO2: 
  INC BH
  JMP B 

YES:
  MOV DL, BL 
  ADD DL, 30h
  MOV AH, 2
  INT 21h
  INC BL
  JMP A 

YES2:
  MOV DL, BH 
  ADD DL, 30h
  MOV AH, 2
  INT 21h
  INC BH
  JMP B  

EXIT:
  JMP e

e:
;exit to DOS
MOV AX,4C00H
INT 21H

MAIN ENDP
   END MAIN