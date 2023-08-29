;TASK 03
.MODEL SMALL

.STACK 100H

.DATA

 X DB "Sample Input: $" 
 Y DB "Sample Output: $"

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

  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h

  MOV AH, 1
  INT 21h
  MOV AH, 0
  MOV CX, AX 
  SUB CX, 30h  

  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h

  LEA DX, Y
  MOV AH, 9
  INT 21h

  MOV AL, BH
  MOV BL, 1 

A:
  MUL BL
  MOV DL, AL
  ADD DL, 30h
  MOV AH, 2
  INT 21h
  INC BL
  MOV AL, BH

  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h 
  MOV AL, BH

  LOOP A
  JMP exit

exit:

;exit to DOS
MOV AX,4C00H
INT 21H

MAIN ENDP
   END MAIN