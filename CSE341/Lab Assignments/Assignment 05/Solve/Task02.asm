;TASK 02
.MODEL SMALL

.STACK 100H

.DATA

 X DB "Enter Three numbers: $" 
 Y DB "Largest Number: $" 
 
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
  MOV [SI], AL
  INC SI

  MOV AH, 1
  INT 21h 
  MOV [SI], AL
  INC SI

  MOV AH, 1
  INT 21h
  MOV [SI], AL 

  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h

  LEA DX, Y
  MOV AH, 9
  INT 21h

  MOV BL, [SI]
  SUB SI, 1
  MOV BH, [SI]
  SUB SI, 1  
  MOV CH, [SI]

  CMP BL, BH
  JG  P
  CMP BH, CH
  JG  R
  MOV DL, CH
  MOV AH,2
  INT 21h
  JMP exit

P:
  CMP BL, CH
  JG  Q
  MOV DL, CH
  MOV ah,2
  INT 21h
  JMP exit 

Q:
  MOV DL, BL
  MOV AH,2
  INT 21h 
  JMP exit 
  
R:
  MOV DL, BH
  MOV AH,2
  INT 21h
  JMP exit  

exit: 

;exit to DOS
MOV AX,4C00H
INT 21H

MAIN ENDP
   END MAIN
